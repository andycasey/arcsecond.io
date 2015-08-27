/**
 * Created by onekiloparsec on 09/08/15.
 */

var API_VERSION = "1";
var API_PROTOCOL = "http";

var app = angular.module('arcsecondApp', []);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

app.controller('ObservingSitesNavigationCtlr', ['$scope', '$http', '$rootScope',
        function ($scope, $http, $rootScope) {
            var sitesCtlr = this;

            sitesCtlr.continents = [
                {name:'Africa', key:'africa'},
                {name:'Antarctica', key:'antarctica'},
                {name:'Asia', key:'asia'},
                {name:'Europe', key:'europe'},
                {name:'North America', key:'north_america'},
                {name:'Oceania', key:'oceania'},
                {name:'South America', key:'south_america'}
            ];

            sitesCtlr.sites = {};
            sitesCtlr.markers = {};
            sitesCtlr.infowindows = {};
            sitesCtlr.siteProperties = ["name", "long_name", "IAUCode",  "continent",  "address_line_1",  "address_line_2",
                "zip_code", "country",  "time_zone", "time_zone_name"];

            sitesCtlr.installMarkers = function(current_map, continent_key) {
                continent_sites = $scope.sitesCtlr.sites[continent_key];
                var continent_markers = [];
                var continent_infowindows = [];

                for (var j = 0; j < continent_sites.length; j++) {
                    var site = continent_sites[j];
                    var latlong = new google.maps.LatLng(site.coordinates.latitude,site.coordinates.longitude);

                    continent_infowindows[j] = new google.maps.InfoWindow({
                        content: '<h5>'+site.long_name+'</h5><br/>'+site.country
                    });

                    continent_markers[j] = new google.maps.Marker({
                        position: latlong,
                        title: site.name,
                        icon: "http://maps.google.com/mapfiles/ms/icons/red-dot.png"
                    });
                    continent_markers[j].setMap(current_map);

                    (function(k) {
                        continent_markers[j].addListener('click', function() {
                            continent_infowindows[k].open(current_map, continent_markers[k]);
                        });
                    })(j);
                }

                $scope.sitesCtlr.markers[continent_key] = continent_markers;
                $scope.sitesCtlr.infowindows[continent_key] = continent_infowindows;
            };

            //$rootScope.$on('GoogleMapReady', function (event, data) {
            //    console.log('Hey GoogleMapReady!');
            //});

            for (var i = 0; i < sitesCtlr.continents.length; i++) {
                var continentName = sitesCtlr.continents[i].name;
                $http({
                    url: API_PROTOCOL + "://" + location.host + "/" + API_VERSION + "/observingsites",
                    method: "GET",
                    params: {continent: continentName}
                })
                    .then(function (response) {
                        var continent_key = response.config.params.continent.toLowerCase().replace(' ', '_');
                        $scope.sitesCtlr.sites[continent_key] = response.data;
                        $scope.sitesCtlr.installMarkers(window.map, continent_key);
                    }, function (response) {
                        console.log("error " + response.status);
                    });
            }

            sitesCtlr.selectContinent = function(continent_key) {
                $('.site-list').not('.'+continent_key).hide();
                $('.site-list.'+continent_key).show();

                var bounds = new google.maps.LatLngBounds();

                for (var i = 0; i < $scope.sitesCtlr.continents.length; i++) {
                    var current_continent_key = $scope.sitesCtlr.continents[i].key;
                    current_markers = $scope.sitesCtlr.markers[current_continent_key];
                    for (var j = 0; j < current_markers.length; j++) {
                        if (current_continent_key === continent_key) {
                            bounds.extend(current_markers[j].position);
                            current_markers[j].setIcon("http://maps.google.com/mapfiles/ms/icons/blue-dot.png");
                        }
                        else {
                            current_markers[j].setIcon("http://maps.google.com/mapfiles/ms/icons/red-dot.png");
                        }
                    }
                }
                map.fitBounds(bounds);
            };

            sitesCtlr.selectSite = function(continent_key, site_index) {
                markers = $scope.sitesCtlr.markers[continent_key];
                google.maps.event.trigger(markers[site_index], 'click');
                $scope.sitesCtlr.selectedSite = $scope.sitesCtlr.sites[continent_key][site_index];
            };
        }]);

