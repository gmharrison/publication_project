$(document).ready(function() {
    // $(window).scroll(function(){
    //     var fromTop = $(window).scrollTop();
    //     $(".landing-container").css('margin', '-' + (100 - fromTop) + 'px 0px 0px 0px');
    // });
    var _window = $(window);
    var landing = $('.scroll-content-container .content-box');
    var max = -1000;
    var top = parseFloat(landing.css('top'));
    var scrollPos = _window.scrollTop();

    _window.scroll(function() {

        if (scrollPos > top){
            console.log(top);
            landing.css({top: -(scrollPos)});
        }

        // if (scrollPos < _window.scrollTop() && currentMargin < max) {
        //     landing.css('margin', '-' + (100 - scrollPos) + 'px 0px 0px 0px');
        // } else if (scrollPos > _window.scrollTop() && currentMargin > margin) {
        //     landing.css('margin', '+' + (100 - scrollPos) + 'px 0px 0px 0px');
        // }

        if (_window.scrollTop() == 0)
            landing.css({top: 0});

        scrollPos = _window.scrollTop();
    });
});