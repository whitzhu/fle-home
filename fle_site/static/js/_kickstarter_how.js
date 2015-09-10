$(function() {
    var internet_cloud = $('.internet_cloud');
    var option_text = $('.option_text');
    var click = true;

    setInterval(function(){
        animate_cloud();
    }, 3000);

    function animate_cloud() {
        if(!click){
            click = true;
            internet_cloud.removeClass('animated flipOutX').addClass('hidden');
            option_text.removeClass('animated fadeOut').addClass('hidden');
            setTimeout(function (){
                internet_cloud.addClass('animated flipInX').removeClass('hidden');
                option_text.addClass('animated fadeIn').removeClass('hidden');
            }, 1000);
        }else{
            click = false;
            internet_cloud.removeClass('animated flipInX');
            option_text.removeClass('animated fadeIn');
            setTimeout(function (){
                internet_cloud.addClass('animated flipOutX');
                option_text.addClass('animated fadeOut');
            }, 1000);
        }
    }
});