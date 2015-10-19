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
        .module('webapp.authentication', ['ngCookies', 'ngResource', 'ngSanitize', 'ngRoute']);

    angular
        .module('webapp')
        .run(run);

    run.$inject = ['$http', 'editableOptions', 'editableThemes', 'djangoAuth'];

    function run($http, editableOptions, editableThemes, djangoAuth) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
        $http.defaults.withCredentials = true;

        $http.defaults.useXDomain = true;
        delete $http.defaults.headers.common['X-Requested-With'];

        editableOptions.theme = 'bs3';
        editableThemes.bs3.inputClass = 'input-sm';
        editableThemes.bs3.buttonsClass = 'btn-sm';

        djangoAuth.initialize('//127.0.0.1:8000/rest-auth', false);
    }
})();
