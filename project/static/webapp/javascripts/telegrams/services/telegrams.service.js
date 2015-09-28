(function () {
    'use strict';

    angular
        .module('webapp.telegrams.services')
        .factory('Telegrams', Telegrams);

    Telegrams.$inject = ['$cookies', '$http', '$window'];

    function Telegrams($cookies, $http, $window) {
        var Telegrams = {
            all: all,
            get: get,
        };

        return Telegrams;

        ////////////////////

        function all(config) {
            return $http.get($window.ARCSECOND_API_ROOT_URL + '/1/telegrams/', config);
        }

        function get(identifier, config) {
            return $http.get($window.ARCSECOND_API_ROOT_URL + '/1/telegrams/' + identifier, config);
        }
    }
})();

