$(".search_field").on("input", function () {
    $("#id_si_number").removeClass("is-invalid");
    $("#id_si_number").removeClass("is-invalid");
    $("#id_sale_order").removeClass("is-invalid");
    $("#id_customer").removeClass("is-invalid");
    $("#id_project").removeClass("is-invalid");
});
$("#id_search_btn").click(function () {
if (($.trim($("#id_si_number").val()).length === 0 ) &&
    ($.trim($("#id_sale_order").val()).length === 0 ) &&
    ($.trim($("#id_customer").val()).length === 0 ) &&
    ($.trim($("#id_project").val()).length === 0 )) {
        $("#id_si_number").addClass("is-invalid");
        $("#id_sale_order").addClass("is-invalid");
        $("#id_customer").addClass("is-invalid");
        $("#id_project").addClass("is-invalid");
        console.log("Fill in the required fields");
  }
else {
    var search_param = $("#id_customer").val();
    var url = $("#id_search_form").attr("invoice-search-url")
    console.log(search_param);
    console.log(url);

    $.ajax({
      url: url,
      datatype:'json',
      data: {
        'invoice_number': $("#id_si_number").val(),
        'sale_order': $("#id_sale_order").val(),
        'project': $("#id_project").val(),
        'customer': $("#id_customer").val(),
      },
      success: function (new_html_table) {
          console.log(new_html_table);
          $("#invoiceviewtable").html(new_html_table);
          }
        });
  }
});
