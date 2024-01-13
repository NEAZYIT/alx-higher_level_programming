// 5-script.js

// Ensure the DOM is ready before executing the script
$(document).ready(function () {
  // Use jQuery to select the element with id 'add_item'
  $('#add_item').click(function () {
    // Use jQuery to create a new <li> element with text 'Item'
    var newItem = $('<li>').text('Item');
    // Use jQuery to select the <ul> element with class 'my_list' and append the new <li> element
    $('ul.my_list').append(newItem);
  });
});
