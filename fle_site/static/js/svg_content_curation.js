var svg_cc = Snap("#svg_content_curation");

// var g_cc = svg_cc.gradient("l(0, 0, 1, 1)#FFCC00-#33CCFF");
// var tablet_cc_out = svg_cc.rect(100, 100, 200, 300, 20, 20);
// var tablet_cc_in = svg_cc.rect(120, 120, 160, 250);
// var tablet_cc_camera = svg_cc.circle(198.5, 110, 3);
// var tablet_cc_btn = svg_cc.rect(187.5, 380, 25, 10, 5, 5);
// tablet_cc_camera.attr({fill: 'white'});
// tablet_cc_btn.attr({fill: 'white'});
// tablet_cc_in.attr({fill: g_cc});

// var tablet_cc = svg_cc.group(tablet_cc_out, tablet_cc_in, tablet_cc_camera, tablet_cc_btn);

var circle_1 = svg_cc.circle(270, 0, 50);
circle_1.attr({fill: 'pink', stroke: 'white', strokeWidth: 15});

var circle_2 = svg_cc.circle(160, 220, 80);
circle_2.attr({fill: 'yellow', stroke: 'white', strokeWidth: 15});

var circle_3 = svg_cc.circle(580, 420, 70); //blue circle
circle_3.attr({fill: '#66CCFF', stroke: 'white', strokeWidth: 15});

var circle_4 = svg_cc.circle(280, 420, 50);
circle_4.attr({fill: 'grey', stroke: 'white', strokeWidth: 15});

var circle_5 = svg_cc.circle(600, 20, 80);
circle_5.attr({fill: 'orange', stroke: 'white', strokeWidth: 15});

var circle_group = svg_cc.group(circle_1, circle_2, circle_3, circle_4, circle_5);


var center_circle = svg_cc.circle(400, 230, 100);
center_circle.attr({fill: 'white', "fill-opacity": 0.0, stroke: 'white', strokeWidth: 15});

var center_text = svg_cc.text(335, 290, "💡");
center_text.attr({"font-size": "130px"});

animate_concentrate(circle_2);

function animate_concentrate(group_element) {
    group_element.animate({x: 0}, 1000, mina.easein);
}