from django.db import connection
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
