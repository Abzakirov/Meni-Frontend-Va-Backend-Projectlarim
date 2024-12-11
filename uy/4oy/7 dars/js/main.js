// let originalArray = ["olma", "anor", "nok", "banan", "Uzum", "olma"];


// let uniqueNames = [];
// for (let i = 0; i < originalArray.length; i++) {
//   if (uniqueNames.indexOf(originalArray[i]) === -1) {
//     uniqueNames.push(originalArray[i]);
//   }
// }


// console.log(uniqueNames)





let   ism = ["olma", "Anor", "nok", "baban","uzum","olma"];

for(let i=0;i<ism.length -1;i++){
    for(let j=i+1;j<ism.length;j++){
        if(ism[i]==ism[j]){
            console.log(ism[i])
            i++
        }
    }
}

// let namesString = "";
// for (let i = 0; i < names.length; i++) {
//   namesString += names[i] + " ";
// }

// console.log(namesString );