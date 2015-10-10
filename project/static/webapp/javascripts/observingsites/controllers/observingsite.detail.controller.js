(function () {
    'use strict';

    angular
        .module('webapp.observingsites.controllers')
        .controller('ObservingSiteDetailController', ObservingSiteDetailController);

    ObservingSiteDetailController.$inject = ['$scope'];

    function ObservingSiteDetailController($scope) {
        var vm = this;
        vm.observingsite_detail = undefined;
        activate();

        function activate() {
            $scope.$watch(function () { return $scope.observingsite_detail; }, render);
        }

        function render(current, original) {
            if (current !== original) {
                vm.observingsite_detail = current;
            }
        }
    }
})();

