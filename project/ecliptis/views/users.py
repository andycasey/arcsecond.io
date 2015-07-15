from django.template import RequestContext
from django.shortcuts import render_to_response, render

from django.views.generic.edit import UpdateView
from django.contrib.auth import get_user_model

from .. import models
# from .. import forms

def UserProfileView(request):
    # context_data = {}
    # users = get_user_model().objects.filter(username=username)
    # if len(users) == 1:
    #     user = users.first()
    #     context_data["user_to_show"] = user
    #     profile, created = models.UserProfile.objects.get_or_create(user=user)
    #     context_data["user_profile_to_show"] = profile
    return render_to_response('ecliptis/user-profile.html', {}, RequestContext(request))
    # else:
    #     context_data["username"] = username
    #     return render_to_response('ecliptis/no-user-profile.html', context_data, RequestContext(request))

# From the doc of SingleObjectMixin
# See https://docs.djangoproject.com/en/dev/ref/class-based-views/mixins-single-object/#django.views.generic.detail.SingleObjectMixin.queryset
# class UserProfileUpdateView(UpdateView):
#     model = models.UserProfile
#     template_name = 'picolegends/pages/user-profile-edit.html'
#     form_class = forms.UserProfileForm
#
#     def get(self, request, *args, **kwargs):
#         self.initial = {}
#         form = self.form_class(request.user, initial=self.initial)
#         return render(request, self.template_name, {'form': form})
#
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.user, request.POST)
#         context_data = {'form': form}
#         if form.is_valid():
#             form.save()
#             context_data['success_message'] = _("Your Author Profile has been saved.")
#         else:
#             context_data['error_message'] = _("Your Author Profile has not been saved.")
#         return render(request, self.template_name, context_data)
#
#     def get_form_kwargs(self):
#         kwargs = super(UserProfileUpdateView, self).get_form_kwargs()
#         if self.request.user:
#             kwargs['user'] = self.request.user
#         return kwargs
#
#     def get_queryset(self):
#         user = get_user_model().objects.get(pk=self.request.user.pk)
#         return models.UserProfile.objects.filter(user=user)
#
#     def get_object(self):
#         user = get_user_model().objects.get(pk=self.request.user.pk)
#         profile, created = models.UserProfile.objects.get_or_create(user=user)
#         return profile

