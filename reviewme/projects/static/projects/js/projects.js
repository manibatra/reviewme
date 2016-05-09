$("#submitForm").submit(function(event) {
    event.preventDefault();
    $.ajax({
        type: "POST",
        url: $('#submitForm').attr('action'),
        data: $('#loginForm').serialize(),
        success: function(data) {
            if (data.status == 1) {
                window.location.replace('/categories/')
            } else if (data.status == 0 || data.status == 2) {
                $('.fadeMe').hide();
                alert(data.msg);
            }
        }
    });
});