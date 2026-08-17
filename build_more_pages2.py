import sys
sys.path.insert(0, '.')
from generate_page import render_page

def crumb(title):
    return f'''<nav class="crumbs" aria-label="Хлібні крихти">
        <a href="/">Головна</a><span class="sep">/</span>
        <span aria-current="page">{title}</span>
      </nav>'''


# ============================================================
# /reviews/
# ============================================================
reviews_main = f'''
  <section class="page-hero">
    <div class="container">
      {crumb("Відгуки")}
      <div class="page-hero-copy" style="max-width:52rem">
        <p class="eyebrow" data-reveal>Відгуки</p>
        <h1 data-reveal data-reveal-delay="1">Слова пацієнтів</h1>
        <p data-reveal data-reveal-delay="2">Середня оцінка 5.0 на основі 184 відгуків у Google та Doc.ua.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="reviews" data-reviews data-reveal>
        <div class="reviews-track" data-reviews-track tabindex="0" role="group" aria-label="Відгуки пацієнтів, гортайте свайпом або стрілками">
          <article class="review-card">
            <div class="review-stars" aria-label="Оцінка 5 з 5">
              <svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg>
            </div>
            <blockquote>Обирала клініку довго й прискіпливо. ST — це рівень, який одразу відчувається: від першого дзвінка до фінального результату. Жодного відчуття конвеєра.</blockquote>
            <div class="review-person">
              <img src="../images/patient-nataliia.png" width="200" height="200" alt="Портрет пацієнтки Наталії К." loading="lazy" decoding="async">
              <div><p class="rname">Наталія К.</p><p class="rmeta">Вініри, 8 одиниць</p></div>
            </div>
          </article>
          <article class="review-card">
            <div class="review-stars" aria-label="Оцінка 5 з 5">
              <svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg>
            </div>
            <blockquote>Імплантацію відкладав роками через страх. У ST усе пояснили заздалегідь, показали 3D-план — і процедура пройшла спокійно, без сюрпризів.</blockquote>
            <div class="review-person">
              <img src="../images/patient-dmytro.png" width="200" height="200" alt="Портрет пацієнта Дмитра С." loading="lazy" decoding="async">
              <div><p class="rname">Дмитро С.</p><p class="rmeta">Імплантація Nobel Biocare</p></div>
            </div>
          </article>
          <article class="review-card">
            <div class="review-stars" aria-label="Оцінка 5 з 5">
              <svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg>
            </div>
            <blockquote>Дизайн усмішки, який мені показали до лікування, збігся з результатом майже ідеально. Це той рівень точності, за який справді хочеться платити.</blockquote>
            <div class="review-person">
              <img src="../images/patient-iryna.png" width="200" height="200" alt="Портрет пацієнтки Ірини П." loading="lazy" decoding="async">
              <div><p class="rname">Ірина П.</p><p class="rmeta">Дизайн усмішки</p></div>
            </div>
          </article>
          <article class="review-card">
            <div class="review-stars" aria-label="Оцінка 5 з 5">
              <svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg><svg aria-hidden="true"><use href="#icon-star"></use></svg>
            </div>
            <blockquote>Привела дитину на профілактику й залишилася сама як пацієнт. Тут не продають зайвого — навпаки, відмовили від процедури, яку радили в іншій клініці.</blockquote>
            <div class="review-person">
              <img src="../images/patient-oksana.png" width="200" height="200" alt="Портрет пацієнтки Оксани Л." loading="lazy" decoding="async">
              <div><p class="rname">Оксана Л.</p><p class="rmeta">Терапія, гігієна</p></div>
            </div>
          </article>
        </div>

        <div class="reviews-controls">
          <div class="reviews-dots" data-reviews-dots role="tablist" aria-label="Навігація по відгуках"></div>
          <div class="gallery-arrows">
            <button type="button" aria-label="Попередній відгук" data-reviews-prev><svg aria-hidden="true"><use href="#icon-chevron-left"></use></svg></button>
            <button type="button" aria-label="Наступний відгук" data-reviews-next><svg aria-hidden="true"><use href="#icon-chevron-right"></use></svg></button>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="cta-banner" data-reveal>
        <div>
          <h3>Хочете стати нашим наступним відгуком?</h3>
          <p>Консультація хірурга безкоштовна — почніть зі знайомства.</p>
        </div>
        <a href="#booking" class="btn btn--gold" data-open-booking>Записатися на консультацію</a>
      </div>
    </div>
  </section>
'''

render_page(
    path="reviews/index.html",
    title="Відгуки про стоматологію ST у Кам'янському — 5.0 з 184 оцінок",
    description="184 відгуки пацієнтів стоматології ST у Кам'янському із середньою оцінкою 5.0. Реальні історії лікування — вініри, імплантація, дизайн усмішки.",
    canonical_path="/reviews/",
    active_href="/reviews/",
    main_html=reviews_main,
    depth=1,
    breadcrumbs=[("Головна","/"),("Відгуки","/reviews/")],
)


# ============================================================
# /faq/
# ============================================================
faq_main = f'''
  <section class="page-hero">
    <div class="container">
      {crumb("Питання")}
      <div class="page-hero-copy" style="max-width:52rem">
        <p class="eyebrow" data-reveal>Питання</p>
        <h1 data-reveal data-reveal-delay="1">Що запитують найчастіше</h1>
        <p data-reveal data-reveal-delay="2">Не знайшли відповідь? Напишіть напряму — адміністратор відповість протягом 15 хвилин у робочі години.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container-narrow">
      <div class="faq-list" data-reveal>
        <details class="acc" open>
          <summary><span class="acc-title">Чи боляче встановлювати вініри?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Ні. Препарування проходить під локальною анестезією і зачіпає мінімальний шар емалі — 0,3–0,5 мм. Більшість пацієнтів описує відчуття як тиск, а не біль. Між візитами ви носите тимчасові накладки, тож дискомфорту в побуті немає.</p></div>
        </details>
        <details class="acc">
          <summary><span class="acc-title">Скільки триває імплантація?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Хірургічний етап займає 40–60 хвилин на одну одиницю — це один візит. Далі йде остеоінтеграція: від 3 до 5 місяців залежно від щелепи та щільності кістки. Після цього встановлюємо коронку за 2 візити.</p></div>
        </details>
        <details class="acc">
          <summary><span class="acc-title">Чи є розсрочка або оплата частинами?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Так. Для лікування вартістю від 30 000 ₴ доступна безвідсоткова розсрочка до 12 місяців. Довідки про доходи не потрібні, оформлення відбувається на першому візиті й займає близько 15 хвилин.</p></div>
        </details>
        <details class="acc">
          <summary><span class="acc-title">Що входить у першу консультацію?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Огляд, фотопротокол, обговорення очікуваного результату та письмовий план лікування з кошторисом. Консультація хірурга-імплантолога — безкоштовна. 3D-томографія за потреби оплачується окремо (1 100 ₴).</p></div>
        </details>
        <details class="acc">
          <summary><span class="acc-title">Скільки служать вініри та імпланти?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Кераміка E.max за коректної гігієни служить 15–20 років, наша гарантія — 7 років. Імпланти Nobel Biocare мають довічну гарантію виробника; коронка на імпланті — гарантія 5 років.</p></div>
        </details>
        <details class="acc">
          <summary><span class="acc-title">Чи можна лікуватися під час вагітності?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Так, терапія та гігієна безпечні у другому триместрі — ми використовуємо анестетики без адреналіну. Хірургічні втручання, відбілювання та планові рентген-обстеження переносимо на період після народження дитини.</p></div>
        </details>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="cta-banner" data-reveal>
        <div>
          <h3>Лишилися питання?</h3>
          <p>Зателефонуйте або запишіться на безкоштовну консультацію — відповімо на все особисто.</p>
        </div>
        <a href="#booking" class="btn btn--gold" data-open-booking>Записатися на консультацію</a>
      </div>
    </div>
  </section>
'''

render_page(
    path="faq/index.html",
    title="Питання про лікування зубів — FAQ | ST Кам'янське",
    description="Відповіді на часті питання про вініри, імплантацію, розстрочку та біль після лікування в стоматології ST, Кам'янське.",
    canonical_path="/faq/",
    active_href="/faq/",
    main_html=faq_main,
    depth=1,
    breadcrumbs=[("Головна","/"),("Питання","/faq/")],
)


# ============================================================
# /portfolio/  (галерея кейсів: вініри + імплантація)
# ============================================================
def ba_case(before_src, after_src, before_alt, after_alt, title, desc, slug, w=900, h=700, reveal_delay=None):
    delay_attr = f' data-reveal-delay="{reveal_delay}"' if reveal_delay else ""
    return f'''<figure class="ba-case" data-reveal{delay_attr}>
          <div class="ba-slider" style="--ba-pos:50%" data-ba>
            <img class="ba-before" src="../images/{before_src}" width="{w}" height="{h}" alt="{before_alt}" loading="lazy" decoding="async">
            <img class="ba-after" src="../images/{after_src}" width="{w}" height="{h}" alt="{after_alt}" loading="lazy" decoding="async">
            <span class="ba-tag before">До</span>
            <span class="ba-tag after">Після</span>
            <div class="ba-handle" aria-hidden="true"><span class="ba-handle-grip"><svg><use href="#icon-drag"></use></svg></span></div>
            <input type="range" min="0" max="100" value="50" step="0.1" class="ba-range" aria-label="Повзунок порівняння до і після, {title}">
          </div>
          <figcaption class="ba-caption">
            <strong>{title}</strong>{desc}
            <a href="/portfolio/{slug}/" class="ba-more">Детальніше про кейс <svg aria-hidden="true"><use href="#icon-arrow"></use></svg></a>
          </figcaption>
        </figure>'''

case1 = ba_case("case-1-before.jpg", "case-1-after.jpg",
    "Стан зубного ряду пацієнта до комплексної реставрації",
    "Стан зубного ряду пацієнта після комплексної реставрації",
    "Комплексна реставрація зубного ряду", "Реальний клінічний випадок пацієнта.",
    slug="kompleksna-restavratsiya", w=1000, h=474)

veneer2 = ba_case("portfolio-veneers-2-before.png", "portfolio-veneers-2-after.png",
    "Стан зубів пацієнта до встановлення вінірів E.max",
    "Стан зубів пацієнта після встановлення вінірів E.max",
    "Вініри E.max, 6 одиниць", "Закриття діастеми та вирівнювання кольору фронтальної групи.",
    slug="vinory-emax-6-odynyts", reveal_delay=1)

veneer3 = ba_case("portfolio-veneers-3-before.png", "portfolio-veneers-3-after.png",
    "Стан зубів пацієнта до художньої реставрації",
    "Стан зубів пацієнта після художньої реставрації",
    "Художня реставрація", "Відновлення сколотого центрального різця композитним матеріалом.",
    slug="khudozhnia-restavratsiya", reveal_delay=2)

implant1 = ba_case("portfolio-implants-1-before.png", "portfolio-implants-1-after.png",
    "Стан прикусу пацієнта до імплантації",
    "Стан прикусу пацієнта після імплантації та протезування",
    "Імплантація Nobel Biocare", "Відновлення двох одиниць у бічній ділянці нижньої щелепи.",
    slug="implantatsiya-nobel-biocare")

implant2 = ba_case("portfolio-implants-2-before.png", "portfolio-implants-2-after.png",
    "Стан щелепи пацієнта до повної реабілітації",
    "Стан щелепи пацієнта після повної реабілітації на імплантах",
    "Повна реабілітація на імплантах", "Комплексне відновлення верхньої щелепи за протоколом All-on-6.",
    slug="povna-reabilitatsiya-all-on-6", reveal_delay=1)

implant3 = ba_case("portfolio-implants-3-before.png", "portfolio-implants-3-after.png",
    "Стан зуба пацієнта до одиночної імплантації",
    "Стан зуба пацієнта після одиночної імплантації",
    "Одиночна імплантація", "Відновлення одного зуба в естетичній зоні без розрізу ясен.",
    slug="odynochna-implantatsiya", reveal_delay=2)

portfolio_main = f'''
  <section class="page-hero">
    <div class="container">
      {crumb("Портфоліо")}
      <div class="page-hero-copy" style="max-width:52rem">
        <p class="eyebrow" data-reveal>Портфоліо</p>
        <h1 data-reveal data-reveal-delay="1">Роботи клініки</h1>
        <p data-reveal data-reveal-delay="2">Перетягніть повзунок на кожному фото, щоб побачити трансформацію. Реальні клінічні випадки пацієнтів ST — усі фото використані за згодою.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="section-head" data-reveal>
        <p class="eyebrow">Категорія</p>
        <h2>Вініри та естетична реставрація</h2>
      </div>
      <div class="ba-wrap ba-wrap--gallery">
        {case1}
        {veneer2}
        {veneer3}
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="section-head" data-reveal>
        <p class="eyebrow">Категорія</p>
        <h2>Імплантологія та протезування</h2>
      </div>
      <div class="ba-wrap ba-wrap--gallery">
        {implant1}
        {implant2}
        {implant3}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <p class="form-fine">Фото використані за згодою пацієнтів. Результат індивідуальний і залежить від вихідного клінічного стану — конкретний прогноз обговорюється на консультації.</p>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="cta-banner" data-reveal>
        <div>
          <h3>Хочете такий самий результат?</h3>
          <p>Консультація хірурга безкоштовна — обговоримо ваш випадок і покажемо орієнтовний план.</p>
        </div>
        <a href="#booking" class="btn btn--gold" data-open-booking>Записатися на консультацію</a>
      </div>
    </div>
  </section>
'''

render_page(
    path="portfolio/index.html",
    title="Портфоліо стоматології Кам'янське — фото до і після | ST",
    description="Фото до і після стоматології ST у Кам'янському: вініри E.max, художня реставрація, імплантація Nobel Biocare. Реальні клінічні випадки пацієнтів.",
    canonical_path="/portfolio/",
    active_href="/portfolio/",
    main_html=portfolio_main,
    depth=1,
    breadcrumbs=[("Головна","/"),("Портфоліо","/portfolio/")],
)


# ============================================================
# /contact/
# ============================================================
contact_main = f'''
  <section class="page-hero">
    <div class="container">
      {crumb("Контакти")}
      <div class="page-hero-copy" style="max-width:52rem">
        <p class="eyebrow" data-reveal>Контакти</p>
        <h1 data-reveal data-reveal-delay="1">Як нас знайти</h1>
        <p data-reveal data-reveal-delay="2">Приходьте на консультацію або зателефонуйте — відповімо на всі питання й підберемо зручний час.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="contact-grid">
        <div class="contact-info" data-reveal>
          <div class="contact-block">
            <h4>Адреса</h4>
            <p>просп. Тараса Шевченка, 5, м. Кам'янське</p>
            <p class="fine">Дніпропетровська область</p>
          </div>
          <div class="contact-block">
            <h4>Телефон</h4>
            <a href="tel:+380972155077">+380 97 215 50 77</a>
          </div>
          <div class="contact-block">
            <h4>Пошта</h4>
            <a href="mailto:hello@st-dental.ua">hello@st-dental.ua</a>
          </div>
          <div class="contact-block">
            <h4>Години роботи</h4>
            <p class="fine">Пн–Пт: 09:00 — 19:00</p>
            <p class="fine">Сб–Нд: вихідний</p>
          </div>
        </div>

        <div class="map-frame" data-reveal data-reveal-delay="1">
          <iframe
            src="https://www.google.com/maps?q=Prospekt%20Tarasa%20Shevchenka%205%2C%20Kamianske%2C%20Dnipropetrovska%20oblast&output=embed"
            title="Карта розташування клініки ST на проспекті Тараса Шевченка, Кам'янське"
            loading="lazy"
            referrerpolicy="no-referrer-when-downgrade"
            aria-label="Інтерактивна карта з розташуванням клініки ST">
          </iframe>
        </div>
      </div>

      <div class="cta-banner" data-reveal style="margin-top:3rem">
        <div>
          <h3>Простіше записатися онлайн</h3>
          <p>Заповніть коротку форму — адміністратор передзвонить протягом 15 хвилин.</p>
        </div>
        <a href="#booking" class="btn btn--gold" data-open-booking>Записатися на консультацію</a>
      </div>
    </div>
  </section>
'''

render_page(
    path="contact/index.html",
    title="Стоматологія в Кам'янському — контакти ST",
    description="Стоматологія ST на просп. Тараса Шевченка, 5, м. Кам'янське. Телефон +380 97 215 50 77, графік роботи, карта проїзду, онлайн-запис на консультацію.",
    canonical_path="/contact/",
    active_href="/contact/",
    main_html=contact_main,
    depth=1,
    breadcrumbs=[("Головна","/"),("Контакти","/contact/")],
)


# ============================================================
# /legal/  — Політика конфіденційності + Ліцензія МОЗ
# ============================================================
legal_main = f'''
  <section class="page-hero">
    <div class="container">
      {crumb("Юридична інформація")}
      <div class="page-hero-copy" style="max-width:52rem">
        <p class="eyebrow" data-reveal>Юридична інформація</p>
        <h1 data-reveal data-reveal-delay="1">Політика конфіденційності та ліцензія</h1>
        <p data-reveal data-reveal-delay="2">Прозорість щодо того, як ми обробляємо ваші дані, та підтвердження права клініки надавати медичні послуги.</p>
      </div>
    </div>
  </section>

  <section class="section" id="privacy">
    <div class="container-narrow">
      <div class="legal-doc" data-reveal>
        <h2>Політика конфіденційності</h2>
        <p class="legal-updated">Останнє оновлення: 08 серпня 2026 р.</p>

        <h3>1. Загальні положення</h3>
        <p>ST Стоматологія (далі — «Клініка», «ми») поважає конфіденційність відвідувачів сайту st-dental.ua та пацієнтів. Ця Політика описує, які персональні дані ми збираємо, з якою метою їх обробляємо та які права ви маєте відповідно до Закону України «Про захист персональних даних» № 2297-VI.</p>

        <h3>2. Які дані ми збираємо</h3>
        <ul class="legal-list">
          <li>Ім'я та прізвище — коли ви заповнюєте форму запису на консультацію.</li>
          <li>Номер телефону — щоб адміністратор міг зв'язатися з вами для підтвердження запису.</li>
          <li>Коментар до заявки (необов'язково) — якщо ви лишаєте додаткову інформацію у формі.</li>
          <li>Технічні дані (тип пристрою, приблизна геолокація за IP, сторінка звернення) — автоматично, для аналітики та захисту від спам-заявок.</li>
        </ul>

        <h3>3. З якою метою ми обробляємо дані</h3>
        <ul class="legal-list">
          <li>Щоб зв'язатися з вами для підтвердження запису на консультацію.</li>
          <li>Щоб вести облік звернень і покращувати якість сервісу.</li>
          <li>Щоб виконувати вимоги законодавства України у сфері охорони здоров'я та бухгалтерського обліку.</li>
        </ul>
        <p>Ми не використовуємо ваші дані для розсилки реклами без окремої згоди та не продаємо їх третім особам.</p>

        <h3>4. Кому передаються дані</h3>
        <p>Заявки з форми запису надходять до внутрішньої системи сповіщень клініки (Telegram) через захищений сервер — номер телефону та ім'я передаються лише адміністратору клініки, відповідальному за запис пацієнтів. Сайт також використовує сторонні сервіси: Google Fonts (шрифти), Google Maps (карта проїзду) — під час їх завантаження ваш браузер може передавати технічні дані (IP-адресу) безпосередньо Google відповідно до їхньої політики конфіденційності.</p>

        <h3>5. Термін зберігання</h3>
        <p>Дані заявок зберігаються протягом строку, необхідного для надання медичних послуг та ведення медичної документації відповідно до законодавства України, але не довше 3 років з моменту останнього звернення, якщо інше не передбачено законом.</p>

        <h3>6. Ваші права</h3>
        <ul class="legal-list">
          <li>Отримати інформацію про те, які ваші дані ми обробляємо.</li>
          <li>Вимагати виправлення неточних даних.</li>
          <li>Відкликати згоду на обробку даних та вимагати їх видалення.</li>
          <li>Звернутися зі скаргою до Уповноваженого Верховної Ради України з прав людини у сфері захисту персональних даних.</li>
        </ul>
        <p>Щоб скористатися цими правами, напишіть на <a href="mailto:hello@st-dental.ua">hello@st-dental.ua</a> або зателефонуйте <a href="tel:+380972155077">+380 97 215 50 77</a>.</p>

        <h3>7. Файли cookie</h3>
        <p>Сайт може використовувати технічні cookie-файли для коректної роботи інтерфейсу (наприклад, запам'ятовування стану мобільного меню). Ми не використовуємо рекламні або трекінгові cookie третіх сторін без вашої явної згоди.</p>

        <p class="legal-disclaimer">⚠️ Це типовий шаблон політики конфіденційності, складений як відправна точка. Перед публікацією рекомендуємо перевірити його з юристом, який спеціалізується на медичному праві та захисті персональних даних в Україні — особливо розділи про строки зберігання медичної документації.</p>
      </div>
    </div>
  </section>

  <section class="section section--alt" id="license">
    <div class="container-narrow">
      <div class="legal-doc" data-reveal>
        <h2>Ліцензія на медичну практику</h2>
        <p>ST Стоматологія провадить діяльність на підставі ліцензії на провадження господарської діяльності з медичної практики, виданої Міністерством охорони здоров'я України.</p>

        <dl class="legal-license">
          <div><dt>Номер ліцензії</dt><dd>[ЗАМІНІТЬ — номер ліцензії МОЗ України]</dd></div>
          <div><dt>Дата видачі</dt><dd>[ЗАМІНІТЬ — дата видачі]</dd></div>
          <div><dt>Орган, що видав</dt><dd>Міністерство охорони здоров'я України</dd></div>
          <div><dt>Юридична назва</dt><dd>[ЗАМІНІТЬ — повна юридична назва ТОВ/ФОП]</dd></div>
          <div><dt>Код ЄДРПОУ / РНОКПП</dt><dd>[ЗАМІНІТЬ]</dd></div>
        </dl>

        <p class="legal-disclaimer">⚠️ Реальні реквізити ліцензії потрібно внести перед публікацією сайту — це важливо як для довіри пацієнтів, так і для SEO (Google перевіряє E-E-A-T для медичних сайтів). Перевірити ліцензію можна в <a href="https://cabinet.moz.gov.ua" target="_blank" rel="noopener noreferrer">реєстрі МОЗ України</a>.</p>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      <div class="cta-banner" data-reveal>
        <div>
          <h3>Є питання щодо обробки даних?</h3>
          <p>Напишіть нам — відповімо протягом одного робочого дня.</p>
        </div>
        <a href="mailto:hello@st-dental.ua" class="btn btn--gold">Написати на пошту</a>
      </div>
    </div>
  </section>
'''

render_page(
    path="legal/index.html",
    title="Політика конфіденційності та ліцензія МОЗ | ST Стоматологія",
    description="Політика конфіденційності ST Стоматологія та реквізити ліцензії МОЗ України на медичну практику.",
    canonical_path="/legal/",
    active_href=None,
    main_html=legal_main,
    depth=1,
    breadcrumbs=[("Головна","/"),("Юридична інформація","/legal/")],
)
