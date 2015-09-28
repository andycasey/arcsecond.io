(function () {
    'use strict';

    angular
        .module('webapp.telegrams.controllers')
        .controller('TelegramsController', TelegramsController);

    TelegramsController.$inject = ['$scope', '$window', 'Telegrams'];

    function TelegramsController($scope, $window, Telegrams) {
        var vm = this;
        vm.telegrams = [];
        activate();

        function activate() {
            $scope.$watchCollection(function () { return $scope.telegrams; }, render);
        }

        function render(current, original) {
            if (current !== original) {
                vm.telegrams = current;
            }
        }
    }
})();

