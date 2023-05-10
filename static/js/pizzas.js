
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

$(document).ready(function(){
    $('.spicy').on('click', function(e) {
        e.preventDefault();
        $.ajax({
            url: '/pizzas/type/2',
            type: 'GET',
            success: function(resp) {
                var newHTML = resp.data.map(d => {
                    return '<div class="pizzas">' +
                               '<a href="/pizzas/' + d.id + '">' +
                                   '<img class="pizza-img" src="' + d.firstImage + '"/>' +
                                   '<h4>' + d.name + '</h4>' +
                                   '<p>' + d.descriptions + '</p>' +
                               '</a>' +
                           '</div>';
                });
                $('.pizzas').html(newHTML.join(''));
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });
    });
$(document).ready(function(){
    $('.spicy').on('click', function() {

        $.ajax({
            url: '/pizzas/type/3',
            type: 'GET',
            success: function(resp) {
                var newHTML = resp.data.map(d => {
                    return '<div class="pizzas">' +
                               '<a href="/pizzas/' + d.id + '">' +
                                   '<img class="pizza-img" src="' + d.firstImage + '"/>' +
                                   '<h4>' + d.name + '</h4>' +
                                   '<p>' + d.descriptions + '</p>' +
                               '</a>' +
                           '</div>';
                });
                $('.pizzas').html(newHTML.join(''));
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        });
    });
});