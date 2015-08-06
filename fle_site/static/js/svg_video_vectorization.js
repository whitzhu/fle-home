var svg_vv = Snap("#svg_video_vectorization");

var vv_1_url = document.getElementById("vv_1").src;
var vv_2_url = document.getElementById("vv_2").src;//a hack to get the image url

var vv_1 = svg_vv.image(vv_1_url, 60, -100, 700, 700);
var vv_2 = svg_vv.image(vv_2_url, 60, -100, 700, 700);

var moving_box = svg_vv.rect(0, -200, 400, 900).attr({fill: 'white', 'fill-opacity': 0.2, stroke: 'white', strokeWidth: 5});

var mask_1 = svg_vv.rect(-400, -200, 400, 800).attr({fill: '#fff'});
var mask_2 = svg_vv.rect(400, -200, 400, 800).attr({fill: '#fff'});
var mask_group = svg_vv.group(mask_1, mask_2);

vv_2.attr({mask: mask_group});

animate_box(moving_box, 400, 0);
animate_box(mask_group.select('rect:nth-child(1)'), 0, -400);
animate_box(mask_group.select('rect:nth-child(2)'), 800, 400);

function animate_box(element, move1, move2) {
    element.animate({x: move1}, 3000, function(){
        animate_box(element, move2, move1);
    });
}