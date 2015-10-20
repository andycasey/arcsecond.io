(function () {
    'use strict';

    angular
        .module('webapp.routes')
        .config(config);

    config.$inject = ['$routeProvider'];

    function config($routeProvider) {
        $routeProvider
            .when('/', {
                controller: 'IndexController',
                controllerAs: 'vm',
                templateUrl: '/static/webapp/templates/layout/index.www.html',
                resolve: {
                    authenticated: ['djangoAuth', function(djangoAuth){
                        return djangoAuth.authenticationStatus();
                    }]
                }
            })
            .when('/login', {
                templateUrl: '/static/webapp/templates/authentication/login.html',
                resolve: {
                    authenticated: ['djangoAuth', function(djangoAuth){
                        return djangoAuth.authenticationStatus();
                    }]
                }
            })
            .when('/userProfile', {
                templateUrl: '/static/webapp/templates/authentication/userprofile.html',
                resolve: {
                    authenticated: ['djangoAuth', function(djangoAuth){
                        return djangoAuth.authenticationStatus();
                    }]
                }
            })
            .when('/observingsites', {
                controller: 'ObservingSitesIndexController',
                controllerAs: 'vm',
                templateUrl: '/static/webapp/templates/layout/index.observingsites.html',
                resolve: {
                    authenticated: ['djangoAuth', function(djangoAuth){
                        return djangoAuth.authenticationStatus();
                    }]
                }
            })
            .when('/observingsites/activity', {
                controller: 'ObservingSitesActivityController',
                controllerAs: 'vm',
                templateUrl: '/static/webapp/templates/layout/activity.observingsites.html',
                resolve: {
                    authenticated: ['djangoAuth', function(djangoAuth){
                        return djangoAuth.authenticationStatus();
                    }]
                }
            })
            .when('/observingsites/:site_name', {
                controller: 'ObservingSiteUpdateController',
                controllerAs: 'vm',
                templateUrl: '/static/webapp/templates/layout/update.observingsite.html',
                resolve: {
                    authenticated: ['djangoAuth', function(djangoAuth){
                        return djangoAuth.authenticationStatus();
                    }]
                }
            })
            .when('/archives', {
                controller: 'ArchivesIndexController',
                controllerAs: 'vm',
                templateUrl: '/static/webapp/templates/layout/index.archives.html',
                resolve: {
                    authenticated: ['djangoAuth', function(djangoAuth){
                        return djangoAuth.authenticationStatus();
                    }]
                }
            })
            .when('/telegrams', {
                controller: 'TelegramsIndexController',
                controllerAs: 'vm',
                templateUrl: '/static/webapp/templates/layout/index.telegrams.html',
                resolve: {
                    authenticated: ['djangoAuth', function(djangoAuth){
                        return djangoAuth.authenticationStatus();
                    }]
                }
            });
    }
})();

