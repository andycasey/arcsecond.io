(function () {
    'use strict';

    angular
        .module('webapp.telegrams.controllers')
        .controller('TelegramController', TelegramController);

    TelegramController.$inject = ['$scope'];

    function TelegramController($scope) {
        var vm = this;
        vm.telegram = undefined;
        activate();

        function activate() {
            $scope.$watch(function () { return $scope.telegram; }, render);
        }

        function render(current, original) {
            if (current !== original) {
                vm.telegram = current;
            }
        }
    }
})();

