$(document).ready(function() {
  var formUserInfo = $('#user-info');
  formUserInfo.submit(function() {
    var data = formUserInfo.serialize();
    data += '&password=' + hex_sha512($('#password').val());
    $.ajax('/login', {
      type: 'POST',
      dataType: "json",
      data: data,
      success: function(data) {
        console.log(data);
        if (data.hasOwnProperty('error') && data.error === 0) {
          console.log('success');
          window.location = '/';
        } else {
          console.log('fails');
        }
      },
      error: function() {
        console.log('errors happen');
      }
    });
    return false;
  });
});