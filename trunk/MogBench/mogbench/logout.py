#coding: utf-8	
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from write_log import WriteLog
from admin_exist import AdminExists

# Logout the system
def logout(request):
    if not AdminExists(request):
        return render_to_response('messages.html',{'msg':'请先登录', 'url':'../login'})
        
    try:
        WriteLog(request.session['aLoginID'], 'Logout')
        del request.session['aLoginID']
        
    except KeyError:
        pass
    
    return render_to_response('logout.html') # Redirect URL
    
