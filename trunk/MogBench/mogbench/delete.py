#coding: utf-8	
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db import connection
from admin_exist import AdminExists
from write_log import WriteEvent


def deletetracker(trackerID):
    '''删除一个tracker'''
    try:
        connect = connection.cursor()
        sqlCmd = ("DELETE FROM trackers WHERE trackerID = %s") % (trackerID)
        connect.execute(sqlCmd)
        connect.close()
        return 1
    except Exception, e:
        return 0

def delTracker(request):
    '''删除一个Ｔracker
    '''
    if not AdminExists(request):
        return render_to_response('messages.html',{'msg':'请先登录', 'url':'../login'})
        
    tracID = request.GET.get('trackerID', None)
    if not tracID:
        return render_to_response("messages.html", {'msg':"找不到Tracker!",'url':'../addtracker/'})
    if (deletetracker(tracID) == 0):
       return render_to_response("messages.html", {'msg':"删除失败，数据库中没该信息!",'url':'../addtracker/'})
    else:
       WriteEvent(request, ('delete Tracker -> %s') % (tracID))
       return render_to_response("messages.html", {'msg':"删除成功!" , 'url':'../addtracker/'})
        
        
def delMogileFS(request):
    '''删除一个群组,同时把所属tracker删除'''
    if not AdminExists(request):
        return render_to_response('messages.html',{'msg':'请先登录', 'url':'../login'})
    mogID = request.GET.get('mogID', None)
    if not mogID.isdigit():
        return render_to_response("messages.html", {'msg':"找不到MogileFS组群!",'url':'../index'})
    
    connect = connection.cursor()
    sqlCmd = ("DELETE FROM trackers WHERE MogGroupID = %s") % (mogID)
    connect.execute(sqlCmd)
    sqlCmd = ("DELETE FROM mogfs_group WHERE mID = %s") % (mogID)
    connect.execute(sqlCmd)
    connect.close()
    
    WriteEvent(request, 'delete MogileFS system -> %s' % mogID)
    return render_to_response("messages.html", {'msg':"删除成功,点击返回首页!" , 'url':'../index'})

def delLog(request):
    '''删除一个日志'''
    if not AdminExists(request):
        return render_to_response('messages.html',{'msg':'请先登录', 'url':'../login'})
    
    logID = request.GET.get('logID', None)
    if not logID.isdigit():
        return render_to_response("messages.html", {'msg':"找不到日志记录!点击返回管理页!",'url':'../admin_mgr'})
    
    connect = connection.cursor()
    sqlCmd = ("DELETE FROM klog WHERE lID = %s") % (logID)
    connect.execute(sqlCmd)
    connect.close()
    
    return render_to_response("messages.html", {'msg':"<SCRIPT language=JavaScript> history.back()</SCRIPT>",'url':""   })
 
if __name__ == '__main__': #8.模块入口
   delTracker()        
        
        
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    pass  