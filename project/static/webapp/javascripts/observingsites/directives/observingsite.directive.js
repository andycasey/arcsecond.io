/**
 * ObservingSite
 * @namespace webapp.observingsites.directives
 */
(function () {
    'use strict';

    angular
        .module('webapp.observingsites.directives')
        .directive('observingsite', observingsite);

    /**
     * @namespace Observing Site
     */
    function observingsite() {
        /**
         * @name directive
         * @desc The directive to be returned
         * @memberOf webapp.observingsites.directives.ObservingSite
         */
        var directive = {
            restrict: 'E',
            scope: {
                observingsite: '='
            },
            templateUrl: '/static/webapp/templates/observingsites/observingsite.html'
        };

        return directive;
    }
})();
