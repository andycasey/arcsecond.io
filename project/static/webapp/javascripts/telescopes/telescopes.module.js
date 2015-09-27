(function () {
    'use strict';

    angular
        .module('webapp.telescopes', [
            'webapp.telescopes.controllers',
            'webapp.telescopes.directives',
            'webapp.telescopes.services'
        ]);

    angular
        .module('webapp.telescopes.controllers', []);

    angular
        .module('webapp.telescopes.directives', ['ngDialog']);

    angular
        .module('webapp.telescopes.services', ['ngCookies']);
})();
