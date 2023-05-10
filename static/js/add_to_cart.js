$(document).ready(function() {
  $(".add-to-cart").on('click', function(e) {
    e.preventDefault();
    $.ajax({
      url: "/cart",
      type: "GET",
      success: function(resp) {
          return console.log('hello')
      },
      error: function(xhr, status, error) {
        alert("Error adding product to cart.");
      }
    });
  });
});