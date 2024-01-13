// 8-script.js

// Ensure the DOM is ready before executing the script
$(document).ready(function () {
  // Make an AJAX request to fetch movies data
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      // Iterate through each movie and append its title to the UL#list_movies
      $.each(data.results, function (index, movie) {
        $('#list_movies').append('<li>' + movie.title + '</li>');
      });
    },
    error: function () {
      // Handle errors if the request fails
      console.error('Failed to fetch movies data');
    }
  });
});
