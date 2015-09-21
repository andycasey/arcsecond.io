/**
 * ObservingSites
 * @namespace webapp.observingsites.services
 */
(function () {
    'use strict';

    angular
        .module('webapp.observingsites.services')
        .factory('ObservingSites', ObservingSites);

    ObservingSites.$inject = ['$cookies', '$http', '$window'];

    function ObservingSites($cookies, $http, $window) {
        var ObservingSites = {
            all: all,
            create: create,
            get: get,
            update: update,
            activities: activities
        };

        ObservingSites.continents = [
            {name:'Africa', key:'africa'},
            {name:'Antarctica', key:'antarctica'},
            {name:'Asia', key:'asia'},
            {name:'Europe', key:'europe'},
            {name:'North America', key:'north_america'},
            {name:'Oceania', key:'oceania'},
            {name:'South America', key:'south_america'}
        ];

        return ObservingSites;

        ////////////////////

        function all(continent_name) {
            var url = $window.ARCSECOND_API_ROOT_URL + '/1/observingsites/';
            if (continent_name !== undefined) {
                url += "?continent="+continent_name;
            }
            return $http.get(url);
        }

        function create(content) {
            return $http.post('/1/observingsites/', {
                content: content
            });
        }

        function get(original_name) {
            return $http.get($window.ARCSECOND_API_ROOT_URL + '/1/observingsites/' + original_name);
        }

        function update(original_name, name, long_name, IAUCode) {
            return $http.post('/1/observingsites/'+original_name, {
                name: name,
                long_name: long_name,
                IAUCode: IAUCode
            });
        }

        function activities() {
            return $http.get($window.ARCSECOND_API_ROOT_URL + '/1/observingsites/activities');
        }
    }
})();

