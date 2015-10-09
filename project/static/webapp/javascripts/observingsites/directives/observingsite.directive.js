(function () {
    'use strict';

    angular
        .module('webapp.observingsites.directives')
        .directive('observingsite', observingsite);

    function observingsite() {
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
