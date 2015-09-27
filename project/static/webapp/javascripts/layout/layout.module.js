(function () {
    'use strict';

    angular
        .module('webapp.layout', [
            'webapp.layout.controllers'
        ]);

    angular
        .module('webapp.layout.controllers', ['timer']);
})();
