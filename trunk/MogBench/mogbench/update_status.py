#coding: utf-8	
'''

状态同步更新脚本,以系统的计划任务定时执行，按实时性需求，自行调整定时时间,建议30分钟/次
由于本脚本在检查Trackers, Hosts, Devices时耗时较长，连接数据库时易超时，需反复连接数据库

'''
import settings
import MySQLdb
import os
##import time

#key = raw_input('press any key to continue...')

#-------------------------by toontong----------------------------------------------------
    ##  使用全局的数据库 连接操作, update_tracker(),update_host(),update_device()三个函数都用到了

#-------------------------by toontong----------------------------------------------------

#-------------------------by toontong  update tracker---------------------------------------------------
def update_tracker(trackerip, trackerport, trackerstatus, mogGroupID):
    '''更新tracker 状态到本地数据库中'''
    try:
        conn = MySQLdb.connect(host=settings.DATABASE_HOST, user=settings.DATABASE_USER,passwd=settings.DATABASE_PASSWORD,db=settings.DATABASE_NAME)
        cursor = conn.cursor()
        print 'MySql ok'
    except Exception, e:
        print "MySQL Error!"
    
    if settings.DEBUG:
        print 'tracker-ip:', trackerip, 'tracker port: ', trackerport, 'tracker status', trackerstatus
   
    SqlCmd = "UPDATE trackers SET status='%s' where trackerIP='%s'" %(trackerstatus, trackerip)
    res = cursor.execute(SqlCmd) #执行更新语句
    conn.close() #关闭连接  
    print res

    
def update_host(hostid, hoststatus, mogGroupID):
    '''更新host 状态到本地数据库中'''
    try:
        conn = MySQLdb.connect(host=settings.DATABASE_HOST, user=settings.DATABASE_USER,passwd=settings.DATABASE_PASSWORD,db=settings.DATABASE_NAME)
        cursor = conn.cursor()
        print 'MySql ok'
    except Exception, e:
        print "MySQL Error!"
        
        
    if settings.DEBUG:
        print 'host id:', hostid, 'host status:', hoststatus
        
    SqlCmdSel = "select status from host_status where mogid=%d and hostid=%d" % (int(mogGroupID),int(hostid))
    print SqlCmdSel
    res = cursor.execute(SqlCmdSel)
    print res
    SqlCmd2 =''
    if res > 0: #表示存在host,更新即可
        SqlCmd2 = "UPDATE host_status SET status='%s' where mogid=%d and hostid=%d" % (hoststatus, mogGroupID, int(hostid))
    else:
        SqlCmd2 = "INSERT INTO host_status(mogid,hostid,status) values(%d,%d,'%s')" % \
                 (mogGroupID, int(hostid), hoststatus)
   
    res = cursor.execute(SqlCmd2)
    conn.close() #关闭连接  
    if settings.DEBUG:
        print SqlCmd2 ,res

        
        
        
def update_device(hostid, deviceid, devicestatus, mogGroupID):
    '''更新deviec 状态到本地数据库中'''
    try:
        conn = MySQLdb.connect(host=settings.DATABASE_HOST, user=settings.DATABASE_USER,passwd=settings.DATABASE_PASSWORD,db=settings.DATABASE_NAME)
        cursor = conn.cursor()
        print 'MySql ok'
    except Exception, e:
        print "MySQL Error!"
    
    if settings.DEBUG:
        print 'host id: ', hostid, 'deviceid: ', deviceid, 'device status: ', devicestatus
        
    SqlCmdSel = "select * from device_status where mogid=%d and hostid=%s and devid=%s" % (mogGroupID, hostid, deviceid)
    res = cursor.execute(SqlCmdSel)
    
    if res > 0: #表示存在host,更新即可
        SqlCmd3 = "UPDATE device_status SET status='%s' where mogid=%d and hostid=%d and devid=%s" % \
                  (devicestatus, mogGroupID, int(hostid), deviceid)
    else:
        SqlCmd3 = "INSERT INTO device_status(mogid,hostid,devid,status) values(%d,%d,%d,'%s')" % \
                 (mogGroupID, int(hostid), int(deviceid),devicestatus)
   
    res = cursor.execute(SqlCmd3)
    conn.close() #关闭连接  
    if settings.DEBUG:
        print SqlCmd3 ,res
#-------------------------up site by toontong----------------------------------------------------        
        

        
        
def check_status(trackersip=r'192.168.1.60:6001,192.168.1.86:6001,', mogGroupID='1'):
    '''检测MogileFS系统的trcker,host,device状态'''
    
    mogGroupID = int(mogGroupID)
    print trackersip
    if (len(trackersip) < 4):
	return 1
    command = 'mogadm -trackers=%s check' % trackersip
   
    f = os.popen(command)
    
    line = f.readline()
    if (line == ''):
        return 1
    if (line.find('Checking trackers...') != -1):
        while (True):
            line  = f.readline()
            end = line.find(':')
            if (end == -1):
                break
            trackerip = line[:end]
            start = end + 1
            end = line.find('...')
            trackerport = line[start:end]
            end += 3
            trackerstatus = line[end:]
            if trackerstatus.find('OK') != -1:
                trackerstatus = 'alive'
            else:
                trackerstatus = 'error'
           
            trackerip = trackerip.replace(' ','')
            
            #-------------------------by toontong  update tracker---------------------------------------------------
            update_tracker(trackerip, trackerport, trackerstatus, mogGroupID)
            #-------------------------by toontong----------------------------------------------------------------------
            
    line = f.readline()
    if (line == ''):
        return 0
    if (line.find('Checking hosts...') != -1):
        while (True):
            line = f.readline()
            start = line.find('[')
            if (start == -1):
                break
            end = line.find(']')
            hostid = line[start + 1 : end]
            start = line.find('...')
            start += 3
            hoststatus = line[start:]
            if hoststatus.find('OK') == -1:
                hoststatus = 'error'
            else:
                hoststatus= 'alive'
            print 'host id:', hostid, 'host status:', hoststatus    

            #-------------------------by toontong update host status----------------------------------------------------
            update_host(hostid, hoststatus, mogGroupID)
            #-------------------------by toontong----------------------------------------------------

            
    line = f.readline()
    if (line == ''):
        return 0
    if (line.find('Checking devices...') != -1):
        f.readline()
        f.readline()
        while (True):
            line = f.readline()
            start = line.find('[')
            if (start == -1):
                break
            end = line.find(']')
            hostid = line[start + 1 : end]
            start = line.find('dev')
            start += len('dev')
            end = line.find(' ', start)
            deviceid = line[start : end]
            tail = line[end:]
            if (tail.find('%') == -1):
                devicestatus = 'error'
            else:
                devicestatus = "alive"
            print 'host id: ', hostid, 'deviceid: ', deviceid, 'device status: ', devicestatus

            #-------------------------by toontong update device status----------------------------------------------------
            update_device(hostid, deviceid, devicestatus, mogGroupID)
            #-------------------------by toontong----------------------------------------------------------------------------
                
    
    return 0





#-------------------------by toontong----------------------------------------------------
def update():
    '''更新MogileFS系统的所有工作机器状态到本地数据库
    
       以实现实时更新
    '''
    conn = MySQLdb.connect(host = settings.DATABASE_HOST, user = settings.DATABASE_USER,\
                           passwd = settings.DATABASE_PASSWORD, db = settings.DATABASE_NAME)
    cursor = conn.cursor()
    SqlCmd = "select mID from mogfs_group"
    cursor.execute(SqlCmd)
    MogGroupInfo = cursor.fetchall()
    conn.close() #关闭连接     
    
    for mog in MogGroupInfo:
        conn = MySQLdb.connect(host = settings.DATABASE_HOST, user = settings.DATABASE_USER,\
                           passwd = settings.DATABASE_PASSWORD, db = settings.DATABASE_NAME)
        cursor = conn.cursor()
        SqlCmd = "select trackerIP,trackerPort from trackers where MogGroupID = %s" % mog[0]
        cursor.execute(SqlCmd)
        conn.close() #关闭连接     
        TrackerInfo = cursor.fetchall()
        trackersIP =''
        for trac in TrackerInfo: #此循环用于格式化一组IP与端口
            str = '%s:%s' % (trac[0],trac[1])
            trackersIP += str + ','
            
        check_status(trackersIP, mog[0])
         
    
#-------------------------by toontong----------------------------------------------------

if __name__ == '__main__':
    update()
     
