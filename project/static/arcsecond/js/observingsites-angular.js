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

app.controller('SitesListController', ['$scope', '$http',
    function ($scope, $http) {
        var siteList = this;

        siteList.continents = [
            {name:'Africa', key:'africa'},
            {name:'Antarctica', key:'antarctica'},
            {name:'Asia', key:'asia'},
            {name:'Europe', key:'europe'},
            {name:'North America', key:'north_america'},
            {name:'Oceania', key:'oceania'},
            {name:'South America', key:'south_america'}
        ];

        siteList.sites = {};
        siteList.markers = {};
        siteList.infowindows = {};

        for (var i = 0; i < siteList.continents.length; i++) {
            var continentName = siteList.continents[i].name;
            $http({
                url: API_PROTOCOL+"://"+location.host+"/"+API_VERSION+"/observingsites",
                method: "GET",
                params: {continent: continentName}
            })
                .then(function(response) {
                    var continent_key = response.config.params.continent.toLowerCase().replace(' ', '_');
                    $scope.siteList.sites[continent_key] = response.data;

                    if (map !== "undefined") {
                        continent_sites = $scope.siteList.sites[continent_key];
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
                            continent_markers[j].setMap(map);
                        }

                        $scope.siteList.markers[continent_key] = continent_markers;
                        $scope.siteList.infowindows[continent_key] = continent_infowindows;
                    }

                }, function(response) {
                    alert("error "+response.status);
                });
        }

        siteList.selectContinent = function(continent_key) {
            $('.site-list').not('.'+continent_key).hide();
            $('.site-list.'+continent_key).show();

            var bounds = new google.maps.LatLngBounds();

            for (var i = 0; i < $scope.siteList.continents.length; i++) {
                var current_continent_key = $scope.siteList.continents[i].key;
                current_markers = $scope.siteList.markers[current_continent_key];
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
    }]);

