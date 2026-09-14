import os
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'output' / 'site'


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.lang = None
        self.title = []
        self.in_title = False
        self.classes = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.lang = attrs.get('lang')
        if tag == 'title':
            self.in_title = True
        if tag in ('a', 'link', 'script', 'img'):
            target = attrs.get('href') or attrs.get('src')
            if target:
                self.links.append((tag, target))
        if 'class' in attrs:
            self.classes.extend(attrs['class'].split())

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)


class GeneratedSiteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not SITE.exists():
            raise AssertionError('Build the site before running generated-site tests')
        cls.pages = sorted(SITE.rglob('*.html'))

    def test_expected_language_pages_exist(self):
        self.assertGreaterEqual(len(self.pages), 80)
        self.assertTrue((SITE / 'index.html').is_file())
        self.assertTrue((SITE / 'tr' / 'index.html').is_file())
        self.assertTrue((SITE / 'pinout' / 'pwm.html').is_file())
        self.assertTrue((SITE / 'tr' / 'pinout' / 'pwm.html').is_file())
        self.assertTrue((SITE / 'pinout' / 'ardupilot.html').is_file())
        self.assertTrue((SITE / 'tr' / 'pinout' / 'ardupilot.html').is_file())
        self.assertFalse((SITE / 'phatstack').exists())

    def test_html_metadata_and_templates(self):
        for page in self.pages:
            content = page.read_text(encoding='utf-8')
            parser = PageParser()
            parser.feed(content)
            expected_lang = 'tr' if page.relative_to(SITE).parts[0] == 'tr' else 'en'
            with self.subTest(page=page):
                self.assertEqual(parser.lang, expected_lang)
                self.assertTrue(''.join(parser.title).strip())
                self.assertNotIn('{{', content)
                self.assertNotIn('translate-me', parser.classes)
                self.assertNotIn('gemstone-logo.png', content)

    def test_every_internal_link_and_asset_resolves(self):
        failures = []
        for page in self.pages:
            parser = PageParser()
            parser.feed(page.read_text(encoding='utf-8'))
            for tag, target in parser.links:
                split = urlsplit(target)
                if target.startswith('//') or split.scheme or target.startswith(('#', 'mailto:', 'tel:')):
                    continue

                path = unquote(split.path)
                candidate = SITE / path.lstrip('/') if path.startswith('/') else page.parent / path
                candidate = Path(os.path.normpath(candidate))
                if candidate.is_dir():
                    candidate = candidate / 'index.html'
                if not candidate.exists():
                    failures.append('{}: {} {}'.format(page.relative_to(SITE), tag, target))

                if tag == 'a' and 'pinout.t3gemstone.org' in target:
                    failures.append('{}: language link leaves the local site: {}'.format(
                        page.relative_to(SITE), target))

        self.assertEqual(failures, [], '\n' + '\n'.join(failures))

    def test_gemstone_safety_and_default_signal_content(self):
        english = (SITE / 'index.html').read_text(encoding='utf-8')
        turkish = (SITE / 'tr' / 'index.html').read_text(encoding='utf-8')
        pin_13 = (SITE / 'pinout' / 'pin13_gpio27.html').read_text(encoding='utf-8')
        pin_26 = (SITE / 'pinout' / 'pin26_gpio7.html').read_text(encoding='utf-8')
        pin_27 = (SITE / 'pinout' / 'pin27_gpio0.html').read_text(encoding='utf-8')
        pin_29 = (SITE / 'pinout' / 'pin29_gpio5.html').read_text(encoding='utf-8')
        pin_32 = (SITE / 'pinout' / 'pin32_gpio12.html').read_text(encoding='utf-8')
        pin_36 = (SITE / 'pinout' / 'pin36_gpio16.html').read_text(encoding='utf-8')
        boards = (SITE / 'boards' / 'index.html').read_text(encoding='utf-8')
        ardupilot_tr = (SITE / 'tr' / 'pinout' / 'ardupilot.html').read_text(encoding='utf-8')

        self.assertIn('UART-MAIN1 TX', english)
        self.assertIn('UART-MAIN1 TX', turkish)
        self.assertNotIn('UART0 TX', english)
        self.assertIn('SPI-MCU0 CS2', pin_26)
        self.assertNotIn('SPI0 CE1', pin_26)
        self.assertIn('I2C-WKUP0', pin_27)
        self.assertIn('notice-warning', pin_27)
        self.assertIn('General-purpose I/O', pin_13)
        self.assertIn('PWM-0A', pin_29)
        self.assertIn('PWM-0B', pin_32)
        self.assertIn('UART-MAIN1 CTS', pin_36)
        self.assertIn('boards-empty', boards)
        self.assertIn('Servo ve diğer yükleri', ardupilot_tr)

    def test_schematic_derived_signal_assignments(self):
        """Signals the T3-GEM-O1 schematic, sheet 31, puts on each header pin."""
        index = (SITE / 'index.html').read_text(encoding='utf-8')
        pwm = (SITE / 'pinout' / 'pwm.html').read_text(encoding='utf-8')
        i2c = (SITE / 'pinout' / 'i2c.html').read_text(encoding='utf-8')
        pin_13 = (SITE / 'pinout' / 'pin13_gpio27.html').read_text(encoding='utf-8')

        # Positions the schematic settles, as labelled on the header diagram.
        for number, name in ((7, 'AUDIO REFCLK2'),
                             (11, 'UART-MAIN1 RTS'),
                             (32, 'PWM-0B'),
                             (36, 'UART-MAIN1 CTS'),
                             (38, 'PCM-McASP0 DATA0'),
                             (40, 'PCM-McASP0 DATA1')):
            with self.subTest(pin=number):
                self.assertIn(name, self.header_pin(index, number))

        # The system name is what you type into gpioinfo, so it has to survive.
        self.assertIn('GPIO0_33', pin_13)

        # Hardware PWM is on pins 29/31/32/33; the eCAP claims are gone.
        self.assertIn('29 and 32', pwm)
        self.assertIn('31 and 33', pwm)
        self.assertNotIn('PWM-ECAP', pwm)

        # Pins 27 and 28 are shared with the board's own chips, not off limits.
        self.assertIn('power-management chip', i2c)
        self.assertNotIn('reserved for HAT identification EEPROM', i2c)
        self.assertNotIn('not for you', i2c)

    @staticmethod
    def header_pin(page, number):
        """The one list item the header diagram renders for a physical pin."""
        match = re.search(r'<li class="pin{}[ "].*?</li>'.format(number), page, re.S)
        if match is None:
            raise AssertionError('pin {} is missing from the header'.format(number))
        return match.group(0)


if __name__ == '__main__':
    unittest.main()
