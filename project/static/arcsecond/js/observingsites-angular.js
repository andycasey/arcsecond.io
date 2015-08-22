/**
 * Created by onekiloparsec on 09/08/15.
 */

var API_VERSION = "1";
var API_PROTOCOL = "http";
var API_ROOT_URL = "127.0.0.1:8000";

var app = angular.module('arcsecondApp', []);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

app.controller('SitesListController', ['$scope', '$http',
    function ($scope, $http) {
        var siteList = this;

        siteList.continents = [
            {name:'Africa'},
            {name:'Antarctica'},
            {name:'Asia'},
            {name:'Europe'},
            {name:'North America'},
            {name:'Oceania'},
            {name:'South America'}
        ];

        siteList.sites = {};
        siteList.markers = {};
        siteList.infowindows = {};

        for (var i = 0; i < siteList.continents.length; i++) {
            var continentName = siteList.continents[i].name;
            $http({
                url: API_PROTOCOL+"://"+API_ROOT_URL+"/"+API_VERSION+"/observingsites",
                method: "GET",
                params: {continent: continentName}
            })
                .then(function(response) {
                    var continent_name = response.config.params.continent;
                    $scope.siteList.sites[continent_name] = response.data;

                    if (map !== "undefined") {
                        continent_sites = $scope.siteList.sites[continent_name];
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
                                title: site.name
                            });
                            continent_markers[j].setMap(map);

                            (function(k) {
                                continent_markers[j].addListener('click', function() {
                                    continent_infowindows[k].open(map, continent_markers[k]);
                                });
                            })(j);
                        }

                        $scope.siteList.markers[continent_name] = continent_markers;
                        $scope.siteList.infowindows[continent_name] = continent_infowindows;
                    }

                }, function(response) {
                    alert("error "+response.status);
                });
        }

    }]);

