(function () {
    'use strict';

    angular
        .module('webapp.telegrams.directives')
        .directive('telegrams', telegrams);

    function telegrams() {
        var directive = {
            controller: 'ObservingSitesController',
            controllerAs: 'vm',
            restrict: 'E',
            scope: {
                telegrams: '='
            },
            templateUrl: '/static/webapp/templates/telegrams/telegrams.html'
        };

        return directive;
    }
})();

