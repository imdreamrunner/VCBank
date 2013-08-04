function resizeFrame() {
  $('#main-frame').css({
    height: $(window).height() - 40,
    width: $(window).width() - 220
  });
}

function loadFrame(name) {
  var mainFrame = document.getElementById('main-frame');
  return function() {
    $('#menu').find('.active').removeClass('active');
    $('#menu-'+name).addClass('active');
    mainFrame.src = '/admin?frame=' + name;
  }
}

$(document).ready(function() {
  $(window).resize(resizeFrame);
  resizeFrame();

  $('#menu-accounts').on('click', loadFrame('accounts'));

  $('#menu-dashboard').on('click', loadFrame('dashboard'));
});