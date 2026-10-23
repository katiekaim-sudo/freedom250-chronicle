(()=>{
 const q=document.querySelector('#graphic-query');if(!q)return;
 const cards=[...document.querySelectorAll('[data-graphic-search]')],refs=[...document.querySelectorAll('.gfx-reference')],research=document.querySelector('#research-query-link');
 let expanded=null;
 function run(){
  const query=q.value.trim(),words=query.toLocaleLowerCase().split(/\s+/).filter(Boolean);
  if(words.length&&expanded===null)expanded=refs.map(d=>d.open);
  for(const c of cards)c.hidden=(!words.length&&!!c.closest('[data-search-only]'))||!words.every(w=>c.dataset.graphicSearch.includes(w));
  for(const s of document.querySelectorAll('.gfx-room,.gfx-start,.gfx-background'))s.hidden=(!words.length&&s.hasAttribute('data-search-only'))||![...s.querySelectorAll('[data-graphic-search]')].some(c=>!c.hidden);
  const count=new Set(cards.filter(c=>!c.hidden).map(c=>c.dataset.graphicId||c.dataset.graphicRoute)).size,status=document.querySelector('#graphic-count');
  if(status)status.textContent=words.length?(count?count+' matching graphics, tools or featured studies':'No matching graphics or featured studies here. Search all research for documents and companies.'):new Set(cards.filter(c=>c.dataset.graphicId).map(c=>c.dataset.graphicId)).size+' question and reference pages · filter these below or search all research';
  if(research){const url=new URL(research.href,location.href);query?url.searchParams.set('q',query):url.searchParams.delete('q');research.href=url.href;research.textContent=query?'Search all research for “'+query+'” →':'Search all research →'}
  refs.forEach(d=>{const match=[...d.querySelectorAll('[data-graphic-search]')].some(c=>!c.hidden);d.hidden=!!words.length&&!match;if(words.length&&match)d.open=true});
  if(!words.length&&expanded!==null){refs.forEach((d,i)=>d.open=expanded[i]);expanded=null}
 }
 q.addEventListener('input',run);
 q.addEventListener('keydown',e=>{if(e.key==='Enter'&&research&&!e.isComposing){e.preventDefault();run();location.assign(research.href)}});
 window.addEventListener('pageshow',run);run();
})();