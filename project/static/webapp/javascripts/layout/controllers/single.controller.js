(function () {
    'use strict';

    angular
        .module('webapp.layout.controllers')
        .controller('SingleController', SingleController);

    SingleController.$inject = ['$scope', '$routeParams', 'ObservingSites', 'Snackbar'];

    function SingleController($scope, $routeParams, ObservingSites, Snackbar) {
        var vm = this;
        vm.observingsite = undefined;
        activate();

        function activate() {
            ObservingSites.get($routeParams.site_name).then(observingsitesSuccessFn, observingsitesErrorFn);

            function observingsitesSuccessFn(data, status, headers, config) {
                vm.observingsite = data.data;
            }

            function observingsitesErrorFn(data, status, headers, config) {
                Snackbar.error(data.error);
            }
        }
    }
})();

