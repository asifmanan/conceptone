$(document).ready(function(){
  $('body').on('click','#id_btn_supplier_select',select_supplier);
  $('body').on('click','#id_btn_saleorder_fetch',select_sale_order);
  // $("#id_btn_supplier_select").click(select_supplier);
  // $("#id_btn_saleorder_fetch").click(select_sale_order);
});
// $("#id_btn_saleorder_fetch").click(select_sale_order);
function select_supplier(){
  console.log("Btn Supplier Clicked")
  const csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
  var url = $("#id_select_supplier_url").val();
  var company = $("#id_supplier").val();
  // console.log("hello!")
  if(company){
    $.ajax({
      type:"POST",
      url:url,
      // headers: {'X-CSRFToken': '{{ csrf_token }}'},
      headers: {'X-CSRFToken':csrftoken},
      datatype: 'json',
      data: {
        'company':company
      },
      success: function(data){
        // $("#id_get_form_data_url").val();
        $("#id_sale_order_form").html(data);
        $("#id_supplier").prop('required',false);
        console.log(data);
      }
    })
  }
}

function select_sale_order(){
  const csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
  var url = $("#id_select_saleorder_url").val();
  var sale_order = $("#id_sale_order").val();
  // console.log("hello!")
  if(sale_order){
    $.ajax({
      type:"POST",
      url:url,
      // headers: {'X-CSRFToken': '{{ csrf_token }}'},
      headers: {'X-CSRFToken':csrftoken},
      datatype: 'json',
      data: {
        'sale_order':sale_order
      },
      success: function(select_supplier_return){
        // $("#id_get_form_data_url").val();
        $("#id_sale_order_form").html(select_supplier_return);
        $("#id_supplier").prop('required',false);
        $("#id_sale_order").prop('required',false);
        console.log("####################################")
        console.log(select_supplier_return);
      }
    })
  }
}
