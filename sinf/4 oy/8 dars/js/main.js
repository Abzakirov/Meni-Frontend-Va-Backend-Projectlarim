

let sikil = true;
while (sikil) {
    let tanlov = +prompt("O'zbekiston poytaxti\n1. Toshkent\n2. Namangan\n3. Andijon\n4. Amerika");
    switch (tanlov) {
        case 1:
            alert("1. Togri javob tanladingiz\n");
            sikil = false; 
            break;
        default:
            alert("Noto'g'ri javob tanladingiz");
    }
}

let sikil3 = true;
while (sikil3) {
    let tanlov = +prompt("Payg'ambarimiz nechinchi yil tug'ilgan\n1. 571 yilda\n2. 430 yilda\n3. 580 yilda\n4. 590 yilda");
    switch (tanlov) {
        case 1:
            alert("1. Togri javob tanladingiz\n");
            sikil3 = false;
            break;
        default:
            alert("Noto'g'ri javob tanladingiz");
    }
}

let sikil4 = true;
while (sikil4) {
    let tanlov = +prompt("Payg'ambarimiz nechinchi yil vafot etkan\n1. 563 yil\n2. 630 yil\n3. 632 yil\n4. 560 yil");
    switch (tanlov) {
        case 3:
            alert("1. Togri javob tanladingiz\n");
            sikil4 = false; // Exit the loop after a correct answer
            break;
        default:
            alert("Noto'g'ri javob tanladingiz");
    }
}

let sikil5 = true;
while (sikil5) {
    let tanlov = +prompt("Payg'ambarimiz Qay'si oyda vafot etkan\n1.yanvar\n2.fevral\n3.Iuyl\n4.iyun");
    switch (tanlov) {
        case 4:
            alert("1. Togri javob tanladingiz\n");
            sikil5 = false; 
            break;
        default:
            alert("Noto'g'ri javob tanladingiz");
    }
}