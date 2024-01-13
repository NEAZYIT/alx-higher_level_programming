// 4-script.js

// Ensure the DOM is ready before executing the script
$(document).ready(function () {
  // Use jQuery to select the element with id 'toggle_header'
  $('#toggle_header').click(function () {
    // Use jQuery to select the <header> element and toggle between 'red' and 'green' classes
    $('header').toggleClass('red green');
  });
});
