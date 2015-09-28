(function () {
    'use strict';

    angular
        .module('webapp.telegrams.directives')
        .directive('telegram', telegram);

    function telegram() {
        var directive = {
            restrict: 'E',
            scope: {
                telegram: '='
            },
            templateUrl: '/static/webapp/templates/telegrams/telegram.html'
        };

        return directive;
    }
})();
