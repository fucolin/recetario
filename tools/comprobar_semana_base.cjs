// Prueba de lógica con geometría simulada, no sustituye a una revisión visual.
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const source=fs.readFileSync(__dirname+'/semana_base.js','utf8');
for(const width of [350,900])for(let today=0;today<7;today++){
  let frames=[],timers=[],resize;
  const buttons={};
  const track={children:[],scrollLeft:0,clientWidth:width,style:{},events:{},
    querySelectorAll(){return this.children.slice()},
    append(day){this.children=this.children.filter(d=>d!==day);this.children.push(day)},
    getBoundingClientRect(){return {left:0,width:this.clientWidth}},
    scrollTo({left}){this.scrollLeft=left;this.events.scroll?.()},
    addEventListener(name,fn){this.events[name]=fn},contains(){return false}};
  const days=Array.from({length:7},(_,n)=>({dataset:{weekday:String(n)},
    classList:{add(){}},setAttribute(){},
    getBoundingClientRect(){const w=track.clientWidth<=650?track.clientWidth*.84:(track.clientWidth-24)/3;return {left:track.children.indexOf(this)*(w+12)-track.scrollLeft,width:w}}}));
  track.children=days.slice();
  for(const id of ['week-prev','week-next','week-today'])buttons[id]={addEventListener(_,fn){this.click=fn}};
  const context={document:{activeElement:null,getElementById:id=>id==='week-track'?track:buttons[id],querySelector:()=>({hidden:true})},
    window:{matchMedia:()=>({matches:false})},
    Intl:{DateTimeFormat:class{format(){return ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'][today]}}},Date,
    requestAnimationFrame:fn=>frames.push(fn),setTimeout:fn=>(timers.push(fn),fn),clearTimeout:fn=>{timers=timers.filter(t=>t!==fn)},
    ResizeObserver:class{constructor(fn){resize=fn}observe(){}}};
  function flush(){for(let limit=0;frames.length||timers.length;limit++){assert(limit<30);const jobs=frames.splice(0);jobs.forEach(f=>f());if(!frames.length){const t=timers.splice(0);t.forEach(f=>f())}}}
  function check(expected){assert.equal(track.children[3],days[expected]);assert.equal(new Set(track.children).size,7);const b=days[expected].getBoundingClientRect();assert(Math.abs(b.left+b.width/2-track.clientWidth/2)<.01);for(let i=1;i<7;i++)assert.equal(+track.children[i].dataset.weekday,(+track.children[i-1].dataset.weekday+1)%7)}
  vm.runInNewContext(source,context);flush();check(today);
  let selected=today;
  for(const direction of [1,-1])for(let count=0;count<25;count++){
    buttons[direction===1?'week-next':'week-prev'].click();flush();selected=(selected+direction+7)%7;check(selected);
  }
  // Deslizamiento manual de dos días y cambio de ancho.
  const target=track.children[5];const b=target.getBoundingClientRect();track.scrollLeft+=b.left+b.width/2-width/2;track.events.scroll();flush();selected=+target.dataset.weekday;check(selected);
  track.clientWidth=width===350?900:350;resize();flush();check(selected);
  buttons['week-today'].click();flush();check(today);
}
console.log('OK: 14 escenarios, ambos tamaños, 700 pasos circulares, gesto de dos días, redimensionado y Hoy; siete nodos únicos.');
