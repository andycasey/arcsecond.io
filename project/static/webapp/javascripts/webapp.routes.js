(function () {
    'use strict';

    angular
        .module('webapp.routes')
        .config(config);

    config.$inject = ['$routeProvider'];

    function config($routeProvider) {
        $routeProvider
            .when('/observingsites', {
                controller: 'IndexController',
                controllerAs: 'vm',
                templateUrl: '/static/webapp/templates/layout/index.html'
            })
            .when('/observingsites/activity', {
                controller: 'ActivityController',
                controllerAs: 'vm',
                templateUrl: '/static/webapp/templates/layout/activity.html'
            })
            .when('/observingsites/:site_name', {
                controller: 'SingleController',
                controllerAs: 'vm',
                templateUrl: '/static/webapp/templates/layout/single.html'
            });
    }
})();

