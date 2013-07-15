from django.shortcuts import render_to_response, redirect
from django.template import RequestContext

def home(request):
    if request.user.groups.filter(name="admins").exists():
        return render_to_response('home.html', {"": ""}, context_instance=RequestContext(request))
    else:
        return redirect('login')

def login(request):
    return render_to_response('login.html', {"": ""}, context_instance=RequestContext(request)) 
