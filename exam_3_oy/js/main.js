const menuBtn = document.querySelector('.menu-btn');
const navUl = document.querySelector('.nav__ul');

menuBtn.addEventListener('click', () => {
    menuBtn.classList.toggle('active');
    navUl.classList.toggle('active'); 
});


