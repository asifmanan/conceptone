$("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
});

$(".sidenav-btn-collapse").click(function(e) {
   e.preventDefault();
    if (!$(this).next(".sidebar-collapse-menu").hasClass("show")) {
        console.log("its open");
        $(".sidebar-collapse-menu").each(function(){
          $(".sidebar-collapse-menu").removeClass("show");
        })
        $(this).next(".sidebar-collapse-menu").addClass("show");
    }
    else {
        $(this).next(".sidebar-collapse-menu").removeClass("show");
    }
});

$("#id--toggle-table-view").click(function(e) {
    e.preventDefault();
    $(".collapse--field").toggleClass("compressed");
});
