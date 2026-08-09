import sys
sys.path.insert(0, '.')
from generate_page import render_page

def crumbs(current):
    return f'''<nav class="crumbs" aria-label="Хлібні крихти">
        <a href="/">Головна</a><span class="sep">/</span>
        <a href="/services/">Послуги</a><span class="sep">/</span>
        <span aria-current="page">{current}</span>
      </nav>'''

def related(exclude_slug):
    cards = {
        "veneers": ("/services/veneers/", "Преміум вініри", "Керамічні реставрації E.max під анатомію та тон емалі."),
        "implants": ("/services/implants/", "Цифрова імплантологія", "Nobel Biocare з хірургічним шаблоном за 3D-томографією."),
        "smile-design": ("/services/smile-design/", "Дизайн усмішки", "3D-прев'ю результату ще до початку лікування."),
        "hygiene": ("/services/hygiene/", "Терапія та гігієна", "Професійна гігієна Air Flow та лікування карієсу під мікроскопом."),
        "orthodontics": ("/services/orthodontics/", "Ортодонтія", "Елайнери та брекет-системи для вирівнювання прикусу."),
        "pediatric": ("/services/pediatric/", "Дитяча стоматологія", "Лікування молочних і постійних зубів без страху та сліз."),
    }
    out = []
    for slug, (href, title, desc) in cards.items():
        if slug == exclude_slug:
            continue
        if len(out) >= 3:
            break
        out.append(f'''<a class="related-card" href="{href}" data-reveal>
          <h4>{title}</h4>
          <p>{desc}</p>
          <span class="link-arrow">Детальніше <svg aria-hidden="true"><use href="#icon-arrow"></use></svg></span>
        </a>''')
    return "\n        ".join(out)

def cta_banner(service_name):
    return f'''<div class="cta-banner" data-reveal>
        <div>
          <h3>Обговоримо ваш випадок?</h3>
          <p>Консультація хірурга безкоштовна. Отримаєте план лікування й кошторис на першому візиті.</p>
        </div>
        <a href="#booking" class="btn btn--gold" data-open-booking data-service="{service_name}">Записатися на консультацію</a>
      </div>'''


# ============================================================
# 1. ПРЕМІУМ ВІНІРИ
# ============================================================
veneers_main = f'''
  <section class="page-hero">
    <div class="container">
      {crumbs("Преміум вініри")}
      <div class="page-hero-grid">
        <div class="page-hero-copy">
          <p class="eyebrow" data-reveal>Послуга · Естетична стоматологія</p>
          <h1 data-reveal data-reveal-delay="1">Преміум вініри E.max</h1>
          <p data-reveal data-reveal-delay="2">Керамічні накладки товщиною 0,3–0,5 мм, виготовлені індивідуально під анатомію обличчя й тон емалі. Мінімальне препарування зуба, максимально природний результат — вініри не відрізнити від власних зубів навіть зблизька.</p>
          <div class="page-hero-actions" data-reveal data-reveal-delay="3">
            <a href="#booking" class="btn btn--gold" data-open-booking data-service="Преміум вініри">Записатися на консультацію</a>
            <a href="#price" class="link-arrow">Вартість <svg aria-hidden="true"><use href="#icon-arrow"></use></svg></a>
          </div>
        </div>
        <figure class="page-hero-media" data-reveal data-reveal-delay="1">
          <img src="https://picsum.photos/seed/st-veneers-hero/900/1125" alt="Керамічні вініри E.max, готова робота" loading="eager">
        </figure>
      </div>

      <dl class="spec-grid" data-reveal>
        <div class="spec-cell"><dt>Матеріал</dt><dd>E.max</dd></div>
        <div class="spec-cell"><dt>Візитів</dt><dd>2</dd></div>
        <div class="spec-cell"><dt>Гарантія</dt><dd>7 років</dd></div>
        <div class="spec-cell"><dt>Товщина</dt><dd>0,3–0,5 мм</dd></div>
      </dl>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container-narrow">
      <div class="section-head" data-reveal>
        <p class="eyebrow">Що це таке</p>
        <h2>Як працюють вініри E.max</h2>
        <p>Вінір — це тонка керамічна накладка на передню поверхню зуба. На відміну від коронки, вона не вимагає обточування зуба «під конус» — знімається лише мінімальний шар емалі, порівнянний із товщиною нігтя.</p>
      </div>
      <div class="journey-list" data-reveal>
        <div class="journey-step" data-reveal>
          <p class="jnum">01</p>
          <h4>Діагностика й дизайн</h4>
          <p>Сканування, фотопротокол і цифрове моделювання майбутньої усмішки — mock-up, який можна приміряти ще до старту.</p>
        </div>
        <div class="journey-step" data-reveal data-reveal-delay="1">
          <p class="jnum">02</p>
          <h4>Препарування</h4>
          <p>Мінімальна обробка емалі під анестезією, зняття відбитків. Встановлення тимчасових накладок на час виготовлення.</p>
        </div>
        <div class="journey-step" data-reveal data-reveal-delay="2">
          <p class="jnum">03</p>
          <h4>Виготовлення в лабораторії</h4>
          <p>Кераміка E.max пресується та фарбується вручну технологом під ваш індивідуальний відтінок емалі.</p>
        </div>
        <div class="journey-step" data-reveal data-reveal-delay="3">
          <p class="jnum">04</p>
          <h4>Фіксація</h4>
          <p>Примірка, коригування форми та кольору, адгезивна фіксація на постійний цемент — результат одразу.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="price">
    <div class="container-narrow">
      <div class="section-head center" data-reveal>
        <p class="eyebrow">Вартість</p>
        <h2>Ціни на вініри</h2>
      </div>
      <div class="price-accordion" data-reveal>
        <details class="acc" open>
          <summary>
            <span class="acc-title">Преміум вініри</span>
            <span class="acc-meta">3 позиції</span>
            <span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span>
          </summary>
          <div class="acc-body">
            <div class="price-row">
              <div class="price-row-top"><span class="name">Вінір E.max</span><span class="leader"></span><span class="price">від 18 500 ₴</span></div>
              <span class="desc">за одиницю, кераміка пресована</span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">Цифровий mock-up</span><span class="leader"></span><span class="price">6 800 ₴</span></div>
              <span class="desc">3D-прев'ю результату, зараховується в остаточну вартість</span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">Тимчасові накладки</span><span class="leader"></span><span class="price">900 ₴</span></div>
              <span class="desc">за одиницю, на період виготовлення</span>
            </div>
          </div>
        </details>
      </div>
      <p class="form-fine" style="margin-top:1.5rem">Точна вартість залежить від кількості одиниць і складності випадку — фінальний кошторис ви отримаєте після діагностики.</p>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container-narrow">
      <div class="section-head" data-reveal>
        <p class="eyebrow">Питання</p>
        <h2>Що запитують про вініри</h2>
      </div>
      <div class="faq-list" data-reveal>
        <details class="acc">
          <summary><span class="acc-title">Чи боляче встановлювати вініри?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Ні. Препарування проходить під локальною анестезією і зачіпає мінімальний шар емалі. Більшість пацієнтів описує відчуття як тиск, а не біль.</p></div>
        </details>
        <details class="acc">
          <summary><span class="acc-title">Скільки служать вініри E.max?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>За коректної гігієни — 15–20 років. Наша гарантія на роботу — 7 років.</p></div>
        </details>
        <details class="acc">
          <summary><span class="acc-title">Чи можна відбілити вініри згодом?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Ні, кераміка не змінює колір з часом і не відбілюється — саме тому важливо підібрати відтінок ще на етапі mock-up.</p></div>
        </details>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      {cta_banner("Преміум вініри")}
      <h2 class="sr-only">Інші послуги</h2>
      <div class="related-services">
        {related("veneers")}
      </div>
    </div>
  </section>
'''

render_page(
    path="services/veneers/index.html",
    title="Вініри E.max у Кам'янському — ціна від 18 500 грн | ST Стоматологія",
    description="Вініри E.max у Кам'янському: ціна від 18 500 грн за одиницю, мінімальне препарування, гарантія 7 років, mock-up до старту лікування. Запис на консультацію.",
    canonical_path="/services/veneers/",
    active_href="/services/",
    main_html=veneers_main,
    depth=2,
)


# ============================================================
# 2. ЦИФРОВА ІМПЛАНТОЛОГІЯ
# ============================================================
implants_main = f'''
  <section class="page-hero">
    <div class="container">
      {crumbs("Цифрова імплантологія")}
      <div class="page-hero-grid">
        <div class="page-hero-copy">
          <p class="eyebrow" data-reveal>Послуга · Хірургія та імплантологія</p>
          <h1 data-reveal data-reveal-delay="1">Цифрова імплантологія</h1>
          <p data-reveal data-reveal-delay="2">Імплантація системами Nobel Biocare з хірургічним шаблоном, надрукованим за даними 3D-томографії. Точність постановки до десятої частки міліметра — і в 70% випадків без розрізу ясен.</p>
          <div class="page-hero-actions" data-reveal data-reveal-delay="3">
            <a href="#booking" class="btn btn--gold" data-open-booking data-service="Цифрова імплантологія">Записатися на консультацію</a>
            <a href="#price" class="link-arrow">Вартість <svg aria-hidden="true"><use href="#icon-arrow"></use></svg></a>
          </div>
        </div>
        <figure class="page-hero-media" data-reveal data-reveal-delay="1">
          <img src="https://picsum.photos/seed/st-implants-hero/900/1125" alt="Хірургічний шаблон для імплантації Nobel Biocare" loading="eager">
        </figure>
      </div>

      <dl class="spec-grid" data-reveal>
        <div class="spec-cell"><dt>Система</dt><dd>Nobel Biocare</dd></div>
        <div class="spec-cell"><dt>Хірургія</dt><dd>40–60 хв</dd></div>
        <div class="spec-cell"><dt>Гарантія</dt><dd>Довічна</dd></div>
        <div class="spec-cell"><dt>Без розрізу</dt><dd>70%</dd></div>
      </dl>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container-narrow">
      <div class="section-head" data-reveal>
        <p class="eyebrow">Що це таке</p>
        <h2>Як працює цифрова імплантація</h2>
        <p>Замість «на око» хірург спирається на 3D-модель щелепи: комп'ютер розраховує ідеальну вісь і глибину імпланта ще до операції, а надрукований шаблон переносить цей план у ротову порожнину з мінімальною похибкою.</p>
      </div>
      <div class="journey-list" data-reveal>
        <div class="journey-step" data-reveal>
          <p class="jnum">01</p>
          <h4>3D-томографія</h4>
          <p>Об'ємне сканування щелепи показує щільність кістки, розташування нервів і пазух.</p>
        </div>
        <div class="journey-step" data-reveal data-reveal-delay="1">
          <p class="jnum">02</p>
          <h4>Хірургічний шаблон</h4>
          <p>За даними томографії друкується індивідуальний шаблон з отворами під точну траєкторію імпланта.</p>
        </div>
        <div class="journey-step" data-reveal data-reveal-delay="2">
          <p class="jnum">03</p>
          <h4>Встановлення</h4>
          <p>40–60 хвилин на одиницю. У більшості випадків — без розрізу, через прокол ясна (flapless-протокол).</p>
        </div>
        <div class="journey-step" data-reveal data-reveal-delay="3">
          <p class="jnum">04</p>
          <h4>Остеоінтеграція й коронка</h4>
          <p>3–5 місяців на приживлення, далі — постійна коронка за 2 візити.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="price">
    <div class="container-narrow">
      <div class="section-head center" data-reveal>
        <p class="eyebrow">Вартість</p>
        <h2>Ціни на імплантацію</h2>
      </div>
      <div class="price-accordion" data-reveal>
        <details class="acc" open>
          <summary>
            <span class="acc-title">Імплантологія та хірургія</span>
            <span class="acc-meta">4 позиції</span>
            <span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span>
          </summary>
          <div class="acc-body">
            <div class="price-row">
              <div class="price-row-top"><span class="name">Імплант Nobel Biocare</span><span class="leader"></span><span class="price">від 34 900 ₴</span></div>
              <span class="desc">імплант + хірургічний етап</span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">3D-томографія</span><span class="leader"></span><span class="price">1 100 ₴</span></div>
              <span class="desc">повна щелепа</span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">Хірургічний шаблон</span><span class="leader"></span><span class="price">4 200 ₴</span></div>
              <span class="desc">індивідуальний друк за даними КТ</span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">Коронка на імпланті</span><span class="leader"></span><span class="price">від 16 000 ₴</span></div>
              <span class="desc">кераміка, індивідуальний абатмент</span>
            </div>
          </div>
        </details>
      </div>
      <p class="form-fine" style="margin-top:1.5rem">Консультація хірурга-імплантолога — безкоштовна. Кошторис формується після 3D-томографії.</p>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container-narrow">
      <div class="section-head" data-reveal>
        <p class="eyebrow">Питання</p>
        <h2>Що запитують про імплантацію</h2>
      </div>
      <div class="faq-list" data-reveal>
        <details class="acc">
          <summary><span class="acc-title">Скільки триває вся процедура?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Хірургічний етап — 40–60 хвилин. Повна реабілітація з остеоінтеграцією — від 3 до 5 місяців, після чого встановлюється постійна коронка.</p></div>
        </details>
        <details class="acc">
          <summary><span class="acc-title">Це боляче?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Операція проходить під місцевою анестезією — під час втручання відчуттів болю немає. У перші 1–2 дні можливий помірний дискомфорт, що знімається звичайним знеболювальним.</p></div>
        </details>
        <details class="acc">
          <summary><span class="acc-title">Що як не вистачає кістки?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>3D-томографія покаже це заздалегідь. За потреби виконуємо синус-ліфтинг або нарощування кістки — хірург обговорить це на консультації.</p></div>
        </details>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      {cta_banner("Цифрова імплантологія")}
      <h2 class="sr-only">Інші послуги</h2>
      <div class="related-services">
        {related("implants")}
      </div>
    </div>
  </section>
'''

render_page(
    path="services/implants/index.html",
    title="Імплантація зубів Nobel Biocare у Кам'янському — ціна | ST",
    description="Імплантація зубів Nobel Biocare у Кам'янському від 34 900 грн: хірургічний шаблон, 3D-планування, у 70% випадків без розрізу. Довічна гарантія.",
    canonical_path="/services/implants/",
    active_href="/services/",
    main_html=implants_main,
    depth=2,
)


# ============================================================
# 3. ДИЗАЙН УСМІШКИ
# ============================================================
smile_main = f'''
  <section class="page-hero">
    <div class="container">
      {crumbs("Дизайн усмішки")}
      <div class="page-hero-grid">
        <div class="page-hero-copy">
          <p class="eyebrow" data-reveal>Послуга · Цифрове моделювання</p>
          <h1 data-reveal data-reveal-delay="1">Дизайн усмішки</h1>
          <p data-reveal data-reveal-delay="2">Цифрове моделювання майбутньої усмішки ще до початку лікування. Ви приміряєте mock-up у роті й затверджуєте форму, довжину та колір зубів — і лише тоді ми починаємо роботу.</p>
          <div class="page-hero-actions" data-reveal data-reveal-delay="3">
            <a href="#booking" class="btn btn--gold" data-open-booking data-service="Дизайн усмішки">Записатися на консультацію</a>
            <a href="#price" class="link-arrow">Вартість <svg aria-hidden="true"><use href="#icon-arrow"></use></svg></a>
          </div>
        </div>
        <figure class="page-hero-media" data-reveal data-reveal-delay="1">
          <img src="https://picsum.photos/seed/st-smile-hero/900/1125" alt="Цифрове моделювання дизайну усмішки" loading="eager">
        </figure>
      </div>

      <dl class="spec-grid" data-reveal>
        <div class="spec-cell"><dt>Прев'ю</dt><dd>3D</dd></div>
        <div class="spec-cell"><dt>Примірка</dt><dd>Mock-up</dd></div>
        <div class="spec-cell"><dt>Затвердження</dt><dd>До старту</dd></div>
        <div class="spec-cell"><dt>Термін</dt><dd>3–5 днів</dd></div>
      </dl>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container-narrow">
      <div class="section-head" data-reveal>
        <p class="eyebrow">Що це таке</p>
        <h2>Як працює цифровий дизайн усмішки</h2>
        <p>Ми скануємо ваш прикус і обличчя, будуємо 3D-модель майбутньої усмішки з урахуванням пропорцій, і виготовляємо тимчасовий mock-up — накладки, які можна «приміряти» в роті ще до початку основного лікування.</p>
      </div>
      <div class="journey-list" data-reveal>
        <div class="journey-step" data-reveal>
          <p class="jnum">01</p>
          <h4>Сканування та фото</h4>
          <p>Цифровий відбиток прикусу, фотопротокол обличчя й посмішки в різних ракурсах.</p>
        </div>
        <div class="journey-step" data-reveal data-reveal-delay="1">
          <p class="jnum">02</p>
          <h4>3D-моделювання</h4>
          <p>Дизайнер будує кілька варіантів форми й довжини зубів з урахуванням рис обличчя.</p>
        </div>
        <div class="journey-step" data-reveal data-reveal-delay="2">
          <p class="jnum">03</p>
          <h4>Примірка mock-up</h4>
          <p>Тимчасові накладки з обраного дизайну фіксуються в роті — ви бачите й відчуваєте результат наживо.</p>
        </div>
        <div class="journey-step" data-reveal data-reveal-delay="3">
          <p class="jnum">04</p>
          <h4>Затвердження й лікування</h4>
          <p>Після вашого «так» дизайн передається в роботу — вініри, реставрації або ортодонтія за затвердженим планом.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="price">
    <div class="container-narrow">
      <div class="section-head center" data-reveal>
        <p class="eyebrow">Вартість</p>
        <h2>Ціни на дизайн усмішки</h2>
      </div>
      <div class="price-accordion" data-reveal>
        <details class="acc" open>
          <summary>
            <span class="acc-title">Дизайн усмішки</span>
            <span class="acc-meta">2 позиції</span>
            <span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span>
          </summary>
          <div class="acc-body">
            <div class="price-row">
              <div class="price-row-top"><span class="name">Цифровий дизайн усмішки</span><span class="leader"></span><span class="price">6 800 ₴</span></div>
              <span class="desc">3D-моделювання, зараховується в подальше лікування</span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">Mock-up (примірка)</span><span class="leader"></span><span class="price">від 450 ₴/зуб</span></div>
              <span class="desc">тимчасові накладки для примірки в роті</span>
            </div>
          </div>
        </details>
      </div>
      <p class="form-fine" style="margin-top:1.5rem">Вартість дизайну зараховується в чек подальшого лікування (вініри, реставрація, ортодонтія).</p>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container-narrow">
      <div class="section-head" data-reveal>
        <p class="eyebrow">Питання</p>
        <h2>Що запитують про дизайн усмішки</h2>
      </div>
      <div class="faq-list" data-reveal>
        <details class="acc">
          <summary><span class="acc-title">Чи зобов'язує дизайн до лікування?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Ні. Ви можете затвердити, попросити зміни або відмовитися після примірки mock-up — жодних зобов'язань до підписання плану лікування.</p></div>
        </details>
        <details class="acc">
          <summary><span class="acc-title">Скільки триває процес моделювання?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Від сканування до примірки mock-up — зазвичай 3–5 днів, залежно від складності випадку.</p></div>
        </details>
        <details class="acc">
          <summary><span class="acc-title">Дизайн підходить для будь-якого лікування?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Так — його використовують і для вінірів, і для реставрацій, і як орієнтир для ортодонтичного лікування.</p></div>
        </details>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      {cta_banner("Дизайн усмішки")}
      <h2 class="sr-only">Інші послуги</h2>
      <div class="related-services">
        {related("smile-design")}
      </div>
    </div>
  </section>
'''

render_page(
    path="services/smile-design/index.html",
    title="Дизайн усмішки у Кам'янському — 3D mock-up | ST Стоматологія",
    description="Цифровий дизайн усмішки у Кам'янському від 6 800 грн: 3D-моделювання, примірка mock-up ще до початку лікування. Запис на консультацію.",
    canonical_path="/services/smile-design/",
    active_href="/services/",
    main_html=smile_main,
    depth=2,
)
