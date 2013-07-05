$(document).ready(function() {
  var mainFrame = $('#main-frame');

  function resizeFrame() {
    console.log('here');
    mainFrame.css({
      height: $(window).height() - 50,
      width: $(window).width() - 220
    });

  }

  $(window).resize(resizeFrame);

  resizeFrame();
});