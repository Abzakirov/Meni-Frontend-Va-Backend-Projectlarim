let container = document.getElementById('container');
fetch("https://restcountries.com/v3.1/all")
    .then(response => {
        if (!response.ok) {
            throw new Error('Error fetching data');
        }
        return response.json();
    })
    .then(data => {
        container.innerHTML = ""; 
        data.forEach(element => {
            let div = document.createElement('div');
            div.innerHTML = `
                <img src="${element.flags.svg}" alt="">
                <h1>Country name: <span>${element.name.common}</span></h1>
                <h1>Region: <span>${element.region}</span></h1>
                <h1>Capital: <span>${element.capital}</span></h1>
                <h1>Population: <span>${element.population}</span></h1>
            `;
            div.classList.add('country');
            container.append(div);
        });
    });

const btn = document.getElementById('btn');
const body = document.body;

btn.addEventListener('click', () => {
    body.style.backgroundColor = body.style.backgroundColor === 'black' ? 'white' : 'black';
});

let myInput = document.getElementById('myInput');
myInput.addEventListener('keyup', function () {
    let currentCountry = myInput.value.toLowerCase();
    fetch("https://restcountries.com/v3.1/all")
        .then(response => {
            if (!response.ok) {
                throw new Error('Error fetching data');
            }
            return response.json();
        })
        .then(data => {
            container.innerHTML = ""; 
            data.forEach(element => {
                if (element.name.common.toLowerCase().startsWith(currentCountry)) {
                    let div = document.createElement('div');
                    div.innerHTML = `
                        <img src="${element.flags.svg}" alt="">
                        <h1>Country name: <span>${element.name.common}</span></h1>
                        <h1>Region: <span>${element.region}</span></h1>
                        <h1>Capital: <span>${element.capital}</span></h1>
                        <h1>Population: <span>${element.population}</span></h1>
                    `;
                    div.classList.add('country');
                    container.append(div);
                }
            });
        });
});
        