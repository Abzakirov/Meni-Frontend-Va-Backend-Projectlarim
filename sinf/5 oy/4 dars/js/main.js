

let  myForm = document.getElementById('myForm');
let  surname = document.getElementById('surname');
let  names = document.getElementById('name');
let  number = document.getElementById('mark');
let tbody = document.getElementById('tbody')
 


myForm.addEventListener('submit', function(event) {
    event.preventDefault();
    console.log(`Фамилия ${surname.value} Имя ${names.value} Возраст ${number.value}`);
    
    myForm.reset();
}); 
