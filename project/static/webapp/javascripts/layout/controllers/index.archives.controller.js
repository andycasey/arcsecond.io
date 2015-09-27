(function () {
    'use strict';

    angular
        .module('webapp.layout.controllers')
        .controller('ArchivesIndexController', ArchivesIndexController);

    ArchivesIndexController.$inject = ['$scope', '$http', '$interval', '$document', 'Archives', 'Times', 'Snackbar'];

    function ArchivesIndexController($scope, $http, $interval, $document, Archives, Times, Snackbar) {
        var vm = this;

        vm.data_rows = undefined;
        vm.coordinates = undefined;
        vm._mappings = {};

        var tick = function() {
            $scope.times = Times.all(vm.coordinates);
        };
        tick();
        $interval(tick, 1000);

        activate();

        function activate() {
            $scope.viewLoading = true;
            $('#timer').css("display", "none");

            Archives.latest('ESO').then(archivesSuccessFn, archivesErrorFn);

            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(positionSuccessFn, positionErrorFn, {enableHighAccuracy: true});
            }

            function archivesSuccessFn(data, status, headers, config) {
                if (data.data.results !== undefined && data.data.count !== undefined) {
                    vm.data_rows = data.data.results;
                }
                else {
                    vm.data_rows = data.data;
                }

                for (var i = 0; i < vm.data_rows.length; i++) {
                    var data_row = vm.data_rows[i];
                    if (data_row.telescope !== undefined) {
                        var telescope = vm._mappings[data_row.instrument_name];
                        if (telescope !== undefined) {
                            data_row.telescope = telescope;
                        }
                        else {
                            $http.get(data_row.telescope, {"data_row": data_row}).then(telescopeSuccessFn, telescopeErrorFn)
                        }
                    }
                }

                $scope.viewLoading = false;
                $('#timer').css("display", "block");
                document.getElementById("timer")['start']();
            }

            function archivesErrorFn(data, status, headers, config) {
                $scope.viewLoading = false;
                console.log(data.error);
            }

            function positionSuccessFn(position) {
                vm.coordinates = position.coords;
            }

            function positionErrorFn(error) {
                console.log(error);
            }

            function telescopeSuccessFn(response) {
                var data_row = response.config.data_row;
                data_row.telescope = response.data;
                vm._mappings[data_row.instrument_name] = data_row.telescope;

                var observing_site = vm._mappings[data_row.telescope.name];
                if (observing_site !== undefined) {
                    data_row.telescope.observing_site = observing_site;
                }
                else {
                    $http.get(data_row.telescope.observing_site, {"telescope": data_row.telescope}).then(observingSiteSuccessFn, telescopeErrorFn)
                }
            }

            function observingSiteSuccessFn(response) {
                var telescope = response.config.telescope;
                telescope.observing_site = response.data;
                vm._mappings[telescope.name] = telescope.observing_site;
            }

            function telescopeErrorFn(response) {
                console.log(response);
            }
        }
    }
})();

