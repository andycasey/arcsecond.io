(function () {
    'use strict';

    angular
        .module('webapp.layout.controllers')
        .controller('ObservingSiteUpdateController', ObservingSiteUpdateController);

    ObservingSiteUpdateController.$inject = ['$scope', '$routeParams', 'ObservingSites', 'uiGmapGoogleMapApi', 'Snackbar'];

    function ObservingSiteUpdateController($scope, $routeParams, ObservingSites, uiGmapGoogleMapApi, Snackbar) {
        var vm = this;
        vm.observingsitedetail = undefined;

        activate();

        function activate() {
            if ($routeParams.site_name !== "new" && $routeParams.site_name !== undefined) {
                ObservingSites.get($routeParams.site_name).then(successFn, errorFn);
            }

            function successFn(response, status, headers, config) {
                vm.observingsitedetail = response.data;
            }

            function errorFn(response, status, headers, config) {
                //Snackbar.error(data.error);
            }
        }
    }
})();

