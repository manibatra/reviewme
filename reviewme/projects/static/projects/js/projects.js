// $("#submitForm").submit(function(event) {
//     event.preventDefault();
//     $.ajax({
//         type: "POST",
//         url: $('#submitForm').attr('action'),
//         data: $('#submitForm').serialize(),
//         success: function(data) {
//             if (data.status == 1) {
//                 window.location.replace('/projects/categories/')
//             } else if (data.status == 0 || data.status == 2) {
//                 $('.fadeMe').hide();
//                 alert(data.msg);
//             }
//         }
//     });
// });