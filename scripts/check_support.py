#!/usr/bin/env python3
"""Validate the static support handoff without sending mail or contacting a provider."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]

class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.text = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('href', 'src'):
            if key in attrs:
                self.links.append(attrs[key])
    def handle_data(self, data):
        self.text.append(data)

page = Page()
page.feed((ROOT / 'support/index.html').read_text())
bodies = []
for link in page.links:
    u = urlsplit(link)
    assert u.scheme != 'tel' and u.hostname not in ('wa.me', 'api.whatsapp.com'), 'Do not publish a direct phone/WhatsApp link'
    if u.scheme == 'mailto' and u.path == 'auratv@mesikalabs.com':
        q = parse_qs(u.query)
        assert q.get('subject') == ['Aura TV Support'], 'Support subject missing'
        bodies.append(q.get('body', [''])[0])
    elif not u.scheme and not u.netloc and u.path:
        target = (ROOT / u.path.lstrip('/')) if u.path.startswith('/') else (ROOT / 'support' / unquote(u.path))
        assert target.exists(), f'Broken local support link: {u.path}'
assert len(bodies) >= 2 and len(set(bodies)) == 1, 'Every support email link must share the complete template'
for required in ('within 48 hours', 'App version and build', 'Device model and OS version',
                 'live channel / movie / episode', 'one / some / all', 'time zone',
                 'Exact error message', 'stay open', 'Wi-Fi / cellular', 'public domain only',
                 'WhatsApp coordination (optional; yes/no)', 'Do not send passwords',
                 'tokens', 'full playlist/stream URLs', 'on your own device'):
    assert required in bodies[0], f'Missing support contract: {required}'
visible = ' '.join(page.text)
for required in ('within 48 hours', 'No email app?', 'Immediate availability is not guaranteed', 'Do not send passwords'):
    assert required in visible, f'Missing visible guidance: {required}'
assert '2 business days' not in visible, 'Stale response commitment'
print('Support contract, email payloads and local links: passed')
