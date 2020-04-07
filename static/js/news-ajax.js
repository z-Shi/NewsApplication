$(document).ready(function() {
    $('.view_more_btn').click(function() {
        var results = $(this).attr('data-results');
        var btn = $(this)

        $.get('/news/show_more/',
            {'results': results},
            function(data) {
                $('#story-list').html(data);
                btn.hide();
        })
    })
});
