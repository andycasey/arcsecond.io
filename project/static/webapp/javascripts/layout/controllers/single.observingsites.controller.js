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
            if ($routeParams.site_name !== "new" && $routeParams.site_name !== undefined) {
                ObservingSites.get($routeParams.site_name).then(successFn, errorFn);
            }

            function successFn(response, status, headers, config) {
                vm.observingsite = response.data;
            }

            function errorFn(response, status, headers, config) {
                //Snackbar.error(data.error);
            }
        }
    }
})();

