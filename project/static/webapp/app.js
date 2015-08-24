
var app = angular.module('arcsecondApp', []);

app.config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
});
