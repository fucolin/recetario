// Solo lee la copia pública confirmada. Nunca consulta el editor ni envía credenciales.
(()=>{
 const endpoint='https://menu-publicado-casa-marisa.snappyseal256.chatgpt.site/menu.json';
 const cacheKey='casa-marisa-menu-publicado-v1';
 const names=['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo'];
 const track=document.getElementById('week-track');if(!track)return;
 const text=(s,n)=>typeof s==='string'&&s.length>0&&s.length<=n&&s===s.trim()&&!/[\u0000-\u001f\u007f]/.test(s);
 function valid(data){return data&&data.schema===1&&Number.isSafeInteger(data.revision)&&data.revision>0&&typeof data.publishedAt==='string'&&!isNaN(Date.parse(data.publishedAt))&&Array.isArray(data.days)&&data.days.length===7&&data.days.every((d,i)=>d&&d.day===names[i]&&['comida','cena'].every(m=>Array.isArray(d[m])&&d[m].length<=2&&d[m].every(p=>p&&text(p.title,120)&&(p.category===null||text(p.category,80))&&(p.url===null||(typeof p.url==='string'&&/^[a-z0-9]+(?:-[a-z0-9]+)*\.html$/.test(p.url))))));}
 function dishName(dish,category){
  const node=document.createElement(dish.url?'a':'span');
  const parts=dish.title.match(/^(\S+)\s+(.+)$/u);
  const repeated=category&&parts&&parts[1].normalize('NFC').toLocaleLowerCase('es')===category.normalize('NFC').toLocaleLowerCase('es');
  node.textContent=repeated?parts[2]:dish.title;
  if(dish.url)node.setAttribute('href',dish.url);
  if(repeated)node.setAttribute('aria-label',dish.title);
  return node;
 }
 let lastRevision=0;
 function render(data){
  if(!valid(data)||data.revision<lastRevision)return false;
  const changes=[];
  for(let index=0;index<7;index++){
   const day=track.querySelector('[data-weekday="'+index+'"]');if(!day)return false;
   const meals=day.querySelectorAll('.week-meal');if(meals.length!==2)return false;
   for(let mealIndex=0;mealIndex<2;mealIndex++){
    const dishes=data.days[index][mealIndex===0?'comida':'cena'];
    const host=meals[mealIndex].querySelector('.week-dishes');if(!host)return false;
    const children=[];
    const grouped=dishes.length===2&&(!dishes[0].category||!dishes[1].category||dishes[0].category===dishes[1].category);
    if(grouped){
     const node=document.createElement('div');node.className='week-dish';
     const category=dishes[0].category||dishes[1].category;
     if(category){const heading=document.createElement('strong');heading.textContent=category;node.appendChild(heading);}
     const example=document.createElement('div');example.className='week-example';
     dishes.forEach((dish,i)=>{
      if(i){const plus=document.createElement('span');plus.textContent=' + ';example.appendChild(plus);}
      example.appendChild(dishName(dish,category));
     });
     node.appendChild(example);children.push(node);
    }else for(const dish of dishes.length?dishes:[{title:'Libre',category:null,url:null}]){
     const node=document.createElement('div');node.className='week-dish';
     const heading=document.createElement('strong');heading.textContent=dish.category||dish.title;node.appendChild(heading);
     if(dish.category||dish.url){
      const example=document.createElement('div');example.className='week-example';
      example.appendChild(dishName(dish,dish.category));node.appendChild(example);
     }
     if(!dishes.length){const warning=document.createElement('div');warning.className='week-example';warning.textContent='⚠️ Respete vd. las cantidades';node.appendChild(warning);}
     children.push(node);
    }
    changes.push({meal:meals[mealIndex],host,children,pair:children.length===2});
   }
  }
  // Construct everything before replacing any of the existing, usable fallback.
  for(const change of changes){while(change.host.firstChild)change.host.removeChild(change.host.firstChild);for(const child of change.children)change.host.appendChild(child);change.meal.classList.toggle('has-pair',change.pair);}
  lastRevision=data.revision;return true;
 }
 try{const cached=JSON.parse(localStorage.getItem(cacheKey));render(cached)}catch{}
 let loading=false;
 async function refresh(){
  if(loading||document.visibilityState==='hidden'||typeof fetch!=='function')return;
  loading=true;const controller=typeof AbortController==='function'?new AbortController():null;
  const timer=controller?setTimeout(()=>controller.abort(),6000):null;
  try{const response=await fetch(endpoint,{mode:'cors',credentials:'omit',cache:'no-store',redirect:'error',...(controller?{signal:controller.signal}:{})});if(!response.ok)return;const data=await response.json();if(render(data)){try{localStorage.setItem(cacheKey,JSON.stringify(data))}catch{}}}catch{}finally{if(timer)clearTimeout(timer);loading=false;}
 }
 void refresh();setInterval(()=>void refresh(),30000);
 window.addEventListener('focus',()=>void refresh());document.addEventListener('visibilitychange',()=>void refresh());
})();

