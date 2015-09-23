(function () {
    'use strict';

    angular
        .module('webapp.layout.controllers')
        .controller('ArchivesIndexController', ArchivesIndexController);

    ArchivesIndexController.$inject = ['$scope', 'Archives', 'Snackbar'];

    function ArchivesIndexController($scope, Archives, Snackbar) {
        var vm = this;
        vm.data_rows = undefined;
        activate();

        function activate() {
            Archives.latest('ESO').then(successFn, errorFn);

            function successFn(data, status, headers, config) {
                vm.data_rows = data.data;
            }

            function errorFn(data, status, headers, config) {
                Snackbar.error(data.error);
                console.log(data.error);
            }
        }
    }
})();

