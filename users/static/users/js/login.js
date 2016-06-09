$("#signupForm").submit(function(event) {
    event.preventDefault();
    $.ajax({
        type: "POST",
        url: $('#signupForm').attr('action'), // or whatever
        data: $('#signupForm').serialize(),
        success: function(response) {
            if (response.status == 1 || response.status == 2) {
                $('.fadeMe').hide();
                window.location.replace('/users/verification-start/')
            } else if (response.status == 0) {
                $('.fadeMe').hide();
                alert(response.msg);
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
                window.location.replace('/content/categories/');
            } else if (data.status == 0 || data.status == 2) {
                $('.fadeMe').hide();
                alert(data.msg);
            }
        }
    });
});