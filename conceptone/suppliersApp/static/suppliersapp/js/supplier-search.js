$(".search_field").on("input", function () {
    $("#id_supplier_name").removeClass("is-invalid");
    $("#id_supplier_code").removeClass("is-invalid");
    $("#id_supplier_ntn_number").removeClass("is-invalid");
    $("#id_supplier_phone").removeClass("is-invalid");
});
$("#id_search_btn").click(function () {
if (($.trim($("#id_supplier_name").val()).length === 0 ) &&
    ($.trim($("#id_supplier_code").val()).length === 0 ) &&
    ($.trim($("#id_supplier_ntn_number").val()).length === 0 ) &&
    ($.trim($("#id_supplier_phone").val()).length === 0 )) {
        $("#id_supplier_name").addClass("is-invalid");
        $("#id_supplier_code").addClass("is-invalid");
        $("#id_supplier_ntn_number").addClass("is-invalid");
        $("#id_supplier_phone").addClass("is-invalid");
        console.log("Fill in the required fields");
  }
else {
    var url = $("#id_search_form").attr("supplier-search-url")
    console.log(url);
    $.ajax({
      url: url,
      datatype:'json',
      data: {
        'supplier_name': $("#id_supplier_name").val(),
        'supplier_code': $("#id_supplier_code").val(),
        'supplier_ntn_number': $("#id_supplier_ntn_number").val(),
        'supplier_phone': $("#id_supplier_phone").val(),
      },
      success: function (new_html_table) {
          console.log(new_html_table);
          $("#id_supplierstable").html(new_html_table);
          }
        });
  }
});
