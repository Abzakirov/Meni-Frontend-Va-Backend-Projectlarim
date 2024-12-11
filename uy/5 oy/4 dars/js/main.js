let myForm = document.getElementById('myForm');
let ism = document.getElementById('name');
let surname = document.getElementById('surname');
let mark = document.getElementById('mark');
let tbody = document.getElementById('tbody');
let index = 2;

myForm.addEventListener('submit', function(event) {
    event.preventDefault(); 
    tyle(ism.value, surname.value, mark.value);
    myForm.reset();
});

function tyle(ism, surname, mark) {
    let tr = document.createElement('tr'); 
    let numbertd = document.createElement('td');
    let surnametd = document.createElement('td');
    let marktd = document.createElement('td');
    let baltd = document.createElement('td');
    let deletebtntd = document.createElement('td'); 
    let deletebtn = document.createElement('button');
    deletebtn.textContent = 'Delete'; 
    deletebtn.onclick = function() { deleterow(this); }; 

    numbertd.textContent = index++;
    surnametd.textContent = ism;
    marktd.textContent = surname;
    baltd.textContent = mark;
    deletebtntd.appendChild(deletebtn); 
    tr.append(numbertd, surnametd, marktd, baltd, deletebtntd); 
    tbody.append(tr);
}

function deleterow(btn){
   let tr = btn.parentNode.parentNode;
   tr.remove();
}
