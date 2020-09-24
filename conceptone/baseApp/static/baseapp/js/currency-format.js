$(document).ready(function(){
   $(".amount--field").each(convert_number)
});

function convert_number(){
    var raw_num = $(this).text();
    var num = Number(raw_num).toLocaleString('en');
    $(this).text(num);
}
