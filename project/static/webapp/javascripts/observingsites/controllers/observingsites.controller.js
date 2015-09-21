(function () {
    'use strict';

    angular
        .module('webapp.observingsites.controllers')
        .controller('ObservingSitesController', ObservingSitesController);

    ObservingSitesController.$inject = ['$scope', '$window', 'ObservingSites'];

    function ObservingSitesController($scope, $window, ObservingSites) {
        var vm = this;
        vm.observingsites = [];
        vm.continents = ObservingSites.continents;
        activate();

        function activate() {
            $scope.$watchCollection(function () { return $scope.observingsites; }, render);
        }

        function render(current, original) {
            if (current !== original) {
                vm.observingsites = current;
            }
        }
    }
})();

