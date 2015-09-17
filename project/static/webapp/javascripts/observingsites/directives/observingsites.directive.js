(function () {
    'use strict';

    angular
        .module('webapp.observingsites.directives')
        .directive('observingsites', observingsites);

    function observingsites() {
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

