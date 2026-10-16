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
                assert (ROOT / example['pagina']).is_file(), example['pagina']
                recipe = json.loads((ROOT / Path(example['pagina']).with_suffix('.json')).read_text())
                assert recipe['categoria_menu'] == part['categoria'], part['texto']
                item += f'<a class="week-example" href="{escape(example["pagina"], quote=True)}">{escape(example["titulo"])}</a>'
            elif part['texto'] != 'Libre':
                item += '<span class="week-pending">Ejemplo pendiente</span>'
            result.append(item + '</div>')
        return '<div class="week-meal"><p class="meal-label">' + label + '</p>' + '<span class="week-plus" aria-hidden="true">+</span>'.join(result) + '</div>'
    block = ['<!-- SEMANA_BASE_INICIO -->', '<section class="week-base" aria-labelledby="semana-base-titulo">',
             '<h2 id="semana-base-titulo">Mi semana base</h2>',
             '<div class="week-controls" hidden><button type="button" id="week-prev" aria-label="Día anterior" aria-controls="week-track">←</button><button type="button" id="week-today" aria-controls="week-track">Hoy</button><button type="button" id="week-next" aria-label="Día siguiente" aria-controls="week-track">→</button></div>',
             '<div class="week-track" id="week-track" role="list" aria-label="Semana de lunes a domingo">']
    for n, day in enumerate(data['dias']):
        block.append(f'<article class="week-day" role="listitem" data-weekday="{n}" aria-labelledby="week-day-{n}"><header><h3 id="week-day-{n}">{escape(day["dia"])}</h3><span class="week-today-badge" hidden>Hoy</span></header>{meal(day["comida"], "Comida")}{meal(day["cena"], "Cena")}</article>')
    block += ['</div></section>', '''<script>(()=>{
const track=document.getElementById('week-track');
const days=Array.from(track.querySelectorAll('.week-day'));
const weekday=new Intl.DateTimeFormat('en-US',{weekday:'short',timeZone:'Europe/Madrid'}).format(new Date());
const current=['Mon','Tue','Wed','Thu','Fri','Sat','Sun'].indexOf(weekday);
const mobile=window.matchMedia('(max-width:650px)');
const reduced=window.matchMedia('(prefers-reduced-motion:reduce)');
let selected=current<0?0:current;
function center(index,smooth){selected=Math.max(0,Math.min(6,index));if(!mobile.matches)return;const item=days[selected];const box=item.getBoundingClientRect();const viewport=track.getBoundingClientRect();track.scrollTo({left:track.scrollLeft+box.left-viewport.left-(track.clientWidth-box.width)/2,behavior:smooth&&!reduced.matches?'smooth':'instant'})}
if(current>=0){days[current].classList.add('is-today');days[current].querySelector('.week-today-badge').hidden=false}
document.querySelector('.week-controls').hidden=false;
document.getElementById('week-prev').addEventListener('click',()=>center(selected-1,true));
document.getElementById('week-next').addEventListener('click',()=>center(selected+1,true));
document.getElementById('week-today').addEventListener('click',()=>center(current,true));
track.addEventListener('scroll',()=>{const box=track.getBoundingClientRect();const middle=box.left+box.width/2;let distance=Infinity;days.forEach((day,i)=>{const b=day.getBoundingClientRect();const d=Math.abs(b.left+b.width/2-middle);if(d<distance){distance=d;selected=i}})},{passive:true});
requestAnimationFrame(()=>center(current,false));
mobile.addEventListener('change',()=>center(current,false));
})();</script>''', '<!-- SEMANA_BASE_FIN -->']
    page = ROOT / 'index.html'
    html, count = re.subn(r'<!-- SEMANA_BASE_INICIO -->.*?<!-- SEMANA_BASE_FIN -->', '\n'.join(block), page.read_text(), flags=re.S)
    assert count == 1, 'El bloque de semana base debe aparecer exactamente una vez'
    page.write_text(html)
    (ROOT / 'datos/semana-base.json').write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    print('Semana base actualizada: siete columnas, carrusel móvil y ejemplos de categorías comprobados.')


if __name__ == '__main__':
    main()
