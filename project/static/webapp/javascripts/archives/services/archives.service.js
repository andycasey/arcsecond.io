(function () {
    'use strict';

    angular
        .module('webapp.archives.services')
        .factory('Archives', Archives);

    Archives.$inject = ['$cookies', '$http', '$window'];

    function Archives($cookies, $http, $window) {
        var Archives = {
            latest: latest
        };

        return Archives;

        function latest(archive_name) {
            var url = $window.ARCSECOND_API_ROOT_URL + '/1/archives/';
            if (archive_name !== undefined) {
                url += archive_name+"/";
            }
            else {
                url += "ESO/"
            }
            return $http.get(url);
        }
    }
})();

