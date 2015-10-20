(function () {
    'use strict';

    angular.module('webapp.authentication.controllers')
        .controller('VerifyemailCtrl', function ($scope, $routeParams, djangoAuth) {
            djangoAuth.verify($routeParams["emailVerificationToken"]).then(function (data) {
                $scope.success = true;
            }, function (data) {
                $scope.failure = false;
            });
        });
})();
