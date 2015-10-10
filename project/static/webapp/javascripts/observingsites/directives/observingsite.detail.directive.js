(function () {
    'use strict';

    angular
        .module('webapp.observingsites.directives')
        .directive('observingsitedetail', observingsitedetail);

    function observingsitedetail() {
        var directive = {
            controller: 'ObservingSiteDetailController',
            controllerAs: 'vm',
            restrict: 'E',
            scope: {
                observingsitedetail: '='
            },
            templateUrl: '/static/webapp/templates/observingsites/observingsite.detail.html'
        };
        return directive;
    }
})();
