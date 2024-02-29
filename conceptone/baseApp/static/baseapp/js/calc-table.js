$(document).on("click","#id--toggle-table-view", function(e){
  e.preventDefault();
  $(".description--field").toggleClass("compressed");
})

// $("#id--toggle-table-view").click(function(e) {
//     e.preventDefault();
//     $(".description--field").toggleClass("compressed");
// });
