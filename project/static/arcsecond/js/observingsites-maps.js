/**
 * Created by onekiloparsec on 20/07/15.
 */

/* Requires Google Maps API */

function map_initialize() {
    var myLatlng = new google.maps.LatLng(0.0, 0.0);
    var mapOptions = {
        zoom: 2,
        scrollwheel: false,
        center: myLatlng
    };

    window.map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

    window.map_centers = {};
    window.map_centers['europe'] = new google.maps.LatLng(5.0, 45.0);
}

google.maps.event.addDomListener(window, 'load', map_initialize);

