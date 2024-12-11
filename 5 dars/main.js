// const loding = document.querySelector(".loading");
// setTimeout(() => {
//     loding.classList.add('remove');
// }, 3000);

let check = document.querySelector(".switch");
check.addEventListener("click",()=>{
    if (check.checked===true){
        document.body.style.background = "red"
    }
    else{
        document.body.style.background = "white"
    }
})