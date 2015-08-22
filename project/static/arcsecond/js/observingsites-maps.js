/**
 * Created by onekiloparsec on 20/07/15.
 */

/* Requires Google Maps API */

function initialize() {
    var myLatlng = new google.maps.LatLng(0.0, 0.0); // Change your location
    var mapOptions = {
        zoom: 2, // Change zoom value
        scrollwheel: false, // Change to "true" to enable users scale map on scroll
        center: myLatlng
    };

    window.map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
}

google.maps.event.addDomListener(window, 'load', initialize);
