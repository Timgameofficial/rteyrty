// api/notify.js
// Vercel Serverless Function (Node.js runtime).
//
// Приймає заявку з форми запису (POST JSON) і пересилає її в Telegram
// через Bot API. Токен бота НІКОЛИ не потрапляє у фронтенд — він живе
// лише тут, як змінна оточення на сервері Vercel.
//
// Обов'язково задайте в Vercel → Project → Settings → Environment Variables:
//   TELEGRAM_BOT_TOKEN   — токен бота від @BotFather
//   TELEGRAM_CHAT_ID     — chat_id, куди слати заявки (див. інструкцію в README)
//
// Опційно:
//   ALLOWED_ORIGIN        — якщо форма колись викликатиметься з іншого домену
//   NOTIFY_RATE_LIMIT_MAX — максимум запитів з одного IP за вікно (за замовч. 5)

const RATE_LIMIT_WINDOW_MS = 10 * 60 * 1000; // 10 хвилин
const RATE_LIMIT_MAX = Number(process.env.NOTIFY_RATE_LIMIT_MAX || 5);

// Проста in-memory обмежувалка — переживає лише "теплий" інстанс функції,
// це навмисно: мета — збити примітивний спам-бот, а не бути повноцінним WAF.
const hits = new Map();

function isRateLimited(ip) {
  const now = Date.now();
  const entry = hits.get(ip);
  if (!entry || now - entry.start > RATE_LIMIT_WINDOW_MS) {
    hits.set(ip, { start: now, count: 1 });
    return false;
  }
  entry.count += 1;
  return entry.count > RATE_LIMIT_MAX;
}

function escapeHtml(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function clean(value, maxLen) {
  return String(value ?? "").trim().slice(0, maxLen);
}

module.exports = async function handler(req, res) {
  const allowedOrigin = process.env.ALLOWED_ORIGIN || "";
  if (allowedOrigin) {
    res.setHeader("Access-Control-Allow-Origin", allowedOrigin);
    res.setHeader("Vary", "Origin");
  }
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type");

  if (req.method === "OPTIONS") {
    res.status(204).end();
    return;
  }

  if (req.method !== "POST") {
    res.status(405).json({ ok: false, error: "Method not allowed" });
    return;
  }

  const ip =
    (req.headers["x-forwarded-for"] || "").split(",")[0].trim() ||
    req.socket?.remoteAddress ||
    "unknown";

  if (isRateLimited(ip)) {
    res.status(429).json({ ok: false, error: "Too many requests, try again later" });
    return;
  }

  const token = process.env.TELEGRAM_BOT_TOKEN;
  const chatId = process.env.TELEGRAM_CHAT_ID;

  if (!token || !chatId) {
    console.error("notify: TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID is not set");
    res.status(500).json({ ok: false, error: "Server is not configured" });
    return;
  }

  let body = req.body;
  if (typeof body === "string") {
    try {
      body = JSON.parse(body);
    } catch {
      body = {};
    }
  }
  body = body || {};

  const name = clean(body.name, 120);
  const phone = clean(body.phone, 40);
  const service = clean(body.service, 120);
  const note = clean(body.note, 600);
  const page = clean(body.page, 300);

  if (name.length < 2 || phone.replace(/\D/g, "").length < 11) {
    res.status(400).json({ ok: false, error: "Invalid name or phone" });
    return;
  }

  // Honeypot: якщо на формі колись з'явиться приховане поле "website",
  // бот заповнить його, людина — ні.
  if (clean(body.website, 50)) {
    res.status(200).json({ ok: true }); // тихо ковтаємо, ботові знати не треба
    return;
  }

  const text =
    `🦷 <b>Нова заявка — ST Стоматологія</b>\n\n` +
    `<b>Ім'я:</b> ${escapeHtml(name)}\n` +
    `<b>Телефон:</b> ${escapeHtml(phone)}\n` +
    (service ? `<b>Напрям:</b> ${escapeHtml(service)}\n` : "") +
    (note ? `<b>Коментар:</b> ${escapeHtml(note)}\n` : "") +
    (page ? `\n<i>Сторінка:</i> ${escapeHtml(page)}` : "");

  try {
    const tgRes = await fetch(`https://api.telegram.org/bot${token}/sendMessage`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        chat_id: chatId,
        text,
        parse_mode: "HTML",
        disable_web_page_preview: true,
      }),
    });

    if (!tgRes.ok) {
      const errBody = await tgRes.text().catch(() => "");
      console.error("Telegram API error:", tgRes.status, errBody);
      res.status(502).json({ ok: false, error: "Telegram delivery failed" });
      return;
    }

    res.status(200).json({ ok: true });
  } catch (err) {
    console.error("notify: unexpected error", err);
    res.status(500).json({ ok: false, error: "Unexpected server error" });
  }
};
