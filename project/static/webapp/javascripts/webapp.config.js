(function () {
    'use strict';

    angular
        .module('webapp.config')
        .config(config);

    config.$inject = ['$locationProvider', 'uiGmapGoogleMapApiProvider'];

    function config($locationProvider, uiGmapGoogleMapApiProvider) {
        $locationProvider.html5Mode(true);
        $locationProvider.hashPrefix('!');

        uiGmapGoogleMapApiProvider.configure({
            //key: 'YOUR KEY HERE',
            v: '3.17',
            libraries: 'weather,geometry,visualization'
        });
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
