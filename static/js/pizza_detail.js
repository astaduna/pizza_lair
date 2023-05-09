$(document).ready(function() {
  $(".add-to-cart").click(function() {
    var pizza_id = $(this).data("pizza-id");
    var pizza_size = "";
    if ($("#small-btn").is(":focus")) {
      pizza_size = "small";
    } else if ($("#medium-btn").is(":focus")) {
      pizza_size = "medium";
    } else if ($("#large-btn").is(":focus")) {
      pizza_size = "large";
    }
    $.ajax({
      url: "{% url 'cart-index' %}",
      method: "POST",
      data: {
        pizza_id: pizza_id,
        pizza_size: pizza_size,
        csrfmiddlewaretoken: "{{ csrf_token }}"
      },
      success: function(response) {
        alert("Pizza added to cart.");
      },
      error: function(xhr, status, error) {
        alert("Error adding pizza to cart.");
      }
    });
  });
});