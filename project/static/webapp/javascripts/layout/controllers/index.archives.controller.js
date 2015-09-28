(function () {
    'use strict';

    angular
        .module('webapp.layout.controllers')
        .controller('ArchivesIndexController', ArchivesIndexController);

    ArchivesIndexController.$inject = ['$scope', '$http', '$interval', 'Archives', 'Times', 'Telescopes', 'ObservingSites', 'Snackbar'];

    function ArchivesIndexController($scope, $http, $interval, Archives, Times, Telescopes, ObservingSites, Snackbar) {
        var vm = this;

        vm.data_rows = [];
        vm.coordinates = undefined;
        vm.instruments = [];
        vm.telescopes = {};
        vm.observingsites = {};
        vm.first_data_row_date = undefined;

        vm._telRowsMapping = {};

        var tick = function() {
            $scope.times = Times.all(vm.coordinates);
        };
        tick();
        $interval(tick, 1000);

        $scope.updateCountdownFinished = function(timer) {
            fetch_last_data_rows();
        };

        activate();

        function activate() {
            $scope.viewLoading = true;

            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(positionSuccessFn, positionErrorFn, {enableHighAccuracy: true});
            }

            fetch_last_data_rows();

            function positionSuccessFn(position) {
                vm.coordinates = position.coords;
            }

            function positionErrorFn(error) {
                console.log(error);
            }
        }

        function fetch_last_data_rows() {
            $('#timer').css("display", "none");

            Archives.latest('ESO', {start:vm.first_data_row_date}).then(archivesSuccessFn, archivesErrorFn);

            function archivesSuccessFn(response, status, headers, config) {
                var new_rows_count = 0;
                if (undefined !== response.data.results && undefined !== response.data.count) {
                    new_rows_count = response.data.results.length;
                    vm.data_rows = response.data.results.concat(vm.data_rows);
                }
                else {
                    new_rows_count = response.data.length;
                    vm.data_rows = response.data.concat(vm.data_rows);
                }

                var telescope_names = [];
                for (var i = 0; i < new_rows_count; i++) {
                    var data_row = vm.data_rows[i];
                    if (i == 0) {
                        vm.first_data_row_date = data_row.date;
                    }

                    if ($.inArray(data_row.instrument_name, vm.instruments) == -1) {
                        vm.instruments.push(data_row.instrument_name);
                    }

                    if (data_row.telescope !== undefined && data_row.telescope != null) {
                        var encoded_telescope_name = URI(data_row.telescope).path().split("/").filter(function (el) {return el.length}).pop();
                        var telescope_name = decodeURIComponent(encoded_telescope_name);

                        if (undefined === vm.telescopes[telescope_name]) {
                            if (vm._telRowsMapping[telescope_name] == undefined) {
                                vm._telRowsMapping[telescope_name] = [];
                            }
                            vm._telRowsMapping[telescope_name].push(data_row);

                            if ($.inArray(telescope_name, telescope_names) == -1) {
                                telescope_names.push(telescope_name);
                            }
                        }
                        else {
                            data_row.telescope = vm.telescopes[telescope_name];
                        }
                    }
                }

                for (var j = 0; j < telescope_names.length; j++) {
                    Telescopes.get(telescope_names[j]).then(telescopeSuccessFn, telescopeErrorFn);
                }

                $scope.viewLoading = false;
                $('#timer').css("display", "block");
                document.getElementById("timer")['start']();
            }

            function archivesErrorFn(response, status, headers, config) {
                $scope.viewLoading = false;
                console.log(response.error);
            }

            function telescopeSuccessFn(response) {
                var telescope = response.data;
                vm.telescopes[telescope.name] = telescope;

                var data_rows = vm._telRowsMapping[telescope.name];
                for (var i = 0; i < data_rows.length; i++) {
                    data_rows[i].telescope = telescope;
                }
                delete vm._telRowsMapping[telescope.name];

                var encoded_observingsite_name = URI(telescope.observing_site).path().split("/").filter(function (el) {return el.length}).pop();
                var observingsite_name = decodeURIComponent(encoded_observingsite_name);

                ObservingSites.get(observingsite_name, {telescope: telescope}).then(observingsiteSuccessFn, observingsiteErrorFn);
            }

            function telescopeErrorFn(response) {
                console.log(response);
            }

            function observingsiteSuccessFn(response) {
                var observingsite = response.data;
                var telescope = response.config.telescope;
                telescope.observingsite = observingsite;
            }

            function observingsiteErrorFn(response) {
                console.log(response);
            }
        }
    }
})();

