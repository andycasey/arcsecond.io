(function () {
    'use strict';

    angular.module('webapp.authentication.controllers')
        .controller('LoginCtrl', function ($scope, $location, djangoAuth, Validate) {
            $scope.model = {'email': '', 'password': ''};
            $scope.complete = false;
            $scope.login = function (formData) {
                $scope.errors = [];
                Validate.form_validation(formData, $scope.errors);
                if (!formData.$invalid) {
                    djangoAuth.login($scope.model.email, $scope.model.password)
                        .then(function (data) {
                            // success case
                            $location.path("/");
                        }, function (data) {
                            // error case
                            $scope.errors = data;
                        });
                }
            }
        });
})();
