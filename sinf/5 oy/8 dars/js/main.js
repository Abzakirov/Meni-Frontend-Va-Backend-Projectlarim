fetch('https://restcountries.com/v3.1/all')
  .then(response => {
    if (!response.ok) {
      throw new Error('Failed to fetch data');
    }
    return response.json();
  })
  .then(data => {
    for (let i = 0; i < 10; i++) {
      let myDiv = document.createElement('div');
      myDiv.innerHTML = `
      <div class='myDiv'>
        <h1>${data[i].common}</h1>
        <p>${data[i].official}</p>
        <p>${data[i].pol}</p>
        <img src="https://via.placeholder.com/600/92c952" alt="">
        <img src="https://via.placeholder.com/150/92c952" alt=""> 
      </div>
      `;
      document.body.appendChild(myDiv); 
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });