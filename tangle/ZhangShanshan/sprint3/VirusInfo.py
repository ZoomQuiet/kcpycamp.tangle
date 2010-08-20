# -*- coding: cp936 -*-
from env import *
import sql
def GetInfo(path):
    k=g_dtxt.keys()
    d={}#单词
    for ki in k:
        d[ki]=''
    #print len(k)
#    path = raw_input('file name:')
    f = open(path,"r")     #文件输入
    lines = f.readlines()
    sum = len(lines)
    temp=''
    for i in range(sum):
        temp+=lines[i]
        if i+1<sum and HasKey(lines[i+1],d):
            Token(temp,d)
            temp=''
    #print temp
    temp+=lines[sum-1]
    Token(temp,d)
    f.close()
    return d
if __name__ == '__main__':
    ReadCfg('cfg.txt')
    d1=GetInfo('sample.txt')
    print '___________'
    for ki in g_dtxt.keys():
        #pass
        print (ki+':'+d1[ki]+'\n')
    print '------------TestSQL---------------------'
    ssql=sql.MakeSql(200,200,1110,d1)
    print ssql
    print '================SQLSQLSQL==============='
    



