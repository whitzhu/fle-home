var svg_cc = Snap("#svg_content_curation");

var g_cc = svg_cc.gradient("l(0, 0, 1, 1)#FFCC00-#33CCFF");
var tablet_cc_out = svg_cc.rect(100, 100, 200, 300, 20, 20);
var tablet_cc_in = svg_cc.rect(120, 120, 160, 250);
var tablet_cc_camera = svg_cc.circle(198.5, 110, 3);
var tablet_cc_btn = svg_cc.rect(187.5, 380, 25, 10, 5, 5);
tablet_cc_camera.attr({fill: 'white'});
tablet_cc_btn.attr({fill: 'white'});
tablet_cc_in.attr({fill: g_cc});

var tablet_cc = svg_cc.group(tablet_cc_out, tablet_cc_in, tablet_cc_camera, tablet_cc_btn);