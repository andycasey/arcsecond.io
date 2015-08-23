/**
 * Created by onekiloparsec on 09/08/15.
 */

var API_VERSION = "1";
var API_PROTOCOL = "http";

angular.isUndefinedOrNull = function(val) {
    return angular.isUndefined(val) || val === null
};

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

        siteList.selectedSite = null;
        siteList.siteProperties = ["name", "long_name", "IAUCode",  "continent",  "address_line_1",  "address_line_2",
            "zip_code", "country",  "time_zone", "time_zone_name"];

        var location_host = location.host;
        if (location_host === 'www.arcsecond.io') {
            location_host = 'api.arcsecond.io';
        }

        for (var i = 0; i < siteList.continents.length; i++) {
            var continentName = siteList.continents[i].name;
            $http({
                url: API_PROTOCOL+"://"+location_host+"/"+API_VERSION+"/observingsites",
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

                            (function(k) {
                                continent_markers[j].addListener('click', function() {
                                    continent_infowindows[k].open(map, continent_markers[k]);
                                });
                            })(j);
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

        siteList.selectSite = function(continent_key, site_index) {
            markers = $scope.siteList.markers[continent_key];
            google.maps.event.trigger(markers[site_index], 'click');
            $scope.siteList.selectedSite = $scope.siteList.sites[continent_key][site_index];
        };
    }]);

