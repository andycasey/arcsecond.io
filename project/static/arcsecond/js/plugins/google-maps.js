/*------------------------------------------------------------------
Project:        Wolfram
Author:         Yevgeny Simzikov
URL:            http://simpleqode.com/
                https://twitter.com/YevSim
                https://www.facebook.com/simpleqode
Version:        2.2.0
Created:        18/08/2014
Last change:    30/04/2015
-------------------------------------------------------------------*/

/* -------------------- *\
    #GOOGLE MAP
\* -------------------- */

/* Requires Google Maps API */

function initialize() {
  var grenobleLatlng = new google.maps.LatLng(45.1864039,5.7183749); // Change your location
  var genevaLatlng = new google.maps.LatLng(46.2050295,6.1440885); // Change your location

  var mapOptions = {
    zoom: 6, // Change zoom value
    scrollwheel: false, // Change to "true" to enable users scale map on scroll
    center: grenobleLatlng
  }
  var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

  var grenobleMarker = new google.maps.Marker({
      position: grenobleLatlng,
      map: map,
      animation: google.maps.Animation.DROP,
      title: 'Day & Night-time development of arcsecond.io during all time left!'
  });

  var genevaMarker = new google.maps.Marker({
      position: genevaLatlng,
      map: map,
      animation: google.maps.Animation.DROP,
      title: 'Night-time only development of arcsecond.io during weekdays'
  });
}

google.maps.event.addDomListener(window, 'load', initialize);
