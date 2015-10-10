(function () {
    'use strict';

    angular
        .module('webapp.layout.controllers')
        .controller('ObservingSitesIndexController', ObservingSitesIndexController);

    ObservingSitesIndexController.$inject = ['$scope', 'ObservingSites', 'Authentication', 'uiGmapGoogleMapApi', 'Snackbar'];

    function ObservingSitesIndexController($scope, ObservingSites, Authentication, uiGmapGoogleMapApi, Snackbar) {
        var vm = this;
        vm.observingsites = undefined;
        vm._all_observingsites = undefined;
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
                    zoom: 1,
                    markers: [], // array of models to display
                    markersEvents: {
                        click: function(marker, eventName, model, args) {
                            $scope.map.window.model = model;
                            $scope.map.windowOptions.show = true;
                        }
                    },
                    window: {
                        model: {},
                        closeClick: function() {
                            this.model = {};
                            $scope.windowOptions.show = false;
                        }
                    },
                    options: {
                        scrollwheel: false,
                        dragging: true
                    },
                    closeClick: function () {
                        $scope.map.window.model = {};
                        $scope.map.windowOptions.show = false;
                    },
                    windowOptions: {
                        show: false
                    },
                    events: {
                        bounds_changed: function(map, eventName, args) {
                            vm.observingsites = vm._all_observingsites.filter(function (el) {
                                var ll = new google.maps.LatLng(el.coordinates.latitude, el.coordinates.longitude);
                                return map.getBounds().contains(ll);
                            });
                        }
                    }
                };

                $scope.zoomInToObservingSite = function(site) {
                    $scope.map.center = site.coordinates;
                    $scope.map.zoom = 8;
                };
            });

            ObservingSites.all().then(successFn, errorFn);

            function successFn(response, status, headers, config) {
                $scope.viewLoading = false;
                vm._all_observingsites = response.data;
                vm.observingsites = response.data;

                var markersPromise = getMapMarkers(vm.observingsites);
                markersPromise.done(function(data){
                    $scope.map.markers = data;
                });
            }

            function errorFn(response, status, headers, config) {
                $scope.viewLoading = false;
                Snackbar.error(response.error);
                console.log(response.error);
            }

            function getMapMarkers(observingsites) {
                var deferred = $.Deferred();

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
                        "country": site.country,
                        "icon": "http://maps.google.com/mapfiles/ms/icons/red-dot.png"
                    };
                    markers.push(marker);
                }
                deferred.resolve(markers);

                return deferred.promise();
            }
        }
    }
})();

