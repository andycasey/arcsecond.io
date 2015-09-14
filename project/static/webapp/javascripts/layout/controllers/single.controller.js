/**
 * IndexController
 * @namespace webapp.layout.controllers
 */
(function () {
    'use strict';

    angular
        .module('webapp.layout.controllers')
        .controller('SingleController', SingleController);

    SingleController.$inject = ['$scope', '$routeParams', 'ObservingSites', 'Snackbar'];

    /**
     * @namespace SingleController
     */
    function SingleController($scope, $routeParams, ObservingSites, Snackbar) {
        var vm = this;
        vm.observingsite = undefined;
        activate();

        /**
         * @name activate
         * @desc Actions to be performed when this controller is instantiated
         * @memberOf webapp.layout.controllers.SingleController
         */
        function activate() {
            ObservingSites.get($routeParams.site_name).then(observingsitesSuccessFn, observingsitesErrorFn);

            /**
             * @name observingsitesSuccessFn
             * @desc Update observingsites array on view
             */
            function observingsitesSuccessFn(data, status, headers, config) {
                vm.observingsite = data.data;
            }

            /**
             * @name observingsitesErrorFn
             * @desc Show snackbar with error
             */
            function observingsitesErrorFn(data, status, headers, config) {
                Snackbar.error(data.error);
            }
        }
    }
})();

