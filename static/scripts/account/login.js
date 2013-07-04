$(document).ready(function() {
  var formUserInfo = $('#user-info');
  formUserInfo.submit(function() {
    $.ajax('/login', {
      type: 'POST',
      dataType: "json",
      data: formUserInfo.serialize(),
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