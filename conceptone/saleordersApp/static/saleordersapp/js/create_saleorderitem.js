$(document).ready(function(){
  $(".item-input").each(id_serializer);
  $(".tax-input").each(id_serializer)
  $(".order-quantity-input").each(id_serializer)
  $(".sale-price-input").each(id_serializer)
  $("#id_order_quantity1").change(calculate_amount1);
  $("#id_sale_price1").change(calculate_amount1);
  $("#id_tax1").change(get_tax_value);
});

function id_serializer(i,obj){
  var current_id = $(this).attr('id');
  var new_id = current_id+i;
  $(this).attr('id',new_id);
}

function calculate_amount1(){
  order_quantity = $("#id_order_quantity1").val();
  sale_price = $("#id_sale_price1").val();
  amount = order_quantity*sale_price;
  $("#id_amount1").val(parseFloat(amount).toFixed(2));
  calculate_tax_amount1();
}

function calculate_tax_amount1(){
  var tax_value = parseFloat($("#id_tax_value").val());
  var amount = parseFloat($("#id_amount1").val());
  var tax_amount = tax_value*amount;
  // console.log(tax_value);
  // console.log(amount);
  // console.log(tax_amount);
  $("#id_tax_amount1").val(parseFloat(tax_amount).toFixed(2));
  calculate_total_amount1();
}

function calculate_total_amount1(){
  var amount = parseFloat($("#id_amount1").val());
  var tax_amount = parseFloat($("#id_tax_amount1").val());
  var total_amount = amount + tax_amount;
  $("#id_total_amount1").val(parseFloat(total_amount).toFixed(2));
}

function get_tax_value(){
  var url = $("#id_get_tax_value_url").val();
  var tax_id = $(this).val();
  if($(this).val()){
    // console.log("value selected!");
    if(tax_id!=""){
      // console.log(tax_id);
      $.ajax({
        url: url,
        datatype: 'json',
        data: {
          'tax_id': tax_id
        },
        success: function (data){
          // console.log(data.data);
          var tax_value = data.data;
          $("#id_tax_value").val(tax_value);
          calculate_tax_amount1();
        }
      })
    }
  }
  else{
    $("#id_tax_value").val(0);
    calculate_tax_amount1();
  }
}
