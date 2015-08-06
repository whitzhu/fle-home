var svg_cc = Snap("#svg_content_curation");


var circle_1 = svg_cc.circle(270, 0, 50);
circle_1.attr({fill: 'pink', stroke: 'white', strokeWidth: 15});
// var line_1 = svg_cc.line(400, 230, 270, 0).attr({strokeWidth: 15, stroke: "white"});

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

console.log('FFFF: ', circle_2.getBBox().cx);

animate_concentrate_center(circle_1, circle_1.getBBox().cx, circle_1.getBBox().cy);
animate_concentrate(circle_2, circle_2.getBBox().cx, circle_2.getBBox().cy);
animate_concentrate(circle_3, circle_3.getBBox().cx, circle_3.getBBox().cy);
animate_concentrate(circle_4, circle_4.getBBox().cx, circle_4.getBBox().cy);
animate_concentrate(circle_5, circle_5.getBBox().cx, circle_5.getBBox().cy);

function animate_concentrate(element, x, y) {
    element.animate({cx: 400, cy: 230}, 1000, mina.backin, function(){
        element.attr({opacity: 0});
        element.animate({cx: x, cy: y}, 1000, function(){
            element.animate({opacity: 1}, 1000, function(){
                animate_concentrate(element, x, y);
            });
        });
    });
}

function animate_concentrate_center(element, x, y) {
    element.animate({cx: 400, cy: 230}, 1000, mina.backin, function(){
        center_circle.animate({'fill-opacity': 1}, 300, mina.easein);
        element.attr({opacity: 0});
        element.animate({cx: x, cy: y}, 1000, function(){
            center_circle.animate({'fill-opacity': 0}, 500, mina.easeout);
            element.animate({opacity: 1}, 1000, function(){
                animate_concentrate_center(element, x, y);
            });
        });
    });
}