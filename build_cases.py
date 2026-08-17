import sys
sys.path.insert(0, '.')
from generate_page import render_page

CASES = [
    dict(
        slug="kompleksna-restavratsiya",
        category="Вініри та реставрація",
        title="Комплексна реставрація зубного ряду",
        before="case-1-before.jpg", after="case-1-after.jpg", w=1000, h=474,
        before_alt="Стан зубного ряду пацієнта до комплексної реставрації",
        after_alt="Стан зубного ряду пацієнта після комплексної реставрації",
        spec=[("Матеріал", "Кераміка / композит"), ("Візитів", "4"), ("Гарантія", "5 років"), ("Термін", "3 тижні")],
        narrative=[
            "Пацієнт звернувся зі скаргами на потемніння емалі та нерівний край фронтальної групи зубів — результат багаторічного впливу кави та відсутності професійної гігієни.",
            "План лікування включав професійну гігієну, вибіркове відбілювання та комплексну естетичну реставрацію фронтальної групи. Кожен етап узгоджувався з пацієнтом за допомогою фотопротоколу.",
            "Результат: рівний, природний колір і форма зубного ряду без відчуття «штучності» — саме цього прагнуть більшість пацієнтів, які звертаються по естетичну реставрацію.",
        ],
        service_href="/services/veneers/", service_label="Преміум вініри",
    ),
    dict(
        slug="vinory-emax-6-odynyts",
        category="Вініри та реставрація",
        title="Вініри E.max, 6 одиниць",
        before="portfolio-veneers-2-before.png", after="portfolio-veneers-2-after.png", w=900, h=700,
        before_alt="Стан зубів пацієнта до встановлення вінірів E.max",
        after_alt="Стан зубів пацієнта після встановлення вінірів E.max",
        spec=[("Матеріал", "E.max"), ("Візитів", "2"), ("Гарантія", "7 років"), ("Термін", "10 днів")],
        narrative=[
            "Запит пацієнта — закрити діастему (проміжок між центральними різцями) та вирівняти відтінок емалі без ортодontичного лікування, яке зайняло б понад рік.",
            "Шість вінірів E.max товщиною 0,3–0,5 мм дозволили закрити проміжок і уніфікувати колір фронтальної групи за два візити — без обточування сусідніх зубів під конус.",
            "Цифровий mock-up на етапі планування дав змогу пацієнту побачити й затвердити форму ще до фіксації постійних вінірів.",
        ],
        service_href="/services/veneers/", service_label="Преміум вініри",
    ),
    dict(
        slug="khudozhnia-restavratsiya",
        category="Вініри та реставрація",
        title="Художня реставрація",
        before="portfolio-veneers-3-before.png", after="portfolio-veneers-3-after.png", w=900, h=700,
        before_alt="Стан зубів пацієнта до художньої реставрації",
        after_alt="Стан зубів пацієнта після художньої реставрації",
        spec=[("Матеріал", "Композит"), ("Візитів", "1"), ("Гарантія", "3 роки"), ("Термін", "1 день")],
        narrative=[
            "Пацієнт звернувся невдовзі після сколу центрального різця — типова травма, з якою стикаються дорослі пацієнти при падінні чи вживанні твердої їжі.",
            "Художня реставрація композитним матеріалом дозволила відновити форму зуба за один візит, підібравши відтінок за шкалою кольору просто в кріслі.",
            "Це найшвидший спосіб відновлення для точкових сколів — на відміну від вінірів, композит наносять і моделюють одразу, без лабораторного етапу.",
        ],
        service_href="/services/veneers/", service_label="Преміум вініри",
    ),
    dict(
        slug="implantatsiya-nobel-biocare",
        category="Імплантологія",
        title="Імплантація Nobel Biocare",
        before="portfolio-implants-1-before.png", after="portfolio-implants-1-after.png", w=900, h=700,
        before_alt="Стан прикусу пацієнта до імплантації",
        after_alt="Стан прикусу пацієнта після імплантації та протезування",
        spec=[("Система", "Nobel Biocare"), ("Візитів", "3"), ("Гарантія", "Довічна"), ("Термін", "4 місяці")],
        narrative=[
            "Пацієнт втратив два зуби в бічній ділянці нижньої щелепи кілька років тому й звик жувати на протилежному боці — типова компенсаторна звичка, яка з часом навантажує здорові зуби.",
            "3D-томографія підтвердила достатній об'єм кістки для імплантації без додаткового нарощення. Хірургічний шаблон дозволив встановити два імпланти Nobel Biocare за одну операцію без розрізу ясен.",
            "Після 4 місяців остеоінтеграції встановлено постійні керамічні коронки — пацієнт повернувся до звичного двостороннього жування.",
        ],
        service_href="/services/implants/", service_label="Цифрова імплантологія",
    ),
    dict(
        slug="povna-reabilitatsiya-all-on-6",
        category="Імплантологія",
        title="Повна реабілітація на імплантах",
        before="portfolio-implants-2-before.png", after="portfolio-implants-2-after.png", w=900, h=700,
        before_alt="Стан щелепи пацієнта до повної реабілітації",
        after_alt="Стан щелепи пацієнта після повної реабілітації на імплантах",
        spec=[("Протокол", "All-on-6"), ("Візитів", "5"), ("Гарантія", "Довічна"), ("Термін", "6 місяців")],
        narrative=[
            "Пацієнт звернувся з практично повною втратою зубів верхньої щелепи та зношеним знімним протезом, який погано фіксувався й ускладнював харчування.",
            "За протоколом All-on-6 встановлено шість імплантів, що стали опорою для незнімного мостоподібного протеза на всю щелепу — рішення, яке відновлює й естетику, і повноцінну жувальну функцію.",
            "Це один зі складніших випадків повної реабілітації — вимагає точного 3D-планування й досвіду хірурга для рівномірного розподілу навантаження між опорними імплантами.",
        ],
        service_href="/services/implants/", service_label="Цифрова імплантологія",
    ),
    dict(
        slug="odynochna-implantatsiya",
        category="Імплантологія",
        title="Одиночна імплантація",
        before="portfolio-implants-3-before.png", after="portfolio-implants-3-after.png", w=900, h=700,
        before_alt="Стан зуба пацієнта до одиночної імплантації",
        after_alt="Стан зуба пацієнта після одиночної імплантації",
        spec=[("Система", "Nobel Biocare"), ("Візитів", "2"), ("Гарантія", "Довічна"), ("Термін", "3 місяці")],
        narrative=[
            "Втрата одного зуба в естетичній зоні (видимій при посмішці) — випадок, де особливо важлива точність позиціонування імпланта.",
            "Завдяки flapless-протоколу (без розрізу ясен) операція пройшла за 40 хвилин, а тимчасова коронка встановлена одразу — пацієнт не залишався без зуба в естетичній зоні на час загоєння.",
            "Через 3 місяці остеоінтеграції встановлено постійну керамічну коронку з індивідуальним абатментом, підібраним під контур ясна пацієнта.",
        ],
        service_href="/services/implants/", service_label="Цифрова імплантологія",
    ),
]


def render_case(case, index):
    prev_case = CASES[(index - 1) % len(CASES)]
    next_case = CASES[(index + 1) % len(CASES)]

    spec_html = "\n        ".join(
        f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k, v in case["spec"]
    )
    narrative_html = "\n        ".join(f"<p>{p}</p>" for p in case["narrative"])

    main_html = f'''
  <section class="page-hero">
    <div class="container">
      <nav class="crumbs" aria-label="Хлібні крихти">
        <a href="/">Головна</a><span class="sep">/</span>
        <a href="/portfolio/">Портфоліо</a><span class="sep">/</span>
        <span aria-current="page">{case["title"]}</span>
      </nav>
      <div class="page-hero-copy" style="max-width:52rem">
        <p class="eyebrow" data-reveal>{case["category"]}</p>
        <h1 data-reveal data-reveal-delay="1">{case["title"]}</h1>
        <p data-reveal data-reveal-delay="2">Перетягніть повзунок, щоб побачити трансформацію.</p>
      </div>

      <div class="case-hero-slider" data-reveal>
        <div class="ba-slider" style="--ba-pos:50%" data-ba>
          <img class="ba-before" src="../../images/{case["before"]}" width="{case["w"]}" height="{case["h"]}" alt="{case["before_alt"]}" loading="eager" decoding="async">
          <img class="ba-after" src="../../images/{case["after"]}" width="{case["w"]}" height="{case["h"]}" alt="{case["after_alt"]}" loading="eager" decoding="async">
          <span class="ba-tag before">До</span>
          <span class="ba-tag after">Після</span>
          <div class="ba-handle" aria-hidden="true"><span class="ba-handle-grip"><svg><use href="#icon-drag"></use></svg></span></div>
          <input type="range" min="0" max="100" value="50" step="0.1" class="ba-range" aria-label="Повзунок порівняння до і після">
        </div>
      </div>

      <dl class="case-spec-sheet" data-reveal>
        {spec_html}
      </dl>
    </div>
  </section>

  <section class="section">
    <div class="container-narrow">
      <div class="case-narrative" data-reveal>
        <h2>Про випадок</h2>
        {narrative_html}
      </div>

      <div class="case-nav">
        <a href="/portfolio/{prev_case["slug"]}/">
          <svg aria-hidden="true" style="transform:scaleX(-1)"><use href="#icon-arrow"></use></svg>
          {prev_case["title"]}
        </a>
        <a href="/portfolio/{next_case["slug"]}/">
          {next_case["title"]}
          <svg aria-hidden="true"><use href="#icon-arrow"></use></svg>
        </a>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="cta-banner" data-reveal>
        <div>
          <h3>Хочете такий самий результат?</h3>
          <p>Консультація хірурга безкоштовна — обговоримо ваш випадок.</p>
        </div>
        <a href="#booking" class="btn btn--gold" data-open-booking data-service="{case["service_label"]}">Записатися на консультацію</a>
      </div>
      <p class="form-fine" style="margin-top:2rem">Фото використані за згодою пацієнта. Результат індивідуальний і залежить від вихідного клінічного стану.</p>
    </div>
  </section>
'''

    render_page(
        path=f'portfolio/{case["slug"]}/index.html',
        title=f'{case["title"]} — фото до і після | ST Стоматологія',
        description=f"{case['title']}: реальний клінічний випадок ST Стоматологія у Кам'янському. Фото до і після, деталі лікування, гарантія.",
        canonical_path=f'/portfolio/{case["slug"]}/',
        active_href="/portfolio/",
        main_html=main_html,
        depth=2,
        breadcrumbs=[("Головна","/"),("Портфоліо","/portfolio/"),(case["title"], f'/portfolio/{case["slug"]}/')],
    )


for i, c in enumerate(CASES):
    render_case(c, i)
