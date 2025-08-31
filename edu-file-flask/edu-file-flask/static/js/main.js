// simple ripple/hover helpers (placeholder)
document.querySelectorAll('.card-subject').forEach(el=>{
  el.addEventListener('mousemove', e=>{
    el.style.transform = 'translateY(-2px)';
  });
  el.addEventListener('mouseleave', ()=>{
    el.style.transform = 'translateY(0)';
  });
});
