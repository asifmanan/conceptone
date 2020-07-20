$(".search_field").on("input", function () {
    $("#id_invoice_number").removeClass("is-invalid");
    $("#id_customer").removeClass("is-invalid");
    $("#id_project").removeClass("is-invalid");
    $("#id_date").removeClass("is-invalid");
});
$("#id_search_btn").click(function () {
if (($.trim($("#id_invoice_number").val()).length === 0 ) &&
    ($.trim($("#id_customer").val()).length === 0 ) &&
    (!Date.parse($("#id_date").val())) &&
    ($.trim($("#id_project").val()).length === 0 )) {
        $("#id_invoice_number").addClass("is-invalid");
        $("#id_customer").addClass("is-invalid");
        $("#id_project").addClass("is-invalid");
        $("#id_date").addClass("is-invalid");
        console.log("Fill in the required fields");
  }
else {
    var url = $("#id_search_form").attr("inv-search-url")
    console.log(url);
    $.ajax({
      url: url,
      datatype:'json',
      data: {
        'customer': $("#id_customer").val(),
        'project': $("#id_project").val(),
        'invoice_number': $("#id_invoice_number").val(),
        'invoice_date': $("#id_date").val(),
      },
      success: function (new_html_table) {
          console.log(new_html_table);
          $("#standardinvoicetable").html(new_html_table);
          }
        });
  }
});
