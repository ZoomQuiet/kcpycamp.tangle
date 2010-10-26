from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
from AdminExist import AdminExists
    
def index(request):
    if not AdminExists(request):
        return HttpResponseRedirect('/login/')
    else:
        AdminID = request.session.get('aLoginID', None)
        context = Context({'AdminID' : AdminID})
        return render_to_response('top.html', context)
