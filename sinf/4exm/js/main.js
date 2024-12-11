// Examen JavaScript Amaliy savollar 

// 1-savol Arifmetik operatorla

//  5 sonini 2 ga bo'ling va qoldig`ini alertga chiqaring!

// javob:Pasdan yozib keting kodini
// 1 vazifa
// let result = 5 % 2;
// alert(result);





// 2-savol  Math metodlari

// 1 dan 10 gacha bo'lgan random son yasang va alertga chiqaring

// Javob:Pasdan yozib keting kodini
//2 VAzifa
// let randomNumber = Math.floor(Math.random() * 10) + 1;
// alert(randomNumber);



// 3-savol Math metodlari

// 12.510 sonini butun songa aylantiring! 

// javob: 12 chiqishi kerak!

// 3 VAZIFA
// let number = 12.510;
// let result = Math.floor(number);
// alert(result);




// 4-savol function

// "MARS IT SCHOOL" sozini nechta harfdan iboratligini funksiya orqali topib va alertga chiqaring!.

// Javob:Kodini yozib bering 

// function findStringLength(str) {
//     let stringWithoutSpaces = str.replaceAll(" ", ""); 
//     alert(stringWithoutSpaces.length + " ta harfdan iborat: ");
//   }

// findStringLength("MARS IT SCHOOL")



// 5-savol for loop

// "MARS IT SCHOOL" sozini javascript funksiyasi orqali 10 marta console.log ga chiqaring!

// Javob:Kodini yozib bering
//5 VAZIFA


//  for(let t =0; t<  f.length- 3; t++ ){
    // console.log("MARS IT SCHOOL")
// }



// 6-savol Array methods

// let harflar = ["a" , "b" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t",  "u" , "v" , "x" , "y" , "z" ]

// Shu arraydan foydalangan holda console.log ga o'zingizni ismigizni chiqaring

// Javob:Kodini yozib bering
//6 vazifa
// let harflar = ["a" , "b" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" , "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t",  "u" , "v" , "x" , "y" , "z" ];

// let ism = harflar[0] + harflar[1] + harflar[2] + harflar[19]+ harflar[10]+ harflar[10]+ harflar[13]+ harflar[6]; 

// alert(ism);




// 7-savol if else

// Promtdan yosh kiriting agar yoshi 18 yoshdan katta bo'lsa console da Siz balag'ot yoshiga yetgansiz , aks holda  siz balog'at yoshiga yetmagansiz  // agar yoshi 18 yoshga teng bolsa  balog'at yoshi muborak deb console da chiqarish kerak

// Javob:Kodini yozib bering
//7 vazifa
// let yosh = prompt("Yoshingizni kiriting:");
// if (yosh > 18) {
//   alert("Siz balag'ot yoshiga yetgansiz");
// } else if (yosh == 18) {
//   alert("Balog'at yoshi muborak!");
// } else {
//  alert("Siz balog'at yoshiga yetmagansiz");
// }






// 8-savol String metodlari vs Array metodlari

// Promtdan ismigizni kiriting va console.log da ismigizni teskarisini chiqaring

// Javob:Kodini yozib bering
//8 vazifa
// let ism = prompt("Ismingizni kiriting:");
// let reversedName = ism.split('').reverse().join('');
// alert("Ismingizning teskari: " + reversedName);  






// 9-savol Switch case 


// Promt 1 dan 7 gacha bo'lgan raqam kiriting va kiritilgan raqam qaysi hafta kuniga to'gri kelishini chiqarib bering
// masalan 4 raqamini kiritsam console.log da("Siz kiritgan raqam haftaning Payshanba kuniga to'gri keladi") bo'lib chiqish kerak
// agar kiritilgan raqam 7 dan katta bolsa ya'ni 8 yoki 15 kiritilsa console da (Namalum raqam kiritdingiz ) deb chiqish kerak


// Javob:Kodini yozib bering
//9VAZIFA
let inputNumber = parseInt(prompt("1 dan 7 gacha bo'lgan raqam kiriting:"));


switch (inputNumber) {
  case 1:
    alert("Siz kiritgan raqam haftaning Dushanba kuniga to'g'ri keladi");
    break;
  case 2:
    alert("Siz kiritgan raqam haftaning Seshanba kuniga to'g'ri keladi");
    break;
  case 3:
    alert("Siz kiritgan raqam haftaning Chorshanba kuniga to'g'ri keladi");
    break;
  case 4:
    alert("Siz kiritgan raqam haftaning Payshanba kuniga to'g'ri keladi");
    break;
  case 5:
    alert("Siz kiritgan raqam haftaning Juma kuniga to'g'ri keladi");
    break;
  case 6:
    alert("Siz kiritgan raqam haftaning Shanba kuniga to'g'ri keladi");
    break;
  case 7:
    alert("Siz kiritgan raqam haftaning Yakshanba kuniga to'g'ri keladi");
    break;
  default:
    alert("Namalum raqam kiritdingiz");
}





// 10-savol Array metodlari

// let sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// shu arraydagi juft sonlarni console ga chiqaring


// Javob :Kodini yozib bering
//10 VAZIFA
// let sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

// let evenNumbers = sonlar.filter(num => num % 2 === 0);
// alert("Shu arraydagi juft sonlar: " + evenNumbers);









