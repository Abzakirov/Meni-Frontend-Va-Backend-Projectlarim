function displayData(data) {
  data.forEach(country => {
    let html;

    html.innerHTML = `
      <div class="country">
        <img src="${country.flag}" alt="${flagAlt}">
        <h1>Country name: ${country.name}</h1>
        <h1>Region: ${region}</h1>
        <h1>Population: ${population}</h1>
        <h1>Capital: ${capital}</h1>
      </div>
    `;
    document.getElementById('container').append(html);

  });

}
