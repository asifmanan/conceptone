$(document).ready(function(){
  $('body').on('click','#id_btn_fetch_so',fetch_saleorder);
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
  // console.log(company);
  // console.log(sale_order);

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
        // console.log(data['check_flag'])
        if (data['check_flag'] == 1){
          console.log("Condition Failed")
          // $("#id_div_select_supplier_form").html(data)
        }
        else{
          $("#id_saleorder_info_section").html(data)
          $(".input--amount--field").each(convert_number_input)

          // console.log(data['company']);
          // console.log(data['sale_order']);
          // console.log(data['check_flag']);
        }
      }
    })
  }
  else{
    // e.preventDefault();
    // console.log("invalid Inputs")
  }
}

function convert_number_input(){
    var raw_num = $(this).val();
    console.log(raw_num);
    var num = Number(raw_num).toLocaleString('en');
    $(this).val(num);
}
