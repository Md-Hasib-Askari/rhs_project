
$(document).ready( ()=> {
    // post images
    $('.card .card-body p img').addClass('img-fluid');
    var card_body_image_width = $('.card').width() - 40;
    var card_body_image_height = card_body_image_width * 3/4;
    $('.card .card-body p img').css({'width': card_body_image_width, 'height': card_body_image_height, 'margin-bottom': '10px'});

    // Facebook Sidebar Plugin width
    var facebook_plugin_width = $('.facebool-plugin').width();
    $('.facebool-plugin > .card-body > iframe').attr('width', facebook_plugin_width);

    // Google Maps Sidebar Plugin width
    var google_map_api_width = $('.google-map-api').width() - 40;
    $('.google-map-api > .card-body > iframe').attr('width', google_map_api_width);

    // Google Calendar Sidebar Plugin width
    var google_calendar_width = $('.google-calendar').width() - 40;
    $('google_calendar > .card-body > iframe').attr('width', google_calendar_width);

    $(window).resize( ()=> {

        // Facebook Sidebar Plugin width
        var facebook_plugin_width = $('.facebool-plugin').width();
        $('.facebool-plugin > .card-body > iframe').attr('width', facebook_plugin_width);

        // Google Maps Sidebar Plugin width
        var google_map_api_width = $('.google-map-api').width() - 40;
        $('.google-map-api > .card-body > iframe').attr('width', google_map_api_width);

        // Google Calendar Sidebar Plugin width
        var google_calendar_width = $('.google-calendar').width() - 40;
        var google_calendar_height = google_calendar_width * 2/3;

        $('.google-calendar > .card-body > iframe').attr('width', google_calendar_width);
        $('.google-calendar > .card-body > iframe').attr('height', google_calendar_height);

	// post images
        var card_body_image_width = $('.card').width() - 40;
        var card_body_image_height = card_body_image_width * 3/4;
	$('.card .card-body p img').css({'width': card_body_image_width, 'height': card_body_image_height});

    });
});
