#-*- coding: utf-8 -*-
#coding = utf-8
dfield={}#字段字典
dsql={}#sql
ddb={}#dbconf
f = open ('config.txt')
i =0
for line in f.readlines():
    line=line.strip()
    i+=1
#   l =len(line)
    if ':' in line :
        s=line.split(':')
        dsql[s[0]]=s[1]
    elif '=' in line:
        s=line.split('=')
        ddb[s[0]]=s[1]
#   print i,line.strip(),(s[1]=='')
#    dfield[s[0]]=''
    

if 1:
    for k,v in dsql.items():
        print k,v
    print '------'
    for k,v in ddb.items():
        print k,v
f.close()
f=open('env.py')
lines = f.readlines()
for i in range(len(lines)):
    if lines[i].startswith('conf ='):
        print lines[i]
        lines[i] ='conf ='+`dsql`+'\n'
        sss=''+repr(dsql)
        print sss
        print lines[i]
    elif lines[i].startswith('dbcon ='):
        lines[i] ='dbcon ='+`ddb`+'\n'
for line in lines:
    print line
f.close()
f1 = open ('env.py','w')
for i in range (len(lines)):
    f1.write (lines[i])
f1.close()

