# from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.registration.views import SocialLoginView

# class FacebookLogin(SocialLoginView):
#     adapter_class = FacebookOAuth2Adapter

class TwitterLogin(SocialLoginView):
    adapter_class = TwitterOAuthAdapter
