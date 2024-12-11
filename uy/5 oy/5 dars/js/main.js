
let form = document.getElementById('myForm');
let contactsContainer = document.getElementById('contacts');


form.addEventListener('submit', function (event) {
    event.preventDefault();

    
    let name = document.getElementById('name').value;
    let ship = document.getElementById('ship').value;
    let phone = document.getElementById('phone').value;

   
    let newContact = document.createElement('div');
    newContact.classList.add('contact__info');
    newContact.innerHTML = `
        <h1 class="title__name">${name}</h1>
        <h1 class="title__ship">${ship}</h1>
        <h1 class="title__number">${phone}</h1>
        <button class="delete__btn">Delete</button>`;
    

    contactsContainer.appendChild(newContact);


    document.getElementById('name').value = '';
    document.getElementById('ship').value = '';
    document.getElementById('phone').value = '';
});

contactsContainer.addEventListener('click', function (event) {
    if (event.target.classList.contains('delete__btn')) {
        event.target.parentElement.remove();
    }
});
