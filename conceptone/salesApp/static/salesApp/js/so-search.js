$(".search_field").on("input", function () {
    $("#id_so_number").removeClass("is-invalid");
    $("#id_customer").removeClass("is-invalid");
    $("#id_project").removeClass("is-invalid");
    $("#id_date").removeClass("is-invalid");
});
$("#id_search_btn").click(function () {
if (($.trim($("#id_so_number").val()).length === 0 ) &&
    ($.trim($("#id_customer").val()).length === 0 ) &&
    (!Date.parse($("#id_date").val())) &&
    ($.trim($("#id_project").val()).length === 0 )) {
        $("#id_so_number").addClass("is-invalid");
        $("#id_customer").addClass("is-invalid");
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
        'customer': $("#id_customer").val(),
        'project': $("#id_project").val(),
        'so_number': $("#id_so_number").val(),
        'so_date': $("#id_date").val(),
      },
      success: function (new_html_table) {
          console.log(new_html_table);
          $("#saleordertable").html(new_html_table);
          }
        });
  }
});
