#�жϴ�s���Ƿ����ֵ�dk�е�key��ͷ
def HasKey(s, dk):
    for kk in dk:
        if s.startswith(kk):
            return True
    return False

#������s�е��ֶ�����ֵ�������ֵ�dk��
def Token(s,dk):
    a=s.split(':',1)
    if a[0] in dk:
        dk[a[0]]=a[1].strip()

#������ϢӦ���ļ���ȡ
conf={'����Ӣ������':'field_enname_value','��������':'','��в����':'field_level_value',\
      '�ؼ���':'','Ӱ��ϵͳ':'',\
      '��������':'field_category_value','��Ⱦ;��':'','�������':'',\
      '��Ϊ����':'field_remark_value'}

#for k,v in conf.items():
#    print k,v
k=conf.keys()
#kkk=['����Ӣ������','��������','��в����','�ؼ���','Ӱ��ϵͳ',\
#  '��������','��Ⱦ;��','�������','��Ϊ����']
d={}#����
for ki in k:
    d[ki]=''
print len(k)
f = open("sample.txt","r")     #�ļ�����
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

#�����¼SQL��
#insert into virus1 (field_enname_value ,field_level_value,\
#field_category_value,field_remark_value)values('name','***','class','test');

#ƴ��SQL��
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

print "---------------------SQL��---------------------"
print strsql
print "---------------------SQL��---------------------"

#�������ݿ�
import MySQLdb
try:
   conn = MySQLdb.connect(user="ivirus",passwd="ivirus",host="kcpy.kc.kingsoft.net",db="ivirus")
except:
   print "Could not connect to MySQL server."
cursor = conn.cursor()
#�����¼
cursor.execute(strsql)
#��ѯ��
strsql = "select * from virus1"
cursor.execute(strsql)

for row in cursor.fetchall():
    print "\n----------------------record:", row[0],"--------------------------"
    print row[4],'\t|',row[1],'\t|',row[2] 
    print row[3],
    print "\n______________________record:", row[0],"_____________________________"
   
