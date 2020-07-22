$("#id_order_quantity").change(function () {
  var order_quantity = $("#id_order_quantity").val();
  console.log(order_quantity);
  if(isNumeric($("#id_order_quantity").val())) {
    console.log("value is good");
    // $("#order_quantity").val("good")
  }
  else{
    console.log("Not Numeric");
  }
});
