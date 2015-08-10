/*!
 * Start Bootstrap - Agency Bootstrap Theme (http://startbootstrap.com)
 * Code licensed under the Apache License v2.0.
 * For details, see http://www.apache.org/licenses/LICENSE-2.0.
 */

// jQuery for page scrolling feature - requires jQuery Easing plugin
$(function() {
    $('a.page-scroll').bind('click', function(event) {
        var $anchor = $(this);
        $('html, body').stop().animate({
            scrollTop: $($anchor.attr('href')).offset().top
        }, 1500, 'easeInOutExpo');
        event.preventDefault();
    });
});

// Highlight the top nav as scrolling occurs
$('body').scrollspy({
    target: '.navbar-fixed-top'
})

// Back to top button
$(document).ready(function() {
    var offset = $("#kickstarter-header").height() + $("#fle-navbar").height() + $("#parallax").height();
    console.log(offset);
    $(window).scroll(function() {
        if ($(this).scrollTop() > offset) {
            $('.back-to-top').fadeIn(500);
        } else {
            $('.back-to-top').fadeOut(500);
        }
    });
    
    $('.back-to-top').click(function() {
        $('html, body').animate({
        	scrollTop: $( $.attr(this, 'href') ).offset().top
        }, 600);
        return false;
    })
});

// Makes scrolling smooth


// fade in and out subscribing message
// $('.email_submit').click(function(){
//     // $('#mce-responses').show();
//     if ($('#mce-success-response').innerHTML == ''){
//         $('#mce-responses').delay(3000).fadeOut(1000, function() {
//             $('#mce-error-response').html('');
//             // $('#mce-success-response').html('');
//             $('#mce-responses').show();
//         });
//     }
//     $('#mce-success-response').html('');
// })