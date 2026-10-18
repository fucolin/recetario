#!/usr/bin/env python3
"""Comprueba la política de buscadores en una copia canónica sin revisiones locales."""
from html.parser import HTMLParser
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {'build', 'node_modules', '__pycache__'}


class RobotsParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_head = False
        self.rules = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'head':
            self.in_head = True
        if tag == 'meta' and attrs.get('name', '').lower() in {'robots', 'googlebot', 'bingbot'}:
            if not self.in_head:
                self.errors.append('meta de robots fuera de head')
            tokens = {s.strip().lower() for s in attrs.get('content', '').split(',')}
            if attrs.get('name', '').lower() == 'robots':
                self.rules.append(tokens)
            if tokens & {'index', 'all', 'nofollow', 'none'}:
                self.errors.append('directiva ajena a la política acordada')

    def handle_endtag(self, tag):
        if tag == 'head':
            self.in_head = False


def main():
    pages = sorted(p for p in ROOT.rglob('*.html')
                   if not any(part.startswith('.') or part in EXCLUDED
                              for part in p.relative_to(ROOT).parts))
    errors = []
    for path in pages:
        parser = RobotsParser()
        parser.feed(path.read_text(encoding='utf-8'))
        if parser.rules != [{'noindex', 'noimageindex'}]:
            parser.errors.append('debe haber una única meta robots con noindex, noimageindex')
        errors.extend(f'{path.relative_to(ROOT)}: {error}' for error in parser.errors)
    if not pages:
        errors.append('no se encontraron páginas HTML')
    # Esta política no utiliza bloqueos de rastreo en robots.txt.
    robots = ROOT / 'robots.txt'
    if robots.exists():
        for line in robots.read_text().splitlines():
            directive = line.split('#', 1)[0].strip().split(':', 1)
            if len(directive) == 2 and directive[0].lower() == 'disallow' and directive[1].strip():
                errors.append('robots.txt contiene un bloqueo de rastreo; revisar antes de publicar')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'OK: {len(pages)} HTML con noindex, noimageindex en head; sin bloqueos locales de rastreo.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
