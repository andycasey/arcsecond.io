(function () {
    'use strict';

    angular.module('webapp.authentication.controllers')
        .controller('PasswordchangeCtrl', function ($scope, djangoAuth, Validate) {
            $scope.model = {'new_password1': '', 'new_password2': ''};
            $scope.complete = false;
            $scope.changePassword = function (formData) {
                $scope.errors = [];
                Validate.form_validation(formData, $scope.errors);
                if (!formData.$invalid) {
                    djangoAuth.changePassword($scope.model.new_password1, $scope.model.new_password2)
                        .then(function (data) {
                            // success case
                            $scope.complete = true;
                        }, function (data) {
                            // error case
                            $scope.errors = data;
                        });
                }
            }
        });
})();
