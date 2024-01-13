// 101-script.js

// Ensure the DOM is ready before executing the script
$(document).ready(function () {
  // Add item to the list when clicking on DIV#add_item
  $('#add_item').click(function () {
    $('<li>Item</li>').appendTo('ul.my_list');
  });

  // Remove the last item from the list when clicking on DIV#remove_item
  $('#remove_item').click(function () {
    $('ul.my_list li:last-child').remove();
  });

  // Clear all items from the list when clicking on DIV#clear_list
  $('#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
