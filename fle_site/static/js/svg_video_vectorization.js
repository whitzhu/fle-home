var svg_vv = Snap("#svg_video_vectorization");

var vv_1_url = document.getElementById("vv_1").src;
var vv_2_url = document.getElementById("vv_2").src;//a hack to get the image url

var vv_1 = svg_vv.image(vv_1_url, 60, -100, 700, 700);
var vv_2 = svg_vv.image(vv_2_url, 60, -100, 700, 700);

var mask_rect = svg_vv.rect(0, -120, 400, 800);
mask_rect.attr({fill: '#fff'});

vv_2.attr({mask: mask_rect});

animate_mask_left(mask_rect, 3000);

function animate_mask_left(element, dur) {
    element.animate({width: 10}, dur, mina.easein, function(){
        animate_mask_right(element, dur);
    });
}

function animate_mask_right(element, dur) {
    element.animate({width: 600}, dur, mina.elastic, function(){
        animate_mask_left(element, dur);
    });
}