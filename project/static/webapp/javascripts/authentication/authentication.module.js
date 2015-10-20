(function () {
    'use strict';

    angular
        .module('webapp.authentication', [
            'webapp.authentication.controllers',
            'webapp.authentication.services'
        ]);

    angular
        .module('webapp.authentication.controllers', []);

    angular
        .module('webapp.authentication.services', ['ngCookies', 'ngResource', 'ngSanitize', 'ngRoute']);
})();
