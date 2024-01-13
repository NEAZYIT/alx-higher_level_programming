// 7-script.js

// Ensure the DOM is ready before executing the script
$(document).ready(function () {
  // Make an AJAX request to fetch character data
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      // Update the content of the DIV#character with the character name
      $('#character').text(data.name);
    },
    error: function () {
      // Handle errors if the request fails
      console.error('Failed to fetch character data');
    }
  });
});
