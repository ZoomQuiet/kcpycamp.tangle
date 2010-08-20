from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db import connection
from django.template import Context
import md5
import AdminExist

def modify(request):
    if not AdminExists(request):
        return HttpResponseRedirect('/login/')
    
    password = request.POST.get('newPsw', None)
    password2 = request.POST.get('newPsw2', None)
    email = request.POST.get('txtEmail', None)
    AdminID = request.session.get('aLoginID', None)
    
    append_obj = {'AdminID':AdminID}
    
    if password and password2:
        if password != password2:
            append_obj['NotSame'] = 'NotSame'
            
        else:
            append_obj['UpdateOk'] = 'UpdateOk'
            my_md5 = md5.new()
            my_md5.update(password)
            md5_password = my_md5.hexdigest()

            sql = "update admin set aPsw = (%s), aEmail = (%s) where aLoginID = (%s)"
            param = (md5_password, email, AdminID)
    
            connect = connection.cursor()
            connect.execute(sql, param)
            # Test ?
            connect.close()
            
    else:
        append_obj['Empty'] = 'Empty'
        
    context = Context(append_obj)        
    return render_to_response('admin_mofpsw.html', context)
        
