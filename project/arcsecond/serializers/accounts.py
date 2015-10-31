
from django.contrib import auth
from rest_framework import serializers
from project.arcsecond.models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = auth.get_user_model()
        fields = ('id', 'first_name', 'last_name', 'username')

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'user', 'membership_date', 'email_verified')
    user = UserSerializer()
