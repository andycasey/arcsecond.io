
from django.shortcuts import render, render_to_response
from django.template import RequestContext

def index_www(request):
  context = RequestContext(request)
  context_dict = {"title": ("arcsecond.io")}
  return render_to_response('arcsecond/index.html', context_dict, context)

def about(request):
  context = RequestContext(request)
  context_dict = {"title": ("about arcsecond.io")}
  return render_to_response('arcsecond/about.html', context_dict, context)

def custom_404(request):
    return render(request, 'arcsecond/404.html')

def sky_home(request, path=None):
    return render(request, 'arcsecond/sky_home.html', {'api_version': '1'})

def earth_home(request, path=None):
    return render(request, 'arcsecond/earth_home.html', {'api_version': '1'})


