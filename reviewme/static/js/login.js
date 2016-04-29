$("#loginForm").submit(function(event) {
    event.preventDefault();
    $.ajax({
        type: "POST",
        url: $('#loginForm').attr('action'), // or whatever
        data: $('#loginForm').serialize(),
        success: function(data) {
            if (data.status == 1) {
                $('.fadeMe').hide();
                window.location.replace('/user/verification-start/')
            } else if (data.status == 0) {
                $('.fadeMe').hide();
                alert(data.msg);
            }
        }
    });
});