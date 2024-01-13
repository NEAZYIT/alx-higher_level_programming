// 102-script.js

// Ensure the DOM is ready before executing the script
$(document).ready(function () {
  // Attach a click event handler to INPUT#btn_translate
  $('#btn_translate').click(function () {
    // Fetch the language code from INPUT#language_code
    const languageCode = $('#language_code').val();

    // Make a GET request to the API with the specified language code
    $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function (data) {
      // Display the fetched translation in DIV#hello
      $('#hello').text(data.hello);
    });
  });
});
