from django.conf import settings
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import ensure_csrf_cookie
from django.template import RequestContext
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator

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

def privacy_policy(request):
    context = RequestContext(request)
    context_dict = {"title": ("arcsecond.io - Privacy Policy")}
    return render_to_response('arcsecond/privacy-policy.html', context_dict, context)


# Rest Auth

class AccountConfirmEmailView(TemplateView):
    template_name = 'account/email_confirm.html'

    def get_context_data(self, **kwargs):
        context = super(AccountConfirmEmailView, self).get_context_data(**kwargs)
        context["title"] = "arcsecond.io"
        context['api_version'] = '1'
        context['meta'] = get_generic_meta(title="arcsecond.io")
        return context

    def dispatch(self, *args, **kwargs):
        return super(AccountConfirmEmailView, self).dispatch(*args, **kwargs)


# Angular Web App

class IndexView(TemplateView):
    template_name = 'arcsecond/index_www.html'

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


