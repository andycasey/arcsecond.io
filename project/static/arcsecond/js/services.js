/**
 * Created by onekiloparsec on 09/08/15.
 */

var arcsecondServices = angular.module('arcsecondServices', ['ngResource']);

arcsecondServices.factory('ObservingSite', ['$resource',
    function($resource){
        return $resource('observingsites/:phoneId.json', {}, {
            query: {
                method: 'GET',
                params: {phoneId:'phones'},
                isArray: true
            }
        });
    }]);

