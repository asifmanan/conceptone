$(document).ready(function(){
  $('body').on('click','#id_btn_supplier_select',select_supplier);
  $('body').on('click','#id_btn_saleorder_fetch',select_sale_order);
  $('body').on('click','#id_sale_order_item_selection',select_sale_order_item);
  // $("#id_btn_supplier_select").click(select_supplier);
  // $("#id_btn_saleorder_fetch").click(select_sale_order);
});
// $("#id_btn_saleorder_fetch").click(select_sale_order);
function select_supplier(){
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
        // console.log(data);
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
        // console.log("####################################")
        // console.log(select_supplier_return);
      }
    })
  }
}

function selected_items(){
  var selected_item = [];
  $.each($("input[name='saleorderitem']:checked"),function(){
    selected_item.push($(this).val());
  });
  // console.log(selected_item);
  return selected_item
}

function select_sale_order_item(){
  const csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
  var url = $("#id_select_saleorder_item_url").val();
  var sale_order_item = selected_items();
  console.log(sale_order_item);
  if(!(sale_order_item === undefined || sale_order_item.length==0)){
    $.ajax({
      type:"POST",
      url:url,
      // headers: {'X-CSRFToken': '{{ csrf_token }}'},
      headers: {'X-CSRFToken':csrftoken},
      datatype: 'json',
      data: {
        'sale_order_item[]':sale_order_item
      },
      success: function(selected_item_list){
        console.log("Success");
        console.log(selected_item_list);
        // $("#id_get_form_data_url").val();
        // $("#id_sale_order_form").html(select_supplier_return);
        // $("#id_supplier").prop('required',false);
        // $("#id_sale_order").prop('required',false);
        // console.log("####################################")
        // console.log(select_supplier_return);
      }
    })
  }
}
