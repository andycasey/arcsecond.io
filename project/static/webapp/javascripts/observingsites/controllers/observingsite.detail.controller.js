(function () {
    'use strict';

    angular
        .module('webapp.observingsites.controllers')
        .controller('ObservingSiteDetailController', ObservingSiteDetailController);

    ObservingSiteDetailController.$inject = ['$rootScope', '$scope', '$filter', 'ObservingSites', 'uiGmapGoogleMapApi'];

    function ObservingSiteDetailController($rootScope, $scope, $filter, ObservingSites, uiGmapGoogleMapApi) {
        var vm = this;
        vm.observingsitedetail = undefined;

        $scope.showAuthenticationWarning = false;
        $scope.continents = [
            '(undefined)',
            'Africa',
            'Antarctica',
            'Asia',
            'Europe',
            'North America',
            'Oceania',
            'South America'
        ];
        $scope.showContinents = function() {
            var selected = $filter('filter')($scope.continents, vm.observingsitedetail.continent);
            return (vm.observingsitedetail.continent && selected.length) ? selected[0] : '(toto)';
        };

        $scope.checkAndShow = function(sender, btnName) {
            if ($rootScope.authenticated) {
                sender[btnName].$show();
            }
            else {
                $scope.showAuthenticationWarning = true;
            }
        };

        $scope.closeAlert = function(sender) {
            $scope.showAuthenticationWarning = false;
        };

        $scope.updateObservingSite = function (field_name, data) {
            var update_data = {};
            update_data[field_name.toString()] = data;
            return ObservingSites.update(vm.observingsitedetail, update_data);
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

