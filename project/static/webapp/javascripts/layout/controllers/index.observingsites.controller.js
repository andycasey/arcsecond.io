(function () {
    'use strict';

    angular
        .module('webapp.layout.controllers')
        .controller('ObservingSitesIndexController', ObservingSitesIndexController);

    ObservingSitesIndexController.$inject = ['$scope', 'ObservingSites', 'uiGmapGoogleMapApi', 'Snackbar'];

    function ObservingSitesIndexController($scope, ObservingSites, uiGmapGoogleMapApi, Snackbar) {
        var vm = this;
        vm.observingsites = undefined;
        activate();

        function activate() {
            vm.continents = ObservingSites.continents;
            $scope.viewLoading = true;

            uiGmapGoogleMapApi.then(function(maps) {
                $scope.map = {
                    center: {
                        latitude: 15.0,
                        longitude: 0.0
                    },
                    zoom: 2,
                    markers: [], // array of models to display
                    markersEvents: {
                        click: function(marker, eventName, model, args) {
                            $scope.map.window.model = model;
                            $scope.map.window.show = true;
                        }
                    },
                    window: {
                        marker: {},
                        show: false,
                        closeClick: function() {
                            this.show = false;
                        },
                        options: {} // define when map is ready
                    }
                };
                $scope.options = {
                    scrollwheel: false
                };
            });

            $scope.markers = [];
            ObservingSites.all().then(successFn, errorFn);

            function successFn(data, status, headers, config) {
                $scope.viewLoading = false;
                vm.observingsites = data.data;
                $scope.map.markers = getMapMarkers(vm.observingsites);
            }

            function errorFn(data, status, headers, config) {
                $scope.viewLoading = false;
                Snackbar.error(data.error);
                console.log(data.error);
            }

            function getMapMarkers(observingsites) {
                var markers = [];
                for (var i = 0; i < observingsites.length; i++) {
                    var site = observingsites[i];

                    var marker = {
                        "idKey": site.id,
                        "coords": {
                            "latitude": site.coordinates.latitude,
                            "longitude": site.coordinates.longitude
                        },
                        "name": site.name,
                        "icon": "http://maps.google.com/mapfiles/ms/icons/red-dot.png",
                        "window": {
                            "title": site.name,
                            "subtitle": site.country
                        }
                    };
                    markers.push(marker);
                }
                return markers;
            }
        }
    }
})();

