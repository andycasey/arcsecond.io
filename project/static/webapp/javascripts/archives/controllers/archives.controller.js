(function () {
    'use strict';

    angular
        .module('webapp.archives.controllers')
        .controller('ArchivesController', ArchivesController);

    ArchivesController.$inject = ['$scope', '$window', 'Archives'];

    function ArchivesController($scope, $window, Archives) {
        var vm = this;
        vm.data_rows = [];
        activate();

        function activate() {
            $scope.$watchCollection(function () { return $scope.data_rows; }, render);
        }

        function render(current, original) {
            if (current !== original) {
                vm.data_rows = current;
            }
        }
    }
})();

