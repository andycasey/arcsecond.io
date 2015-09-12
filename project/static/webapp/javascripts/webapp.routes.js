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
        $routeProvider.when('/observingsites/:site_name/update', {
            controller: 'UpdateController',
            controllerAs: 'vm',
            templateUrl: '/static/webapp/templates/observingsites/update.html'
        }).otherwise('/');
    }
})();

