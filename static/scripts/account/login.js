$(document).ready(function() {
  var buttonSubmit = $('#submit-button');
  var originalValue = buttonSubmit.val();

  function disableSubmit() {
    buttonSubmit.attr('disabled', 'disabled');
    buttonSubmit.val('Submitting...')
  }

  function enableSubmit() {
    buttonSubmit.removeAttr('disabled');
    buttonSubmit.val(originalValue);
  }

  function popover(target, text) {
    $(target).popover({
      content: text
    });
    $(target).popover('show');
    $(target).addClass('hasPopover');
  }

  var formUserInfo = $('#user-info');
  formUserInfo.submit(function() {
    $('.hasPopover').popover('destroy');

    var data = formUserInfo.serialize();
    data += '&password=' + hex_sha512($('#password').val());
    disableSubmit();
    $.ajax('/login', {
      type: 'POST',
      dataType: "json",
      data: data,
      success: function(data) {
        console.log(data);
        if (data.hasOwnProperty('error')) {
          if (data.error == 0) {
            console.log('success');
            window.location = '/';
          } else {
            enableSubmit();
            switch (parseInt(data.error)) {
              case 2:
                popover('#email', 'This email has not been registered.');
                break;
              case 3:
                popover('#password', 'This password is incorrect.');
                break;
              default:
                popover('#submit-button', 'Unknown error happens, please try again later.');
            }
          }
        } else {
          enableSubmit();
          console.log('fails');
        }
      },
      error: function() {
        enableSubmit();
        console.log('errors happen');
      }
    });
    return false;
  });
});