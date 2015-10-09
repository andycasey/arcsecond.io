(function () {
    'use strict';

    angular
        .module('webapp', [
            'webapp.config',
            'webapp.filters',
            'webapp.routes',
            'webapp.utils',
            'webapp.layout',
            'webapp.authentication',
            'webapp.observingsites',
            'webapp.telescopes',
            'webapp.archives',
            'webapp.telegrams'
        ]);

    angular
        .module('webapp.config', ['uiGmapgoogle-maps']);

    angular
        .module('webapp.routes', ['ngRoute']);

    angular
        .module('webapp.archives', ['ui.bootstrap']);

    angular
        .module('webapp')
        .run(run);

    run.$inject = ['$http'];

    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';

        $http.defaults.useXDomain = true;
        delete $http.defaults.headers.common['X-Requested-With'];
    }

})();
