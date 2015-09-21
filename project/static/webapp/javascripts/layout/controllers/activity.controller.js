(function () {
    'use strict';

    angular
        .module('webapp.layout.controllers')
        .controller('ActivityController', ActivityController);

    ActivityController.$inject = ['$scope', 'ObservingSites', 'Snackbar'];

    function ActivityController($scope, ObservingSites, Snackbar) {
        var vm = this;
        vm.activities = undefined;
        activate();

        function activate() {
            ObservingSites.activities().then(successFn, errorFn);

            function successFn(data, status, headers, config) {
                vm.activities = data.data;
            }

            function errorFn(data, status, headers, config) {
                Snackbar.error(data.error);
            }
        }
    }
})();

