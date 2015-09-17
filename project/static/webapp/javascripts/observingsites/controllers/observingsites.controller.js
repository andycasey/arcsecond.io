(function () {
    'use strict';

    angular
        .module('webapp.observingsites.controllers')
        .controller('ObservingSitesController', ObservingSitesController);

    ObservingSitesController.$inject = ['$scope', '$window'];

    function ObservingSitesController($scope, $window) {
        var vm = this;
        vm.observingsites = [];
        vm.map = undefined;
        activate();

        function activate() {
            $scope.$watchCollection(function () { return $scope.observingsites; }, render);
            $scope.map = { center: { latitude: 15.0, longitude: 0.0 }, zoom: 2 };
        }

        function render(current, original) {
            if (current !== original) {
                vm.observingsites = current;
            }
        }
    }
})();

