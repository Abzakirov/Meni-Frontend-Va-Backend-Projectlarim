// let ism = +prompt("Ismigizni kiriting ")
// let fam = +prompt("familiyangizni  kiriting ")
// let  yosh  = +prompt("Yoshingizni kiriting kiriting ")
 
// function checkAge("")



// let ism = prompt("Ismigizni kiriting")
// let fam = prompt("familiyangizni  kiriting")
// let age = prompt("Yoshingizni kiriting kiriting")

// function checkAge(ism, fam, age){
//     if(age>10 && age<20){
//         alert("siz oqishga qabul qilindingiz ")
//         choose(ism, fam)
//     }else{
//         alert("Sizni yoshingiz togri kelmadi ")
//     }
// }

// function choose(ism, fam){
//     let yon = prompt("Sizning yoshingiz mos keldi, qaysi yo'nalishda o'qimoqchisiz?")
//     switch(yon){
//         case 1: front(ism, fam)//front
//         case 2: backend(ism, fam)//back
//         case 3: starter(ism, fam)//starter
//         case 4: design(ism, fam)//design
//         default:
//     }
// }

// function front(ism, yosh){
//     //savol
//     if(){

//     }else{

//     }
// }

// function starter(ism, yosh){
//     //savol
//     if(){

//     }else{
        
//     }
// }

// function backend(ism, yosh){
//     //savol
//     if(){

//     }else{
        
//     }
// }

// function design(ism, yosh){
//     //savol
//     if(){

//     }else{
        
//     }
// }


let ism = prompt("Ismingizni kiriting");
let fam = prompt("Familiyangizni kiriting");
let age = prompt("Yoshingizni kiriting");

function checkAge(ism, fam, age) {
    if (age > 10 && age < 20) {
        alert("Siz o'qishga qabul qilindingiz");
        choose(ism, fam);
    } else {
        alert("Sizning yoshingiz mos kelmadi");
    }
}

function choose(ism, fam) {
    let yon = prompt("Sizning yoshingiz mos keldi, qaysi yo'nalishda o'qimoqchisiz?\n1. Front-end\n2. Back-end\n3. Starter\n4. Design");
    switch (yon) {
        case "1":
            front(ism, fam);
            break;
        case "2":
            backend(ism, fam);
            break;
        case "3":
            starter(ism, fam);
            break;
        case "4":
            design(ism, fam);
            break;
        default:
            alert("Noto'g'ri tanlov");
    }
}

function front(ism, fam) {
  let dard = prompt(" как подключать script")
  let  savollar = prompt("1.script src")
  switch (dard) {
    case value:
      
      break;
  
    default:
      break;
  }
}

function starter(ism, fam) {
    
}

function backend(ism, fam) {
    
}

function design(ism, fam) {
    
}

checkAge(ism, fam, age);

                                          