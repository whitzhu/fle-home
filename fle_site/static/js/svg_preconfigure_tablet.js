var svg_pt = Snap("#svg_preconfigure");

var tablet_1_out = svg_pt.rect(100, 100, 200, 300, 20, 20);
var tablet_1_in = svg_pt.rect(120, 120, 160, 250);
var tablet_1_camera = svg_pt.circle(198.5, 110, 3);
var tablet_1_btn = svg_pt.rect(187.5, 380, 25, 10, 5, 5);
tablet_1_camera.attr({fill: 'white'});
tablet_1_btn.attr({fill: 'white'});
tablet_1_in.attr({fill: 'white'});

var tablet_1 = svg_pt.group(tablet_1_out, tablet_1_in, tablet_1_camera, tablet_1_btn);
tablet_1.attr({transform: 't200, s2, r-90'});

var gear_1_url = document.getElementById("gear_1").src;
var gear_2_url = document.getElementById("gear_2").src;

var gear_1 = svg_pt.image(gear_1_url, 230, 120, 200, 200);
var gear_2 = svg_pt.image(gear_2_url, 410, 240, 150, 150);
var gear_set = Snap.set();
gear_set.push(gear_1, gear_2);

animate_gear();

function animate_gear(){
    gear_set.animate(
            [{transform: 'r90,330,220'}, 10000, function(){
                gear_1.attr({ transform: 'rotate(0 330 220)'});
            }], 
            [{ transform: 'r-135,485,315'}, 10000, function(){
                gear_2.attr({ transform: 'rotate(0 485 315)'});
                animate_gear();
            }]
        );
}