$(document).ready(function() {
  var formUserInfo = $('#user-info');
  formUserInfo.submit(function() {
    var data = formUserInfo.serialize();
    data += '&password=' + hex_sha512($('#password').val());
    $.ajax('/signup', {
      type: 'POST',
      dataType: "json",
      data: data,
      success: function(data) {
        console.log(data);
        if (data.hasOwnProperty('error') && data.error === 0) {
          console.log('success');
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