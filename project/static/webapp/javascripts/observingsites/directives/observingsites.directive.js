/**
 * Observing Sites
 * @namespace webapp.observingsites.directives
 */
(function () {
    'use strict';

    angular
        .module('webapp.observingsites.directives')
        .directive('observingsites', observingsites);

    /**
     * @namespace Observing Sites
     */
    function observingsites() {
        /**
         * @name directive
         * @desc The directive to be returned
         * @memberOf webapp.observingsites.directives.ObservingSites
         */
        var directive = {
            controller: 'ObservingSitesController',
            controllerAs: 'vm',
            restrict: 'E',
            scope: {
                observingsites: '='
            },
            templateUrl: '/static/webapp/templates/observingsites/observingsites.html'
        };

        return directive;
    }
})();

