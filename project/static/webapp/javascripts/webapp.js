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
        .module('webapp.config', ['uiGmapgoogle-maps']);

    angular
        .module('webapp.routes', ['ngRoute']);

    angular
        .module('webapp')
        .run(run);

    run.$inject = ['$http'];

    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }

})();
