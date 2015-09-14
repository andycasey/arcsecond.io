/**
 * ObservingSitesController
 * @namespace webapp.observingsites.controllers
 */
(function () {
    'use strict';

    angular
        .module('webapp.observingsites.controllers')
        .controller('ObservingSiteController', ObservingSiteController);

    ObservingSiteController.$inject = ['$scope'];

    /**
     * @namespace ObservingSiteController
     */
    function ObservingSiteController($scope) {
        var vm = this;
        vm.observingsite = undefined;
        activate();

        /**
         * @name activate
         * @desc Actions to be performed when this controller is instantiated
         * @memberOf webapp.observingsites.controllers.ObservingSiteController
         */
        function activate() {
            $scope.$watch(function () { return $scope.observingsite; }, render);
        }

        /**
         * @name render
         * @desc Renders a single ObservingSite
         * @param {Array} current The current value of `vm.observingsite`
         * @param {Array} original The value of `vm.observingsite` before it was updated
         * @memberOf webapp.observingsites.controllers.ObservingSiteController
         */
        function render(current, original) {
            if (current !== original) {
                vm.observingsite = current;
            }
        }
    }
})();

