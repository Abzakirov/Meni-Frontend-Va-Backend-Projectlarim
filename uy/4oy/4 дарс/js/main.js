let matn = prompt("Ismingizni kiriting");
let a = confirm("Ismingiz katta harflarda yozilishini xohlaysizmi");

if (a) {
  matn = matn.toUpperCase();
} else {
  matn = matn.toLowerCase();
}

let cansil = "ismingiz " + (a ? "KATTA" : "KICHIK") + " hariflarda yozildi";
console.log(matn + "  " + cansil + " va " + matn.length + " ta harfdan iborat");

