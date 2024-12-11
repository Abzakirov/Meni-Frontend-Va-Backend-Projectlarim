// Get the form element and input fields
const form = document.getElementById('myform');
const input1 = document.getElementById('myinput');
const input2 = document.getElementById('myinput2');
const button = document.getElementById('add')
// Add an event listener to the form submission
button.addEventListener('submit', function(event) {
  event.preventDefault(); // Prevent the form from submitting

  // Get the values from the input fields
  const value1 = input1.value;
  const value2 = input2.value;

  // Save the values to local storage
  localStorage.setItem('value1', value1);
  localStorage.setItem('value2', value2);

  // Clear the input fields
  input1.value = '';
  input2.value = '';
});