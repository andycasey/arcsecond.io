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

    google.maps.event.addListenerOnce(window.map, 'idle', function(){
        var angScope = angular.element($('#ObservingSitesNavigationCtlr')).scope();
        angScope.sitesCtlr.installSiteCountsAndMapMarkers();
    });
}

google.maps.event.addDomListener(window, 'load', map_initialize);
