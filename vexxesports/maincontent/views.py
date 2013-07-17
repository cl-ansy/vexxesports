from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from maincontent.models import Stream

def home(request):
    return render_to_response('home.html', {"": ""}, context_instance=RequestContext(request))

def streams(request):
    streams = Stream.objects.all()
    return render_to_response('streams.html', {'streams': streams}, context_instance=RequestContext(request))

def matches(request):
    return render_to_response('matches.html', {"": ""}, context_instance=RequestContext(request))

def guides(request):
    return render_to_response('guides.html', {"": ""}, context_instance=RequestContext(request))

def teams(request):
    return render_to_response('teams.html', {"": ""}, context_instance=RequestContext(request))
