// Se incrusta en portada al regenerar el plan. Solo existen los siete días originales.
(()=>{
const track=document.getElementById('week-track');
const days=Array.from(track.querySelectorAll('.week-day'));
const weekday=new Intl.DateTimeFormat('en-US',{weekday:'short',timeZone:'Europe/Madrid'}).format(new Date());
const current=Math.max(0,['Mon','Tue','Wed','Thu','Fri','Sat','Sun'].indexOf(weekday));
const reduced=window.matchMedia('(prefers-reduced-motion:reduce)');
let selected=current, timer, adjusting=false;
const modulo=n=>(n+7)%7;
function nearest(){
  const viewport=track.getBoundingClientRect();
  const middle=viewport.left+track.clientWidth/2;
  return days.reduce((best,day)=>{
    const b=day.getBoundingClientRect(), a=best.getBoundingClientRect();
    return Math.abs(b.left+b.width/2-middle)<Math.abs(a.left+a.width/2-middle)?day:best;
  });
}
function center(day,smooth){
  const b=day.getBoundingClientRect(), viewport=track.getBoundingClientRect();
  track.scrollTo({left:track.scrollLeft+b.left-viewport.left-(track.clientWidth-b.width)/2,behavior:smooth&&!reduced.matches?'smooth':'instant'});
}
function arrange(index){
  adjusting=true;
  clearTimeout(timer);
  track.style.scrollSnapType='none';
  // Tres días de margen a cada lado: el domingo y el lunes son contiguos.
  for(let offset=-3;offset<=3;offset++)track.append(days[modulo(index+offset)]);
  selected=index;
  center(days[index],false);
  requestAnimationFrame(()=>{track.style.scrollSnapType='';adjusting=false});
}
function settle(){
  if(adjusting)return;
  // No mover un enlace que el usuario esté recorriendo con el teclado.
  if(track.contains(document.activeElement))return;
  arrange(Number(nearest().dataset.weekday));
}
function step(direction){
  // Normaliza antes de animar, también con pulsaciones rápidas y movimiento reducido.
  arrange(selected);
  selected=modulo(selected+direction);
  requestAnimationFrame(()=>center(days[selected],true));
}
days[current].classList.add('is-today');
days[current].setAttribute('aria-current','date');
document.querySelector('.week-controls').hidden=false;
document.getElementById('week-prev').addEventListener('click',()=>step(-1));
document.getElementById('week-next').addEventListener('click',()=>step(1));
document.getElementById('week-today').addEventListener('click',()=>{
  selected=current;arrange(current);
});
track.addEventListener('scroll',()=>{
  if(adjusting)return;
  selected=Number(nearest().dataset.weekday);
  clearTimeout(timer);
  timer=setTimeout(settle,180);
},{passive:true});
track.addEventListener('focusout',()=>{clearTimeout(timer);timer=setTimeout(settle,180)});
requestAnimationFrame(()=>arrange(current));
// Mantiene centrado el día elegido al cambiar de orientación o ancho.
if(typeof ResizeObserver!=='undefined')new ResizeObserver(()=>arrange(selected)).observe(track);
})();
