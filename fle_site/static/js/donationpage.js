$(document).ready(
 
  function() {

    $("#other-amount").click(function() {
      $("#input-amount").slideDown();
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
        console.log(amount);
      }       
  });

    var handler = StripeCheckout.configure({
      key: 'pk_test_6pRNASCoBOKtIshFeQd4XMUh',
      image: 'https://s3.amazonaws.com/stripe-uploads/acct_102ejd27dVLKpIVBmerchant-icon-141490-FLE-globe-only-logo.png' ,
      locale: 'auto',
      token: function(data) {

                _.extend(data, $("#donate-form").serializeObject());

                $.ajax({
                    method: "POST",
                    url: "{% url 'process_donation' %}",
                    data: JSON.stringify(data),
                    dataType: "json",
                    contentType: "application/json",
                    beforeSend: function(xhr, settings) {
                        xhr.setRequestHeader("X-CSRFToken", data.csrfmiddlewaretoken);
                    }
                }).then(function(response) {
                    show_message(response.status, response.message, "transaction-message");
                });
          }
    });

    $('#btn-card').on('click', function(e) {
      // Open Checkout with further options
      handler.open({
        name: 'Learning Equality',
        description: 'Donation',
        amount: amount*100,
        panelLabel: "Give",
      });
      e.preventDefault();
    });

    // Close Checkout on page navigation
    $(window).on('popstate', function() {
      handler.close();
    });


});


  
 
  
