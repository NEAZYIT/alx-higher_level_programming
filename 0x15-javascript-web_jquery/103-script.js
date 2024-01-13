// 103-script.js

// Ensure the DOM is ready before executing the script
$(document).ready(function () {
  // Attach a click event handler to INPUT#btn_translate
  $('#btn_translate').click(fetchTranslation);

  // Attach a keypress event handler to INPUT#language_code
  $('#language_code').keypress(function (event) {
    // Check if the pressed key is ENTER (key code 13)
    if (event.which === 13) {
      fetchTranslation();
    }
  });

  // Function to fetch and display the translation
  function fetchTranslation() {
    // Fetch the language code from INPUT#language_code
    const languageCode = $('#language_code').val();

    // Make a GET request to the API with the specified language code
    $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function (data) {
      // Display the fetched translation in DIV#hello
      $('#hello').text(data.hello);
    });
  }
});
