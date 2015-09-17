(function () {
    'use strict';

    angular
        .module('webapp.observingsites.controllers')
        .controller('ObservingSiteController', ObservingSiteController);

    ObservingSiteController.$inject = ['$scope'];

    function ObservingSiteController($scope) {
        var vm = this;
        vm.observingsite = undefined;
        activate();

        function activate() {
            $scope.$watch(function () { return $scope.observingsite; }, render);
        }

        function render(current, original) {
            if (current !== original) {
                vm.observingsite = current;
            }
        }
    }
})();

