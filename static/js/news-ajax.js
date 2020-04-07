$(document).on('click','.view_more_btn',function () {
    var results = $(this).attr('data-results');
    var btn = $(this)

    $.get('/news/show_more/',
        {'results': results},
        function(data) {
            $('#story-list').html(data);
    })
});
