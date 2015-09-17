(function () {
    'use strict';

    angular
        .module('webapp.layout.controllers')
        .controller('IndexController', IndexController);

    IndexController.$inject = ['$scope', 'ObservingSites', 'Snackbar'];

    function IndexController($scope, ObservingSites, Snackbar) {
        var vm = this;
        vm.observingsites = undefined;
        activate();

        function activate() {
            ObservingSites.all().then(successFn, errorFn);

            function successFn(data, status, headers, config) {
                vm.observingsites = data.data;
            }

            function errorFn(data, status, headers, config) {
                Snackbar.error(data.error);
                console.log(data.error);
            }
        }
    }
})();

