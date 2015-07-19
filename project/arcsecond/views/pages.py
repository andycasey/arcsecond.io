
from django.shortcuts import render, render_to_response
from django.template import RequestContext

def index(request):
  context = RequestContext(request)
  context_dict = {"title": ("arcsecond.io"), 'api_version': '1'}
  return render_to_response('arcsecond/index.html', context_dict, context)

def custom_404(request):
    return render(request, 'arcsecond/404.html')


