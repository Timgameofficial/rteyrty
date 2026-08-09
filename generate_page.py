import re

SVG_SPRITE = open('_partial_svg.html', encoding='utf-8').read()
HEADER = open('_partial_header.html', encoding='utf-8').read()
FOOTER = open('_partial_footer.html', encoding='utf-8').read()

def build_chrome(depth, active_href=None):
    """depth = сколько уровней вложенности от корня (1 = /services/, 2 = /services/veneers/)"""
    prefix = "../" * depth  # относительный путь к корню сайта
    home_href = "/" if depth == 0 else prefix  # на кореневих сторінках (напр. 404) — явний "/"

    header = HEADER
    footer = FOOTER

    # логотип и внутристраничные якоря ведуть на головну
    header = header.replace('href="#top"', f'href="{home_href}"')
    footer = footer.replace('href="#top"', f'href="{home_href}"')

    for hash_id in ["clinic", "reviews", "faq", "results", "contact"]:
        header = header.replace(f'href="#{hash_id}"', f'href="{home_href}#{hash_id}"')
        footer = footer.replace(f'href="#{hash_id}"', f'href="{home_href}#{hash_id}"')

    # абсолютні шляхи /services/ /team/ /prices/ лишаються як є (від кореня сайту)

    # tel:/mailto:/#booking/data-open-booking чіпати не треба

    # підсвітити активний пункт меню
    if active_href:
        header = header.replace(
            f'href="{active_href}" class="nav-link"',
            f'href="{active_href}" class="nav-link is-active"'
        )

    css_href = f"{prefix}style.css"
    js_href = f"{prefix}app.js"
    footer = footer.replace('src="app.js"', f'src="{js_href}"')

    return header, footer, css_href, js_href, prefix


def render_page(*, path, title, description, canonical_path, active_href, main_html, depth,
                 og_image="og-cover.jpg", schema_extra=""):
    header, footer, css_href, js_href, prefix = build_chrome(depth, active_href)

    html = f"""<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="https://st-dental.ua{canonical_path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="ST Стоматологія">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="https://st-dental.ua/{og_image}">
<meta property="og:url" content="https://st-dental.ua{canonical_path}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0E0D0B">
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' fill='%230E0D0B'/%3E%3Cg fill='none' stroke='%23C8A96A' stroke-width='5'%3E%3Cpath d='M22 28h56M32 50h36M42 72h16'/%3E%3C/g%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css_href}">
{schema_extra}</head>
<body>

<div class="read-progress" aria-hidden="true"><span data-progress-bar></span></div>

<a href="#top" class="skip-link">Перейти до основного вмісту</a>

{SVG_SPRITE}
{header}
<main id="top">

{main_html}

</main>

{footer}
"""
    import os
    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("wrote", path, len(html), "bytes")
