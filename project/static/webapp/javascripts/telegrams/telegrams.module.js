(function () {
    'use strict';

    angular
        .module('webapp.telegrams', [
            'webapp.telegrams.controllers',
            'webapp.telegrams.directives',
            'webapp.telegrams.services'
        ]);

    angular
        .module('webapp.telegrams.controllers', []);

    angular
        .module('webapp.telegrams.directives', ['ngDialog']);

    angular
        .module('webapp.telegrams.services', ['ngCookies']);
})();
