$(".search_field").on("input", function () {
    $("#id_item_code").removeClass("is-invalid");
    $("#id_item_description").removeClass("is-invalid");
    $("#id_item_type").removeClass("is-invalid");
    $("#id_item_sub_type").removeClass("is-invalid");
});
$("#id_search_btn").click(function () {
if (($.trim($("#id_item_code").val()).length === 0 ) &&
    ($.trim($("#id_item_description").val()).length === 0 ) &&
    ($.trim($("#id_item_type").val()).length === 0 ) &&
    ($.trim($("#id_item_sub_type").val()).length === 0 )) {
        $("#id_item_code").addClass("is-invalid");
        $("#id_item_description").addClass("is-invalid");
        $("#id_item_type").addClass("is-invalid");
        $("#id_item_sub_type").addClass("is-invalid");
        console.log("Fill in the required fields");
  }
else {
    var url = $("#id_search_form").attr("item-search-url")
    console.log(url);
    $.ajax({
      url: url,
      datatype:'json',
      data: {
        'item_code': $("#id_item_code").val(),
        'item_description': $("#id_item_description").val(),
        'item_type': $("#id_item_type").val(),
        'item_sub_type': $("#id_item_sub_type").val(),
      },
      success: function (new_html_table) {
          console.log(new_html_table);
          $("#id_itemstable").html(new_html_table);
          }
        });
  }
});
