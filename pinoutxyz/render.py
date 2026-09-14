from urllib.parse import urlparse

from .slugs import cssify, slugify


def article(name, content):
    return '<article class="page_{}">{}</article>'.format(slugify(name), content)


def pin_name(site, pin):
    pin_type = pin.get('type')
    translated = {
        '+3v3': 'pin_name_3v3',
        '+5v': 'pin_name_5v',
        'GND': 'pin_name_ground',
    }
    if pin_type in translated:
        return site.strings[translated[pin_type]]
    return pin.get('name_{}'.format(site.lang), pin.get('name', ''))


def pin_description(site, pin):
    return pin.get('description_{}'.format(site.lang), pin.get('description'))


def pin_functions(site, number, pin):
    bcm = pin.get('scheme', {}).get('bcm')
    if bcm is None:
        return ''

    models = site.pins.functions['models']
    tabs = []
    tables = []

    for model in models:
        functions = site.pins.functions['functions'][model['id']].get(str(bcm))
        if functions is None:
            continue

        tab_id = 'functions-tab-{}-{}'.format(number, model['id'])
        panel_id = 'functions-{}-{}'.format(number, model['id'])
        selected = 'true' if model is models[-1] else 'false'

        tabs.append('<button type="button" role="tab" id="{tab}" aria-controls="{panel}" aria-selected="{selected}">{name}</button>'.format(
            tab=tab_id, panel=panel_id, name=model['name'], selected=selected))

        headings = ['{}{}'.format(model['prefix'], index) for index in range(model['width'])]

        tables.append('''<div class="functions-panel" id="{panel}" role="tabpanel" aria-labelledby="{tab}">
        <table class="pin-functions">
        <caption>{name}</caption>
        <thead>
            <tr>
                <th>{headings}</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>{functions}</td>
            </tr>
        </tbody>
        </table>
        </div>'''.format(
            panel=panel_id, tab=tab_id, name=model['name'],
            headings='</th><th>'.join(headings),
            functions='</td><td>'.join(function or '' for function in functions)))

    if not tables:
        return ''

    return '''<div class="pin-function-tabs">
        <div class="tabs" role="tablist" aria-label="{label}" hidden>{tabs}</div>
        {tables}
        </div>'''.format(label=site.strings['pin_functions'], tabs=''.join(tabs), tables=''.join(tables))


def pin_page(site, number):
    if number in site.pins.ground():
        return None, None, None

    pin = site.pins[str(number)]
    name = pin_name(site, pin)
    description = pin_description(site, pin)
    pin_url = pin['name']
    title = name
    scheme = pin.get('scheme', {})

    if 'bcm' in scheme:
        pin_url = 'gpio{}'.format(scheme['bcm'])
        title = 'GPIO {}'.format(scheme['bcm'])
    if 'wiringpi' in scheme:
        subtext.append('Wiring Pi pin {}'.format(scheme['wiringpi']))
    if 'bcmAlt' in scheme:
        subtext.append(site.strings['bcm_pin_rev1_pi'].format(scheme['bcmAlt']))

    if description:
        title = '{} ({})'.format(title, description)

    functions = pin_functions(site, number, pin)
    pin_url = slugify('pin{}_{}'.format(number, pin_url))

    html = '<article class="{pin_url}"><h1>{pin_name}</h1>{pin_functions}{pin_facts}{pin_text}</article>'.format(
        pin_url=pin_url,
        pin_name=title,
        pin_functions=functions,
        pin_facts=pin_explanation(site, number, pin, scheme),
        pin_text=site.markdown('pin/pin-{}.md'.format(number)))

    return pin_url, html, title


def pin_explanation(site, number, pin, scheme):
    pin_type = pin.get('type', '')
    guide = 'gpio'
    description = 'pin_desc_gpio'
    warning = 'pin_warning_gpio'
    electrical = site.strings['logic_3v3']

    if pin_type == '+3v3':
        guide, description, warning = '3v3_power', 'pin_desc_3v3', 'pin_warning_3v3'
        electrical = site.strings['supply_3v3']
    elif pin_type == '+5v':
        guide, description, warning = '5v_power', 'pin_desc_5v', 'pin_warning_5v'
        electrical = site.strings['supply_5v']
    elif pin_type == 'GND':
        guide, description, warning = 'ground', 'pin_desc_ground', None
        electrical = site.strings['ground_reference']
    elif 'I2C' in pin_type:
        guide, description, warning = 'i2c', 'pin_desc_i2c', 'pin_warning_i2c'
    elif 'SPI' in pin_type:
        guide, description, warning = 'spi', 'pin_desc_spi', 'pin_warning_spi'
    elif 'UART' in pin_type:
        guide, description, warning = 'uart', 'pin_desc_uart', 'pin_warning_uart'
    elif 'PCM' in pin_type:
        guide, description, warning = 'pcm', 'pin_desc_pcm', 'pin_warning_pcm'

    if number in (27, 28):
        description, warning = 'pin_desc_hat_i2c', 'pin_warning_hat_i2c'

    facts = [
        (site.strings['fact_header'], site.strings['physical_pin_n'].format(number)),
        (site.strings['fact_signal'], pin_name(site, pin) or site.strings['gpio_signal']),
        (site.strings['fact_electrical'], electrical),
    ]
    if 'bcm' in scheme:
        facts.insert(1, (site.strings['fact_gpio'], site.strings['gpio_pin_n'].format(scheme['bcm'])))

    cards = ''.join('<div><strong>{}</strong><span>{}</span></div>'.format(label, value)
                    for label, value in facts)
    link = '{}{}{}'.format(site.base_url, guide, site.url_suffix)
    warning_html = '' if warning is None else (
        '<div class="notice notice-warning"><strong>{}</strong><p>{}</p></div>'.format(
            site.strings['warning_label'], site.strings[warning]))
    return ('<div class="pin-facts">{}</div>'
            '<div class="pin-description"><p>{}</p>'
            '{}<a class="learn-more" href="{}">{} &rarr;</a></div>').format(
                cards, site.strings[description], warning_html, link, site.strings['learn_more'])


def overlay_pin(site, number, overlay, warn):
    bcm = site.pins.bcm(number)
    candidates = (number, str(number), None if bcm is None else 'bcm{}'.format(bcm))

    for candidate in candidates:
        for key in ('ground', 'power', 'pin'):
            if candidate in (overlay.get(key) or {}):
                found = (overlay[key] or {})[candidate]
                if isinstance(found, str):
                    warn("{}: Overlay pin '{}' for pin {} is a string! Should be dict".format(
                        overlay['source'], found, number))
                return found if isinstance(found, dict) else {}, key

    return {}, None


def pin(site, number, selected_url, overlay=None, warn=None):
    entry = site.pins[str(number)]
    types = [value.strip() for value in entry['type'].lower().split('/')]
    name = pin_name(site, entry)
    pin_url = name
    titles = []
    overlay_data = {}
    flag = None

    if overlay is not None:
        overlay_data, flag = overlay_pin(site, number, overlay, warn)

        if flag == 'pin':
            name = overlay_data.get('name', name)
            if 'description' in overlay_data:
                titles.append(overlay_data['description'])
            if overlay_data.get('mode') == 'eeprom_wp':
                name = 'EEPROM WP'

    scheme = entry.get('scheme', {})

    if 'bcm' in scheme:
        pin_url = 'gpio{}'.format(scheme['bcm'])
        subname = ' <small>({})</small>'.format(name) if name != '' else ''
        name = '<span class="name">GPIO {}</span>{}'.format(scheme['bcm'], subname)
    if 'wiringpi' in scheme:
        titles.append(site.strings['wiring_pi_pin'].format(scheme['wiringpi']))

    if 'supported' in overlay_data:
        titles.append(site.strings['supported_on'].format(overlay_data['supported']))

    href = site.base_url + slugify('pin{}_{}'.format(number, pin_url))

    if entry['type'] in site.settings['urls']:
        href = site.base_url + site.settings['urls'][entry['type']]

    selected = ''
    if site.base_url + selected_url == href:
        selected = ' active'
    if flag is not None:
        selected += ' overlay-{}'.format(flag)

    return '<li class="pin{pin_num} {pin_type}{pin_selected}"><a href="{pin_url}" title="{pin_title}"><span class="default"> {pin_name}</span><span class="pin"><span class="visually-hidden">{physical_pin} </span><span class="phys">{pin_num}</span></span></a></li>\n'.format(
        pin_num=number,
        physical_pin=site.strings['physical_pin_label'],
        pin_type=' '.join(map(cssify, types)),
        pin_selected=selected,
        pin_url=href + site.url_suffix,
        pin_title=', '.join(titles),
        pin_name=name)


def nav(site, url, overlay=None, warn=None):
    odd = ''
    even = ''

    for number in range(1, len(site.pins), 2):
        odd += pin(site, number, url, overlay, warn)
        even += pin(site, number + 1, url, overlay, warn)

    return '''<ul class="bottom" aria-label="{}">
{}</ul>
<ul class="top" aria-label="{}">
{}</ul>'''.format(site.strings['pins_odd'], odd, site.strings['pins_even'], even)


def interfaces_sort(overlay):
    name = overlay['name'].lower()
    if name == 'gpio':
        return '0'
    if name == 'ardupilot':
        return '8'
    if name == 'ground':
        return '6'
    if name == '1-wire':
        return '7'
    return overlay['name']


def interfaces_menu(site, current):
    enabled = site.settings.get('interfaces')
    interfaces = sorted((o for o in site.overlays
                         if o['class'] == 'interface'
                         and (not enabled or o['src'] in enabled)), key=interfaces_sort)
    html = ''

    for interface in interfaces:
        selected = ''
        if current is not None and interface['name'] == current.get('name'):
            selected = ' class="selected"'
        html += '<li{}><a href="{}{}{}">{}</a></li>'.format(
            selected, site.base_url, interface['page_url'], site.url_suffix, interface['name'])

    return html


def hreflang(site, src):
    links = []

    for lang in sorted(site.alternates):
        if src in site.alternates[lang]:
            links.append('<link rel="alternate" href="{url}" hreflang="{lang}"/>'.format(
                lang=lang, url=site.alternates[lang][src]))

    if src in site.alternates.get('en', {}):
        links.append('<link rel="alternate" href="{url}" hreflang="x-default"/>'.format(
            url=site.alternates['en'][src]))

    return links


def lang_links(site, src):
    links = []

    for lang in sorted(site.alternates):
        if src not in site.alternates[lang]:
            continue

        name, flag = site.languages.get(lang, (lang, lang))
        current = ''
        grayscale = ''
        if lang == site.lang:
            grayscale = ' class="grayscale"'
            current = ' aria-current="true"'

        local_url = urlparse(site.alternates[lang][src]).path or '/'
        links.append('<a href="{url}" rel="alternate" hreflang="{lang}" lang="{lang}" title="{name}"{current}><img{css} src="{resource_url}flags/{flag}.svg" width="16" height="12" alt="" /><span>{name}</span></a>'.format(
            lang=lang, name=name, flag=flag, url=local_url,
            current=current, resource_url=site.resource_url, css=grayscale))

    return links


def lang_nav(site, links):
    if not links:
        return ''

    return '<nav id="lang" aria-label="{label}">\n\t\t\t\t{links}\n\t\t\t</nav>'.format(
        label=site.strings['choose_language'],
        links='\n\t\t\t\t'.join(links))


def board_tile(site, overlay, types, formfactor):
    return '<li class="board" data-type="{type}" data-manufacturer="{manufacturer}" data-form-factor="{formfactor}" data-compatibility="{compatibility}"><a href="{base_url}{page_url}{url_suffix}"><img loading=\"lazy\" alt="" src="{resource_url}boards/{image}" /><strong>{name}</strong><small>{compatibility_label}</small></a></li>'.format(
        image=overlay.get('image', 'no-image.png'),
        name=overlay['name'],
        page_url=overlay['page_url'],
        base_url=site.base_url,
        url_suffix=site.url_suffix,
        type=types,
        formfactor=formfactor,
        manufacturer=overlay.get('collected', overlay.get('manufacturer')),
        compatibility=overlay.get('compatibility', ''),
        compatibility_label=site.strings.get('compatibility_' + overlay.get('compatibility', ''), ''),
        resource_url=site.resource_url)


def crumbtrail(site, page=None):
    site_url = site.settings['site_url']

    if page is None or page.get('class') != 'board':
        return '<div id="crumbtrail"><p><a class="more" href="{}/boards">{} &raquo;</a></p></div>'.format(
            site_url, site.strings['browse_addons'])

    return '<div id="crumbtrail"><p><a href="{site_url}/">{home}</a> &raquo; <a href="{site_url}/boards">{boards}</a> &raquo; <a href="{site_url}/boards#manufacturer={manufacturer}">{manufacturer}</a> &raquo; {title}</p></div>'.format(
        site_url=site_url,
        title=page['name'],
        manufacturer=page.get('collected', page.get('manufacturer')),
        home=site.strings['home'],
        boards=site.strings['boards'])
