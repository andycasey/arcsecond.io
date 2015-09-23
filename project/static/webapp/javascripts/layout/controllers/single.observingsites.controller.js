(function () {
    'use strict';

    angular
        .module('webapp.layout.controllers')
        .controller('ObservingSitesSingleController', ObservingSitesSingleController);

    ObservingSitesSingleController.$inject = ['$scope', '$routeParams', 'ObservingSites', 'Snackbar'];

    function ObservingSitesSingleController($scope, $routeParams, ObservingSites, Snackbar) {
        var vm = this;
        vm.observingsite = undefined;
        activate();

        function activate() {
            ObservingSites.get($routeParams.site_name).then(successFn, errorFn);

            function successFn(data, status, headers, config) {
                vm.observingsite = data.data;
            }

            function errorFn(data, status, headers, config) {
                Snackbar.error(data.error);
            }
        }
    }
})();

