let myUL = document.getElementById('myUl')
myUL.addEventListener('click', function (event) {
    console.log(event.target.innerText)
})