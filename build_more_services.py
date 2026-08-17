import sys
sys.path.insert(0, '.')
from generate_page import render_page
from build_services import crumbs, related, cta_banner


# ============================================================
# ГІГІЄНА ТА ТЕРАПІЯ
# ============================================================
hygiene_main = f'''
  <section class="page-hero">
    <div class="container">
      {crumbs("Терапія та гігієна")}
      <div class="page-hero-grid">
        <div class="page-hero-copy">
          <p class="eyebrow" data-reveal>Послуга · Терапія та гігієна</p>
          <h1 data-reveal data-reveal-delay="1">Терапія та професійна гігієна</h1>
          <p data-reveal data-reveal-delay="2">Професійна гігієна Air Flow та ультразвук, лікування карієсу й пульпіту під мікроскопом. Основа для будь-якого подальшого естетичного лікування — і найпростіший спосіб запобігти візиту до хірурга.</p>
          <div class="page-hero-actions" data-reveal data-reveal-delay="3">
            <a href="#booking" class="btn btn--gold" data-open-booking data-service="Терапія та гігієна">Записатися на консультацію</a>
            <a href="#price" class="link-arrow">Вартість <svg aria-hidden="true"><use href="#icon-arrow"></use></svg></a>
          </div>
        </div>
        <figure class="page-hero-media" data-reveal data-reveal-delay="1">
          <img src="../../images/clinic-operatory-1.jpg" width="1600" height="853" alt="Кабінет професійної гігієни ST" loading="eager">
        </figure>
      </div>

      <dl class="spec-grid" data-reveal>
        <div class="spec-cell"><dt>Метод</dt><dd>Air Flow</dd></div>
        <div class="spec-cell"><dt>Візитів</dt><dd>1</dd></div>
        <div class="spec-cell"><dt>Мікроскоп</dt><dd>Так</dd></div>
        <div class="spec-cell"><dt>Періодичність</dt><dd>Раз на 6 міс.</dd></div>
      </dl>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container-narrow">
      <div class="section-head" data-reveal>
        <p class="eyebrow">Що входить</p>
        <h2>Професійна гігієна та лікування</h2>
        <p>Ми поєднуємо Air Flow (видалення нальоту повітряно-абразивною сумішшю) з ультразвуковим зняттям твердих відкладень. Лікування карієсу й кореневих каналів проводимо під мікроскопом — це дозволяє бачити мікротріщини та якісно герметизувати канал.</p>
      </div>
      <div class="journey-list" data-reveal>
        <div class="journey-step" data-reveal>
          <p class="jnum">01</p>
          <h4>Огляд і діагностика</h4>
          <p>Візуальний огляд, за потреби — прицільний знімок для оцінки стану під яснами.</p>
        </div>
        <div class="journey-step" data-reveal data-reveal-delay="1">
          <p class="jnum">02</p>
          <h4>Air Flow + ультразвук</h4>
          <p>Видалення нальоту та зубного каменя, полірування емалі.</p>
        </div>
        <div class="journey-step" data-reveal data-reveal-delay="2">
          <p class="jnum">03</p>
          <h4>Лікування за потреби</h4>
          <p>Карієс або пульпіт лікуємо в той самий візит під мікроскопом, з анестезією.</p>
        </div>
        <div class="journey-step" data-reveal data-reveal-delay="3">
          <p class="jnum">04</p>
          <h4>Рекомендації з догляду</h4>
          <p>Підбираємо засоби гігієни та дату наступного профілактичного візиту.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="price">
    <div class="container-narrow">
      <div class="section-head center" data-reveal>
        <p class="eyebrow">Вартість</p>
        <h2>Ціни на терапію та гігієну</h2>
      </div>
      <div class="price-accordion" data-reveal>
        <details class="acc" open>
          <summary>
            <span class="acc-title">Терапія та гігієна</span>
            <span class="acc-meta">3 позиції</span>
            <span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span>
          </summary>
          <div class="acc-body">
            <div class="price-row">
              <div class="price-row-top"><span class="name">Професійна гігієна</span><span class="leader"></span><span class="price">2 200 ₴</span></div>
              <span class="desc">Air Flow + ультразвук</span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">Лікування карієсу</span><span class="leader"></span><span class="price">від 2 100 ₴</span></div>
              <span class="desc">1 поверхня, під мікроскопом</span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">Ендодонтичне лікування</span><span class="leader"></span><span class="price">від 4 800 ₴</span></div>
              <span class="desc">1 канал, під мікроскопом</span>
            </div>
          </div>
        </details>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container-narrow">
      <div class="section-head" data-reveal>
        <p class="eyebrow">Питання</p>
        <h2>Що запитують про гігієну</h2>
      </div>
      <div class="faq-list" data-reveal>
        <details class="acc">
          <summary><span class="acc-title">Як часто потрібна професійна гігієна?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Рекомендуємо раз на 6 місяців — за наявності брекетів чи схильності до утворення каменя частіше, раз на 3–4 місяці.</p></div>
        </details>
        <details class="acc">
          <summary><span class="acc-title">Чи боляче лікувати канали під мікроскопом?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Ні, лікування проходить під анестезією. Мікроскоп не додає дискомфорту — навпаки, дозволяє лікарю працювати точніше й швидше.</p></div>
        </details>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      {cta_banner("Терапія та гігієна")}
      <h2 class="sr-only">Інші послуги</h2>
      <div class="related-services">
        {related("hygiene")}
      </div>
    </div>
  </section>
'''

render_page(
    path="services/hygiene/index.html",
    title="Професійна гігієна зубів у Кам'янському — ціна | ST",
    description="Професійна гігієна Air Flow у Кам'янському від 2 200 грн, лікування карієсу та каналів під мікроскопом. Терапія та гігієна в ST Стоматологія.",
    canonical_path="/services/hygiene/",
    active_href="/services/",
    main_html=hygiene_main,
    depth=2,
    breadcrumbs=[("Головна","/"),("Послуги","/services/"),("Терапія та гігієна","/services/hygiene/")],
)


# ============================================================
# ОРТОДОНТІЯ
# ============================================================
ortho_main = f'''
  <section class="page-hero">
    <div class="container">
      {crumbs("Ортодонтія")}
      <div class="page-hero-grid">
        <div class="page-hero-copy">
          <p class="eyebrow" data-reveal>Послуга · Ортодонтія</p>
          <h1 data-reveal data-reveal-delay="1">Ортодонтія та елайнери</h1>
          <p data-reveal data-reveal-delay="2">Вирівнювання прикусу прозорими елайнерами або керамічними брекетами. Цифрове планування показує прогнозований результат ще до початку лікування.</p>
          <div class="page-hero-actions" data-reveal data-reveal-delay="3">
            <a href="#booking" class="btn btn--gold" data-open-booking data-service="Ортодонтія">Записатися на консультацію</a>
            <a href="#price" class="link-arrow">Вартість <svg aria-hidden="true"><use href="#icon-arrow"></use></svg></a>
          </div>
        </div>
        <figure class="page-hero-media" data-reveal data-reveal-delay="1">
          <img src="../../images/clinic-operatory-2.jpg" width="1024" height="1536" alt="Кабінет ортодонтії ST" loading="eager">
        </figure>
      </div>

      <dl class="spec-grid" data-reveal>
        <div class="spec-cell"><dt>Метод</dt><dd>Елайнери / брекети</dd></div>
        <div class="spec-cell"><dt>Термін</dt><dd>6–18 міс.</dd></div>
        <div class="spec-cell"><dt>Прев'ю</dt><dd>3D-план</dd></div>
        <div class="spec-cell"><dt>Візити</dt><dd>Раз на 6–8 тижнів</dd></div>
      </dl>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container-narrow">
      <div class="section-head" data-reveal>
        <p class="eyebrow">Що це таке</p>
        <h2>Як працює цифрова ортодонтія</h2>
        <p>3D-сканування прикусу дозволяє побудувати покроковий план переміщення зубів і показати пацієнту прогнозований результат ще до початку лікування — незалежно від того, обрано прозорі елайнери чи керамічні брекети.</p>
      </div>
      <div class="journey-list" data-reveal>
        <div class="journey-step" data-reveal>
          <p class="jnum">01</p>
          <h4>3D-сканування прикусу</h4>
          <p>Цифровий відбиток і фотопротокол замінюють традиційні зліпки.</p>
        </div>
        <div class="journey-step" data-reveal data-reveal-delay="1">
          <p class="jnum">02</p>
          <h4>План лікування</h4>
          <p>Симуляція поетапного переміщення зубів із прогнозованим терміном.</p>
        </div>
        <div class="journey-step" data-reveal data-reveal-delay="2">
          <p class="jnum">03</p>
          <h4>Активне лікування</h4>
          <p>Заміна елайнерів кожні 1–2 тижні або корекція брекет-системи раз на 6–8 тижнів.</p>
        </div>
        <div class="journey-step" data-reveal data-reveal-delay="3">
          <p class="jnum">04</p>
          <h4>Ретенційний період</h4>
          <p>Ретейнери фіксують результат і запобігають поверненню зубів у вихідне положення.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="price">
    <div class="container-narrow">
      <div class="section-head center" data-reveal>
        <p class="eyebrow">Вартість</p>
        <h2>Ціни на ортодонтію</h2>
      </div>
      <div class="price-accordion" data-reveal>
        <details class="acc" open>
          <summary>
            <span class="acc-title">Ортодонтія</span>
            <span class="acc-meta">3 позиції</span>
            <span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span>
          </summary>
          <div class="acc-body">
            <div class="price-row">
              <div class="price-row-top"><span class="name">Елайнери (повний курс)</span><span class="leader"></span><span class="price">від 45 000 ₴</span></div>
              <span class="desc">включно з 3D-планом і ретейнерами</span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">Керамічні брекети</span><span class="leader"></span><span class="price">від 32 000 ₴</span></div>
              <span class="desc">на одну щелепу, без активацій</span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">Консультація ортодонта</span><span class="leader"></span><span class="price">безкоштовно</span></div>
              <span class="desc">з 3D-сканом прикусу</span>
            </div>
          </div>
        </details>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container-narrow">
      <div class="section-head" data-reveal>
        <p class="eyebrow">Питання</p>
        <h2>Що запитують про ортодонтію</h2>
      </div>
      <div class="faq-list" data-reveal>
        <details class="acc">
          <summary><span class="acc-title">Елайнери чи брекети — що краще?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Залежить від складності випадку. Елайнери непомітні й знімні, але вимагають дисципліни носіння 20+ годин на добу. Брекети ефективніші для складних випадків і не залежать від сумлінності пацієнта.</p></div>
        </details>
        <details class="acc">
          <summary><span class="acc-title">З якого віку можна почати лікування?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Ортодонтичне лікування підходить і дорослим, і дітям від 7–8 років (рання інтерцепція) — конкретний вік для старту визначає ортодонт на консультації.</p></div>
        </details>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      {cta_banner("Ортодонтія")}
      <h2 class="sr-only">Інші послуги</h2>
      <div class="related-services">
        {related("orthodontics")}
      </div>
    </div>
  </section>
'''

render_page(
    path="services/orthodontics/index.html",
    title="Ортодонтія, елайнери у Кам'янському — ціна | ST",
    description="Вирівнювання прикусу елайнерами від 45 000 грн або брекетами від 32 000 грн у Кам'янському. Цифрове 3D-планування результату. ST Стоматологія.",
    canonical_path="/services/orthodontics/",
    active_href="/services/",
    main_html=ortho_main,
    depth=2,
    breadcrumbs=[("Головна","/"),("Послуги","/services/"),("Ортодонтія","/services/orthodontics/")],
)


# ============================================================
# ДИТЯЧА СТОМАТОЛОГІЯ
# ============================================================
pediatric_main = f'''
  <section class="page-hero">
    <div class="container">
      {crumbs("Дитяча стоматологія")}
      <div class="page-hero-grid">
        <div class="page-hero-copy">
          <p class="eyebrow" data-reveal>Послуга · Дитяча стоматологія</p>
          <h1 data-reveal data-reveal-delay="1">Дитяча стоматологія</h1>
          <p data-reveal data-reveal-delay="2">Лікування молочних і постійних зубів у дітей — у спокійній обстановці, без страху й сліз. Перший візит завжди починається зі знайомства, а не з бормашини.</p>
          <div class="page-hero-actions" data-reveal data-reveal-delay="3">
            <a href="#booking" class="btn btn--gold" data-open-booking data-service="Дитяча стоматологія">Записатися на консультацію</a>
            <a href="#price" class="link-arrow">Вартість <svg aria-hidden="true"><use href="#icon-arrow"></use></svg></a>
          </div>
        </div>
        <figure class="page-hero-media" data-reveal data-reveal-delay="1">
          <img src="../../images/clinic-operatory-1.jpg" width="1600" height="853" alt="Дитячий кабінет ST" loading="eager">
        </figure>
      </div>

      <dl class="spec-grid" data-reveal>
        <div class="spec-cell"><dt>Вік</dt><dd>Від 1 року</dd></div>
        <div class="spec-cell"><dt>Перший візит</dt><dd>Знайомство</dd></div>
        <div class="spec-cell"><dt>Седація</dt><dd>За потреби</dd></div>
        <div class="spec-cell"><dt>Профілактика</dt><dd>Раз на 6 міс.</dd></div>
      </dl>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container-narrow">
      <div class="section-head" data-reveal>
        <p class="eyebrow">Наш підхід</p>
        <h2>Стоматологія без страху</h2>
        <p>Перший візит дитини до ST — це завжди знайомство з кабінетом та інструментами в ігровій формі, без жодних маніпуляцій. Це знімає тривогу й формує довіру, яка знадобиться на майбутніх візитах, коли лікування вже буде необхідне.</p>
      </div>
      <div class="journey-list" data-reveal>
        <div class="journey-step" data-reveal>
          <p class="jnum">01</p>
          <h4>Знайомство</h4>
          <p>Дитина знайомиться з кабінетом, кріслом та інструментами без тиску й поспіху.</p>
        </div>
        <div class="journey-step" data-reveal data-reveal-delay="1">
          <p class="jnum">02</p>
          <h4>Огляд</h4>
          <p>М'який огляд порожнини рота, оцінка стану молочних і постійних зубів.</p>
        </div>
        <div class="journey-step" data-reveal data-reveal-delay="2">
          <p class="jnum">03</p>
          <h4>Лікування за потреби</h4>
          <p>За потреби — лікування карієсу з анестезією, за показаннями — з седацією.</p>
        </div>
        <div class="journey-step" data-reveal data-reveal-delay="3">
          <p class="jnum">04</p>
          <h4>Профілактика</h4>
          <p>Герметизація фісур, фторування — щоб звести майбутнє лікування до мінімуму.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="price">
    <div class="container-narrow">
      <div class="section-head center" data-reveal>
        <p class="eyebrow">Вартість</p>
        <h2>Ціни на дитячу стоматологію</h2>
      </div>
      <div class="price-accordion" data-reveal>
        <details class="acc" open>
          <summary>
            <span class="acc-title">Дитяча стоматологія</span>
            <span class="acc-meta">3 позиції</span>
            <span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span>
          </summary>
          <div class="acc-body">
            <div class="price-row">
              <div class="price-row-top"><span class="name">Перша консультація</span><span class="leader"></span><span class="price">безкоштовно</span></div>
              <span class="desc">знайомство без маніпуляцій</span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">Лікування молочного зуба</span><span class="leader"></span><span class="price">від 1 600 ₴</span></div>
              <span class="desc">з анестезією</span>
            </div>
            <div class="price-row">
              <div class="price-row-top"><span class="name">Герметизація фісур</span><span class="leader"></span><span class="price">від 700 ₴</span></div>
              <span class="desc">за зуб, профілактика карієсу</span>
            </div>
          </div>
        </details>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container-narrow">
      <div class="section-head" data-reveal>
        <p class="eyebrow">Питання</p>
        <h2>Що запитують батьки</h2>
      </div>
      <div class="faq-list" data-reveal>
        <details class="acc">
          <summary><span class="acc-title">Чи варто лікувати молочні зуби?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Так. Molочний зуб з карієсом — джерело інфекції, яке може вплинути на зачаток постійного зуба, а передчасна втрата молочного зуба порушує прикус.</p></div>
        </details>
        <details class="acc">
          <summary><span class="acc-title">Чи можна батькам бути поруч під час прийому?</span><span class="acc-icon" aria-hidden="true"><svg><use href="#icon-plus"></use></svg></span></summary>
          <div class="acc-body"><p>Так, за бажанням дитини та батьків. Іноді для дітей старшого віку легше проходить прийом без присутності батьків у кабінеті — лікар оцінить це індивідуально.</p></div>
        </details>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container">
      {cta_banner("Дитяча стоматологія")}
      <h2 class="sr-only">Інші послуги</h2>
      <div class="related-services">
        {related("pediatric")}
      </div>
    </div>
  </section>
'''

render_page(
    path="services/pediatric/index.html",
    title="Дитяча стоматологія у Кам'янському — ціна | ST",
    description="Лікування молочних зубів у дітей у Кам'янському без страху й сліз. Перша консультація безкоштовно. Дитяча стоматологія ST від 1600 грн.",
    canonical_path="/services/pediatric/",
    active_href="/services/",
    main_html=pediatric_main,
    depth=2,
    breadcrumbs=[("Головна","/"),("Послуги","/services/"),("Дитяча стоматологія","/services/pediatric/")],
)
