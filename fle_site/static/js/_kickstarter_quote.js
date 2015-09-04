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

    if(vid_btn.length > 0){
        var offset = vid_btn.offset();
        var center_x = (offset.left - 45) + (vid_btn.width()/2);
        var center_y = (offset.top) + (vid_btn.height()/2);
        var act_radians = 90;
        // var radians = 0;
        // var degree = 0;
        var only_once = false;

        function mouse(e){
            if(!froze_rotate && Math.abs(center_y - e.pageY) < 300) {
                // radians = Math.atan2(e.pageX - center_x, e.pageY - center_y);
                // degree = (radians * (180 / Math.PI) * -1) + 90; 
                // hardware_rotate(degree);
                var m_x = (e.pageX-center_x)*0.3;
                var m_y = (e.pageY-center_y)*0.3;

                if(m_x > 0){
                    if(m_x > act_radians) m_x = act_radians;
                }else{
                    if(m_x < -act_radians) m_x = -act_radians;
                }

                if(m_y > 0){
                    if(m_y > act_radians) m_y = act_radians;
                }else{
                    if(m_y < -act_radians) m_y = -act_radians;
                }

                hardware_trans(m_x, m_y);
                only_once = true;
            }else{
                if(only_once) {
                    hardware_trans(0, 0);
                    only_once = false;
                }
            }
        }
        $(document).mousemove(mouse);
    }

    function hardware_trans(x, y) {
        vid_btn.css('-moz-transform', 'translate3d( 0, 0, 0)');
        vid_btn.css('-webkit-transform', 'translate3d( 0, 0, 0)');
        vid_btn.css('-o-transform', 'translate3d( 0, 0, 0)');
        vid_btn.css('-ms-transform', 'translate3d( 0, 0, 0)');
        vid_btn.css('transform', 'translate3d('+ x +'px,'+ y +'px, 0)');
    }

    function hardware_rotate(degree) {
        vid_btn.css('-moz-transform', 'rotate3d( 0, 0, 1, '+degree+'deg)');
        vid_btn.css('-webkit-transform', 'rotate3d( 0, 0, 1,'+degree+'deg)');
        vid_btn.css('-o-transform', 'rotate3d( 0, 0, 1,'+degree+'deg)');
        vid_btn.css('-ms-transform', 'rotate3d( 0, 0, 1,'+degree+'deg)');
        vid_btn.css('transform', 'rotate3d( 0, 0, 1,'+degree+'deg)');
    }

    function resetVideo() {
        froze_rotate = false;
        vid.load();
        vid_btn.css("opacity", "1");
    }
});