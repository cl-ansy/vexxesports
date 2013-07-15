from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

def home(request):
    if request.user.groups.filter(name="admins").exists():
        return render_to_response('home.html', {"": ""}, context_instance=RequestContext(request))
    else:
        return redirect('login')

def login(request):
    return render_to_response('login.html', {"": ""}, context_instance=RequestContext(request))

def streams(request):
    return render_to_response('streams.html', {"": ""}, context_instance=RequestContext(request))

def matches(request):
    return render_to_response('matches.html', {"": ""}, context_instance=RequestContext(request))

def guides(request):
    return render_to_response('guides.html', {"": ""}, context_instance=RequestContext(request))

def teams(request):
    return render_to_response('teams.html', {"": ""}, context_instance=RequestContext(request))
