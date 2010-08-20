#判断串s中是否以字典dk中的key开头
def HasKey(s, dk):
    for kk in dk:
        if s.startswith(kk):
            return True
    return False

#解析串s中的字段名和值并存入字典dk中
def Token(s,dk):
    a=s.split(':',1)
    if a[0] in dk:
        dk[a[0]]=a[1].strip()

#配置信息应从文件读取
conf={'病毒英文名称':'field_enname_value','病毒长度':'','威胁级别':'field_level_value',\
      '关键词':'','影响系统':'',\
      '病毒类型':'field_category_value','感染途径':'','病毒简介':'',\
      '行为分析':'field_remark_value'}

#for k,v in conf.items():
#    print k,v
k=conf.keys()
#kkk=['病毒英文名称','病毒长度','威胁级别','关键词','影响系统',\
#  '病毒类型','感染途径','病毒简介','行为分析']
d={}#单词
for ki in k:
    d[ki]=''
print len(k)
f = open("sample.txt","r")     #文件输入
lines = f.readlines()
sum = len(lines)
temp=''
for i in range(sum):
    temp+=lines[i]
    if i+1<sum and HasKey(lines[i+1],d):
        Token(temp,d)
        temp=''
print temp
temp+=lines[sum-1]
Token(temp,d)

f.close()

#插入记录SQL串
#insert into virus1 (field_enname_value ,field_level_value,\
#field_category_value,field_remark_value)values('name','***','class','test');

#拼接SQL串
sk="("#field_enname_value
sv="("#name
for i in k :
    if conf[i]!="":
        sk+=conf[i]
        sk+=" ,"
        
        sv+="'"
        sv+=d[i]
        sv+="'"
        sv+=","
sk=sk[0:len(sk)-1]
sv=sv[0:len(sv)-1]
sk+=")"
sv+=")"
print '*************'
print sk
print sv
#insert into virus1 (field_enname_value ,field_level_value,\
#field_category_value,field_remark_value)values('name','***','class','test');
strsql="insert into virus1 "
strsql+=sk
strsql+="values"
strsql+=sv

print "---------------------SQL串---------------------"
print strsql
print "---------------------SQL串---------------------"

#连接数据库
import MySQLdb
try:
   conn = MySQLdb.connect(user="ivirus",passwd="ivirus",host="kcpy.kc.kingsoft.net",db="ivirus")
except:
   print "Could not connect to MySQL server."
cursor = conn.cursor()
#插入记录
cursor.execute(strsql)
#查询表
strsql = "select * from virus1"
cursor.execute(strsql)

for row in cursor.fetchall():
    print "\n----------------------record:", row[0],"--------------------------"
    print row[4],'\t|',row[1],'\t|',row[2] 
    print row[3],
    print "\n______________________record:", row[0],"_____________________________"
   
