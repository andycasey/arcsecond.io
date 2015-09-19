(function () {
    'use strict';

    angular
        .module('webapp.routes')
        .config(config);

    config.$inject = ['$routeProvider'];

    /**
     * @name config
     * @desc Define valid application routes
     */
    function config($routeProvider) {
        $routeProvider
            .when('/observingsites', {
                controller: 'IndexController',
                controllerAs: 'vm',
                templateUrl: '/static/webapp/templates/layout/index.html'
            })
            .when('/observingsites/:site_name', {
                controller: 'SingleController',
                controllerAs: 'vm',
                templateUrl: '/static/webapp/templates/layout/single.html'
            });
            //.when('/observingsites/:site_name/update', {
            //    controller: 'UpdateController',
            //    controllerAs: 'vm',
            //    templateUrl: '/static/webapp/templates/observingsites/update.html'
            //})
            //.otherwise('/observingsites');
    }
})();

