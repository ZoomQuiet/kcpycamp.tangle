#coding: utf-8	
# 本部分代码并没作任何优化。并不打算作学术研究
#如果你没一点耐心，建议不要浪费时间去看
#
#

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db import connection
from django.template import Context
from admin_exist import AdminExists
import MySQLdb

def index(request):
    ''' mogilefs详细信息页
        
        by toontong
    '''
    if not AdminExists(request):
        return render_to_response('messages.html',{'msg':'请先登录', 'url':'../login'})

    mogID = request.GET.get('mogID',None)
    if  mogID == False:
        return render_to_response('mogfs_view.html')
        
        
    #---------------开始查询Tracker信息,在本地数据库-------------------------------------------    
    connect = connection.cursor()
    sql = "select trackerID,trackerIP,trackerPort,status from trackers where MogGroupID = %d" % int(mogID)  
    connect.execute(sql)
    TrackerInfo = connect.fetchall() #'''查找组群的tracker的详细信息'''
    
    TrackersList = []
    for info in TrackerInfo:
        track = {}  # 默认状态正常
        track['id'], track['ip'], track['port'] = info[0], info[1], info[2]
        if info[3] != 'alive':
            track['state'] = '<p class = "error_red">%s</p>' % info[3]
        else:
            track['state'] = info[3]
        TrackersList.append(track)
    #------------完成了tracker信息--------------------------------------------------    
    
    
    #----------------网页刷新时间----------------------------------------------------------------------------------------------------
    RefreshTime = 60 #默认60秒自动刷新一次
    sql = "select flushTime from config limit 1"
    connect.execute(sql)
    config = connect.fetchall()
    if config:
        RefreshTime = config[0][0]
        
    #------------以下查询数据在远程数据库上--------------------------------------------------------------------------------
    
    
    
    #---------------开始查询Host信息,在各自的mogilefs远程数据库上-----------------------------------------------------------------------
    sqlCmd = "select * from mogfs_group where mID = %d" % int(mogID)
    connect.execute(sqlCmd)             #查询mogGroup
    mogGroupInfo = connect.fetchall()   #'''查找组群的详细信息'''
  
    
    HostList = [] #host主机信息列表
    try:
        conn = MySQLdb.connect(host=mogGroupInfo[0][2], user=mogGroupInfo[0][4],\
                               passwd=mogGroupInfo[0][5],db=mogGroupInfo[0][3])
        cursor = conn.cursor()
        cursor.execute("select hostid,status,http_port,hostname,hostip from host")
    except Exception, e:
        return render_to_response('mogfs_view.html',{'GroupName': mogGroupInfo[0][1],\
                                  'Trackers':TrackersList,'Hosts':HostList})
    
    AllHost = cursor.fetchall() #返回Host在数据库查询信息
    for host in AllHost:
        hostinfo = {}
        hostinfo['id'],hostinfo['state'],hostinfo['port'],hostinfo['name'],hostinfo['ip'] = \
        host[0],host[1],host[2],host[3],host[4]
        
        hostState = hostinfo['state']
        
        #-----------host的状态信息，已同步到本地数据库---------------------------------------------------------------------------------
        mySqlStr = 'select status from host_status where mogid=%d and hostid=%d' % (int(mogID),int(host[0]))
     
        res = connect.execute(mySqlStr)
        if res > 0:   #查询回来只有1条记录
            status = connect.fetchall()         #'''host的状态信息，已同步到本地数据库'''
            hostState = status[0][0]              #查询回来只有条记录
        #-------------------------------------------------------------------------------------------------------------------------------------------------------
        
        if hostState == 'dead':
            hostinfo['state'] = ('<p class = "error_black">%s</p>' % hostState)
        elif hostState == 'down':
            hostinfo['state'] = ('<p class = "error_red">%s</p>' % hostState)
        elif hostState != 'alive':
            hostinfo['state'] =('<p class = "error_red">%s</p>' % hostState)
        
        #-----------------------------开始查询Dev信息------------------------------------------------------------------------------------------------------------------------
        cursor.execute("select devid,status,mb_total,mb_used,mb_asof \
                        from device where hostid = %s " % hostinfo['id'])
        AllDev = cursor.fetchall() #返回数据库查询信息
        DevsList = [] #用于保存每台host中所有dev信息
        for record in AllDev:
            devinfo = {}
            devinfo['id'], devinfo['state'], devinfo['total'], devinfo['used'], devinfo['asof'] = \
            record[0], record[1], record[2], record[3], record[4]
            
            effice = (float(record[3]) / float(record[2])) * 100
            devinfo['effice'] = (('%.2lf') % effice )
            
            if effice > 95:
                devinfo['red'] = True  #进度条红色
            elif effice > 80:
                devinfo['yellow'] = True  #进度条黄色
            else:
                devinfo['no'] = True  #进度条正常颜色
            
            #-----------device的状态信息，已同步到本地数据库---------------------------------------------------------------------------------
            mySqlStr = 'select status from device_status where mogid=%d and hostid=%d and devid=%d' % \
                        (int(mogID), int(host[0]), int(devinfo['id']))
            res = connect.execute(mySqlStr)
            deviceState = devinfo['state']
            if res > 0:   #查询回来只有1条记录
                s = connect.fetchall()         #'''host的状态信息，已同步到本地数据库'''
                deviceState = s[0][0]               #查询回来只有条记录
            #-------------------------------------------------------------------------------------------------------------------------------------------------------
            
            if devinfo['state'] == 'dead':
                devinfo['state'] = '<p class = "error_black">%s</p>' % devinfo['state']
            elif ((devinfo['state'] == 'down') or (hostState != 'alive')):
                devinfo['state'] = '<p class = "error_red">down</p>'
            elif devinfo['state'] == 'drain':
                devinfo['state'] = '<p class = "error_yellow">%s</p>' % devinfo['state']
            elif deviceState != 'alive':
                devinfo['state'] = '<p class = "error_red">%s</p>' % deviceState
               
            #-------------查询完Dev信息--------------------------------------------------------------------------------------------------------------------------------------------   
            DevsList.append(devinfo)
            
        hostinfo['dev'] = DevsList
  
        HostList.append(hostinfo)
    #------------------查询完host主机信息了-------------------------------------------------------------------------------
    
    
    
    #-------------开始查询Domain信息---------------------------------------------------------------------------------------
    cursor.execute("select dmid,namespace from domain") #查询全部domain
    AllDomain = cursor.fetchall() #返回数据库查询信息
    DomainList = []
    for dm in AllDomain:
        dminfo = {}
        dminfo['name'] = dm[1]
        cursor.execute("select classname,mindevcount from class where dmid = %s" % dm[0]) #查询class
        AllClass = cursor.fetchall() #返回数据库查询信息
        
        if AllClass:
            ClassList = []
            for cls in AllClass:
                clsinfo = {}
                clsinfo['name'] = cls[0]
                clsinfo['mindevcount'] = cls[1]
                ClassList.append(clsinfo)
            dminfo['class'] = ClassList
            
        cursor.execute("select count(fid) from file where dmid = %s " % dm[0])
        filesum = cursor.fetchall() #返回数据库查询信息
        if filesum:
            dminfo['filesum']  = filesum[0][0]
        DomainList.append(dminfo)
   #-------------查询完Domain信息---------------------------------------------------------------------------------------
   
    connect.close()   #要以关闭本地数据库连接了
    conn.close() #关闭远程连接
    return render_to_response('mogfs_view.html',{'RefreshTime':RefreshTime,'GroupName': mogGroupInfo[0][1],\
                              'Domains':DomainList,'Trackers':TrackersList,'Hosts':HostList})

if __name__ == '__main__':
    index()
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 