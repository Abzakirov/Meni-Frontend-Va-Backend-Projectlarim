    let myForm = document.getElementById('myForm');
    let hourSpan = document.getElementById('hourSpan');
    let minuteSpan = document.getElementById('minuteSpan');
    let secondSpan = document.getElementById('secondSpan');
    let intervals = [];

    myForm.addEventListener('submit', () => {
        let hour = document.getElementById('hour');
        let minute = document.getElementById('minute');
        let second = document.getElementById('second');
        let hourTime = parseInt(hour.value);
        let minuteTime = parseInt(minute.value);
        let secondTime = parseInt(second.value);

        let interval = setInterval(() => {
            if (hourTime > 0 && minuteTime > 0 && secondTime === 0) {
                minuteTime--;
                secondTime = 59;
            } else if (hourTime > 0 && minuteTime == 0 && secondTime == 0) {
                hourTime--;
                minuteTime = 59;
                secondTime = 59;
            } else if (hourTime === 0 && minuteTime > 0 && secondTime === 0) {
                minuteTime--;
                secondTime = 59;
            } else if (hourTime === 0 && minuteTime === 0 && secondTime === 0) {
                alert('Voht tugadi');
                clearInterval(interval);
            }else{
                secondTime--
            }

            hourSpan.textContent = hourTime;
            minuteSpan.textContent = minuteTime;
            secondSpan.textContent = secondTime;
        }, 1000);

        hour.value = "";
        minute.value = "";
        second.value = "";
    });
