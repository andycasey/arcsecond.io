(function () {
    'use strict';

    angular
        .module('webapp.master')
        .controller('MasterCtrl', function ($rootScope, $location, djangoAuth, alertService) {

            $rootScope.closeAlert = alertService.closeAlert;

            // Assume user is not logged in until we hear otherwise
            $rootScope.authenticated = false;
            // Wait for the status of authentication, set scope var to true if it resolves
            djangoAuth.authenticationStatus(true).then(function () {
                $rootScope.authenticated = true;
            });
            // Wait and respond to the logout event.
            $rootScope.$on('djangoAuth.logged_out', function () {
                $rootScope.authenticated = false;
            });
            // Wait and respond to the log in event.
            $rootScope.$on('djangoAuth.logged_in', function () {
                $rootScope.authenticated = true;
            });
            // If the user attempts to access a restricted page, redirect them back to the main page.
            $rootScope.$on('$routeChangeError', function (ev, current, previous, rejection) {
                console.error("Unable to change routes.  Error: ", rejection);
                $location.path('/restricted').replace();
            });
        })
})();

