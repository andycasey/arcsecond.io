(function () {
    'use strict';

    angular
        .module('webapp', [
            'webapp.config',
            'webapp.routes',
            'webapp.utils',
            'webapp.layout',
            'webapp.observingsites'
        ]);

    angular
        .module('webapp.config', []);

    angular
        .module('webapp.routes', ['ngRoute']);

    angular
        .module('webapp')
        .run(run);

    run.$inject = ['$http'];

    /**
     * @name run
     * @desc Update xsrf $http headers to align with Django's defaults
     */
    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }

})();
