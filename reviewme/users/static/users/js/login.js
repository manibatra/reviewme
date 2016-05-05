$("#signupForm").submit(function(event) {
    event.preventDefault();
    $.ajax({
        type: "POST",
        url: $('#signupForm').attr('action'), // or whatever
        data: $('#signupForm').serialize(),
        success: function(data) {
            if (data.status == 1) {
                $('.fadeMe').hide();
                window.location.replace('/users/verification-start/')
            } else if (data.status == 0) {
                $('.fadeMe').hide();
                alert(data.msg);
            }
        }
    });
});


$("#loginForm").submit(function(event) {
    event.preventDefault();
    $.ajax({
        type: "POST",
        url: $('#loginForm').attr('action'), // or whatever
        data: $('#loginForm').serialize(),
        success: function(data) {
            if (data.status == 1) {
                $('.fadeMe').hide();
                window.location.replace('/')
            } else if (data.status == 0) {
                $('.fadeMe').hide();
                alert(data.msg);
            }
        }
    });
});