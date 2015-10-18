(function () {
    'use strict';

    angular
        .module('webapp.layout', [
            'webapp.layout.controllers',
            'webapp.layout.directives'
        ]);

    angular
        .module('webapp.layout.controllers', ['timer', 'xeditable']);

    angular
        .module('webapp.layout.directives', []);
})();
