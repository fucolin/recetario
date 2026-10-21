// Prueba del DOM simulado: no sustituye una revisión visual en navegador.
const fs=require('node:fs'),vm=require('node:vm'),assert=require('node:assert/strict');
const source=fs.readFileSync(__dirname+'/menu_publicado.js','utf8');
class Element{
 constructor(tag){this.tag=tag;this.children=[];this.textContent='';this.attributes={};this.classes=new Set();this.classList={toggle:(name,on)=>on?this.classes.add(name):this.classes.delete(name)};}
 appendChild(child){this.children.push(child);return child}removeChild(child){this.children.splice(this.children.indexOf(child),1)}get firstChild(){return this.children[0]??null}setAttribute(k,v){this.attributes[k]=v}
}
const names=['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo'];
const snapshot=()=>({schema:1,revision:2,publishedAt:'2026-10-21T20:00:00Z',days:names.map(day=>({day,comida:[],cena:[]}))});
async function scenario({cached=null,response=null,failed=false}){
 const meals=Array.from({length:14},()=>{const m=new Element('div');m.host=new Element('div');m.host.appendChild(Object.assign(new Element('strong'),{textContent:'Respaldo'}));m.querySelector=()=>m.host;return m});
 const days=Array.from({length:7},(_,i)=>({querySelectorAll:()=>meals.slice(i*2,i*2+2)}));
 const track={querySelector:q=>days[+q.match(/"(\d)"/)[1]]};const cache=new Map(cached?[["casa-marisa-menu-publicado-v1",JSON.stringify(cached)]]:[]);let request;
 const context={document:{visibilityState:'visible',getElementById:()=>track,createElement:tag=>new Element(tag),addEventListener(){}},window:{addEventListener(){}},localStorage:{getItem:k=>cache.get(k)??null,setItem:(k,v)=>cache.set(k,v)},fetch:async(url,options)=>{request={url,options};if(failed)throw Error('offline');return {ok:!!response,json:async()=>response}},setTimeout:()=>1,clearTimeout(){},setInterval(){},Date,Number,JSON,Array,isNaN};
 vm.runInNewContext(source,context);await new Promise(resolve=>setImmediate(resolve));return {meals,cache,request};
}
(async()=>{
 let s=await scenario({failed:true});assert.equal(s.meals[0].host.children[0].textContent,'Respaldo');
 const data=snapshot();data.days[0].comida=[{title:'<img onerror=alert(1)>',category:'Vegetales',url:null},{title:'Potaje',category:'Legumbres',url:'potaje-bacalao.html'}];
 s=await scenario({response:data});assert.equal(s.meals[0].host.children.length,2);assert.ok(s.meals[0].classes.has('has-pair'));assert.equal(s.meals[0].host.children[0].children[1].children[0].textContent,'<img onerror=alert(1)>');assert.equal(s.meals[0].host.children[1].children[1].children[0].attributes.href,'potaje-bacalao.html');assert.equal(s.meals[1].host.children[0].children[0].textContent,'Libre');assert.equal(s.request.options.credentials,'omit');assert.ok(s.cache.size);
 s=await scenario({cached:data,failed:true});assert.equal(s.meals[0].host.children.length,2);
 const bad=snapshot();bad.days[6].cena=[{title:'bad',category:null,url:'javascript:alert(1)'}];s=await scenario({response:bad});assert.equal(s.meals[0].host.children[0].textContent,'Respaldo');assert.equal(s.cache.size,0);
 const older=snapshot();older.revision=1;s=await scenario({cached:data,response:older});assert.equal(s.meals[0].host.children.length,2);
 for(const categories of [['Picoteo sanote','Picoteo sanote'],['Picoteo sanote',null],[null,'Picoteo sanote'],[null,null]]){
  const grouped=snapshot();grouped.days[0].cena=[{title:'Barquitas',category:categories[0],url:'barquitas-endivia-requeson.html'},{title:'Hummus',category:categories[1],url:'hummus-zanahoria.html'}];
  s=await scenario({cached:data,response:grouped});const meal=s.meals[1];assert.equal(meal.host.children.length,1);assert.ok(!meal.classes.has('has-pair'));
  const node=meal.host.children[0],category=categories[0]||categories[1];assert.equal(node.children.length,category?2:1);if(category)assert.equal(node.children[0].textContent,category);
  const titles=node.children.at(-1).children;assert.deepEqual(titles.map(n=>n.textContent),['Barquitas',' + ','Hummus']);assert.equal(titles[0].attributes.href,'barquitas-endivia-requeson.html');assert.equal(titles[2].attributes.href,'hummus-zanahoria.html');
  s=await scenario({cached:grouped,failed:true});assert.equal(s.meals[1].host.children.length,1);
 }
 const transitions=snapshot();transitions.days[0].comida=[{title:'A',category:'Igual',url:null},{title:'B',category:'Igual',url:null}];
 s=await scenario({cached:data,response:transitions});assert.ok(!s.meals[0].classes.has('has-pair'));assert.equal(s.meals[0].host.children[0].children[1].children[2].tag,'span');
 const restored=snapshot();restored.revision=3;restored.days[0].comida=data.days[0].comida;s=await scenario({cached:transitions,response:restored});assert.ok(s.meals[0].classes.has('has-pair'));assert.equal(s.meals[0].host.children.length,2);
 for(const [category,title,expected] of [['Tortilla','Tortilla de boniato','de boniato'],['Ensalada','ensalada de tomate','de tomate'],['Puré','PURÉ de calabaza','de calabaza'],['Puré','Pure\u0301 de calabaza','de calabaza'],['Tortilla','Tortillitas de verduras','Tortillitas de verduras'],['Puré','Pure de calabaza','Pure de calabaza'],['Pescado azul','Pescado a la plancha','Pescado a la plancha'],['Tortilla','Tortilla','Tortilla'],[null,'Tortilla de boniato','Tortilla de boniato']]){
  const abbreviated=snapshot();abbreviated.days[0].comida=[{category,title,url:'tortilla.html'}];
  s=await scenario({response:abbreviated});const link=s.meals[0].host.children[0].children[1].children[0];assert.equal(link.textContent,expected);assert.equal(link.attributes.href,'tortilla.html');if(expected!==title)assert.equal(link.attributes['aria-label'],title);assert.equal(abbreviated.days[0].comida[0].title,title);
  s=await scenario({cached:abbreviated,failed:true});assert.equal(s.meals[0].host.children[0].children[1].children[0].textContent,expected);
 }
 for(const categories of [['Ensalada','Ensalada'],['Ensalada',null],[null,'Ensalada']]){
  const grouped=snapshot();grouped.days[0].comida=[{title:'Ensalada de tomate',category:categories[0],url:'tomate.html'},{title:'Ensalada de mango',category:categories[1],url:null}];s=await scenario({response:grouped});const titles=s.meals[0].host.children[0].children[1].children;assert.deepEqual(titles.map(n=>n.textContent),['de tomate',' + ','de mango']);assert.equal(titles[0].attributes.href,'tomate.html');
 }
 const html=fs.readFileSync(__dirname+'/../index.html','utf8');assert.ok(html.includes('<script>\n'+source.trim()+'\n</script>'));
 console.log('OK: shared/missing categories grouped with +, individual links/plain titles preserved, distinct categories separated, layout transitions, Libre, safe text/links, atomic validation, fallback, no credentials, stale snapshots ignored, embedded loader synchronized.');
})().catch(error=>{console.error(error);process.exitCode=1});


