var svg_vv = Snap("#svg_video_vectorization");

var vv_1_url = document.getElementById("vv_1").src;
var vv_2_url = document.getElementById("vv_2").src;//a hack to get the image url

var vv_1 = svg_vv.image(vv_1_url, 60, -100, 700, 700);
var vv_2 = svg_vv.image(vv_2_url, 60, -100, 700, 700);

var moving_box = svg_vv.rect(0, -300, 400, 1100).attr({id:'mv', fill: 'white', 'fill-opacity': 0.2, stroke: 'white', strokeWidth: 5});

var mask_1 = svg_vv.rect(-400, -200, 400, 800).attr({id:'mv', fill: '#fff'});
var mask_2 = svg_vv.rect(400, -200, 400, 800).attr({id:'mv', fill: '#fff'});
var mask_group = svg_vv.group(mask_1, mask_2);

vv_2.attr({mask: mask_group});

var set = svg_vv.selectAll('#mv');

vector_scan(set, "t400,0", "t0,0");

function vector_scan(set, m1, m2){
	set.animate({transform: m1}, 3000, function(){vector_scan(set, m2, m1);});
}