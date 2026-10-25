#!/usr/bin/env python3
"""Actualiza solo el bloque de semana base de portada y su JSON."""
import json
import re
from html import escape
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def main():
    data = yaml.safe_load((ROOT / 'semana-base.md').read_text().split('---', 2)[1])
    assert len(data['dias']) == 7
    def meal(parts, label):
        result = []
        for part in parts:
            item = '<div class="week-dish"><strong>' + escape(part['texto']) + '</strong>'
            example = part.get('ejemplo')
            if example:
                assert set(example) <= {'titulo', 'pagina', 'categoria', 'componentes'}, 'Revisar claves YAML del ejemplo: ' + str(example)
                components = example.get('componentes', [example])
                rendered = []
                for component in components:
                    assert set(component) <= {'titulo', 'pagina', 'categoria'}, 'Revisar claves YAML del ejemplo: ' + str(component)
                    title = escape(component['titulo'])
                    if component.get('pagina'):
                        assert (ROOT / component['pagina']).is_file(), component['pagina']
                        recipe = json.loads((ROOT / Path(component['pagina']).with_suffix('.json')).read_text())
                        assert recipe['categoria_menu'] == component.get('categoria', part['categoria']), part['texto']
                        rendered.append(f'<a href="{escape(component["pagina"], quote=True)}">{title}</a>')
                    else:
                        rendered.append('<span>' + title + '</span>')
                item += '<div class="week-example">' + ' + '.join(rendered) + '</div>'
            elif part['texto'] != 'Libre':
                item += '<span class="week-pending">Ejemplo pendiente</span>'
            if part.get('aclaracion'):
                icon = '<span aria-label="Advertencia">⚠️</span> ' if part.get('icono_aclaracion') == 'advertencia' else ''
                item += '<div class="week-example">' + icon + escape(part['aclaracion']) + '</div>'
            result.append(item + '</div>')
        pair = ' has-pair' if len(parts) > 1 else ''
        return '<div class="week-meal' + pair + '"><p class="meal-label">' + label + '</p><div class="week-dishes">' + ''.join(result) + '</div></div>'
    block = ['<!-- SEMANA_BASE_INICIO -->', '<section class="week-base" aria-label="Plan semanal de comidas y cenas">',
             '<div class="week-controls" hidden><button type="button" id="week-prev" aria-label="Día anterior" aria-controls="week-track">←</button><button type="button" id="week-today" aria-controls="week-track">Hoy</button><button type="button" id="week-next" aria-label="Día siguiente" aria-controls="week-track">→</button></div>',
             '<div class="week-track" id="week-track" role="list" aria-label="Semana de lunes a domingo">']
    for n, day in enumerate(data['dias']):
        block.append(f'<article class="week-day" role="listitem" data-weekday="{n}" aria-labelledby="week-day-{n}"><header><h3 id="week-day-{n}">{escape(day["dia"])}</h3></header>{meal(day["comida"], "Comida")}{meal(day["cena"], "Cena")}</article>')
    block += ['</div><nav class="week-caption" aria-label="Menú y compra">'
              '<a class="edit-menu-link" href="https://compra-casa-marisa-prueba.snappyseal256.chatgpt.site/menu"><span><svg class="edit-menu-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m15 5 4 4M4 20l4-1L20 7a2.1 2.1 0 0 0-3-3L5 16l-1 4Z"></path></svg>Editar menú</span></a>'
              '<a class="edit-menu-link" href="https://compra-casa-marisa-prueba.snappyseal256.chatgpt.site"><span><svg class="edit-menu-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m3 5 2 2 3-3m-5 9 2 2 3-3m-5 9 2 2 3-3M12 5h9m-9 8h9m-9 8h9"></path></svg>Lista de la compra</span></a>'
              '<p class="private-access-note">Acceso privado <svg class="private-access-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="5" y="10" width="14" height="11" rx="2"></rect><path d="M8 10V7a4 4 0 0 1 8 0v3m-4 5v2"></path></svg> Iniciar sesión con ChatGPT</p>'
              '</nav></section>', '<script>' + (ROOT / 'tools/semana_base.js').read_text() + '</script>', '<!-- MENU_PUBLICADO_INICIO -->', '<script>\n' + (ROOT / 'tools/menu_publicado.js').read_text().strip() + '\n</script>', '<!-- MENU_PUBLICADO_FIN -->', '<!-- SEMANA_BASE_FIN -->']
    page = ROOT / 'index.html'
    html, count = re.subn(r'<!-- SEMANA_BASE_INICIO -->.*?<!-- SEMANA_BASE_FIN -->', lambda _: '\n'.join(block), page.read_text(), flags=re.S)
    assert count == 1, 'El bloque de semana base debe aparecer exactamente una vez'
    page.write_text(html)
    (ROOT / 'datos/semana-base.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print('Semana base actualizada: carrusel circular y ejemplos de categorías comprobados.')


if __name__ == '__main__':
    main()

