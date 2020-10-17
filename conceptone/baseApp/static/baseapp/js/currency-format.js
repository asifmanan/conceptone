$(document).ready(function(){
   $(".amount--field").each(convert_number)
   $(".input--amount--field").each(convert_number_input)
});

function convert_number(){
    var raw_num = $(this).text();
    var num = Number(raw_num).toLocaleString('en');
    $(this).text(num);
}

function convert_number_input(){
    var raw_num = $(this).val();
    concole.log(raw_num);
    var num = Number(raw_num).toLocaleString('en');
    $(this).val(num);
}
