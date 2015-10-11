(function () {
    'use strict';

    angular
        .module('webapp.observingsites.controllers')
        .controller('ObservingSiteDetailController', ObservingSiteDetailController);

    ObservingSiteDetailController.$inject = ['$scope', '$filter', 'ObservingSites', 'uiGmapGoogleMapApi'];

    function ObservingSiteDetailController($scope, $filter, ObservingSites, uiGmapGoogleMapApi) {
        var vm = this;
        vm.observingsitedetail = undefined;

        $scope.continents = ObservingSites.continents;
        $scope.showContinents = function() {
            if (vm.observingsitedetail === undefined) {
                return 'Undefined';
            }
            var selected = $filter('filter')($scope.continents, {'name': vm.observingsitedetail.continent});
            return (vm.observingsitedetail.continent && selected.length) ? selected[0].name : 'Undefined';
        };

        activate();

        function activate() {
            $scope.$watch(function () { return $scope.observingsitedetail; }, render);
        }

        function render(current, original) {
            if (current !== original) {
                vm.observingsitedetail = current;

                uiGmapGoogleMapApi.then(function(maps) {
                    $scope.map = {
                        center: {
                            latitude: vm.observingsitedetail.coordinates.latitude,
                            longitude: vm.observingsitedetail.coordinates.longitude
                        },
                        zoom: 15,
                        options: {
                            scrollwheel: false,
                            dragging: false,
                            mapTypeId: google.maps.MapTypeId.HYBRID
                        }
                    }
                });

            }
        }
    }
})();

