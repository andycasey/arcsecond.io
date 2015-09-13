(function () {
    'use strict';

    angular
        .module('webapp.config')
        .config(config);

    config.$inject = ['$locationProvider'];

    /**
     * @name config
     * @desc Enable HTML5 routing
     */
    function config($locationProvider) {
        $locationProvider.html5Mode(true);
        $locationProvider.hashPrefix('!');
    }
})();

//
//arcsecondApp.config(function($interpolateProvider, $httpProvider) {
//    $interpolateProvider.startSymbol('[[');
//    $interpolateProvider.endSymbol(']]');
//
//    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
//    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
//    $httpProvider.defaults.withCredentials = true;
//});
//
