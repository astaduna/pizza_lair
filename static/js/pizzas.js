$(document).ready(function(){
    $('#search-btn').on('click', function(e){
        e.preventDefault();
        var searchText = $('#search_bar').val();
        $.ajax( {
            url: '/pizzas?search_filter=' + searchText,
                type: 'GET',
                success: function(resp) {
                var newHTML = resp.data.map(d => {
                    return //´<div class='pizzas'>
                            //<a href='/pizzas/${d.id}'>
                                    //<img class='pizza-img' src='${d.firstimage}'/>
                                    //<h4>${d.name}</h4>
                                    //<p>d.descriptions</p>
                                 //</a>
                            //</div>´
                });
                $('.pizzas').html(newHTML.join(''));
                $('#search_bar').val('');

            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        })
    });
});