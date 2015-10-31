(function () {
    'use strict';

    angular.module('webapp.authentication.controllers')
        .controller('UserprofileCtrl', function ($scope, $http, $window, $routeParams) {
            $scope.profile = {user: {username: $routeParams.username}};
            $http.get($window.ARCSECOND_API_ROOT_URL + '/1/profiles/' + $routeParams.username + '/').then(successFn, errorFn);

            function successFn(response, status, headers, config) {
                $scope.profile = response.data;
            }

            function errorFn(response, status, headers, config) {
                console.log(response);
            }
        });
})();
