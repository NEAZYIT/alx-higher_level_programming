// 6-script.js

// Ensure the DOM is ready before executing the script
$(document).ready(function () {
  // Use jQuery to select the element with id 'update_header'
  $('#update_header').click(function () {
    // Use jQuery to select the <header> element and update its text to 'New Header!!!'
    $('header').text('New Header!!!');
  });
});
