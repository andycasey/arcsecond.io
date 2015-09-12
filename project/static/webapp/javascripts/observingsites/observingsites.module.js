(function () {
  'use strict';

  angular
    .module('webapp.observingsites', [
      'webapp.observingsites.controllers',
      'webapp.observingsites.services'
    ]);

  angular
    .module('webapp.observingsites.controllers', []);

  angular
    .module('webapp.observingsites.services', ['ngCookies']);
})();
