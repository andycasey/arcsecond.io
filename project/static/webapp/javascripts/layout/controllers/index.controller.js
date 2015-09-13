/**
 * IndexController
 * @namespace webapp.layout.controllers
 */
(function () {
    'use strict';

    angular
        .module('webapp.layout.controllers')
        .controller('IndexController', IndexController);

    IndexController.$inject = ['$scope', 'ObservingSites', 'Snackbar'];

    /**
     * @namespace IndexController
     */
    function IndexController($scope, ObservingSites, Snackbar) {
        var vm = this;

        //vm.isAuthenticated = Authentication.isAuthenticated();
        vm.observingsites = [];

        activate();

        /**
         * @name activate
         * @desc Actions to be performed when this controller is instantiated
         * @memberOf webapp.layout.controllers.IndexController
         */
        function activate() {
            ObservingSites.all().then(observingsitesSuccessFn, observingsitesErrorFn);

            $scope.$on('observingsite.created', function (event, observingsite) {
                vm.observingsites.unshift(observingsite);
            });

            $scope.$on('observingsite.created.error', function () {
                vm.observingsites.shift();
            });


            /**
             * @name observingsitesSuccessFn
             * @desc Update observingsites array on view
             */
            function observingsitesSuccessFn(data, status, headers, config) {
                vm.observingsites = data.data;
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

