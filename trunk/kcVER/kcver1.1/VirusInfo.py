# -*- coding: cp936 -*-
from env import *
import sql
import os.path
import re
def reTest(s):
    print '-'*60
    url = re.compile(r'http://\w*')
    print url.match(s)
    print '-'*60
    
def GetInfo(path):
    k=g_dtxt.keys()
    d={}#单词
    for ki in k:
        d[ki]=''
    #print len(k)
#    path = raw_input('file name:')

    bfile = os.path.isfile(path)
    if not bfile:
        print 'not file or not exist'
        return False,d
    bfile = os.path.splitext(path)
    if bfile[1] != '.txt':
        print 'not text file'
        return False,d
    f = open(path,"r")     #文件输入
    lines = f.readlines()
    sum = len(lines)
    if sum < 1:
        return False ,d
    if not lines[0].startswith('病毒英文名称'):
        print lines[0]
        print 'not starts with'
        return False ,d
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
    return (True,d)
if __name__ == '__main__':
    ReadCfg('cfg.txt')
    #path = raw_input('file name:')
    path = 'sample.txt'
    (b,d1)=GetInfo(path)
    if b:   
        print '___________'
        for ki in g_dtxt.keys():
            print (ki+':'+d1[ki]+'\n')
            #reTest(d1[ki])
        print '*'*50

        sret = sql.AddNodeSql(6000,6000,25,0,d1,'')
        print sret
    else:
        print 'error'
    



