const menuBtn = document.querySelector('.menu-btn');
const navUl = document.querySelector('.nav_ul');

menuBtn.addEventListener('click', () => {
    menuBtn.classList.toggle('active');
    navUl.classList.toggle('active'); 
});


navUl.addEventListener('click', () => {
    navUl.classList.remove('active'); 
    menuBtn.classList.remove('active'); 
});