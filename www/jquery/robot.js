$( document ).bind( "mobileinit", function() {
    // Make your jQuery Mobile framework configuration changes here!
    $.support.cors = true;
    $.mobile.allowCrossDomainPages = true; 
});

$(document).keydown(function(e){
	if (e.keyCode == 37 || e.keyCode == 65) {
		$("#left").click();
	} else if (e.keyCode == 38 || e.keyCode == 87) {
		$("#forward").click();
	} else if (e.keyCode == 39 || e.keyCode == 68) {
		$("#right").click();
	} else if (e.keyCode == 40 || e.keyCode == 83) {
		$("#backward").click();
	} else if (e.keyCode == 32) {
		$("#stop").click();
	}
});

$( document ).ready( function() {

	$("#status").delegate("a", "click", function(e) {
		var act = $(this).data('act');
		$.ajax({
			url: '/json/'+act,
			dataType: "jsonp",
			jsonp: "callback",
			jsonpCallback: "jsoncallback"
		});

		function jsonpcallback(data) {
		
		}

	});
});
