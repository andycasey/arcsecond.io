(function () {
    'use strict';

    angular
        .module('webapp.layout.controllers')
        .controller('ObservingSiteUpdateController', ObservingSiteUpdateController);

    ObservingSiteUpdateController.$inject = ['$scope', '$routeParams', 'ObservingSites', 'Snackbar'];

    function ObservingSiteUpdateController($scope, $routeParams, ObservingSites, Snackbar) {
        var vm = this;
        vm.observingsitedetail = undefined;

        $scope.continents = ObservingSites.continents;
        $scope.showContinents = function() {
            var selected = $filter('filter')($scope.continents, vm.observingsitedetail.continent);
            return (vm.observingsitedetail.continent && selected.length) ? selected[0] : 'Not set';
        };

        activate();

        function activate() {
            if ($routeParams.site_name !== "new" && $routeParams.site_name !== undefined) {
                ObservingSites.get($routeParams.site_name).then(successFn, errorFn);
            }

            function successFn(response, status, headers, config) {
                vm.observingsitedetail = response.data;
            }

            function errorFn(response, status, headers, config) {
                //Snackbar.error(data.error);
            }
        }
    }
})();

