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
  }
  var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

  //var marker = new google.maps.Marker({
  //    position: myLatlng,
  //    map: map,
  //    title: 'Home of onekilopars.ec and arcsecond.io'
  //});
}

google.maps.event.addDomListener(window, 'load', initialize);
