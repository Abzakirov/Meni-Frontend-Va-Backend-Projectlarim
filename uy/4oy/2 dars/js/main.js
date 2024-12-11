let desm = prompt("ismingizni kiriting")
let arname = prompt("familiya")
let yosh1 = prompt("yoshingizni kiriting")

let desm2 = prompt("ismingizni kiriting")
let arname2 = prompt("familiya")
let yosh2 = prompt("yoshingizni kiriting")
 
let desm3 = prompt("ismingizni kiriting")
let arname4 = prompt("familiya")
let yosh5 = prompt("yoshingizni kiriting")

let desm6 = prompt("vasha ism")
let arname6 = prompt("familiya")
let yosh6 = prompt("yoshingizni kiriting")


let desm7 = prompt("ismingizni kiriting")
let arname7 = prompt("familiya")
let yosh7 = prompt("yoshingizni kiriting")

console.log(desm+", "+arname+", "+yosh1+", ");
console.log(desm2+", "+arname2+", "+yosh5+", ");
console.log(desm3+", "+arname4+", "+yosh2);

console.log(desm6+", "+arname6+", "+yosh6+", ");
console.log(desm7+", "+arname7+", "+yosh7+", "); 







let ism = []
let ags = []




for (let i = 0; i < 10; i++)  {
let ismi = prompt("“ismingizni kiriting")
ism.push(ismi)
let yosh = prompt("Yoshingizni kiriting")
ags.push(parseInt(yosh) )
}

let maxAge = Math.max(...ags)
let minAge = Math.min(...ags)

let oldestPerson = ism[ags.indexOf(maxAge) ]
let youngestPerson = ism[ags.indexOf(minAge) ]


console.log("Eng katta yosh:", maxAge," - ", oldestPerson)

console.log("Eng kichik yosh:", minAge," - ", youngestPerson)