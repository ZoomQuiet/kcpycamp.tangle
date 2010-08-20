#coding: utf-8	
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
from admin_exist import AdminExists
    
def index(request):
    if not AdminExists(request):
        return render_to_response('messages.html',{'msg':'请先登录', 'url':'../login'})
    else:
        AdminID = request.session.get('aLoginID', None)
        context = Context({'AdminID' : AdminID})
        return render_to_response('index.html', context)
