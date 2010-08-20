#coding: utf-8	
# Add MogGroup 
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
from django.db import connection
from admin_exist import AdminExists
from write_log import WriteEvent
import MySQLdb

# Main Process of Add
def AddMogGroup(request):
    if not AdminExists(request):
        return render_to_response('messages.html',{'msg':'请先登录', 'url':'../login'})

    res = {}

    mogName = request.POST.get('mogName', None)
    mogdbIP = request.POST.get('mogdbIP', None)
    dbName = request.POST.get('dbName', None)
    dbUser = request.POST.get('dbUser', None)
    dbPsw = request.POST.get('dbPsw', None)

    if mogName and mogdbIP and dbName and dbUser and dbPsw:
        if TestIP(mogdbIP):
            try:
                conn = MySQLdb.connect(host = mogdbIP, user = dbUser, passwd = dbPsw, db = dbName)
                cursor = conn.cursor()
                cursor.execute("select hostid from host") #随便运行一条ＳＱＬ语句查一下是否正确表结构
                conn.close()
            except Exception, e:
                msg = ("添加组群 %s,连接数据库 IP=%s db=%s user=%s, psw=%s \n出错!请确认数据库信息再添加!") % \
                      (mogName, mogdbIP, dbName, dbUser, dbPsw)
                return render_to_response('messages.html',{'msg':msg, 'url':"../addmogilefs"})

            if Add(mogName, mogdbIP, dbName, dbUser, dbPsw):
                WriteEvent(request, 'Add MogileFS Group -> %s' % mogName)
                res['AddOk'] = 'AddOk'
        else:
            res['WrongIP'] = 'WrongIP'
    else:
        res['Empty'] = 'Empty'
    
    # Get  info  of  all  mogs  from  DB
    allMogs = []
    singleMog =  {}
    cursor = connection.cursor()
    cursor.execute("select * from mogfs_group")
    for record in cursor.fetchall():
        singleMog['id'] = record[0]
        singleMog['name'] = record[1]
        allMogs.append(singleMog.copy())
    
    res['Mogilefs'] = allMogs
    
    context = Context(res)
    return render_to_response('addmogilefs.html', context)
      
# Add (for mog_group)
def Add(mogName, mogdbIP, dbName, dbUser, dbPsw):
    connect = connection.cursor()
 
    sql = "insert into mogfs_group (mName,mdbIP,mdbName,mdbUser,mdbPsw) values (%s,%s,%s,%s,%s)"

    param = (mogName, mogdbIP, dbName, dbUser, dbPsw)
    connect.execute(sql, param)
    connect.close()

    return True

# Test IP
def TestIP(mogdbIP):
    if mogdbIP.__len__() > 15 or mogdbIP.__len__() < 7:
        return False
    else:
        dota = 0
        gap = 0
        for ch in mogdbIP:
            if ch.isdigit():
                gap = gap + 1
                if gap > 3:
                    return False
            elif ch == '.':
                dota = dota + 1
                if dota > 3 or gap == 0:
                    return False
                gap = 0
    return True

if __name__ == '__main__': #8.模块入口
   AddMogGroup()