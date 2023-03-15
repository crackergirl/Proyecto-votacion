$ ('#username').keyup(function()
{
    var username = $('#username').val();
    if (username != '' )
    {
        $.post('check_user.php',{username:username}),
        function(data)
        {
            $('$status').html(data);
        }

    }else{
        $('#status').html('');
    }
}
)