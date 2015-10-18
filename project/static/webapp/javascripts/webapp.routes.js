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
                templateUrl: '/static/webapp/templates/layout/index.www.html'
            })
            .when('/observingsites', {
                controller: 'ObservingSitesIndexController',
                controllerAs: 'vm',
                templateUrl: '/static/webapp/templates/layout/index.observingsites.html'
            })
            .when('/observingsites/activity', {
                controller: 'ObservingSitesActivityController',
                controllerAs: 'vm',
                templateUrl: '/static/webapp/templates/layout/activity.observingsites.html'
            })
            .when('/observingsites/:site_name', {
                controller: 'ObservingSiteUpdateController',
                controllerAs: 'vm',
                templateUrl: '/static/webapp/templates/layout/update.observingsite.html'
            })
            .when('/archives', {
                controller: 'ArchivesIndexController',
                controllerAs: 'vm',
                templateUrl: '/static/webapp/templates/layout/index.archives.html'
            })
            .when('/telegrams', {
                controller: 'TelegramsIndexController',
                controllerAs: 'vm',
                templateUrl: '/static/webapp/templates/layout/index.telegrams.html'
            });
    }
})();

