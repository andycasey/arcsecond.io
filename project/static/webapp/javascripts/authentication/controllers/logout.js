(function () {
    'use strict';

    angular.module('webapp.authentication.controllers')
        .controller('LogoutCtrl', function ($scope, $location, djangoAuth) {
            djangoAuth.logout();
        });
})();
