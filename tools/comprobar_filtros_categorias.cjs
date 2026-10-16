// Prueba la lógica real del índice con un DOM mínimo y casos representativos.
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const assert = require('node:assert/strict');
const html = fs.readFileSync(path.join(__dirname, '..', 'index.html'), 'utf8');
const script = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].at(-1)[1];
class Element {
  constructor() { this.hidden = false; this.dataset = {}; this.attrs = {}; this.listeners = {}; this.textContent = ''; }
  setAttribute(k, v) { this.attrs[k] = v; }
  getAttribute(k) { return this.attrs[k]; }
  addEventListener(k, fn) { this.listeners[k] = fn; }
  focus() { this.focused = true; }
  click() { this.listeners.click(); }
}
const ids = Object.fromEntries(['search-data','recipe-search','search-clear','search-status','search-empty','category-all'].map(k => [k,new Element()]));
ids['recipe-search'].value = '';
const form = new Element();
const names = ['legumbres','ensaladas','huevos','vegetales','picoteo'];
const sections = names.map(id => Object.assign(new Element(), {id}));
const buttons = {};
const links = names.map(id => {
  const el = new Element(); el.attrs.href = '#'+id; el.textContent = id;
  el.replaceWith = b => { buttons[id] = b; }; return el;
});
const texts = {};
function card(category, title, pages, upcoming=false) {
  const el = new Element(); el.textContent = title; el.dataset.search = title;
  el.classList = {contains: name => name === 'is-upcoming' && upcoming};
  el.closest = () => sections.find(s => s.id === category);
  const variants = pages.map(([href,text]) => {const l=new Element();l.attrs.href=href;texts[href]=text;return l;});
  const standalone = pages.length === 1;
  if (standalone) {el.attrs.href=pages[0][0];}
  el.matches = () => standalone;
  el.querySelectorAll = () => variants;
  el.variants = variants;
  return el;
}
const cards = [
  card('legumbres','Lentejas',[['300.html','Lentejas calabaza curry 300 g'],['400.html','Lentejas calabaza curry 400 g']]),
  card('ensaladas','Ensalada',[['ensalada.html','Ensalada mango aguacate']]),
  card('huevos','Tortilla',[['tortilla.html','Tortilla boniato espinacas']]),
  card('huevos','Revuelto',[['revuelto.html','Revuelto champiñones trigueros']]),
  card('vegetales','Menestra Vegetales',[],true),
  card('picoteo','Barquitas',[['barquitas.html','Barquitas endivia requesón']]),
];
ids['search-data'].textContent = JSON.stringify(texts);
const document = {
  getElementById: id => ids[id],
  querySelector: q => {assert.equal(q,'.search');return form;},
  querySelectorAll: q => q === '.category' ? sections : q === '.category-nav a' ? links : cards,
  createElement: tag => {assert.equal(tag,'button');return new Element();},
};
vm.runInNewContext(script,{document});
const visible = () => cards.filter(c => !c.hidden);
const search = text => {ids['recipe-search'].value=text;ids['recipe-search'].listeners.input();};
const pressed = el => el.attrs['aria-pressed'] === 'true';
assert.equal(visible().length,6);assert(pressed(ids['category-all']));
buttons.legumbres.click();assert.equal(visible().length,1);assert(!pressed(ids['category-all']));
buttons.ensaladas.click();assert.equal(visible().length,2);
buttons.legumbres.click();assert.equal(visible().length,1);
buttons.ensaladas.click();assert.equal(visible().length,6);assert(pressed(ids['category-all']));
buttons.huevos.click();search('mango');
assert.equal(visible().length,0);assert(!buttons.huevos.hidden);assert(!buttons.ensaladas.hidden);assert(buttons.vegetales.hidden);assert(!ids['search-empty'].hidden);
ids['category-all'].click();assert.equal(ids['recipe-search'].value,'mango');assert.equal(visible().length,1);
search('zzzinexistente');assert.equal(visible().length,0);assert(!ids['category-all'].hidden);
search('');buttons.legumbres.click();search('400');
assert.equal(visible().length,1);assert(cards[0].variants[0].hidden);assert(!cards[0].variants[1].hidden);
ids['search-clear'].click();assert(pressed(buttons.legumbres));assert.equal(visible().length,1);
ids['category-all'].click();search('REQUESON');assert.equal(visible().length,1);
ids['recipe-search'].listeners.keydown({key:'Escape'});assert.equal(visible().length,6);
buttons.vegetales.click();assert.equal(visible().length,1);assert(ids['search-status'].textContent.includes('0 fichas disponibles · 1 próximamente'));
console.log('OK: Todas, selección múltiple, búsqueda combinada, cero resultados, variantes, tildes, Escape y contador de próximas fichas.');
