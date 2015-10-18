(function () {
    'use strict';

    angular
        .module('webapp.layout.directives')
        .directive('bootstrapNavbar', bootstrapNavbar);

    function bootstrapNavbar() {
        var directive = {
            restrict: 'E',
            replace: true,
            transclude: true,
            templateUrl: '/static/webapp/templates/layout/bootstrap.navbar.html'
        };
        return directive;
    }
})();
