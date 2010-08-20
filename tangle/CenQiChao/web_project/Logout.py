from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from Writelog import WriteLog

# Logout the system
def logout(request):
    try:
        WriteLog(request.session['aLoginID'], 'Logout')
        del request.session['aLoginID']
        
    except KeyError:
        pass
    
    return render_to_response('logout.html') # Redirect URL
    
