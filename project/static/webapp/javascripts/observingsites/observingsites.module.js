(function () {
    'use strict';

    angular
        .module('webapp.observingsites', [
            'webapp.observingsites.controllers',
            'webapp.observingsites.directives',
            'webapp.observingsites.services'
        ]);

    angular
        .module('webapp.observingsites.controllers', ['ngMap']);

    angular
        .module('webapp.observingsites.directives', ['ngDialog']);

    angular
        .module('webapp.observingsites.services', ['ngCookies']);
})();
