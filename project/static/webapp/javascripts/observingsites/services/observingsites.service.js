/**
 * ObservingSites
 * @namespace webapp.observingsites.services
 */
(function () {
    'use strict';

    angular
        .module('webapp.observingsites.services')
        .factory('ObservingSites', ObservingSites);

    ObservingSites.$inject = ['$cookies', '$http'];

    /**
     * @namespace Authentication
     * @returns {Factory}
     */
    function ObservingSites($cookies, $http) {
        /**
         * @name ObservingSites
         * @desc The Factory to be returned
         */
        var ObservingSites = {
            all: all,
            create: create,
            get: get,
            update: update
        };

        return ObservingSites;

        ////////////////////

        /**
         * @name all
         * @desc Get all Observing Sites
         * @returns {Promise}
         * @memberOf webapp.observingsites.services.ObservingSites
         */
        function all() {
            return $http.get('/1/observingsites/');
        }

        /**
         * @name create
         * @desc Create a new Observing Site
         * @param {string} content The content of the new Observing Site
         * @returns {Promise}
         * @memberOf webapp.observingsites.services.ObservingSites
         */
        function create(content) {
            return $http.post('/1/observingsites/', {
                content: content
            });
        }

        /**
         * @name get
         * @desc Get an ObservingSite
         * @returns {Promise}
         * @memberOf webapp.observingsites.services.ObservingSites
         */
        function get(original_name) {
            return $http.get('/1/observingsites/' + original_name);
        }

        /**
         * @name update
         * @desc Update an ObservingSite
         * @returns {Promise}
         * @memberOf webapp.observingsites.services.ObservingSites
         */
        function update(original_name, name, long_name, IAUCode) {
            return $http.post('/1/observingsites/'+original_name, {
                name: name,
                long_name: long_name,
                IAUCode: IAUCode
            });
        }
    }
})();

