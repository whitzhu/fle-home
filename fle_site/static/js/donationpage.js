$(document).ready(
 
  function() {
    $("#other").click(function() {
      $("#input-amount").slideDown();;
    });
  
  $(".btn-amount").click(function(){
   $(this).toggleClass('active').siblings().removeClass("active");
  });
  
    $(".btn-amount-number").click(function(){
      $("#input-amount").hide();
    });
  });

  
 
  
