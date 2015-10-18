(function () {
    'use strict';

    angular
        .module('webapp.layout.controllers')
        .controller('IndexController', IndexController);

    IndexController.$inject = ['$scope', '$routeParams', 'uiGmapGoogleMapApi'];

    function IndexController($scope, $routeParams, uiGmapGoogleMapApi) {
        $scope.initial = true;

        var vm = this;
        activate();

        function activate() {
        }
    }
})();

