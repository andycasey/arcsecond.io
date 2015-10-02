(function ($, _) {
    'use strict';

    angular
        .module('webapp.utils.services')
        .factory('Times', Times);

    function Times() {
        var Times = {
            all: all
        };

        return Times;

        function all(coordinates) {
            var now = new Date();
            var times = {};
            times.date_local = now;

            var now_UT = new Date(Date.UTC(
                now.getFullYear(),
                now.getMonth(),
                now.getDate(),
                now.getHours(),
                now.getMinutes(),
                now.getSeconds()
            ));
            times.date_UTC = now_UT;

            var year = parseFloat(now_UT.getFullYear());
            var month = parseFloat(now_UT.getMonth());
            var day = parseFloat(now_UT.getDate());
            var ut = parseFloat(now_UT.getHours()) + parseFloat(now_UT.getMinutes())/60.0 + parseFloat(now_UT.getSeconds())/3600.0;

            var jd = 367.0*year - Math.floor( 7.0*( year+Math.floor((month+9.0)/12.0))/4.0 ) -
                Math.floor( 3.0*(Math.floor((year+(month-9.0)/7.0)/100.0) +1.0)/4.0) +
                Math.floor(275.0*month/9.0) + day + 1721028.5 + ut/24.0;

            var mjd = jd - 2400000.5;

            times.jd = jd.toFixed(5).toString();
            times.mjd = mjd.toFixed(5).toString();

            if (coordinates !== undefined) {
                var ONE_DEG_IN_HOURS = 0.06666666666666666666666666666;
                var t = (jd - 2451545.0) / 36525.0;

                // Greenwhich SiderealTime in degrees!
                var gmst = 280.46061837 + 360.98564736629*(jd-2451545.0) + 0.000387933*t*t - t*t*t/38710000.0;

                while (gmst < 0.) {
                    gmst = gmst + 360.0;
                }
                if (gmst > 360.) {
                    gmst = gmst%360;
                }

                // Greenwhich SiderealTime in hours.
                gmst = gmst * ONE_DEG_IN_HOURS;

                // Correct for longitude and make sure it is positive. aLongitude is always expressed in degrees, East positive.
                // See Terrestrial coordinates.

                // See AA. p92. LMST = theta_0 - L, for L the longitude, if L is positive West.
                // Hence, LMST = theta_0 + L if longitude is positive East, as we have here.

                var lmst = gmst + coordinates.longitude*ONE_DEG_IN_HOURS + 24.0;
                if (lmst > 24.0) {
                    lmst = lmst%24;
                }

                var h = Math.floor(lmst);
                var m = Math.floor((lmst-h)*60.0);
                var s = Math.floor((lmst-h-m/60.0)*3600.0);

                times.lmst = { "h": h, "m": m, "s": s};
            }

            return times;
        }
    }
})();

