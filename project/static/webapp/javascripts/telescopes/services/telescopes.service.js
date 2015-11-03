(function () {
    'use strict';

    angular
        .module('webapp.telescopes.services')
        .factory('Telescopes', Telescopes);

    Telescopes.$inject = ['$cookies', '$http', '$window'];

    function Telescopes($cookies, $http, $window) {
        var Telescopes = {
            all: all,
            create: create,
            get: get,
            activities: activities
        };

        return Telescopes;

        ////////////////////

        function all(config) {
            return $http.get($window.ARCSECOND_API_ROOT_URL + '/1/telescopes/', config);
        }

        function create(content) {
            return $http.post($window.ARCSECOND_API_ROOT_URL + '/1/telescopes/', {
                content: content
            });
        }

        function get(name, config) {
            return $http.get($window.ARCSECOND_API_ROOT_URL + '/1/telescopes/' + name + "/", config);
        }

        function activities(config) {
            return $http.get($window.ARCSECOND_API_ROOT_URL + '/1/telescopes/activities', config);
        }
    }
})();

