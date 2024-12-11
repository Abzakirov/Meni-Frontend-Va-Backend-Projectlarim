// let myDiv = document.getElementById('myDiv')
// let btn = document.getElementById('btn')
// btn.addEventListener("click", function () {
//     if (myDiv.classList.contains('active')) {
//         myDiv.classList.remove('active')
//     } else {
//         myDiv.classList.add('active')
//     }
// })

let myinput = document.getElementById('myinput')
let btn = document.getElementById('btn')
let myform = document.getElementById('myform')
myinput.addEventListener('keyup', function () {
    console.log(`siz kiritingan : ${myinput.value}`)
})
myform.addEventListener('sumbit', function () {
    console.log(`siz kiritingan : ${myinput.value}`)
})