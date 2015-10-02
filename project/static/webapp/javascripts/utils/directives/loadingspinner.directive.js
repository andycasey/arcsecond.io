(function () {
    'use strict';

    angular
        .module('webapp.utils.directives')
        .directive('myLoadingSpinner', myLoadingSpinner);

    function myLoadingSpinner() {
        var directive = {
            restrict: 'A',
            replace: true,
            transclude: true,
            scope: {
                loading: '=myLoadingSpinner'
            },
            templateUrl: '/static/webapp/templates/utils/loadingspinner.html',

            link: function(scope, element, attrs) {
                var opt = {scale: 0.5, radius: 7, top: 90};
                var spinner = new Spinner(opt).spin();
                var loadingContainer = element.find('.my-loading-spinner-container')[0];
                loadingContainer.appendChild(spinner.el);
            }
        };

        return directive;
    }
})();
