(function () {
    'use strict';

    angular
        .module('webapp.filters', [])
        .filter('nameContainsSubstring', function () {
            return function (items, searchString) {
                if (searchString === undefined) {
                    return items;
                }
                var filtered = [];
                var stringRegex = new RegExp(searchString, 'i');
                for (var i = 0; i < items.length; i++) {
                    var item = items[i];
                    if (stringRegex.test(item.name)) {
                        filtered.push(item);
                    }
                }
                return filtered;
            };
        });

    angular
        .module('webapp.filters', [])
        .filter('timeAgo', ['$interval', function ($interval) {
            $interval(function (){}, 60000);

            function fromNowFilter(time){
                return moment(time).fromNow();
            }

            fromNowFilter.$stateful = true;
            return fromNowFilter;
        }]);

})();

