$(".search_field").on("input", function () {
    $("#id_customer_name").removeClass("is-invalid");
    $("#id_customer_code").removeClass("is-invalid");
    $("#id_customer_ntn_number").removeClass("is-invalid");
    $("#id_customer_phone").removeClass("is-invalid");
});
$("#id_search_btn").click(function () {
if (($.trim($("#id_customer_name").val()).length === 0 ) &&
    ($.trim($("#id_customer_code").val()).length === 0 ) &&
    ($.trim($("#id_customer_ntn_number").val()).length === 0 ) &&
    ($.trim($("#id_customer_phone").val()).length === 0 )) {
        $("#id_customer_name").addClass("is-invalid");
        $("#id_customer_code").addClass("is-invalid");
        $("#id_customer_ntn_number").addClass("is-invalid");
        $("#id_customer_phone").addClass("is-invalid");
        console.log("Fill in the required fields");
  }
else {
    var url = $("#id_search_form").attr("customer-search-url")
    console.log(url);
    $.ajax({
      url: url,
      datatype:'json',
      data: {
        'customer_name': $("#id_customer_name").val(),
        'customer_code': $("#id_customer_code").val(),
        'customer_ntn_number': $("#id_customer_ntn_number").val(),
        'customer_phone': $("#id_customer_phone").val(),
      },
      success: function (new_html_table) {
          console.log(new_html_table);
          $("#id_customerstable").html(new_html_table);
          }
        });
  }
});
