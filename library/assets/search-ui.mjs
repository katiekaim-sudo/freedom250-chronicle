import {prepare, search, pageOf} from '/freedom250-chronicle/library/assets/search-core.mjs';
const box=document.querySelector('#search'), kind=document.querySelector('#search-kind'), order=document.querySelector('#search-order'), list=document.querySelector('#results'), count=document.querySelector('#count'), nav=document.querySelector('#search-pages');
let prepared=[];
const group=row=>{
 const value=(row.kind||'').toLocaleLowerCase();
 if(value==='study')return 'studies';
 if(value.includes('graphic')||value==='comparison'||value==='graphics directory')return 'graphics';
 if(value.includes('document')||value.includes('transcript')||value==='saved research')return 'documents';
 return 'entities';
};
function selectedRows(){
 let rows=search(prepared,box.value);
 if(kind?.value)rows=rows.filter(row=>group(row)===kind.value);
 if(order?.value==='recent')rows=[...rows].sort((a,b)=>String(b.evidence_through||'').localeCompare(String(a.evidence_through||''))||a.title.localeCompare(b.title)||a.route.localeCompare(b.route));
 return rows;
}
function draw(page=1, historyMode='replace') {
 const result=pageOf(selectedRows(),page);
 list.replaceChildren();list.start=result.start || 1;
 count.textContent=result.total ? `Showing ${result.start}–${result.end} of ${result.total} results · Page ${result.page} of ${result.pages}` : 'No matches. Try fewer words, or search answers and passages in the earlier archive below.';
 for(const row of result.records){const li=document.createElement('li'),a=document.createElement('a'),p=document.createElement('p');a.href=row.route;a.textContent=row.title;p.textContent=(row.document_role_label||row.kind)+(row.evidence_through?' · Evidence through '+row.evidence_through:'');li.append(a,p);list.append(li);}
 nav.replaceChildren();for(const [label,next] of [['Previous results',result.page-1],['Next results',result.page+1]]){if(next<1||next>result.pages)continue;const a=document.createElement('a'),url=new URL(location.href);url.searchParams.set('q',box.value);url.searchParams.set('page',next);a.href=url.pathname+url.search;a.textContent=label;a.addEventListener('click',event=>{event.preventDefault();draw(next,'push');box.focus();});nav.append(a);}
 const url=new URL(location.href);box.value?url.searchParams.set('q',box.value):url.searchParams.delete('q');kind?.value?url.searchParams.set('kind',kind.value):url.searchParams.delete('kind');order?.value==='recent'?url.searchParams.set('order','recent'):url.searchParams.delete('order');result.page>1?url.searchParams.set('page',result.page):url.searchParams.delete('page');if(historyMode!=='none')history[historyMode+'State']({},'',url.pathname+url.search);
}
function fromURL(){const q=new URLSearchParams(location.search);box.value=q.get('q')||'';if(kind)kind.value=q.get('kind')||'';if(order)order.value=q.get('order')||'relevance';draw(q.get('page')||1,'none');}
box.addEventListener('input',()=>draw(1));kind?.addEventListener('change',()=>draw(1));order?.addEventListener('change',()=>draw(1));window.addEventListener('popstate',fromURL);
count.textContent='Loading the Library search…';
fetch('/freedom250-chronicle/library/data/search.json').then(response=>{if(!response.ok)throw Error('Search unavailable');return response.json();}).then(rows=>{prepared=prepare(rows);fromURL();}).catch(()=>{count.textContent='Search could not load. Reload to try again, or browse studies and the bot word directory below.';});
