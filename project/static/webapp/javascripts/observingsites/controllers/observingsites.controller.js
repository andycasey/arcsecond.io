(function () {
    'use strict';

    angular
        .module('webapp.observingsites.controllers')
        .controller('ObservingSitesController', ObservingSitesController);

    ObservingSitesController.$inject = ['$scope', '$window', 'ObservingSites'];

    function ObservingSitesController($scope, $window, ObservingSites) {
        var vm = this;
        vm.observingsites = [];
        vm.map = undefined;
        activate();

        function activate() {
            $scope.$watchCollection(function () { return $scope.observingsites; }, render);
            vm.map = { center: { latitude: 15.0, longitude: 0.0 }, zoom: 2 };
        }

        function render(current, original) {
            vm.continents = ObservingSites.continents;
            if (current !== original) {
                vm.observingsites = current;
            }
        }
    }
})();

