# -*- coding: cp936 -*-
import post2db,MySQLdb,env,VirusInfo,time,sql
#test
try:
    #conn = MySQLdb.connect(user="ivirus",passwd="ivirus",host="192.168.1.51",db="ivirus",charset="utf8")
    #conn = MySQLdb.connect(user="ivirus",passwd="ivirus",host="kcpy.kc.kingsoft.net",db="ivirus",charset="utf8")
    conn = MySQLdb.connect(user="root",passwd="123456",host="localhost",db="test1",charset="utf8")
    #conn = MySQLdb.connect(user=dbcon['user'],passwd=dbcon['passwd'],host=dbcon['host'],db=dbcon['db'],charset="utf8")
except:
    print "Could not connect to MySQL server."
cursor = conn.cursor()
if 1:
    id=post2db.QueryTerm('六合彩广告',cursor)
    print id
    id=post2db.QueryTitle('Exploit.JPEG',cursor)
    print id
    id = post2db.QueryField(cursor,'sequences','id','name','term_data_tid')
    print id , `id`
    #conn.close()
    "select id from sequences  where `name` ='term_data_tid'"
env.ReadCfg('cfg.txt')
dinfo=VirusInfo.GetInfo('sample.txt')
if 0:
    var_uid=3
    q=post2db.UpdateNode(var_uid,dinfo,cursor)
    print '*'*30,'SQL','*'*30
    print q
    print '*'*30,'SQL','*'*30
if 0:
    var_nid=post2db.QueryField(cursor,'sequences','id','name','node_revisions_vid')
    var_vid=post2db.QueryField(cursor,'sequences','id','name','term_data_tid')
    platformtxt = post2db.QueryField(cursor,'node_field','global_settings','field_name','field_platform')
    platformtxt=platformtxt.encode('cp936')
if 0:
    platformtxt=""""a:4:{s:15:"text_processing";s:1:"0";s:10:"max_length";s:3:"100";s:14:"allowed_values";s:614:"Win9x WinNT 
    Win9x
    未打GDI+漏洞补丁
    未打MS04-028补丁的英文版WinXP SP1
    Win9x Win2000 WinXP
    Win9x WinNT Win2000 WinXP Win2003 
    Win9x Win2000 WinXP Win2003
    DOS
    DOS Win3.1
    Win9x WinNT Win2000 WinXP
    WinNT Win2000 WinXP Win2003
    Win2000 WinXP
    Win32
    WinNT Win2000
    Win2000 WinXP Win2003
    Win9x Win2000
    Win9x WinMe WinNT Win2000 Win2003
    Win9x WinMe WinNT Win2000 WinXP Win2003
    Win9x WinMe WinNT Win2000 WinXP
    Win9x WinNT Win2000
    Win9x WinMe Win2000 WinXP
    Win98
    Win9x WinMe
    Win9x WinMe Win2000
    Win9x WinXP
    WinNT Win2000 WinXP
    WinNT
    Win9x WinNT Win2000 Unix Linux
    其它
    WinXP Win2003";s:18:"allowed_values_php";s:0:"";}"""
    var_time=int(time.time())
    print var_nid,var_vid,platformtxt,var_time
    var_uid=15555
    q=sql.AddNodeSql(var_nid,var_vid,var_uid,var_time,dinfo,platformtxt)
print '*'*30
s='Worm21,ge1,zs1,zs2'
keys=post2db.TokenTerms(s)
nid = 2005
post2db.UpdateTerm(keys,nid,cursor)

