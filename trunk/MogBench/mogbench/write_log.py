#coding: utf-8	
from django.db import connection
from django.shortcuts import render_to_response
from django.http import HttpResponse
import datetime

# Wrtie the info of event to 'aLog' Table
def WriteLog(aLoginID, event):
    if aLoginID:
        CurrentTime = datetime.datetime.now()

        connect = connection.cursor()
        sql = 'insert into klog (aloginID,logTime,logEvent) values (%s,%s,%s)'
        param = (aLoginID,CurrentTime,event)
        connect.execute(sql,param)
        connect.close()
        
        return True
    else:
        return False

def WriteEvent(request, event):
    AdminID = request.session.get('aLoginID', None)
    if not AdminID:
        return render_to_response('messages.html',{'msg':'请先登录', 'url':'../login'})
    else:
        return WriteLog(AdminID, event)
