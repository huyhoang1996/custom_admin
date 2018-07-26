$(document).ready(function() {
    console.log("Load JS");
    $("#id_publish").on('click', function(){
        if($("#id_publish").is(':checked')){
            $(".field-users").hide();
        }else{
            
            $(".field-users").show();
        }
    });
    
});