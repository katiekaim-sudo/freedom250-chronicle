const STOP = new Set('a an and are as at be by do does for from how in is it of on or that the this to was what when where which who with'.split(' '));
export const normalize = value => String(value || '').normalize('NFKD').replace(/\p{M}/gu, '').toLocaleLowerCase().match(/[\p{L}\p{N}]+/gu)?.join(' ') || '';
export function words(value) { const all = normalize(value).split(' ').filter(Boolean); const useful = all.filter(word => !STOP.has(word)); return useful.length ? useful : all; }
export function prepare(rows) { return rows.map(row => ({row, title: normalize(row.title), tokens: new Set(words(row.title + ' ' + (row.description || '') + ' ' + (row.search_context || '')))})); }
const has = (tokens, word) => tokens.has(word) || (word.length >= 4 && [...tokens].some(t => t.startsWith(word)));
export function search(prepared, query) {
 const phrase = normalize(query), wanted = [...new Set(words(query))];
 const visualQuery = wanted.some(w => ['map','maps','globe','chart','charts','compare','comparison','matrix'].includes(w));
 return prepared.filter(x => !phrase || wanted.every(word => has(x.tokens, word))).map(x => ({...x, score: !phrase ? (x.row.kind === 'Source document' ? 0 : 1) : (x.title === phrase ? 1000 : x.title.startsWith(phrase) ? 500 : x.title.includes(phrase) ? 250 : 0) + wanted.filter(w => words(x.title).some(t => t === w || t.startsWith(w))).length * 20 + (x.row.kind === 'Study' ? 30 : 0) + (visualQuery && ['Interactive graphic','Comparison chart','Research graphic','Comparison'].includes(x.row.kind) ? (x.row.kind === 'Comparison' ? 120 : 80) : 0)})).sort((a,b) => b.score-a.score || a.row.title.localeCompare(b.row.title) || a.row.route.localeCompare(b.row.route)).map(x => x.row);
}
export function pageOf(rows, page = 1, size = 40) { const pages = Math.max(1, Math.ceil(rows.length / size)), current = Math.max(1, Math.min(pages, Math.trunc(Number(page)) || 1)); return {total: rows.length, pages, page: current, start: rows.length ? (current-1)*size+1 : 0, end: Math.min(current*size, rows.length), records: rows.slice((current-1)*size,current*size)}; }
