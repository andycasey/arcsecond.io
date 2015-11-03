(function () {
    'use strict';

    angular
        .module('webapp.telescopes', [
            'webapp.telescopes.services'
        ]);

    angular
        .module('webapp.telescopes.services', ['ngCookies']);
})();
