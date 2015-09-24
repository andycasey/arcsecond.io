(function () {
    'use strict';

    angular
        .module('webapp.layout.controllers')
        .controller('ArchivesIndexController', ArchivesIndexController);

    ArchivesIndexController.$inject = ['$scope', '$interval', 'Archives', 'Times', 'Snackbar'];

    function ArchivesIndexController($scope, $interval, Archives, Times, Snackbar) {
        var vm = this;

        vm.data_rows = undefined;
        vm.coordinates = undefined;

        var tick = function() {
            $scope.times = Times.all(vm.coordinates);
        };
        tick();
        $interval(tick, 1000);

        activate();

        function activate() {
            Archives.latest('ESO').then(successFn, errorFn);
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(positionSuccessFn, positionErrorFn, {enableHighAccuracy: true});
            }

            function successFn(data, status, headers, config) {
                vm.data_rows = data.data;
            }

            function errorFn(data, status, headers, config) {
                Snackbar.error(data.error);
                console.log(data.error);
            }

            function positionSuccessFn(position) {
                console.log(position);
                vm.coordinates = position.coords;
            }

            function positionErrorFn(error) {
                Snackbar.error(error);
                console.log(error);
            }
        }
    }
})();

