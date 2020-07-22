$(document).ready(function(){
    console.log("Document is ready");
    $("#id_amount").val("900000");
    // $("#id_order_quantity").change(input_validation());
    // $("#id_sale_price").change(input_validation());
      // var item = $('#id_order_quantity').val();
      // console.log("its working!");
      // if($().isNumeric($("#id_order_quantity").val())) {
      //   console.log("value is good");
      //   $("#order_quantity").val("good")
      // }
      // else{
      //   console.log("Not Numeric");
      // }
    );
});
// $("#id_order_quantity").change(input_validation());
// $("#id_sale_price").change(input_validation());

function input_validation () {
  var order_quantity = $("#id_order_quantity").val();
  var sale_price = $("#id_sale_price").val()
  amount = order_quantity*sale_price
  $("#id_amount").innerHTML(amount);
  console.log(amount);
}
