/* Return to the same Library view in this tab; no network or research changes. */
(()=>{'use strict';
 const key='f250-reader-return-v1:'+location.pathname+location.search;
 let saved=null,restoring=false;
 try{saved=JSON.parse(sessionStorage.getItem(key)||'null')}catch{}
 const frames=new Map(),allDetails=()=>[...document.querySelectorAll('details')];
 const controls=()=>[...document.querySelectorAll('main input[id],main select[id],#nodeSearch,#entityFilter,#lensFilter,#statusFilter')].filter(el=>!el.matches('[data-view-chooser],[type=password],[type=file],[type=hidden],[name=site-theme]'));
 function nySelection(){const info=document.querySelector('#info');if(!info||getComputedStyle(info).display==='none')return null;const title=info.querySelector('h2')?.textContent.trim();return [...document.querySelectorAll('[data-node-id]')].find(el=>el.querySelector('.node-entry-name')?.textContent.trim()===title)?.getAttribute('data-node-id')||null}
 function snapshot(){return {hash:location.hash,y:scrollY,x:scrollX,details:allDetails().map((el,i)=>({id:el.id||null,i,open:el.open})),controls:controls().map(el=>({id:el.id,value:el.value,checked:el.checked})),node:nySelection(),frames:Object.fromEntries(frames),focus:document.activeElement?.id||null}}
 function save(){if(restoring)return;try{sessionStorage.setItem(key,JSON.stringify(snapshot()))}catch{}}
 function restore(){const nav=performance.getEntriesByType('navigation')[0];if(!saved||(!['back_forward','reload'].includes(nav?.type)&&!restore.fromCache)||saved.hash!==location.hash)return;
  restoring=true;
  for(const field of saved.controls||[]){const el=document.getElementById(field.id);if(!el||el.matches('[data-view-chooser]'))continue;el.value=field.value;if(typeof field.checked==='boolean')el.checked=field.checked;el.dispatchEvent(new Event('input',{bubbles:true}));el.dispatchEvent(new Event('change',{bubbles:true}))}
  let attempts=0;
  function finish(){attempts++;const node=saved.node&&[...document.querySelectorAll('[data-node-id]')].find(el=>el.getAttribute('data-node-id')===saved.node);
   if(saved.node&&!node&&attempts<25){setTimeout(finish,80);return}
   if(node)node.click();
   const details=allDetails();for(const entry of saved.details||[]){const el=entry.id?document.getElementById(entry.id):details[entry.i];if(el?.tagName==='DETAILS')el.open=entry.open}
   document.querySelectorAll('iframe[data-reader-return]').forEach((frame,i)=>frame.contentWindow?.postMessage({channel:'f250-reader-frame-v1',type:'restore',selection:saved.frames?.[i]||null},'*'));
   requestAnimationFrame(()=>requestAnimationFrame(()=>{if(saved.focus)document.getElementById(saved.focus)?.focus({preventScroll:true});scrollTo(saved.x||0,saved.y||0);restoring=false}));
  }finish();
 }
 window.addEventListener('message',event=>{const list=[...document.querySelectorAll('iframe[data-reader-return]')],i=list.findIndex(frame=>frame.contentWindow===event.source);if(i<0||event.data?.channel!=='f250-reader-frame-v1')return;
  if(event.data.type==='selection'&&typeof event.data.selection==='string'&&event.data.selection.length<100){frames.set(i,event.data.selection);save()}
  if(event.data.type==='ready'){const value=saved?.frames?.[i];if(value)event.source.postMessage({channel:'f250-reader-frame-v1',type:'restore',selection:value},'*')}
 });
 window.addEventListener('pagehide',save);
 document.addEventListener('click',event=>{if(event.target.closest('a[href]'))save()},true);
 window.addEventListener('pageshow',event=>{restore.fromCache=event.persisted;restore()});
 document.querySelectorAll('iframe[data-reader-return]').forEach(frame=>{const request=()=>frame.contentWindow?.postMessage({channel:'f250-reader-frame-v1',type:'request'},'*');frame.addEventListener('load',request);request()});
 if(document.readyState==='complete')restore();
})();
