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
        for (var i = 0; i < siteList.continents.length; i++) {
            var continentName = siteList.continents[i].name;
            $http({
                url: API_PROTOCOL+"://"+API_ROOT_URL+"/"+API_VERSION+"/observingsites",
                method: "GET",
                params: {continent: continentName}
            })
                .then(function(response) {
                    $scope.siteList.sites[response.config.params.continent] = response.data;
                }, function(response) {
                    alert("error "+response.status);
                });
        }

    }]);

