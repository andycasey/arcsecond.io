/**
 * Register controller
 * @namespace webapp.observingsites.controllers
 */
(function () {
    'use strict';

    angular
        .module('webapp.observingsites.controllers')
        .controller('UpdateController', UpdateController);

    UpdateController.$inject = ['$location', '$scope', 'ObservingSites'];

    /**
     * @namespace UpdateController
     */
    function UpdateController($location, $scope, $routeParams, ObservingSites) {
        var vm = this;

        vm.original_name = $routeParams.site_name;
        vm.update = update;

        /**
         * @name update
         * @desc Update an ObservingSite
         * @memberOf webapp.observingsites.controllers.UpdateController
         */
        function update() {
            ObservingSites.update(vm.original_name, vm.name, vm.long_name, vm.IAUCode);
        }
    }
})();