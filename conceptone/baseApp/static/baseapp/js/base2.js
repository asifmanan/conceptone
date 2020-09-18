$("#menu-toggle").click(function(e) {
    e.preventDefault();
    $("#wrapper").toggleClass("toggled");
    $("#menu-toggle-btn-icon").toggleClass("fa-angle-left");
    $("#menu-toggle-btn-icon").toggleClass("fa-angle-right");
});
