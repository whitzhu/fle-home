$(function() {
    var timeline_canvas = document.getElementById("timeline_canvas");
    timeline_canvas.height = 800;
    var context = timeline_canvas.getContext('2d');
    var tl_img_1 = $('#tl_img_1');
    var tl_img_2 = $('#tl_img_2');
    var tl_img_3 = $('#tl_img_3');
    var tl_img_4 = $('#tl_img_4');

    var tl_text_1 = $('#tl_text_1');
    var tl_text_2 = $('#tl_text_2');
    var tl_text_3 = $('#tl_text_3');
    var tl_text_4 = $('#tl_text_4');

    $(window).on('resize', function (event) {
        zigzag_line();
    });
    zigzag_line();

    function zigzag_line() {
        timeline_canvas.width  = $(window).width();

        context.beginPath();
        context.moveTo(-6, 0);
        context.lineTo(tl_img_1.offset().left + 70, 500);
        context.lineTo(tl_img_2.offset().left + 70, 300);
        context.lineTo(tl_img_3.offset().left + 70, 500);
        context.lineTo(tl_img_4.offset().left + 70, 300);
        context.strokeStyle = '#8670A1';
        context.lineWidth = 6;
        context.stroke();

        // context.setLineDash([10, 10]);
        // context.lineTo(tl_img_4.offset().left + 70, 300);
        // context.stroke();

        context.font = "bold 68px sans-serif";
        // context.translate(canvas.width / 2, canvas.height / 2);
        context.rotate(angle(-6, 0, tl_img_1.offset().left + 70, 500));
        context.fillStyle = '#8670A1';
        context.fillText("TIMELINE", 100, 0);

        tl_text_1.offset({top: tl_img_1.offset().top + 180, left: tl_img_1.offset().left});
        tl_text_2.offset({top: tl_img_2.offset().top - 190, left: tl_img_2.offset().left});
        tl_text_3.offset({top: tl_img_3.offset().top + 180, left: tl_img_3.offset().left});
        tl_text_4.offset({top: tl_img_4.offset().top - 190, left: tl_img_4.offset().left});
    }

    function angle(cx, cy, ex, ey) {
        var dy = ey - cy;
        var dx = ex - cx;
        var theta = Math.atan2(dy, dx); // range (-PI, PI]
        // theta *= Math.PI; // rads to degs, range (-180, 180]
        //if (theta < 0) theta = 360 + theta; // range [0, 360)
        return theta;
    }
});