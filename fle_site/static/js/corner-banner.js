$(function() {

    var anim_in_progress = false;

    // expand or hide banner initially based on cookie
    var banner_expanded = $.cookie("banner_hidden") != "true";
    slide_banner({expand: banner_expanded, duration: 0});

    $('.banner_img').click(function() {
        if (!anim_in_progress) {
            ga('send', 'event', 'banner', 'click', banner_expanded ? "hide" : "show");

            anim_in_progress = true;

            banner_expanded = !banner_expanded;

            slide_banner({expand: banner_expanded, callback: function() {
                // Animation complete.
                anim_in_progress = false;
            }});
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
    $('.email_submit').click(function() {
        if (validateEmail($('.email_input').val())) {

            ga('send', 'event', 'banner', 'signup', $('.email_input').val(), 1);

            slide_banner({expand: false, callback: function() {
                // Animation complete.
                $(".subscribe_success").fadeIn(300, function() {
                    $(this).delay(1000).fadeOut(1000);
                });
            }});

        } else {
            $('.sliding').effect('shake');
        }

    });

    $(document).scroll(function() {
        checkOffset();
    });

});

function slide_banner(options) {

    options = $.extend({
        duration: 500,
        callback: null,
        expand: true
    }, options);

    $('.sliding').animate({
        'right': options.expand ? 0 : '-100%'
    }, options.duration, options.callback);

    $.cookie("banner_hidden", !options.expand, {expires: 30});
}

function checkOffset() {

    if ($('.corner_banner').offset().top + $('.corner_banner').height() >= $('#footer').offset().top) {
        $('.corner_banner').css({'position': 'absolute', 'margin-bottom': '20px'});
        $('.sliding').css({'position': 'absolute'});
    }

    if ($(document).scrollTop() + window.innerHeight < $('#footer').offset().top) {
        $('.corner_banner').css({'position': 'fixed', 'margin-bottom': '0px'}); // restore when you scroll up
    }
}

function validateEmail(email) {
    var re = /^([\w-]+(?:\.[\w-]+)*)@((?:[\w-]+\.)*\w[\w-]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$/i;
    return re.test(email);
}

