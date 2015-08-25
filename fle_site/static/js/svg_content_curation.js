var svg_cc = Snap("#svg_content_curation");

var line_1 = svg_cc.line(400, 230, 270, 0).attr({id:'l', strokeWidth: 15, stroke: "black"});
var circle_1 = svg_cc.circle(270, 0, 50).attr({id:'c', fill: 'pink', stroke: 'black', strokeWidth: 15});

var line_2 = svg_cc.line(400, 230, 160, 220).attr({id:'l', strokeWidth: 15, stroke: "black"});
var circle_2 = svg_cc.circle(160, 220, 80).attr({id:'c', fill: 'yellow', stroke: 'black', strokeWidth: 15});

var line_3 = svg_cc.line(400, 230, 580, 420).attr({id:'l', strokeWidth: 15, stroke: "black"});
var circle_3 = svg_cc.circle(580, 420, 70).attr({id:'c', fill: '#66CCFF', stroke: 'black', strokeWidth: 15});

var line_4 = svg_cc.line(400, 230, 280, 420).attr({id:'l', strokeWidth: 15, stroke: "black"});
var circle_4 = svg_cc.circle(280, 420, 50).attr({id:'c', fill: 'grey', stroke: 'black', strokeWidth: 15});

var line_5 = svg_cc.line(400, 230, 600, 20).attr({id:'l', strokeWidth: 15, stroke: "black"});
var circle_5 = svg_cc.circle(600, 20, 80).attr({id:'c', fill: 'orange', stroke: 'black', strokeWidth: 15});

var c_set = svg_cc.selectAll('#c');
var l_set = svg_cc.selectAll('#l');

var c_position = [{cx:270, cy:0}, {cx:160, cy:220}, {cx:580, cy:420}, {cx:280, cy:420}, {cx:600, cy:20}];

var center_circle = svg_cc.circle(400, 230, 100).attr({fill: 'white', stroke: 'black', strokeWidth: 15});

var cc_bulb_url = document.getElementById("cc_bulb").src;
var cc_bulb = svg_cc.image(cc_bulb_url, 355, 170, 90, 120);

loop_circle();

function loop_circle() {
    l_set.animate({x2: 400, y2: 230}, 1000, mina.backin);
    c_set.animate({cx: 400, cy: 230}, 1000, mina.backin, function(){
        cc_bulb.animate({'opacity': 1}, 300, mina.easein);
        center_circle.animate({'fill': '#8670A1'}, 300, mina.easein, function(){
            setTimeout(function() {
                reset_circle();
                l_set.animate(
                    [{x2: 270, y2: 0}, 1000, mina.backin], 
                    [{x2: 160, y2: 220}, 1000, mina.backin],
                    [{x2: 580, y2: 420}, 1000, mina.backin],
                    [{x2: 280, y2: 420}, 1000, mina.backin],
                    [{x2: 600, y2: 20}, 1000, mina.backin, function(){
                        loop_circle();
                    }]
                );
                c_set.animate({opacity: 1}, 1000);
            }, 1000);
        });
    });
}

function reset_circle() {
    c_set.forEach(function(e, index){
        e.attr({opacity: 0, cx: c_position[index].cx, cy: c_position[index].cy});
    });
    center_circle.animate({'fill': 'white'}, 500, mina.easeout);
    cc_bulb.animate({'opacity': 0}, 500, mina.easeout);
}