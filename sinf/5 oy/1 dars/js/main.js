
// let malumot = {
//     ism: prompt("ismingizni kiriting"),
//     familiya: prompt("familiyangizni kiriting"),
//     yosh: prompt("YOshingizni kiriting"),
//     nomer: prompt("nomerizi kiriting"),
//     info: function () {
//         alert(`odamni ismi ${this.ism}odamni yoshi ${this.familiya} telefon raqami ${this.nomer} `)
//     }
// };
// alert(malumot)

// let malumot = []
// for(let b = 0; b < 10; b++){
//     let ism = prompt("ismingizni kiriting")
//     let familiya = prompt("familiyangizni kiriting")
// }

let odamlar = [];

for (let i = 0; i < 10; i++) {
    let ism = prompt("Ismingizni kiriting:");
    let odam = new Object();
    odam.ism = ism;
    odamlar.push(odam);
}

console.log(odamlar);
let engKattaOdam = odamlar.reduce((a, b) => (a.ism > b.ism ? a : b));
let engKichikOdam = odamlar.reduce((a, b) => (a.ism < b.ism ? a : b));

console.log("Eng katta odam:", engKattaOdam);
console.log("Eng kichik odam:", engKichikOdam);
let topilganIsm = prompt("Kimni topib beray? Ismini yozing:");
let topilganOdam = odamlar.find((odam) => odam.ism === topilganIsm);

if (topilganOdam) {
    console.log("Topilgan odam:", topilganOdam);
} else {
    console.log("Topilmadi!");
}




