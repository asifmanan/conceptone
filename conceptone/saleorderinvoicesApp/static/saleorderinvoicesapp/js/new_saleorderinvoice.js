$(document).ready(function(){
  $('body').on('click','#id_btn_fetch_so',fetch_saleorder);
  $('body').on('click','#id_btn_select_items',select_items);
  $('body').on('click','#id_btn_submit_invoice_items',submit_invoice);
  // $('body').on('click','#id_btn_saleorder_fetch',select_sale_order);
  // $('body').on('click','#id_sale_order_item_selection',select_sale_order_item);
});
// $(document).ajaxStop(function(){
//   $(document).on("click","#id--toggle-table-view", function(e){
//     e.preventDefault();
//     $(".description--field").toggleClass("compressed");
//   })
// })
function fetch_saleorder(e){
  var company = $("#id_company").val();
  var sale_order = $("#id_sale_order").val();
  if(company && sale_order){
    e.preventDefault();
    const csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
    var url = $("#id_fetch_saleorder_url").val();
    $.ajax({
      type:"POST",
      url:url,
      headers: {'X-CSRFToken':csrftoken},
      datatype:'json',
      data:{
        'company':company,
        'sale_order':sale_order,
      },
      success: function(data){
        if (data['check_flag'] == 1){
          console.log("Condition Failed")
        }
        else{
          $("#id_saleorder_info_section").html(data)
          $(".input--amount--field").each(convert_number_input)
        }
      }
    })
  }
  else{
    // e.preventDefault();
    // console.log("invalid Inputs")
  }
}

function select_items(){
  var selected_item = [];
  $('input[name="saleorderitem"]:checked').each(function(){
    selected_item.push($(this).val());
  });
  // console.log(selected_item);
  if (selected_item.length===0) {
    // console.log("Not Selected");
  }
  else {
    const csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
    var url = $("#id_submit_saleorder_items_url").val();
    // console.log(selected_item.length);
    $.ajax({
      type:"POST",
      url:url,
      headers: {'X-CSRFToken':csrftoken},
      datatype:'json',
      data:{
        'selected_item':selected_item,
      },
      success: function(data){
        if(data['value_error'] == 1){
          console.log("Value Error Occured")
        }
        if (data['check_flag'] == 1){
          console.log("Condition Failed")
        }
        else{
          $("#id_items_section").html(data)
          // $("#id_saleorder_info_section").html(data)
          // $(".input--amount--field").each(convert_number_input)
          console.log("Operation Successful")
        }
      }
    })

    // console.log("Selected");
  }
}

function submit_invoice(e){
  var inv_num = $("#id_invoice_number").val();
  var inv_dt = $("#id_invoice_date").val();
  var bl_qtys = [];
  var bq_fd_ct = 0;
  $("input[name$='bill_quantity']").each(function(){
    bq_fd_ct++;
    if($(this).val()!==""){
      bl_qtys.push($(this).val());
      // console.log($(this).val())
    }
  })
  if (inv_num && inv_dt && bl_qtys.length !== 0 && bl_qtys.length === bq_fd_ct){
    e.preventDefault();
    // console.log(inv_num);
    // console.log(inv_dt);
    for (x in bl_qtys){
      console.log(bl_qtys[x]);
    }
    console.log(bl_qtys);
    const csrftoken = $('input[name="csrfmiddlewaretoken"]').val();
    const url = $("#id_submit_saleorderinvoice_items_url").val();
    $.ajax({
      type:"post",
      url: url,
      headers: {'X-CSRFToken':csrftoken},
      datatype:'json',
      data:{
        'invoice_num':inv_num,
        'invoice_date':inv_dt,
        'bill_quantities':bl_qtys,
        'bill_quantities_count':bq_fd_ct,
      },
      success:function(data){
        if (data['check_flag']==1){
          console.log("Operation failed at server side");
        }
        if (data['value_error']==1){
          console.log("Value Error Occured in the data")
          $("#id_error_message").html(data["error_message"])
        }
        else {
          console.log("Invoice Saved Successfully");
        }
      },
      error:function(xhr,errmsg,err) {
            $('#id_error_message').html("<div class='mt-1 mb-2 alert alert-danger alert-dismissible' role='alert'><button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button>Oops! We have encountered an error: '+errmsg+'</div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
    })
  }
  else{
    // console.log("Enter Invoice Data");
  }
}

function convert_number_input(){
    var raw_num = $(this).val();
    var num = Number(raw_num).toLocaleString('en');
    $(this).val(num);
}
