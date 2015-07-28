$(function() {
    var anima_click = true;
    var sliding_out = '-100%';
    var sliding_out_cookie = $.cookie("sliding_cookie");

    if(sliding_out_cookie){
        $('.sliding').css({'right': sliding_out});
    }else{
        sliding_out = 0;
        $('.sliding').css({'right': sliding_out});
    }

    $('.banner_img').click(function() {
        if(anima_click){
            ga('send', 'event', 'click', 'banner_img');
            anima_click = false;
            if(sliding_out == '-100%'){
                sliding_out = 0;
            }else{
                sliding_out = '-100%';
            }
            $('.sliding').animate({
                'right': sliding_out
            }, 500, function() {
                // Animation complete.
                anima_click = true;
            });
        }
    });
// <-- fixup for jquery-ui shake animation with certain css attr.
    if ($.ui) {
        (function () {
            var oldEffect = $.fn.effect;
            $.fn.effect = function (effectName) {
                if (effectName === "shake") {
                    var old = $.effects.createWrapper;
                    $.effects.createWrapper = function (element) {
                        var result;
                        var oldCSS = $.fn.css;

                        $.fn.css = function (size) {
                            var _element = this;
                            var hasOwn = Object.prototype.hasOwnProperty;
                            return _element === element && hasOwn.call(size, "width") && hasOwn.call(size, "height") && _element || oldCSS.apply(this, arguments);
                        };

                        result = old.apply(this, arguments);

                        $.fn.css = oldCSS;
                        return result;
                    };
                }
                return oldEffect.apply(this, arguments);
            };
        })();
    }
// fixup for jquery-ui shake animation with certain css attr. -->
    $('.email_submit').click(function(){
        if(validateEmail($('.email_input').val())){
            $.cookie("sliding_cookie", true, { expires : 30 }); //make corner banner not shown for a month
            sliding_out = '-100%';
            $('.sliding').animate({
                'right': sliding_out
            }, 500, function() {
                // Animation complete.
                $(".subscribe_success").fadeIn(300, function(){
                    $(this).delay(1000).fadeOut(1000);
                });
            });

            var google_conversion_id = 946262510;
            var google_conversion_label = "-PIICObG2F4Q7qObwwM";
            var image = new Image(1, 1); 
            image.src = "//www.googleadservices.com/pagead/conversion/" + google_conversion_id + "/?label=" + google_conversion_label + "&script=0";

        }else{
            $('.sliding').effect('shake');
        }
    });
});
function checkOffset() {
    if($('.corner_banner').offset().top + $('.corner_banner').height() >= $('#footer').offset().top){
        $('.corner_banner').css({'position': 'absolute', 'margin-bottom': '20px'});
        $('.sliding').css({'position': 'absolute'});
    }
    if($(document).scrollTop() + window.innerHeight < $('#footer').offset().top){
        $('.corner_banner').css({'position': 'fixed', 'margin-bottom': '0px'}); // restore when you scroll up
    }
}
$(document).scroll(function() {
    checkOffset();
});
function validateEmail(email) {
    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    return re.test(email);
}