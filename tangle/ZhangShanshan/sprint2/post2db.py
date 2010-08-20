# -*- coding: cp936 -*-
import MySQLdb
import sql
import VirusInfo
from env import dbcon
def PostTxt(path):
    try:
        conn = MySQLdb.connect(user="ivirus",passwd="ivirus",host="192.168.1.51",db="ivirus",charset="utf8")
        conn = MySQLdb.connect(user="ivirus",passwd="ivirus",host="kcpy.kc.kingsoft.net",db="ivirus",charset="utf8")
        #conn = MySQLdb.connect(user="root",passwd="123456",host="localhost",db="test1",charset="utf8")
        #conn = MySQLdb.connect(user=dbcon['user'],passwd=dbcon['passwd'],host=dbcon['host'],db=dbcon['db'],charset="utf8")
    except:
        print "Could not connect to MySQL server."
    cursor = conn.cursor()
    
    query="select id from sequences  where `name` ='node_nid'"
    cursor.execute(query)
    for row in cursor.fetchall():
        pass
        #print row[0]
    nid=int(row[0])
    query="select id from sequences  where `name` ='node_revisions_vid'"
    cursor.execute(query)
    for row in cursor.fetchall():
        pass
        #print row[0]
    vid=int(row[0])
    query="select id from sequences  where `name` ='term_data_tid'"
    cursor.execute(query)
    for row in cursor.fetchall():
        pass
        #print row[0]
    tid=int(row[0])
#    print nid,tid,vid

    for p in path:
        nid +=1
        tid +=1
        vid +=1
        d=VirusInfo.GetInfo(p)
        query = sql.MakeSql(nid,vid,tid,d)
        query = unicode(query,'cp936')
        qli = query.split(';')
        #print '--------------'
        #print query
        #print '--------------'
        #conn.begin()
        for q in qli:
            try:
                cursor.execute(q)
            except Exception, e:
                print 'error:',e
        print 'done: ',p,'\t',path.index(p)+1,'/',len(path)
    conn.close()
