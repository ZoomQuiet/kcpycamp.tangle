#coding: utf-8	
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.db import connection
from django.template import Context
import MySQLdb
from admin_exist import AdminExists

'''
　首页index.html对应脚本
'''

def GetMogGroup():
    '''查询数据库，得到组群的数据库信息'''
    connect = connection.cursor()
    sql = "select * from mogfs_group"
    connect.execute(sql)
    MogGroupInfo = connect.fetchall()
    connect.close()
    return MogGroupInfo
         
    
def GetMGroupTrackerNumber(nGroupID):
    '''计算组群的tracker的数量'''
    connect = connection.cursor()
    sql = "select count(trackerID) from trackers where MogGroupID = %s" % nGroupID
    connect.execute(sql)
    TrackerNumber= connect.fetchall()
    connect.close()
    return TrackerNumber[0]


def index(request):
    '''index.htnl页面入口
    
        返回系统中所有组群的基本信息到idnex.html页面中
    '''
    if not AdminExists(request):
        return render_to_response('messages.html',{'msg':'请先登录', 'url':'../login'})
        
        
    mogGroupsList = [
     #{'ID':'2', 'name':'mog2', 'Tracker':'3', 'Host':'11', 'Dev':'44', \
     #'Domain':'5', 'Class':'10', 'State':'正常'}
    ]
   
    GroupsInfo = GetMogGroup()
    if  GroupsInfo == False:
        return render_to_response('index.html')
  
    for info in GroupsInfo:
        mog1 = {'State':'alive'} # 默认状态正常
        mog1['ID'] = info[0]     # 组群ID
        mog1['name'] = info[1]   #名称
        mog1['Tracker'] = ('%d' % GetMGroupTrackerNumber(mog1['ID'])) #Trackrer数量
        try:
            conn = MySQLdb.connect(host=info[2], user=info[4],passwd=info[5],db=info[3])
            cursor = conn.cursor()
            cursor.execute("select hostid,status from host")
        except Exception, e:
            msg = ("组群 %s,连接数据库 IP=%s db=%s user=%s, psw = ***出错!请删除组群再添加!") % \
                   (info[1],info[2],info[3],info[4])
            return render_to_response('messages.html',{'msg':msg, 'url':"../addmogilefs"})
            
        Hosts = cursor.fetchall()
        mog1['Host'] = Hosts.__len__() #host数量
        for host in Hosts:
            if  host[1] != 'alive':
                mog1['State'] = ('host %s' % host[1])
                break
                
        for host in Hosts:
            cursor.execute("select devid,status from device where hostid = %s" % host[0])
            Devs = cursor.fetchall()
            mog1['Dev'] = ('%d' % Devs.__len__()) #设备 Dev数量
            for dev in Devs:
                if dev[1] != 'alive':
                    mog1['State'] += ('dev %s' % dev[1])
                    break
            cursor.execute("select count(dmid) from domain")
            domain = cursor.fetchall()
            mog1['Domain'] = ('%d' % domain[0]) #domain数量
            cursor.execute("select count(classid) from class")
            cls = cursor.fetchall()
            mog1['Class'] = ('%s' % cls[0]) #class 数量
        
        conn.close()
        mogGroupsList.append(mog1)

    return render_to_response('index.html',{'mogGroups':mogGroupsList})


if __name__ == '__main__': #8.模块入口
   index()

