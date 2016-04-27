$(function() {
    var vid = document.getElementById("quote_video");
    vid.addEventListener("ended", resetVideo, false);
    var vid_btn = $('#quote_video_btn');
    // vid_btn.css("visibility", "visible");
    var is_play = false;

    vid_btn.bind("click", function() {
        if(!is_play){
            is_play = true;
            vid.play();
            vid_btn.attr('src', '/static/img/kickstarter/quote/pause-btn.png');
            vid_btn.css("animation-iteration-count", "1");
            vid_btn.css("opacity", "0.4");
        }else{
            is_play = false;
            vid.pause();
            vid_btn.attr('src', '/static/img/kickstarter/quote/audio-btn.png');
            vid_btn.css("animation-iteration-count", "infinite");
            vid_btn.css("opacity", "1");
        }
    });

    function resetVideo() {
        is_play = false;
        vid.load();
        vid_btn.attr('src', '/static/img/kickstarter/quote/audio-btn.png');
        vid_btn.css("animation-iteration-count", "infinite");
        vid_btn.css("opacity", "1");
    }
});