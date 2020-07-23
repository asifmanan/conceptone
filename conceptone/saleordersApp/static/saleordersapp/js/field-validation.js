$(document).ready(function(){
  $(".item-input").each(id_serializer);
  $(".tax-input").each(id_serializer)
  $(".order-quantity-input").each(id_serializer)
  $(".sale-price-input").each(id_serializer)
  $("#id_order_quantity1").change(calculate_amount1);
  $("#id_sale_price1").change(calculate_amount1);
  $("#id_tax1").change(get_tax_value);
});

function calculate_amount1(){
  order_quantity = $("#id_order_quantity1").val();
  sale_price = $("#id_sale_price1").val();
  amount = order_quantity*sale_price;
  $("#id_amount1").val(amount);

}
function id_serializer(i,obj){
  var current_id = $(this).attr('id');
  var new_id = current_id+i;
  $(this).attr('id',new_id);
}

function get_tax_value(){
  var url = $("#id_get_tax_value_url").val();
  var tax_id = $(this).val();
  $.ajax({
    url: url,
    datatype: 'json',
    data: {
      'tax_id': tax_id
    },
    success: function (data){
      $("#tax_amount1").val(data.data);
    }
  })
}
// $('#id_order_quantity0').change(function(){
//     console.log(($("#id_order_quantity").val()));
// });
