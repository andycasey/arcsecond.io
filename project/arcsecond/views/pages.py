from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext

def index(request):
    context = RequestContext(request)
    context_dict = {"title": ("arcsecond.io"), 'api_version': '1', 'initial': True}
    return render_to_response('arcsecond/index.html', context_dict, context)

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


