var svg_ptp = Snap("#svg_peer_to_peer");

var wave_1 = svg_ptp.circle(200, 250, 100);
wave_1.attr({
    fill: "#66CCFF",
    "fill-opacity": 0.5,
    stroke: "#66CCFF",
    strokeWidth: 5
});

var wave_2 = svg_ptp.circle(590, 250, 100);
wave_2.attr({
    fill: "#FF6600",
    "fill-opacity": 0.5,
    stroke: "#FF6600",
    strokeWidth: 5
});

animate_wave(wave_1, 2000, 0);
animate_wave(wave_2, 1000, 1000);

// var g_1 = svg_ptp.gradient("l(0, 0, 1, 1)#FFCC00-#33CCFF");
// var g_2 = svg_ptp.gradient("l(0, 0, 1, 1)#33CCFF-#FF3300");
var tablet_1_out = svg_ptp.rect(100, 100, 200, 300, 20, 20);
var tablet_1_in = svg_ptp.rect(120, 120, 160, 250);
var tablet_1_camera = svg_ptp.circle(198.5, 110, 3);
var tablet_1_btn = svg_ptp.rect(187.5, 380, 25, 10, 5, 5);
tablet_1_camera.attr({fill: 'white'});
tablet_1_btn.attr({fill: 'white'});
// tablet_1_in.attr({fill: g_1});
tablet_1_in.attr({fill: '#A3E0FF'});

var tablet_1 = svg_ptp.group(tablet_1_out, tablet_1_in, tablet_1_camera, tablet_1_btn);
var tablet_2 = tablet_1.clone();
// tablet_2.select('rect:nth-child(2)').attr({fill: g_2});
tablet_2.select('rect:nth-child(2)').attr({fill: '#FFB280'});
tablet_2.transform('t390');

function animate_wave(element, dur, delay) {
    setTimeout(function() {
        element.attr({r: 100, "fill-opacity": 0.5});
        element.animate({r: 800, 'fill-opacity': 0}, dur, mina.easeout, function(){
            animate_wave(element, dur, delay);
        });
    }, delay);
}