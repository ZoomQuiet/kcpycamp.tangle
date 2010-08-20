# Add a tracker
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Context
from django.db import connection
from admin_exist import AdminExists

# Main Process of add tracker
def AddTracker(request):
    if not AdminExists(request):
        return render_to_response('messages.html',{'msg':'请先登录', 'url':'../login'})

    trackerIP = request.POST.get('trackerIP', None)
    trackerPort = request.POST.get('trackerPort', None)
    mogGroupID = request.POST.get('mogGroup', None)

    res = {}

    if trackerIP and trackerPort and mogGroupID:

        bRes = True

        # For IP
        if not TestIP(trackerIP):
            res['WrongIP'] = 'WrongIP'
            bRes = False
        else:
            if not Add(trackerIP, trackerPort, mogGroupID):
                bRes = False
        
        # For Port
        if bRes:
            if trackerPort.__len__() <= 4:
                for ch in trackerPort:
                    if not ch.isdigit():
                        bRes = False
                        break
                if bRes:
                    res['AddOk'] = 'AddOk'
                else:
                    res['WrongPort'] = 'WrongPort'
            else:
                res['WrongPort'] = 'WrongPort'
        
    else:
        res['Empty'] = 'Empty'

    connect = connection.cursor()
    
    # all mog's name
    mogGroups= ()
    sql = "select * from mogfs_group"
    connect.execute(sql)
    mogGroups = connect.fetchall()
    res['mogGroups'] = mogGroups

    # all currnet trackers
    allTrackers = ()
    sql = "select * from trackers"
    connect.execute(sql)
    allTrackers = connect.fetchall()
    res['allTrackers'] = allTrackers
        
    connect.close()
    
    context = Context(res)
    return render_to_response('addtracker.html', context)

# Function for add
def Add(trackerIP, trackerPort, mogGroupID):
    connect = connection.cursor()
    
    sql = "insert into trackers (MogGroupID, trackerIP, trackerPort) values (%s,%s,%s)"
    param = (mogGroupID, trackerIP, trackerPort)
    connect.execute(sql, param)
        
    connect.close()

    return True

# Test IP
def TestIP(trackerIP):
    if trackerIP.__len__() > 15 or trackerIP.__len__() < 7:
        return False
    else:
        dota = 0
        gap = 0
        for ch in trackerIP:
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


# Get all mogGroups' name (for choice)
def GetMogGroup(mogGroups):
    connect = connection.cursor()
    sql = "select mName from mogfs_group"
    connect.execute(sql)
    mogGroups = connect.fetchall()
    

# Get all Trackers that exists
def GetAllTracker(allTrackers):
    connect = connection.cursor()
    sql = "select * from trackers"
    connect.execute(sql)
    allTrackers = connect.fetchall()
        
    
if __name__ == '__main__':
    AddTracker()   
