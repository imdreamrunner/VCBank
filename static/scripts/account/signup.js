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

    // TODO: Check other fields of the form before submitting.

    var password = $('#password').val();
    if (password.length < 6) {
      popover('#password', 'Your password is too short.');
      return false;
    }
    if (password != $('#password2').val()) {
      popover('#password2', 'Two passwords are different.');
      return false;
    }

    disableSubmit();
    var data = formUserInfo.serialize();
    data += '&password=' + hex_sha512(password);

    $.ajax('/signup', {
      type: 'POST',
      dataType: "json",
      data: data,
      success: function(data) {
        console.log(data);
        if (data.hasOwnProperty('error')) {
          if (data.error == 0) {
            console.log('success');
          } else {
            enableSubmit();
            switch (parseInt(data.error)) {
              case 2:
                popover('#email', 'This is not a valid email address.');
                break;
              case 3:
                popover('#email', 'This email has been registered.');
                break;
              case 4:
                popover('#firstname', 'Please input your first name.');
                break;
              case 5:
                popover('#lastname', 'Please input your last name.');
                break;
              default:
                popover('#submit-button', 'Unknown error happens, please try again later.');
            }
          }
        } else {
          enableSubmit();
          popover('#submit-button', 'Unknown error happens, please try again later.');
          console.log('fails');
        }
      },
      error: function() {
        enableSubmit();
        popover('#submit-button', 'Unable to submit, please try again later.');
        console.log('errors happen');
      }
    });
    return false;
  });
});