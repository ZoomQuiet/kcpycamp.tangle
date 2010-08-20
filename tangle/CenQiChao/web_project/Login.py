from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
from django.db import connection
from Writelog import WriteLog
import datetime
import md5

# Validate the user's indentity
def validate(userID, password):
    my_md5 = md5.new()
    my_md5.update(password)
    md5_password = my_md5.hexdigest()
    
    connect = connection.cursor()
    sql = "select * from [admin] where [aLoginID] = (%s)"
    param = (userID)
    connect.execute(sql, param)
    all_admin = connect.fetchall()
    connect.close()

    #for record in all_admin:
        #if userID == record['aLoginID'] and md5_password == record[2]:
            #return True
    #return False
    if all_admin:
	if all_admin[1] = userID and md5_password == all_admin[2]:
	return True
    return False

# Login the system
def Checklogin(request):
    aLoginID = request.session.get('aLoginID', None)
    if not aLoginID:
        userID = request.POST.get('UserID', None)
        password = request.POST.get('txtPsw', None)
      
        if userID:
            if validate(userID, password):
                request.session['aLoginID'] = userID
                
        aLoginID = request.session.get('aLoginID', None)

        if aLoginID:
            WriteLog(aLoginID, 'Login')
            return HttpResponseRedirect('/index/')
        else:
            return render_to_response('login.html')
    else:
        return HttpResponseRedirect('/index/')





    
