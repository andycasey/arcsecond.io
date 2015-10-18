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
                if ($location.path() === "/") {
                    $(".navbar").addClass("navbar__initial scrollspy_menu");
                }
                else {
                    $(".navbar").removeClass("navbar__initial scrollspy_menu");
                }

                $rootScope.$on("$routeChangeStart", function (event, next, current) {
                    if ($location.path() === "/") {
                        $(".navbar").addClass("navbar__initial scrollspy_menu");
                    }
                    else {
                        $(".navbar").removeClass("navbar__initial scrollspy_menu");
                    }
                });
            }]
        };
        return directive;
    }
})();
