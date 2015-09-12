/**
* ObservingSites
* @namespace webapp.observingsites.services
*/
(function () {
  'use strict';

  angular
    .module('webapp.observingsites.services')
    .factory('ObservingSites', ObservingSites);

  ObservingSites.$inject = ['$http'];

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
      update: update
    };

    return ObservingSites;

    ////////////////////

    /**
    * @name update
    * @desc Update an ObservingSite
    * @returns {Promise}
    * @memberOf webapp.observingsites.services.ObservingSites
    */
    function update(original_name, name, long_name, IAUCode) {
      return $http.post('/api/v1/observingsites/'+original_name, {
          name: name,
          long_name: long_name,
          IAUCode: IAUCode
        });
    }
  }
})();

