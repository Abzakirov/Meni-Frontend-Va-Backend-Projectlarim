let cont = 0
 let counter = document.getElementById('counter')
 let plus= document.getElementById('plus')
 let minus= document.getElementById('minus')
 plus.addEventListener('click',function(){
    cont++;
    counter.textContent = cont;
 })
 minus.addEventListener('click',function(){
    if (cont>0){

        cont--;
        counter.textContent = cont;
    }
    else {
        alert("Счетчик уже на нуле!");
    }
 })














































