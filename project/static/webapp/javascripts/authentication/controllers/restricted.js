(function () {
    'use strict';

    angular.module('webapp.authentication.controllers')
        .controller('RestrictedCtrl', function ($scope, $location) {
            $scope.$on('djangoAuth.logged_in', function () {
                $location.path('/');
            });
        });
})();
