(function () {
    'use strict';

    angular
        .module('webapp.layout.controllers')
        .controller('IndexController', IndexController);

    IndexController.$inject = ['$scope', 'ObservingSites', 'Snackbar'];

    function IndexController($scope, ObservingSites, Snackbar) {
        var vm = this;

        vm.observingsites = {};
        for (var i = 0; i < ObservingSites.continents.length; i++) {
            var continent_key = ObservingSites.continents[i].key;
            vm.observingsites[continent_key] = [];
        }

        activate();

        function activate() {
            for (var i = 0; i < ObservingSites.continents.length; i++) {
                var continent = ObservingSites.continents[i];
                ObservingSites.all(continent.name).then(successFn, errorFn);
            }

            function successFn(data, status, headers, config) {
                var url = document.createElement('a');
                url.href = data.config.url;
                var continent_key = url.search.split('=')[1].toLowerCase().replace(' ', '_');
                vm.observingsites[continent_key] = data.data;
            }

            function errorFn(data, status, headers, config) {
                Snackbar.error(data.error);
                console.log(data.error);
            }
        }
    }
})();

