(function () {
    'use strict';

    angular
        .module('webapp.layout.controllers')
        .controller('IndexController', IndexController);

    IndexController.$inject = ['$scope', 'ObservingSites', 'uiGmapGoogleMapApi', 'Snackbar'];

    function IndexController($scope, ObservingSites, uiGmapGoogleMapApi, Snackbar) {
        var vm = this;
        vm.observingsites = undefined;
        activate();

        function activate() {
            vm.continents = ObservingSites.continents;

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
                vm.observingsites = data.data;

                for (var i = 0; i < vm.observingsites.length; i++) {
                    var site = vm.observingsites[i];

                    var marker = {
                        "idKey": site.id,
                        "coords": {
                            "latitude": site.coordinates.latitude,
                            "longitude": site.coordinates.longitude
                        },
                        "title": site.name,
                        "icon": "http://maps.google.com/mapfiles/ms/icons/red-dot.png",
                        "window": {
                            "title": site.name,
                            "subtitle": site.country
                        }
                    };

                    $scope.map.markers.push(marker);
                }
            }

            function errorFn(data, status, headers, config) {
                Snackbar.error(data.error);
                console.log(data.error);
            }
        }
    }
})();

