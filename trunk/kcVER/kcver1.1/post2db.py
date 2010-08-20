# -*- coding: cp936 -*-
import wx
import MySQLdb
import sql
import VirusInfo
import md5
from env import *
import time
import os.path
import tword
def test(myapp):
    myapp.load.SetLabel('hahahha')
    pass
    

def CheckUser(user,pwd):
    #for k,v in g_ddb.items():
    #    print k+':'+v
    try:
        #conn = MySQLdb.connect(user="ivirus",passwd="ivirus",host="192.168.1.51",db="ivirus",charset="utf8")
        #conn = MySQLdb.connect(user="ivirus",passwd="ivirus",host="kcpy.kc.kingsoft.net",db="ivirus",charset="utf8")
        #conn = MySQLdb.connect(user="root",passwd="123456",host="localhost",db="test1",charset="utf8")
        conn = MySQLdb.connect(user=g_ddb['user'],passwd=g_ddb['passwd'],host=g_ddb['host'],db=g_ddb['db'],charset="utf8")
    except:
        print "Could not connect to MySQL server."
    cursor = conn.cursor()
    q="select `uid`,`pass` from `users` where `name`='%s'"%(user)
    cursor.execute(q)
    row = cursor.fetchone()
    if row == None:
        return -1
    if md5.md5(pwd).hexdigest() == row[1]:
        return row[0]
    else:
        return -1
    conn.close();
    
def TokenTerms(word):
    sword = word.strip()
    if sword == '':
        return []
    li=sword.split(',')
    li=list(set(li))
    return li
#返回 id
def QueryTerm(term,cursor):
    q='select tid from term_data where name = %s'
    #q = unicode(q,'cp936')
    term = unicode(term ,'cp936')
    cursor.execute(q,term)
    row = cursor.fetchone()
    if row == None:
        return None
    return row[0]
def QueryTitle(title,cursor):
    q='select nid from node where title = %s'
    #title = unicode(title ,'cp936')
    cursor.execute(q,title)
    row = cursor.fetchone()
    if row == None:
        return None
    return row[0]
def QueryField(cursor,table,obj,name,index):
    q="select `%s` from `%s` where `%s` = '%s'" %(obj,table,name,index)
    cursor.execute(q)
    row = cursor.fetchone()
    if row == None:
        return None
    return row[0]
    pass

def PostList(li,uid,myapp,time2quit):
    try:
        conn = MySQLdb.connect(user=g_ddb['user'],passwd=g_ddb['passwd'],host=g_ddb['host'],db=g_ddb['db'],charset="utf8")
    except:
        myapp.fail.AppendText('Could not connect to MySQL server.')
    cursor = conn.cursor()
    
    sumli = len(li)
    sumfail = 0
    #init
    #myapp.process.SetRange(sumli)
    #myapp.process.SetValue(0)
    #myapp.labproc.SetLabel('0 / %d'%(sumli))
    #myapp.succ.SetValue('')
    #myapp.fail.SetValue('')
    #init

    wx.CallAfter(myapp.SetRange,sumli)
    wx.CallAfter(myapp.SetValue,0)
    wx.CallAfter(myapp.SetLabel,'0 / %d'%(sumli))
    wx.CallAfter(myapp.SetText,True,'')
    wx.CallAfter(myapp.SetText,False,'')
    
    for item in li:
        #
        #myapp.labproc.SetLabel('%d / %d %s'%(li.index(item)+1,len(li),os.path.basename(item)))
        #
        sl=('%d / %d %s'%(li.index(item)+1,len(li),os.path.basename(item)))
        wx.CallAfter(myapp.SetLabel,sl)
        time2quit.wait(0.01)
        s=PostFile(item,cursor,uid)
        #
        #myapp.process.SetValue(li.index(item)+1)
        #
        wx.CallAfter(myapp.SetValue,li.index(item)+1)
        s1=unicode(s,'cp936')
        if '录入失败'in s:
            #
            #myapp.fail.AppendText(item + ':'+s1+'\n')
            #
            wx.CallAfter(myapp.AppendText,False,(item + ':'+s1+'\n'))
            sumfail +=1
        else:
            #
            #myapp.succ.AppendText(item + ':'+s1+ '\n')
            #
            wx.CallAfter(myapp.AppendText,True,(item + ':'+s1+'\n'))
    #
    #myapp.succ.AppendText('*******************\n成功录入: %d / %d\n'%(sumli - sumfail , sumli))
    #myapp.fail.AppendText('*******************\n录入失败: %d / %d\n'%(sumfail , sumli))
    wx.CallAfter(myapp.AppendText,True,('*******************\n成功录入: %d / %d\n'%(sumli - sumfail , sumli)))
    wx.CallAfter(myapp.AppendText,False,('*******************\n录入失败: %d / %d\n'%(sumfail , sumli)))

    conn.close();
    pass
def UpdateNode(uid,dinfo,cursor):
    #var_nid,var_vid,var_uid,var_time,dinfo,platformtxt
    var_uid = int(uid)
    var_nid=QueryField(cursor,'sequences','id','name','node_nid')
    var_vid=QueryField(cursor,'sequences','id','name','node_revisions_vid')
    var_nid=int(var_nid)+1
    var_vid=int(var_vid)+1
    #print 'vid=' , var_vid
    #print 'nid=' , var_nid
    platformtxt = QueryField(cursor,'node_field','global_settings','field_name','field_platform')
    platformtxt = platformtxt.encode('cp936')
    #"""SELECT `global_settings` FROM `node_field` WHERE `field_name` = 'field_platform'"""
    var_time=int(time.time())
    q=sql.AddNodeSql(var_nid,var_vid,var_uid,var_time,dinfo,platformtxt)
    q = unicode(q,'cp936')
    li =q.split(';')
    for query in li:
        pass
        #print '[ node ',li.index(query),']',query
        cursor.execute(query)#encode

        #print query
        pass
    #print '*'*30,'node','*'*30
    return var_nid
    pass

def UpdateTerm(keywords,nid,cursor):
    tid0=int(QueryField(cursor,'sequences','id','name','term_data_tid'))
    tid=tid0
    lisql=[]
    #print 'term keywords len = ', len(keywords)
    for word in keywords:
        r=QueryTerm(word,cursor)
        if r == None:
            tid+=1
            lisql.append("INSERT INTO `term_data` (`tid`,`vid`,`name`,`weight`) VALUES ('%s','1','%s','0')"%(tid,word))
            lisql.append("insert into `url_alias` (`src`,`dst`) values ('taxonomy/term/%s','%s%s.html')"%(tid,tword.Word2URL(word),tid))
            r=tid
        lisql.append("INSERT INTO `term_node` (`nid`,`tid`) VALUES ('%s','%s')"%(nid,r))
    if tid !=tid0:
        lisql.append("UPDATE `sequences` SET `id`='%s' WHERE `name`='term_data_tid'"%(tid))
    i =0;
    for q in lisql:
        q1 = unicode(q,'cp936')
        i+=1
        #print '[term ',i,']:',q1
        cursor.execute(q1)
        #print '[term ',lisql.index(q),']:',q1
    #print '$'*30,'term','$'*30
    pass
def PostFile(path,cursor,uid):
    #getinfo
    #0:query title
    #sql two part(1)node(2)term
    #0直接由文件名获取,1.由dtxt的结果
    bret , dtxt=VirusInfo.GetInfo(path)
    if not bret:
        return '录入失败,文件格式错误'
    title=dtxt[g_dsql['var_title']]
    r=QueryTitle(title,cursor)
    if r!= None:
        return '录入失败,病毒档案已存在'
    nid=UpdateNode(uid,dtxt,cursor)
    keywords=TokenTerms(dtxt[g_dsql['var_term']])
    #print 'key[0]=['+keywords[0]+']'
    UpdateTerm(keywords,nid,cursor)
    return ('成功录入,nid=%d'%(nid))
    #return nid
def PostTxt(path):
    try:
        #conn = MySQLdb.connect(user="ivirus",passwd="ivirus",host="192.168.1.51",db="ivirus",charset="utf8")
        #conn = MySQLdb.connect(user="ivirus",passwd="ivirus",host="kcpy.kc.kingsoft.net",db="ivirus",charset="utf8")
        #conn = MySQLdb.connect(user="root",passwd="123456",host="localhost",db="test1",charset="utf8")
        conn = MySQLdb.connect(user=dbcon['user'],passwd=dbcon['passwd'],host=dbcon['host'],db=dbcon['db'],charset="utf8")
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
