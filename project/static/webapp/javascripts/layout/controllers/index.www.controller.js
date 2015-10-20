(function () {
    'use strict';

    angular
        .module('webapp.layout.controllers')
        .controller('IndexController', IndexController);

    IndexController.$inject = ['$scope', '$routeParams'];

    function IndexController($scope, $routeParams) {
        console.log('??'+$scope.authenticated);
        var vm = this;
        activate();

        function activate() {
        }
    }
})();

