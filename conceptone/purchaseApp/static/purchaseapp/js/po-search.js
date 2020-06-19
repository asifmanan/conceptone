$(".search_field").on("input", function () {
    $("#id_po_number").removeClass("is-invalid");
    $("#id_supplier").removeClass("is-invalid");
    $("#id_project").removeClass("is-invalid");
    $("#id_date").removeClass("is-invalid");
});
$("#id_search_btn").click(function () {
if (($.trim($("#id_po_number").val()).length === 0 ) &&
    ($.trim($("#id_supplier").val()).length === 0 ) &&
    (!Date.parse($("#id_date").val())) &&
    ($.trim($("#id_project").val()).length === 0 )) {
        $("#id_po_number").addClass("is-invalid");
        $("#id_supplier").addClass("is-invalid");
        $("#id_project").addClass("is-invalid");
        $("#id_date").addClass("is-invalid");
        console.log("Fill in the required fields");
  }
else {
    var url = $("#id_search_form").attr("po-search-url")
    console.log(url);
    $.ajax({
      url: url,
      datatype:'json',
      data: {
        'supplier': $("#id_supplier").val(),
        'project': $("#id_project").val(),
        'po_number': $("#id_po_number").val(),
        'po_date': $("#id_date").val(),
      },
      success: function (new_html_table) {
          console.log(new_html_table);
          $("#purchaseordertable").html(new_html_table);
          }
        });
  }
});
