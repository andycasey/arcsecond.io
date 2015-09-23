(function () {
    'use strict';

    angular
        .module('webapp.archives', [
            'webapp.archives.controllers',
            'webapp.archives.directives',
            'webapp.archives.services'
        ]);

    angular
        .module('webapp.archives.controllers', []);

    angular
        .module('webapp.archives.directives', ['ngDialog']);

    angular
        .module('webapp.archives.services', ['ngCookies']);
})();
