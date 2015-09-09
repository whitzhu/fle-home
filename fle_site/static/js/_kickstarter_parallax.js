$(function() {
    var slide_tablet = $('#slide_tablet');
    var appear_pos = $('#fle_how').position().top - 200;
    var disappear_pos = $('#fle_features').position().top + 300;

    window.addEventListener('scroll', slidingTablet, false);

    function slidingTablet(e) {
        if( window.pageYOffset > appear_pos &&  window.pageYOffset < disappear_pos) {
            slide_tablet.css("visibility", "visible");
            slide_tablet.css("opacity", "1");
        }else{
            slide_tablet.css("opacity", "0");
            slide_tablet.css("visibility", "hidden");
        }
    }
});