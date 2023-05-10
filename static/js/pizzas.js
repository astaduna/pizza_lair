
$(document).ready(function(){
    $('#search_bar').on('keypress', function(e){
        if(e.keyCode === 13){
            e.preventDefault();
            var searchText = $('#search_bar').val();
            $.ajax({
                url: '/pizzas?search_filter=' + searchText,
                type: 'GET',
                success: function(resp) {
                    var newHTML = resp.data.map(d => {
                        return '<div class="pizzas">' +
                                   '<a href="/pizzas/' + d.id + '">' +
                                       '<img class="pizza-img" src="' + d.firstImage + '"/>' +
                                       '<h4>' + d.name + '</h4>' +
                                       '<p>' + d.descriptions + '</p>' +
                                        '<p>' + d.price.toFixed() + '</p>' +
                                   '</a>' +
                               '</div>';
                    });
                    $('.pizzas').html(newHTML.join(''));
                    $('#search_bar').val('');
                },
                error: function(xhr, status, error) {
                    console.error(error);
                }
            });
        }
    });
});