
//Donation Interface  
$(function() {

  //Other input field slides down
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

  //Hides the other input box when $20, $50, $100 is selected
  $(".btn-amount-number").click(function(){
    $("#input-amount").hide();
  });

});

//Stripe  
$(function(){ 

  var MonthlyGiving = false;
  
  //Stripe Integration
  var handler = StripeCheckout.configure({
    key: 'pk_test_6pRNASCoBOKtIshFeQd4XMUh',
    image: 'https://s3.amazonaws.com/stripe-uploads/acct_102ejd27dVLKpIVBmerchant-icon-141490-FLE-globe-only-logo.png' ,
    locale: 'auto',
    token: function(data) {

              $.ajax({
                  method: "POST",
                  url: "/donate/process/",
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



  //Checkout process when 'Pay by Card' is selected
  $('#btn-card').on('click', function(e) {

    //Check for monthly giving
    if (  $('#monthly-checkbox').prop('checked') ){
      MonthlyGiving = true;
      console.log('Monthy Giving');  //Check if monthly payment is selected
    }
    
    if (  $(".active").val() == "custom"){
      amount = $("#InputAmount").val();
      if (amount.match(/^\d+$/)){
        console.log(amount);
        console.log(MonthlyGiving);

        handler.open({
        name: 'Learning Equality',
        description: 'Donation',
        amount: amount*100,
        panelLabel: "Give",
        });
        e.preventDefault();
      }else{
        alert("Please Enter Valid Number");
      }  
    }else{
      amount = $(".active").val();
      console.log(amount);
      console.log(MonthlyGiving);

      handler.open({
      name: 'Learning Equality',
      description: 'Donation',
      amount: amount*100,
      panelLabel: "Give",
      });
      e.preventDefault();
    } 
  });

  // Close Checkout on page navigation
  $(window).on('popstate', function() {
    handler.close();
  });

});


// Waypoint for Progress Bar



//Circle Progress bar
// $(function(){
//     window.onload = function onLoad() {

//     var circle = new ProgressBar.Circle('#circle-stats', {
//         color: '#FFFFFF',
//         strokeWidth: 3,
     
//         text: { value:'100% Guarantee'}
//     });

//     circle.animate(0.7, function() {
//         circle.animate(1);
//     });
//     }
// });



$(function(){ 
  var times = 0;
  
  $('.guarantee').waypoint(function(direction){ 

    if (direction === 'down' && times == 0){

    var bar = new ProgressBar.Circle('#circle-stats', {
      color: '#FFFFFF',
      // This has to be the same size as the maximum width to
      // prevent clipping
      strokeWidth: 4,
      trailWidth: 0,
      easing: 'easeInOut',
      duration: 1400,
      text: {
        autoStyleContainer: false
      },
      from: { color: '#FFFFFF', width: 0 },
      to: { color: '#FFFFFF', width: 4 },
      // Set default step function for all animate calls
      step: function(state, circle) {
        circle.path.setAttribute('stroke', state.color);
        circle.path.setAttribute('stroke-width', state.width);

        var value = Math.round(circle.value() * 100);
        if (value === 0) {
          circle.setText('');
        } else {
          circle.setText(value + "<html style='font-size: 14px' > % <br> Guarantee</html>" );
        }
      }
    });

    bar.text.style.position = 'relative';
    bar.text.style.top = '-120px';

    bar.animate(1.0);  // Number from 0.0 to 1.0
    }

    times =+ 1;
  }, {
    offset: '60%' 
  })
});
 
  
