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

            var areaLat = 15.0,
                areaLng = 0.0,
                areaZoom = 2;

            uiGmapGoogleMapApi.then(function(maps) {
                $scope.map = {
                    center: {
                        latitude: areaLat,
                        longitude: areaLng
                    },
                    zoom: areaZoom
                };
                $scope.options = {
                    scrollwheel: false
                };
            });

            ObservingSites.all().then(successFn, errorFn);

            function successFn(data, status, headers, config) {
                vm.observingsites = data.data;
            }

            function errorFn(data, status, headers, config) {
                Snackbar.error(data.error);
                console.log(data.error);
            }
        }
    }
})();

