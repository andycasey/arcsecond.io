from django.conf import settings
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie
from django.template import RequestContext

from contact_form import forms
from project.arcsecond.views.utils import get_generic_meta

MESSAGE_SENT = """
<strong>Your message was sent, thanks!</strong> Follow us on
<a href="https://twitter.com/arcsecond_io" class="social__item">
    <i class="fa fa-twitter"></i>
</a> and
<a href="http://facebook.com/arcsecond.io" class="social__item">
    <i class="fa fa-facebook"></i>
</a>.
"""

@ensure_csrf_cookie
def index_www(request):
    context = RequestContext(request)
    context_dict = {"title": ("arcsecond.io"),
                    'api_version': '1',
                    'initial': True,
                    'angular_app': 'webapp',
                    'api_root_url': settings.ARCSECOND_API_ROOT_URL,
                    'meta': get_generic_meta(title="arcsecond.io")}

    if request.method == 'POST':
        form = forms.ContactForm(request=request, data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, MESSAGE_SENT)
            return HttpResponseRedirect(reverse_lazy('index_www'))

    form = forms.ContactForm(request=request)
    context_dict.update({'form': form})
    return render_to_response('arcsecond/index_www.html', context_dict, context)


def index_api(request):
    context = RequestContext(request)
    context_dict = {"title": ("arcsecond.io"),
                    'api_version': '1',
                    'initial': True,
                    'api_root_url': settings.ARCSECOND_API_ROOT_URL,
                    'meta': get_generic_meta(title="api.arcsecond.io", api=True)}

    return render_to_response('arcsecond/index_api.html', context_dict, context)


def custom_404(request):
    return render(request, 'arcsecond/404.html')

def user_account_profile(request):
    u = request.user
    if u.is_authenticated():
        if 'next' in request.GET and (request.GET['next'] is not None):
            return HttpResponseRedirect(request.GET['next'])
        return HttpResponseRedirect(reverse_lazy('user-profile', kwargs={'username': u.username}))
    else:
        return HttpResponseRedirect(reverse_lazy('index'))

def user_profile(request, username):
    context = RequestContext(request)
    context_dict = {"title": ("arcsecond.io - User Profile")}
    try:
        user = get_user_model().objects.get(username=username)
    except ObjectDoesNotExist:
        context_dict['username'] = username
        return render_to_response('arcsecond/no-user-profile.html', context_dict, context)
    else:
        context_dict['user'] = user
        return render_to_response('arcsecond/user-profile.html', context_dict, context)


@login_required
def user_settings(request, username):
    context = RequestContext(request)
    context_dict = {"title": ("arcsecond.io - User Settings")}

    try:
        user = get_user_model().objects.get(username=username)
    except ObjectDoesNotExist:
        raise Http404
    else:
        if user == request.user:
            context_dict['user'] = user
            return render_to_response('arcsecond/user-settings.html', context_dict, context)
        else:
            return HttpResponse('Unauthorized', status=401)


def privacy_policy(request):
    context = RequestContext(request)
    context_dict = {"title": ("arcsecond.io - Privacy Policy")}
    return render_to_response('arcsecond/privacy-policy.html', context_dict, context)




from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator

class IndexView(TemplateView):
    template_name = 'arcsecond/index_webapp.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context["title"] = "arcsecond.io"
        context['api_version'] = '1'
        context['initial'] = True
        context['angular_app'] = "webapp"
        context['api_root_url'] = settings.ARCSECOND_API_ROOT_URL
        context['meta'] = get_generic_meta(title="arcsecond.io")
        return context

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)




class ObservingSitesIndexView(TemplateView):
    template_name = 'arcsecond/index_webapp.html'

    def get_context_data(self, **kwargs):
        context = super(ObservingSitesIndexView, self).get_context_data(**kwargs)
        context['angular_app'] = "webapp"
        context['api_root_url'] = settings.ARCSECOND_API_ROOT_URL
        context['meta'] = get_generic_meta(title="arcsecond.io")
        return context

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(ObservingSitesIndexView, self).dispatch(*args, **kwargs)


class ArchivesIndexView(TemplateView):
    template_name = 'arcsecond/index_webapp.html'

    def get_context_data(self, **kwargs):
        context = super(ArchivesIndexView, self).get_context_data(**kwargs)
        context['angular_app'] = "webapp"
        context['api_root_url'] = settings.ARCSECOND_API_ROOT_URL
        context['meta'] = get_generic_meta(title="arcsecond.io")
        return context

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(ArchivesIndexView, self).dispatch(*args, **kwargs)


class TelegramsIndexView(TemplateView):
    template_name = 'arcsecond/index_webapp.html'

    def get_context_data(self, **kwargs):
        context = super(TelegramsIndexView, self).get_context_data(**kwargs)
        context['angular_app'] = "webapp"
        context['api_root_url'] = settings.ARCSECOND_API_ROOT_URL
        context['meta'] = get_generic_meta(title="arcsecond.io")
        return context

    @method_decorator(ensure_csrf_cookie)
    def dispatch(self, *args, **kwargs):
        return super(TelegramsIndexView, self).dispatch(*args, **kwargs)


