(function () {
    'use strict';

    angular
        .module('webapp.layout.directives')
        .directive('bootstrapNavbar', bootstrapNavbar);

    function bootstrapNavbar() {
        var directive;
        directive = {
            restrict: 'E',
            replace: true,
            scope: {
                initial: '='
            },
            templateUrl: '/static/webapp/templates/layout/bootstrap.navbar.html',
            controller: ['$scope', '$rootScope', '$location', function ($scope, $rootScope, $location) {
                var toggleNavbarInitial = function() {
                    if ($location.path() === "/") {
                        $(".navbar").addClass("navbar__initial scrollspy_menu");
                        Waypoint.enableAll();
                    }
                    else {
                        Waypoint.disableAll();
                        $(".navbar").removeClass("navbar__initial scrollspy_menu");
                    }
                };

                toggleNavbarInitial();
                $rootScope.$on("$routeChangeSuccess", function (event, next, current) {
                    toggleNavbarInitial();
                });
            }]
        };
        return directive;
    }
})();
