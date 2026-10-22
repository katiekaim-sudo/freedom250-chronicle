(()=>{const root=document.querySelector('[data-s3-comparison]');if(!root)return;
const column=root.querySelector('#s3-column'),q=root.querySelector('#s3-search'),first=root.querySelector('#s3-first'),second=root.querySelector('#s3-second'),out=root.querySelector('#s3-count');
const rows=[...root.querySelectorAll('[data-s3-row]')],panels=[...root.querySelectorAll('.s3-cell-detail')],url=new URL(location.href);
for(const [field,key] of [[column,'view'],[q,'q'],[first,'first'],[second,'second']]){const value=url.searchParams.get(key);if(value!==null)field.value=value}
function run(){const chosen=[first.value,second.value].filter(Boolean),terms=q.value.toLocaleLowerCase().split(/\s+/).filter(Boolean);let count=0;
for(const row of rows){const ok=(!chosen.length||chosen.includes(row.dataset.id))&&terms.every(t=>row.dataset.search.includes(t));row.hidden=!ok;if(ok)count++;for(const cell of row.querySelectorAll('[data-s3-column]'))cell.hidden=!!column.value&&cell.dataset.s3Column!==column.value}
for(const cell of root.querySelectorAll('thead [data-s3-column]'))cell.hidden=!!column.value&&cell.dataset.s3Column!==column.value;root.querySelector('.s3-grid-panel').dataset.single=column.value?'1':'0';
const visible=new Set(rows.filter(r=>!r.hidden).map(r=>r.dataset.id));for(const panel of panels)panel.hidden=!visible.has(panel.dataset.id)||(!!column.value&&panel.dataset.s3Column!==column.value);
out.textContent=count+' of '+rows.length+' entries shown · '+(column.value?'1 column':'all 7 columns');
for(const [field,key] of [[column,'view'],[q,'q'],[first,'first'],[second,'second']]){if(field.value)url.searchParams.set(key,field.value);else url.searchParams.delete(key)}url.hash=location.hash;history.replaceState(null,'',url.pathname+url.search+url.hash)}
function openTarget(){let id;try{id=decodeURIComponent(location.hash.slice(1))}catch{return}const target=document.getElementById(id);const panel=target?.closest('.s3-cell-detail');if(!panel)return;let changed=false;
if(column.value&&column.value!==panel.dataset.s3Column){column.value='';changed=true}
const chosen=[first.value,second.value].filter(Boolean);if(chosen.length&&!chosen.includes(panel.dataset.id)){first.value='';second.value='';changed=true}
const row=rows.find(r=>r.dataset.id===panel.dataset.id),terms=q.value.toLocaleLowerCase().split(/\s+/).filter(Boolean);if(row&&!terms.every(t=>row.dataset.search.includes(t))){q.value='';changed=true}
if(changed)run();panel.hidden=false;panel.open=true;for(const d of panel.querySelectorAll('details'))d.open=true;panel.scrollIntoView({block:'start'})}
for(const el of [column,q,first,second])el.addEventListener('input',run);root.querySelector('[data-s3-reset]').addEventListener('click',()=>{for(const el of [column,q,first,second])el.value='';run()});
root.addEventListener('click',event=>{const a=event.target.closest('a[data-s3-cell]');if(!a)return;event.preventDefault();history.pushState(null,'',a.getAttribute('href'));openTarget()});window.addEventListener('hashchange',openTarget);run();openTarget()})();