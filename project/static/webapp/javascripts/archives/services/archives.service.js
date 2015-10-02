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

        function latest(archive_name, params) {
            var url = $window.ARCSECOND_API_ROOT_URL + '/1/archives/';
            if (archive_name !== undefined) {
                url += archive_name+"/";
            }
            else {
                url += "ESO/"
            }

            var append = "";
            if (params !== undefined) {
                for (var key in params) {
                    if (params.hasOwnProperty(key)) {
                        if (params[key] !== undefined) {
                            append += key+"="+params[key]+"&";
                        }
                    }
                }
            }

            if (append.length > 0) {
                url += "?" + append;
            }
            console.log("---> "+url);
            return $http.get(url);
        }
    }
})();

