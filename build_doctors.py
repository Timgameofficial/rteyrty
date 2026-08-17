import sys
sys.path.insert(0, '.')
from generate_page import render_page

def crumb_doctor(name):
    return f'''<nav class="crumbs" aria-label="Хлібні крихти">
        <a href="/">Головна</a><span class="sep">/</span>
        <a href="/team/">Команда</a><span class="sep">/</span>
        <span aria-current="page">{name}</span>
      </nav>'''


# ============================================================
# Олена Крамар — естетична стоматологія / вініри
# ============================================================
olena_main = f'''
  <section class="page-hero">
    <div class="container">
      {crumb_doctor("Олена Крамар")}
      <div class="doctor-hero-grid">
        <div class="doctor-portrait" data-reveal>
          <div class="team-frame">
            <img src="../../images/doctor-olena.png" width="600" height="750" alt="Олена Крамар — лікар-стоматолог ST, спеціаліст з естетичної реставрації" loading="eager" decoding="async">
          </div>
          <div class="doctor-portrait-meta">
            <div><span class="num">18</span><span class="label">років практики</span></div>
            <div><span class="num">400+</span><span class="label">кейсів реставрації</span></div>
          </div>
        </div>
        <div class="doctor-bio" data-reveal data-reveal-delay="1">
          <span class="doctor-role-tag">Естетична стоматологія</span>
          <h1>Олена Крамар</h1>
          <p>Лікар-стоматолог з 18-річною практикою, спеціалізується на естетичній реставрації та мікропротезуванні. Понад 400 успішних кейсів — від одиничних художніх реставрацій до комплексного оновлення усмішки вінірами E.max.</p>
          <p>Олена веде напрям преміум вінірів у ST: від первинної діагностики й цифрового mock-up до фінальної фіксації. Працює за принципом мінімального втручання — знімає рівно стільки емалі, скільки потрібно для природного результату.</p>

          <a href="/services/veneers/" class="doctor-service-link">
            Веде напрям «Преміум вініри»
            <svg aria-hidden="true"><use href="#icon-arrow"></use></svg>
          </a>

          <div class="doctor-pullquote">
            <p>Найкращий вінір — той, якого ніхто не помічає. Моя мета не «нові зуби», а ваша власна усмішка, тільки без вад.</p>
            <cite>— Олена Крамар</cite>
          </div>

          <h2 style="font-size:1.3rem; margin-bottom:1.25rem;">Освіта та кваліфікація</h2>
          <div class="doctor-timeline">
            <div class="doctor-timeline-item">
              <span class="yr">2006</span>
              <h4>Національний медичний університет ім. О. О. Богомольця</h4>
              <p>Диплом лікаря-стоматолога, спеціалізація «Стоматологія».</p>
            </div>
            <div class="doctor-timeline-item">
              <span class="yr">2011</span>
              <h4>Курс естетичної реставрації, Мюнхен</h4>
              <p>Підвищення кваліфікації з мікропротезування та художньої реставрації композитами.</p>
            </div>
            <div class="doctor-timeline-item">
              <span class="yr">2017</span>
              <h4>Сертифікація E.max, Ivoclar Vivadent</h4>
              <p>Офіційна сертифікація з протоколу виготовлення та фіксації вінірів E.max.</p>
            </div>
            <div class="doctor-timeline-item">
              <span class="yr">2023</span>
              <h4>Керівник напряму естетичної стоматології ST</h4>
              <p>Веде повний цикл естетичних кейсів клініки — від дизайну до фіксації.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="cta-banner" data-reveal>
        <div>
          <h3>Хочете консультацію в Олени?</h3>
          <p>Перша консультація — безкоштовна, без зобов'язань.</p>
        </div>
        <a href="#booking" class="btn btn--gold" data-open-booking data-service="Преміум вініри">Записатися на консультацію</a>
      </div>
    </div>
  </section>
'''

render_page(
    path="team/oleksandra-kramar/index.html",
    title="Олена Крамар — лікар-стоматолог, вініри | ST",
    description="Олена Крамар — лікар-стоматолог ST у Кам'янському, 18 років практики, понад 400 кейсів естетичної реставрації. Спеціалізація: вініри E.max.",
    canonical_path="/team/oleksandra-kramar/",
    active_href="/team/",
    main_html=olena_main,
    depth=2,
    breadcrumbs=[("Головна","/"),("Команда","/team/"),("Олена Крамар","/team/oleksandra-kramar/")],
)


# ============================================================
# Андрій Тарасенко — хірургія та імплантологія
# ============================================================
andrii_main = f'''
  <section class="page-hero">
    <div class="container">
      {crumb_doctor("Андрій Тарасенко")}
      <div class="doctor-hero-grid">
        <div class="doctor-portrait" data-reveal>
          <div class="team-frame">
            <img src="../../images/doctor-andrii.png" width="600" height="750" alt="Андрій Тарасенко — лікар-хірург-імплантолог ST" loading="eager" decoding="async">
          </div>
          <div class="doctor-portrait-meta">
            <div><span class="num">22</span><span class="label">роки практики</span></div>
            <div><span class="num">900+</span><span class="label">встановлених імплантів</span></div>
          </div>
        </div>
        <div class="doctor-bio" data-reveal data-reveal-delay="1">
          <span class="doctor-role-tag">Хірургія та імплантологія</span>
          <h1>Андрій Тарасенко</h1>
          <p>Хірург-імплантолог з 22-річним досвідом, сертифікований спеціаліст системи Nobel Biocare. Проводить складні випадки повної реабілітації прикусу, зокрема протоколи All-on-4 і All-on-6.</p>
          <p>Андрій веде напрям цифрової імплантології в ST: планує кожен випадок за даними 3D-томографії та хірургічного шаблону, що дозволяє в більшості випадків обходитись без розрізу ясен.</p>

          <a href="/services/implants/" class="doctor-service-link">
            Веде напрям «Цифрова імплантологія»
            <svg aria-hidden="true"><use href="#icon-arrow"></use></svg>
          </a>

          <div class="doctor-pullquote">
            <p>Хірургічний шаблон прибирає здогадки з операції. Ми знаємо точну траєкторію імпланта ще до того, як пацієнт сів у крісло.</p>
            <cite>— Андрій Тарасенко</cite>
          </div>

          <h2 style="font-size:1.3rem; margin-bottom:1.25rem;">Освіта та кваліфікація</h2>
          <div class="doctor-timeline">
            <div class="doctor-timeline-item">
              <span class="yr">2002</span>
              <h4>Національний медичний університет ім. О. О. Богомольця</h4>
              <p>Диплом лікаря-стоматолога, інтернатура за фахом «Хірургічна стоматологія».</p>
            </div>
            <div class="doctor-timeline-item">
              <span class="yr">2009</span>
              <h4>Курс імплантології, Nobel Biocare Institute</h4>
              <p>Базова та розширена сертифікація з протоколів імплантації Nobel Biocare.</p>
            </div>
            <div class="doctor-timeline-item">
              <span class="yr">2015</span>
              <h4>Стажування з протоколу All-on-4/All-on-6</h4>
              <p>Стажування в європейській клініці з повної реабілітації беззубих щелеп.</p>
            </div>
            <div class="doctor-timeline-item">
              <span class="yr">2021</span>
              <h4>Керівник хірургічного напряму ST</h4>
              <p>Відповідає за всі хірургічні протоколи та навчання молодших лікарів клініки.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="cta-banner" data-reveal>
        <div>
          <h3>Хочете консультацію в Андрія?</h3>
          <p>Консультація хірурга-імплантолога — безкоштовна.</p>
        </div>
        <a href="#booking" class="btn btn--gold" data-open-booking data-service="Цифрова імплантологія">Записатися на консультацію</a>
      </div>
    </div>
  </section>
'''

render_page(
    path="team/andrii-tarasenko/index.html",
    title="Андрій Тарасенко — хірург-імплантолог | ST",
    description="Андрій Тарасенко — хірург-імплантолог ST у Кам'янському, 22 роки практики, понад 900 встановлених імплантів. Сертифікований спеціаліст Nobel Biocare.",
    canonical_path="/team/andrii-tarasenko/",
    active_href="/team/",
    main_html=andrii_main,
    depth=2,
    breadcrumbs=[("Головна","/"),("Команда","/team/"),("Андрій Тарасенко","/team/andrii-tarasenko/")],
)


# ============================================================
# Марія Войтенко — ортодонтія та дизайн усмішки
# ============================================================
mariia_main = f'''
  <section class="page-hero">
    <div class="container">
      {crumb_doctor("Марія Войтенко")}
      <div class="doctor-hero-grid">
        <div class="doctor-portrait" data-reveal>
          <div class="team-frame">
            <img src="../../images/doctor-mariia.png" width="600" height="750" alt="Марія Войтенко — лікар-ортодонт ST" loading="eager" decoding="async">
          </div>
          <div class="doctor-portrait-meta">
            <div><span class="num">14</span><span class="label">років практики</span></div>
            <div><span class="num">600+</span><span class="label">дизайн-проєктів усмішки</span></div>
          </div>
        </div>
        <div class="doctor-bio" data-reveal data-reveal-delay="1">
          <span class="doctor-role-tag">Ортодонтія та дизайн усмішки</span>
          <h1>Марія Войтенко</h1>
          <p>Лікар-ортодонт з 14-річною практикою, автор індивідуального протоколу цифрового дизайну усмішки ST. Веде пацієнтів від первинного 3D-сканування до примірки mock-up і фінального затвердження плану лікування.</p>
          <p>Марія працює на стику ортодонтії та естетики: підбирає форму й положення зубів так, щоб результат гармоніював із рисами обличчя конкретного пацієнта, а не з шаблоном «ідеальної усмішки».</p>

          <a href="/services/smile-design/" class="doctor-service-link">
            Веде напрям «Дизайн усмішки»
            <svg aria-hidden="true"><use href="#icon-arrow"></use></svg>
          </a>

          <div class="doctor-pullquote">
            <p>Коли пацієнт бачить mock-up своєї майбутньої усмішки ще до початку лікування — зникає найбільший страх: «а раптом мені не сподобається результат».</p>
            <cite>— Марія Войтенко</cite>
          </div>

          <h2 style="font-size:1.3rem; margin-bottom:1.25rem;">Освіта та кваліфікація</h2>
          <div class="doctor-timeline">
            <div class="doctor-timeline-item">
              <span class="yr">2010</span>
              <h4>Національний медичний університет ім. О. О. Богомольця</h4>
              <p>Диплом лікаря-стоматолога, інтернатура за фахом «Ортодонтія».</p>
            </div>
            <div class="doctor-timeline-item">
              <span class="yr">2014</span>
              <h4>Сертифікація з елайнер-терапії</h4>
              <p>Навчання з планування та ведення пацієнтів на прозорих капах.</p>
            </div>
            <div class="doctor-timeline-item">
              <span class="yr">2019</span>
              <h4>Курс цифрового дизайну усмішки (DSD)</h4>
              <p>Спеціалізація з протоколу Digital Smile Design — 3D-моделювання результату до лікування.</p>
            </div>
            <div class="doctor-timeline-item">
              <span class="yr">2022</span>
              <h4>Автор протоколу дизайну усмішки ST</h4>
              <p>Розробила внутрішній протокол клініки для передбачуваного результату естетичного лікування.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="cta-banner" data-reveal>
        <div>
          <h3>Хочете консультацію в Марії?</h3>
          <p>Перша консультація — безкоштовна, без зобов'язань.</p>
        </div>
        <a href="#booking" class="btn btn--gold" data-open-booking data-service="Дизайн усмішки">Записатися на консультацію</a>
      </div>
    </div>
  </section>
'''

render_page(
    path="team/mariia-voitenko/index.html",
    title="Марія Войтенко — лікар-ортодонт | ST",
    description="Марія Войтенко — лікар-ортодонт ST у Кам'янському, 14 років практики, автор протоколу цифрового дизайну усмішки. Понад 600 проєктів.",
    canonical_path="/team/mariia-voitenko/",
    active_href="/team/",
    main_html=mariia_main,
    depth=2,
    breadcrumbs=[("Головна","/"),("Команда","/team/"),("Марія Войтенко","/team/mariia-voitenko/")],
)
