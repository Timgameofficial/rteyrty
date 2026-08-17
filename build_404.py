import sys
sys.path.insert(0, '.')
from generate_page import render_page

error_main = '''
  <section class="error-page">
    <div class="container">
      <div class="error-grid">
        <div>
          <p class="eyebrow" style="justify-content:center">Сторінку не знайдено</p>
          <p class="error-num" aria-hidden="true">404</p>
        </div>
        <div class="error-copy">
          <h1>Ця сторінка кудись зникла</h1>
          <p>Можливо, посилання застаріло або адреса введена з помилкою. Скористайтеся навігацією нижче — або поверніться на головну.</p>
          <div class="error-actions">
            <a href="/" class="btn btn--gold">На головну</a>
            <a href="#booking" class="btn" data-open-booking>Записатися на консультацію</a>
          </div>
          <nav class="error-links" aria-label="Швидкі посилання">
            <a href="/services/">Послуги</a>
            <a href="/prices/">Ціни</a>
            <a href="/team/">Команда</a>
            <a href="/portfolio/">Портфоліо</a>
            <a href="/reviews/">Відгуки</a>
            <a href="/faq/">Питання</a>
            <a href="/contact/">Контакти</a>
            <a href="/legal/">Юридична інформація</a>
          </nav>
        </div>
      </div>
    </div>
  </section>
'''

render_page(
    path="404.html",
    title="Сторінку не знайдено (404) | ST Стоматологія",
    description="Сторінку, яку ви шукали, не знайдено. Перейдіть на головну сторінку ST Стоматологія або скористайтеся навігацією.",
    canonical_path="/404.html",
    active_href=None,
    main_html=error_main,
    depth=0,
)
