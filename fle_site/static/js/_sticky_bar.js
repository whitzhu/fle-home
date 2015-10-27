var eli = 55;
var gap = 0;

$(document).ready(function() {

    init_carousel($(".inner_item"), 7);

    // setTimeout(move_carousel, 2000, $(".inner_item"));
    setInterval(move_carousel, 3000, $(".inner_item"));
});


function update_carousel_item(elem){
    var carousel_pos = elem.data('carousel_pos');
    eli += 67;

    if(carousel_pos == 0){
        elem.data("carousel_pos", 8);
        elem.translate3d({x:0, y:300, z:0}, 1000, "ease");
    }else if(carousel_pos == 1){
        elem.data("carousel_pos", 0);
        elem.css({"height": 10});
        elem.translate3d({x:gap-120, y:0, z:0}, 1000, "ease");
    }else if(carousel_pos == 2){
        elem.data("carousel_pos", 1);
        elem.css({"height": 20});
        elem.translate3d({x:gap-80, y:0, z:0}, 1000, "ease");
    }else if(carousel_pos == 3){
        elem.data("carousel_pos", 2);
        elem.css({"height": 30});
        elem.children('.donor_info').css({"opacity": 0});
        elem.translate3d({x:gap-40, y:0, z:0}, 1000, "ease");
    }else if(carousel_pos == 4){   //this going to be the active item
        var d_info = elem.children('.donor_info');
        d_info.html("<div class='gold'>$500"+eli+"</div>Wsada adfkj "+eli);
        d_info.css({"opacity": 1});
        gap = 310 - d_info.width() - 60;
// console.log("EEEE:::::", gap);
        elem.data("carousel_pos", 3);
        elem.css({"height": 50});
        elem.translate3d({x:gap, y:0, z:0}, 1000, "ease");
    }else if(carousel_pos == 5){
        elem.data("carousel_pos", 4);
        elem.css({"height": 30});
        elem.translate3d({x:310, y:0, z:0}, 1000, "ease");
    }else if(carousel_pos == 6){
        elem.data("carousel_pos", 5);
        elem.css({"height": 20});
        elem.translate3d({x:350, y:0, z:0}, 1000, "ease");
    }else if(carousel_pos == 7){
        elem.data("carousel_pos", 6);
        elem.translate3d({x:390, y:0, z:0}, 1000, "ease");
    }else if(carousel_pos == 8){
        elem.data("carousel_pos", 7);
        elem.translate3d({x:450, y:0, z:0}, 1000, "ease");
    }
}

function move_carousel(carousel_items) {
    //it's important to reverse the order so that donor_info text width can be pre-determiined
    $(carousel_items.get().reverse()).each(function(index) {
        update_carousel_item($(this));
    });
}

function get_matrix_x(elem) {
    var matrix = elem.css('transform');
    var values = matrix.match(/-?[\d\.]+/g);
    return values[4];
}

function get_matrix_y(elem) {
    var matrix = elem.css('transform');
    var values = matrix.match(/-?[\d\.]+/g);
    return values[5];
}

;(function($) {
    var delay = 0;
    $.fn.translate3d = function(translations, speed, easing, complete) {
        var opt = $.speed(speed, easing, complete);
        opt.easing = opt.easing || 'ease';
        translations = $.extend({x: 0, y: 0, z: 0}, translations);

        return this.each(function() {
            var $this = $(this);

            $this.css({ 
                transitionDuration: opt.duration + 'ms',
                transitionTimingFunction: opt.easing,
                transform: 'translate3d(' + translations.x + 'px, ' + translations.y + 'px, ' + translations.z + 'px)'
            });

            setTimeout(function() { 
                $this.css({ 
                    transitionDuration: '0s', 
                    transitionTimingFunction: 'ease'
                });

                opt.complete();
            }, opt.duration + (delay || 0));
        });
    };
})(jQuery);

// have to be odd number of items in the carousel
function init_carousel(carousel_items, num_items) {
    var d_info = $(carousel_items[3]).children('.donor_info');
    d_info.html("<div class='gold'>$55</div>Samuel Lawrence Foundation");
    d_info.css({"opacity": 1});
    var init_gap = 310 - d_info.width() - 60;

    carousel_items.each(function(index) {
        switch (index) {
            case 0:
                $(this).data("carousel_pos", 0);
                $(this).css({"height": 10});
                $(this).translate3d({x:init_gap-120, y:0, z:0}, 0);
                break;
            case 1:
                $(this).data("carousel_pos", 1);
                $(this).css({"height": 20});
                $(this).translate3d({x:init_gap-80, y:0, z:0}, 0);
                break;
            case 2:
                $(this).data("carousel_pos", 2);
                $(this).css({"height": 30});
                $(this).translate3d({x:init_gap-40, y:0, z:0}, 0);
                break;
            case 3:   // this is the active item !  !  !  !  !
                $(this).data("carousel_pos", 3);
                $(this).css({"height": 50});
                $(this).translate3d({x:init_gap, y:0, z:0}, 0);
                break;
            case 4:
                $(this).data("carousel_pos", 4);
                $(this).css({"height": 30});
                $(this).translate3d({x:310, y:0, z:0}, 0);
                break;
            case 5:
                $(this).data("carousel_pos", 5);
                $(this).css({"height": 20});
                $(this).translate3d({x:350, y:0, z:0}, 0);
                break;
            case 6:
                $(this).data("carousel_pos", 6);
                $(this).css({"height": 10});
                $(this).translate3d({x:390, y:0, z:0}, 0);
                break;
            case 7:
                $(this).data("carousel_pos", 7);
                $(this).css({"height": 10});
                $(this).translate3d({x:450, y:0, z:0}, 0);
                break;
            case 8:
                $(this).data("carousel_pos", 8);
                $(this).css({"height": 10});
                $(this).translate3d({x:0, y:300, z:0}, 0);
                break;
        }
    });
}