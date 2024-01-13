// 3-script.js

// Ensure the DOM is ready before executing the script
$(document).ready(function () {
  // Use jQuery to select the element with id 'red_header'
  // and add the class 'red' to the <header> element when clicked
  $('#red_header').click(function () {
    $('header').addClass('red');
  });
});
