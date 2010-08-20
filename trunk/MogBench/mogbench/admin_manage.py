#coding: utf-8	
'''用户管理选项实现'''
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
from django.db import connection
from admin_exist import AdminExists
from write_log import WriteEvent
import string
import md5



# Add a ID of admin
def AddAdmin(userID, password, email = 'none'):
    '''添加管理员'''
    res = True
    code = md5.new()
    code.update(password)
    code_psw = code.hexdigest()

    connect = connection.cursor()
    sql = "select * from admin where (aLoginID) = (%s)"
    param = (userID,)
    connect.execute(sql, param)
    temp = connect.fetchall()
    
    if not temp:
        sql = "insert into admin (aLoginID,aPsw) values (%s,%s)"
        param = (userID,code_psw)
        connect.execute(sql, param)
    else:
        res = False
        
    connect.close()

    return res

# Add a ID of admin
def DelAdmin(aLoginID):
    '''删除管理员'''

    res = True
    
    connect = connection.cursor()
    sql = "select * from admin where (aLoginID) = (%s)"
    param = (aLoginID,)
    connect.execute(sql, param)
    temp = connect.fetchall()
    
    if temp:
        sql = "delete from admin where aLoginID = (%s)"
        param = (aLoginID,)
        connect.execute(sql, param)
    else:
        res = False
        
    connect.close()
    
    return res

# Get all info of 
def GetAdminInfo():
    connect = connection.cursor()
    sql = "select aID,aLoginID,aEmail from admin"
    connect.execute(sql)
    allRecord = connect.fetchall()

    res  = []
    value = {}
    
    for record in allRecord:
        sql = "select logTime,logEvent from klog "
        sql = sql + "where aLoginID = (%s) order by logTime desc limit 1"
        param = (record[1],)
        connect.execute(sql, param)
        temp = connect.fetchall()
        
        value['id'] = record[0]
        value['aLoginID'] = record[1]
        value['email'] = record[2]

        if temp:
            value['logTime'] = temp[0][0]
        else:
            value['logTime'] = "-"
        
        res.append(value.copy())
            
    connect.close()
    return res

# Modify  Password
def modify(request):
    password = request.POST.get('newPsw', None)
    password2 = request.POST.get('newPsw2', None)
    email = request.POST.get('txtEmail', None)
    AdminID = request.session.get('aLoginID', None)

    append_obj = {}
    
    if password and password2:
        if password != password2:
            append_obj['MNotSame'] = 'NotSame'
            
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
        append_obj['MEmpty'] = 'Empty'
             
    return append_obj

# Edit Flush Time
def EditFlushTime(request, res):
    flushTime = request.POST.get('flushTime', None)

    if  flushTime:
        if not flushTime.isdigit():
            res["TimeFaile"] = "TimeFaile"
           
        elif not string.atof(flushTime) < 5:
            sql = "update config set flushTime = (%s) where aid = (%s)"  
            param = (flushTime, '1')    #  "1" ??

            connect = connection.cursor()
            if connect.execute(sql, param):
                res["TimeOk"] = "TimeOk"
            else:
                res["TimeFaile"] = "TimeFaile"
            connect.close()
        else:
            res["TimeLimit"] = "TimeLimit"


# Admin Management (main)
def adminManage(request):
    if AdminExists(request):
        aLoginID = request.session.get('aLoginID', None)
    else:
        return render_to_response('messages.html',{'msg':'请先登录', 'url':'../login'})

    #
    # For Modify Psw
    #
    res = modify(request)
    res['AdminID'] = aLoginID
    
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
                    WriteEvent(request, "add Admin -> %s" % AddLoginID)
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
            WriteEvent(request, "delete Admin -> %s" % DelLoginID)
            res['DelOk'] = 'DelOk'
        else:
            res['NameNotExist'] = 'NameNotExist'

    # Get Admin Info
    res['AdminsLogs' ] = GetAdminInfo()

    # For edit flush-time
    EditFlushTime(request, res)
    
    context = Context(res)
    return render_to_response('admin_mgr.html', context)

#-------------------以下 by toontong  --------------------------------------------   
def ViewLog(request):
    '''查看日志，对应viewlog.html页面
        
    '''
    if not AdminExists(request):
        return render_to_response('messages.html',{'msg':'请先登录', 'url':'../login'})
        
    adminID = request.GET.get('aID', None)
    nPage = request.GET.get('page', None)
    
    if not adminID.isdigit():
        return render_to_response('messages.html',{'msg':'找不到该用户日志!', 'url':'../admin_mgr'})
    if not nPage:
        nPage = 0
    
    connect = connection.cursor()
    sqlCmd = ((("select aLoginID from admin where aID= %s ") % (adminID)))
    connect.execute(sqlCmd)
    LoginID = connect.fetchall() 
    if not LoginID[0][0]:
        return render_to_response('messages.html',{'msg':'找不到该用户日志!', 'url':'../admin_mgr'})
    sqlCmd = (("select count(lID) FROM klog WHERE aloginID='%s' ") % (LoginID[0][0]))    
        
    connect.execute(sqlCmd)
    allRecord = connect.fetchall()
    if not allRecord:
        return render_to_response('messages.html',{'msg':'找不到该用户日志!', 'url':'../admin_mgr'})
    nPagelistNumber = 15        #每页显示15条日志
    nSumPage = allRecord[0][0] / nPagelistNumber #每页显示15条日志
    
    nPage = int(nPage) * nPagelistNumber         #每页显示15条日志
    sql = (("select * from klog where aloginID='%s' order by logTime desc LIMIT %s, %d") %\
            (LoginID[0][0], nPage, nPagelistNumber))
    connect.execute(sql)
    allRecord = connect.fetchall()

    if not allRecord:
        return render_to_response('messages.html',{'msg':'找不到该用户日志!', 'url':'../admin_mgr'})
    
    Logs = []
    
    for res in allRecord:
        log = {}
        log['id'], log['time'], log['event'] = res[0], res[2], res[3]
        Logs.append(log)
        
    connect.close()
    Sum = range(1, nSumPage)
    return render_to_response('viewlog.html', {'LoginID':allRecord[0],'Logs':Logs,'adminID':adminID, 'SumPage':Sum})
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    pass     
