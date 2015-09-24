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

            var now_UT = new Date(Date.UTC(
                now.getFullYear(),
                now.getMonth(),
                now.getDate(),
                now.getHours(),
                now.getMinutes(),
                now.getSeconds()
            ));
            $scope.date_UTC = now_UT;

            var year = parseFloat(now_UT.getFullYear());
            var month = parseFloat(now_UT.getMonth());
            var day = parseFloat(now_UT.getDate());
            var ut = parseFloat(now_UT.getHours()) + parseFloat(now_UT.getMinutes())/60.0 + parseFloat(now_UT.getSeconds())/3600.0;

	        var jd = 367.0*year - Math.floor( 7.0*( year+Math.floor((month+9.0)/12.0))/4.0 ) -
                Math.floor( 3.0*(Math.floor((year+(month-9.0)/7.0)/100.0) +1.0)/4.0) +
                Math.floor(275.0*month/9.0) + day + 1721028.5 + ut/24.0;

            var mjd = jd - 2400000.5;

            $scope.jd = jd.toFixed(5).toString();
            $scope.mjd = mjd.toFixed(5).toString();
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

