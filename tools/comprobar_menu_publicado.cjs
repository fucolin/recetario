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
 console.log('OK: public snapshot, two dishes/Libre, safe text/links, atomic validation, static/cache fallback on failure, no credentials, stale snapshots ignored.');
})().catch(error=>{console.error(error);process.exitCode=1});
