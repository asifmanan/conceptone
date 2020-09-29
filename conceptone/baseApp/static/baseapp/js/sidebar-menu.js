$("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
});

$("#id--toggle-table-view").click(function(e) {
    e.preventDefault();
    $(".collapse--field").toggleClass("compressed");
});
