$(function() {
    var vid = document.getElementById("quote_video");
    vid.addEventListener("ended", resetVideo, false);
    var vid_btn = $('#quote_video_btn');
    vid_btn.css("visibility", "visible");
    var froze_rotate = false;

    vid_btn.bind("click", function() {
        froze_rotate = true;
        vid.play();
        vid_btn.css("opacity", "0");
    });

    dim();

    function dim() {
        // vid_btn.css("opacity", "0");
        vid_btn.css("background", "0");
        setTimeout(function(){
            lit();
        }, 1200);
    }

    function lit() {
        vid_btn.css("background", "rgba(134, 112, 161, 0.9)");
        setTimeout(function(){
            dim();
        }, 1200);
    }

    function resetVideo() {
        froze_rotate = false;
        vid.load();
        vid_btn.css("opacity", "1");
    }
});