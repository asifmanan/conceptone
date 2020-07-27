$(document).ready(function(){
  $("#id_btn_supplier_select").click(get_form_data);
});

function get_form_data(){
  var url = $("#id_get_form_data_url").val();
  var company = $("#id_supplier").val();
  console.log("hello!")
  if(company){
    $.ajax({
      url:url,
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
