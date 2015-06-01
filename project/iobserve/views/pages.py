
from django.shortcuts import render, render_to_response
from django.template import RequestContext

def index(request):
  context = RequestContext(request)
  context_dict = {"title": ("eclipt.is")}
  return render_to_response('iobserve/index.html', context_dict, context)

def about(request):
  context = RequestContext(request)
  context_dict = {"title": ("about eclipt.is")}
  return render_to_response('iobserve/about.html', context_dict, context)

def custom_404(request):
    return render(request, 'iobserve/404.html')

def sky_home(request, path=None):
    return render(request, 'iobserve/sky_home.html', {'api_version': '1'})

def earth_home(request, path=None):
    return render(request, 'iobserve/earth_home.html', {'api_version': '1'})


