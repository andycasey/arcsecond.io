(function () {
    'use strict';

    angular
        .module('webapp.authentication', [
            'webapp.authentication.services'
        ]);

    angular
        .module('webapp.authentication.services', ['ngCookies']);
})();
