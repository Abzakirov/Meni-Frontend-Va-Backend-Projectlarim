function updateClock() {
    let  now = new Date();
    let  hour = now.getHours();
    let  minute = now.getMinutes();
    let  second = now.getSeconds();

    document.getElementById('hourSpan').textContent = hour;
    document.getElementById('minuteSpan').textContent = minute;
    document.getElementById('secondSpan').textContent = second;

    setTimeout(updateClock, 1000); 
}

updateClock();
