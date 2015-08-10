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