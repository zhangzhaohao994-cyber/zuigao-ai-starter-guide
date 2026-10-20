const search=document.querySelector('#search');
const chapters=[...document.querySelectorAll('.chapter')];
const links=[...document.querySelectorAll('nav a')];
search.addEventListener('input',()=>{const term=search.value.trim().toLowerCase();let count=0;chapters.forEach((s,i)=>{const show=!term||s.textContent.toLowerCase().includes(term);s.hidden=!show;links[i].hidden=!show;if(show)count++});document.querySelector('#empty').hidden=count>0});
document.querySelector('#font').addEventListener('click',e=>{const on=document.body.classList.toggle('large');e.currentTarget.setAttribute('aria-pressed',String(on));e.currentTarget.textContent=on?'标准字号':'大字阅读'});
document.querySelector('#print').addEventListener('click',()=>window.print());
let toastTimer;function toast(message){const el=document.querySelector('#toast');el.textContent=message;el.classList.add('visible');clearTimeout(toastTimer);toastTimer=setTimeout(()=>el.classList.remove('visible'),2300)}
document.querySelectorAll('.copy').forEach(button=>button.addEventListener('click',async()=>{const text=button.parentElement.querySelector('pre').textContent;try{await navigator.clipboard.writeText(text);toast('已复制，去 AI 对话框粘贴就可以')}catch{const selection=window.getSelection();const range=document.createRange();range.selectNodeContents(button.parentElement.querySelector('pre'));selection.removeAllRanges();selection.addRange(range);toast('请长按已选中的文字，选择复制')}}));
