document.addEventListener("DOMContentLoaded", function () {
  fetch("https://fakestoreapi.com/products")
    .then(function (response) {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error("Error: " + response.status);
      }
    })
    .then(function (data) {
      displayProducts(data);
    })
    .catch(function (error) {
      console.error(error);
    });

  function displayProducts(products) {
    let productsContainer = document.getElementById("products-container");
    productsContainer.innerHTML = "";

    products.forEach(function (product) {
      let productElement = document.createElement("div");
      productElement.classList.add("product");

      let imageElement = document.createElement("img");
      imageElement.src = product.image;
      productElement.appendChild(imageElement);

      let titleElement = document.createElement("h3");
      titleElement.textContent = product.title;
      productElement.appendChild(titleElement);

      let categoryElement = document.createElement("p");
      categoryElement.textContent = "Категория: " + product.category;
      productElement.appendChild(categoryElement);

      let priceElement = document.createElement("p");
      priceElement.textContent = "Цена: $" + product.price;
      productElement.appendChild(priceElement);

      productsContainer.appendChild(productElement);
    });
  }

  let deleButton = document.getElementById("male-button");
  deleButton.addEventListener("click", function () {
    fetch("https://fakestoreapi.com/products/category/men's clothing")
      .then(function (response) {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error("Error: " + response.status);
        }
      })
      .then(function (data) {
        displayProducts(data);
      })
      .catch(function (error) {
        console.error(error);
      });
  });

  let Button = document.getElementById("female-button");
  Button.addEventListener("click", function () {
    fetch("https://fakestoreapi.com/products/category/women's clothing")
      .then(function (response) {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error("Error: " + response.status);
        }
      })
      .then(function (data) {
        displayProducts(data);
      })
      .catch(function (error) {
        console.error(error);
      });
  });
});

let darkMode = false;

function toggleDarkMode() {
  const body = document.body;
  const elementsToChangeColor = document.querySelectorAll('p, h1, h2, h3, span');
  darkMode = !darkMode;

  if (darkMode) {
    body.style.backgroundColor = "gray";
    elementsToChangeColor.forEach(element => {
      element.style.color = "white";
    });
  } else {
    body.style.backgroundColor = "white";
    elementsToChangeColor.forEach(element => {
      element.style.color = "black";
    });
  }
}

document.getElementById('darkMode').addEventListener('click', toggleDarkMode);