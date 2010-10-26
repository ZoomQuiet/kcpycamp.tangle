from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
from django.db import connection
from AdminExist import AdminExists
import md5

# Add a ID of admin
def AddAdmin(userID, password, email = 'none'):
    res = True
    code = md5.new()
    code.update(password)
    code_psw = code.hexdigest()

    sql = "insert into admin (aLoginID,aPsw) values (%s,%s)"
    param = (userID,code_psw)
    
    connect = connection.cursor()
    try:
        connect.execute(sql, param)
        if not connect.fetchall():
            res = False
    except:
        res = False
        
    connect.close()

    return res

# Add a ID of admin
def DelAdmin(aLoginID):
    res = True
    sql = "delete from admin where aLoginID = (%s)"
    param = (aLoginID)
    
    connect = connection.cursor()
    try:
        connect.execute(sql, param)
        if not connect.fetchall():
            res = False
    except:
        res = False
        
    connect.close()
    
    return res

# Admin Management (main)
def adminManage(request):
    if AdminExists(request):
        aLoginID = request.session.get('aLoginID', None)
        res = {'AdminID' : aLoginID}
    else:
         return HttpResponseRedirect('/login/')
    
    #
    #  For Add
    #
    AddLoginID = request.POST.get('loginID', None)
    passWord = request.POST.get('txtpsw', None)
    passWord2 = request.POST.get('txtpsw2', None)
    email = request.POST.get('txtEmail', None)
    if AddLoginID and passWord and passWord2:
        if AddLoginID == aLoginID:
            res['NameExist'] = 'NameExist'  # The new name has already existed
        else:
            if passWord == passWord2:
                if AddAdmin(AddLoginID, passWord, email):
                    res['AddOk'] = 'AddOk'      # Admin add sucessful
                else:
                    res['NameExist'] = 'NameExist' #  Error...
            else:
                res['NotSame'] = 'NotSame'  # The password is not same
    else:
        if AddLoginID or passWord or passWord2:
            res['Empty'] = 'Empty'          # The table isn't integrity
        
    #
    #  For Del
    #
    DelLoginID = request.POST.get('delUserID', None)

    if DelLoginID:
        if DelAdmin(DelLoginID):
            res['DelOk']
        else:
            res['NameNotExist'] = 'NameNotExist'
            
    context = Context(res)
    return render_to_response('admin_mgr.html', context)

    
    
