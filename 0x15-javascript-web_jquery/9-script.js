// 9-script.js

// Ensure the DOM is ready before executing the script
$(document).ready(function () {
  // Make an AJAX request to fetch the translation
  $.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      // Display the translation in the DIV#hello
      $('#hello').text(data.hello);
    },
    error: function () {
      // Handle errors if the request fails
      console.error('Failed to fetch translation');
    }
  });
});
