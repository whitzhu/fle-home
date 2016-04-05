$(document).ready(
 
  function() {
    $("#other-amount").click(function() {
      $("#input-amount").slideDown();;
    });
  
    //Click of donation-amount buttons toggle button-pressed effect
    $(".btn-amount").click(function(){
     $(this).toggleClass('active').siblings().removeClass("active");
    });

    //Click stores value of preset $20, $50, $100 is stored 
    $(".btn-amount-number").click(function(){
     var amount = $(this).attr("value");
     console.log(amount);
    });
  
    $(".btn-amount-number").click(function(){
      $("#input-amount").hide();
    });

    $("#btn-card").click(function(){
      
      if (  $(".active").val() == "custom"){
        amount = $("#InputAmount").val();
        if (amount.match(/^\d+$/)){
          console.log(amount);
        }else{
          alert("Please Enter Valid Number");
        }  
      }else{
        amount = $(".active").val();
        alert(amount); 
      }      
      
    });

  });


//alert($("#InputAmount").val());
//alert($(".active").val());

  
 
  
