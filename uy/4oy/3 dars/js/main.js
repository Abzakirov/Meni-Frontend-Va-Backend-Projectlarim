let son = prompt("1 son kiriting")
let san = prompt("2 son kiriting")
let a = confirm("1 ok bosangiz raqamlar qoshiladi \n2 отмена bosangiz raqamlar ayriladi")
 
if (a) {
    console.log(+son + +san); // Addition
  } else {
    console.log(son - san); // Subtraction
  }

// alert  (+son+" \n"+san+" \n "+a+" \n")