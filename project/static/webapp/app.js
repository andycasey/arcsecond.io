
'use strict';

var arcsecondApp = angular.module('arcsecondApp', []);

arcsecondApp.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});

