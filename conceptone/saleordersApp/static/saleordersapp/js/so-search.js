$(".search_field").on("input", function () {
    $("#id_so_number").removeClass("is-invalid");
    $("#id_buyer").removeClass("is-invalid");
    $("#id_buyer_po_number").removeClass("is-invalid");
    $("#id_buyer_po_date").removeClass("is-invalid");
});
$("#id_search_btn").click(function () {
if (($.trim($("#id_so_number").val()).length === 0 ) &&
    ($.trim($("#id_buyer").val()).length === 0 ) &&
    (!Date.parse($("#id_buyer_po_date").val())) &&
    ($.trim($("#id_buyer_po_number").val()).length === 0 )) {
        $("#id_so_number").addClass("is-invalid");
        $("#id_buyer").addClass("is-invalid");
        $("#id_buyer_po_number").addClass("is-invalid");
        $("#id_buyer_po_date").addClass("is-invalid");
        console.log("Fill in the required fields");
  }
else {
    var url = $("#id_search_form").attr("so-search-url")
    console.log(url);
    $.ajax({
      url: url,
      datatype:'json',
      data: {
        'so_number': $("#id_so_number").val(),
        'buyer': $("#id_buyer").val(),
        'buyer_po_number': $("#id_buyer_po_number").val(),
        'buyer_po_date': $("#id_buyer_po_date").val(),
      },
      success: function (new_html_table) {
          console.log(new_html_table);
          $("#saleordertable").html(new_html_table);
          }
        });
  }
});
