#!/usr/bin/env python
#coding=utf-8
# coding=gbk
#RESPONSE['Content-Type'] = "text/html; charset=utf-8"
class TestData():
    def __init__(self,mtstr, ststr, teststr):
        self.mt = mtstr
        self.st = ststr
        self.teststr = teststr.strip()
        self.mtstr = 'mt'+ self.teststr
        self.testDataList=[]
    def add(self,setdata,result,testinfo):
        self.testDataList.append((setdata,result,testinfo))
    def updateStrToListData(self):
        self.testDataList=[]
    #空值情况
        self.add('',[],'empty')
    #没有mt和st只有字符串的
        self.add(self.mtstr, [[self.mtstr]], 'only str')
    #只有一个mt
        self.add(self.mt + self.mtstr, [[self.mtstr]], 'only mt')
    #有多个mt
        self.add(self.mt + self.mtstr + self.mt + self.mtstr, [[self.mtstr], [self.mtstr]], 'many mt')
    #只有一个st
        self.add(self.st + self.teststr, [['', self.teststr]],'one st')
    #有多个st
        self.add(self.st + self.teststr + self.st + self.teststr, [['', self.teststr, self.teststr]],'many st')
    #有mt又有st的情况------------------
     #第一个出现的tt为mt且只有一个st和mt
        self.add(self.mt + self.mtstr + self.st + self.teststr, [[self.mtstr, self.teststr]],'one mt st,begin mt ')
     #第一个出现的tt为mt 多个mt，st
        #结束标记为st
        self.add(self.mt + self.mtstr + self.st + self.teststr + self.mt + self.mtstr + self.st + self.teststr, \
        [[self.mtstr, self.teststr], [self.mtstr, self.teststr]],'many mt st,begin mt end st')
        #结束标记为mt
        self.add(self.mt + self.mtstr + self.st + self.teststr + self.st + self.teststr + self.mt + self.mtstr,\
        [[self.mtstr, self.teststr, self.teststr], [self.mtstr]],'many mt st,begin mt end mt')
     #第一个出现的tt为st只有一个st和mt
        self.add(self.st + self.teststr + self.mt + self.mtstr, [['',self.teststr],[self.mtstr]],'one mt st,begin st')
     #第一个出现的tt为st 多个mt，st
        #结束标记为mt
        self.add(self.st + self.teststr + self.mt + self.mtstr + self.st + self.teststr + self.mt + self.mtstr,\
        [['',self.teststr], [self.mtstr,self.teststr], [self.mtstr]],'many mt st,begin st end mt')
    #第一个出现的tt为st 多个mt，st
       #结束标记为st
        self.add(self.st + self.teststr + self.mt + self.mtstr + self.mt + self.mtstr + self.st + self.teststr,\
        [['',self.teststr], [self.mtstr], [self.mtstr,self.teststr]],'many mt st,begin st end st')
    def updateListToStrData(self):
        self.testDataList=[]
        #空值情况
        self.add([],'','empty')
        #只有一个mt
        self.add([[self.mtstr,self.teststr]],self.mt + self.mtstr + self.st + self.teststr, 'one mt one st')
        #只有一个mt多个st
        self.add([[self.mtstr,self.teststr,self.teststr]],\
        self.mt + self.mtstr + self.st + self.teststr + self.st + self.teststr, 'one mt many st')
        #有多个mt,st
        self.add([[self.mtstr,self.teststr],[self.mtstr,self.teststr]],\
        self.mt + self.mtstr + self.st + self.teststr + self.mt + self.mtstr + self.st + self.teststr, 'many mt one st')
        
        self.add([[self.mtstr,self.teststr,self.teststr],[self.mtstr,self.teststr,self.teststr]],\
        self.mt + self.mtstr + self.st + self.teststr + self.st + self.teststr + self.mt + self.mtstr + self.st + self.teststr + self.st + self.teststr, 'many mt may st')

    