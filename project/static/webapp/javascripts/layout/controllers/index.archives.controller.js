(function () {
    'use strict';

    angular
        .module('webapp.layout.controllers')
        .controller('ArchivesIndexController', ArchivesIndexController);

    ArchivesIndexController.$inject = ['$scope', '$interval', 'Archives', 'Snackbar'];

    function ArchivesIndexController($scope, $interval, Archives, Snackbar) {
        var vm = this;

        vm.data_rows = undefined;

        var tick = function() {
            var now = new Date();
            $scope.date_local = now;
            $scope.date_UTC = new Date(Date.UTC(
                now.getFullYear(),
                now.getMonth(),
                now.getDate(),
                now.getHours(),
                now.getMinutes(),
                now.getSeconds()
            ));
        };
        tick();
        $interval(tick, 1000);

        activate();

        function activate() {
            Archives.latest('ESO').then(successFn, errorFn);

            function successFn(data, status, headers, config) {
                vm.data_rows = data.data;
            }

            function errorFn(data, status, headers, config) {
                Snackbar.error(data.error);
                console.log(data.error);
            }
        }
    }
})();

