#!/usr/bin/env python
# -*- coding: utf-8 -*-
#RESPONSE['Content-Type'] = "text/html; charset=utf-8"
from webapps.kcHHD.model.kchhd_orm import *
from webapps.kcHHD.conf.db import *
import random
class Title():
    def __init__(self,mt,st):#设置mt标记符，和st标记符
        self.mtSign = mt  
        self.stSign = st
        self.titleStr=''
        self.titleList=[]
    def setTitleList(self,tList):#设置列表
        self.titleList = tList
    def setTitleStr(self,str):   #设置字符串
        self.titleStr = str
    def strToList(self):         #字符串转换成为list
        mtNum = self.titleStr.count(self.mtSign)
        stNum = self.titleStr.count(self.stSign)
        if mtNum == 0 and stNum != 0:#没有mt标记只有st标记的情况
            self.titleList = self.titleStr.split(self.stSign)
            self.titleList.pop(0)
            self.titleList.insert(0,'')
            self.titleList=[self.titleList]
        elif mtNum != 0 and stNum == 0:#只有mt标记而没有st标记的情况
            self.titleList = self.titleStr.split(self.mtSign)
            self.titleList.pop(0)
            self.titleList = [[tt] for tt in self.titleList]
        elif mtNum != 0 and stNum != 0:#既有mt又有st的情况
            if self.titleStr.find(self.mtSign) < self.titleStr.find(self.stSign): #第一个出现的tt标记为mt标记
                self.titleList = self.titleStr.split(self.mtSign)
                self.titleList.pop(0)
                self.titleList = [tt.split(self.stSign) for tt in self.titleList]
            else:                #第一个出现的tt标记为st标记
                self.titleList = self.titleStr.split(self.mtSign)
                self.titleList = [tt.split(self.stSign) for tt in self.titleList]
                self.titleList[0][0]=''
        elif self.titleStr != '':#当输入框没有出现标记的且不框中内容不为空情况
            self.titleList = [[self.titleStr]]
        elif self.titleStr =='':                    #输入框为空
            pass
        self.titleList=[[st.strip() for st in tt] for tt in self.titleList]#过滤前置后置空格或回车符
        return self.titleList
    def listToStr(self):         #list转换成为字符串
        if len(self.titleList) != 0:
            self.titleList = [('\n'+self.stSign).join(tt)+'\n' for tt in self.titleList]
            self.titleStr =  self.mtSign + self.mtSign.join(self.titleList)
        else:
            self.titleStr = ''
       
        return self.titleStr
    def printTT(self):
        print '|||%s'%self.titleList
        print '|||str=%s'%self.titleStr
class TitleDataControl():
    def __init__(self):
        self.store = getStore()
        self.store.rollback()
        self.upDataTitleList()
        
    def upDataTitleList(self):
        self.titleList = []
        mainttiles = self.store.find(Maintitle)
        for mt in mainttiles:
            if mt.subtitles.count() > 0:
                tempList = []
                for st in mt.subtitles:
                    tempList.append((st.ID,st.Name))
                tempList.insert(0,(mt.ID,mt.Name))
                self.titleList.append(tempList)
    def add(self,mtStr,stStr):
        mtStr = unicode(mtStr, 'utf-8')
        stStr = unicode(stStr, 'utf-8')
        STID = random.randrange(1000, 9999)
        MTID = random.randrange(1000, 9999)
        mt = self.store.find(Maintitle,Maintitle.Name == mtStr).one()
        if mt == None:
            mt = self.store.add(Maintitle(MTID, mtStr))
            mt.subtitles.add(Subtitle(STID, stStr))
        else:
            mt.subtitles.add(Subtitle(STID, stStr))
        self.store.commit()
    def edit(self,mtStr,stStr,stID):
        mtStr = mtStr.decode('utf-8')
        stStr = stStr.decode('utf-8')
        stID = int(stID)
        mt = self.store.find(Maintitle, Maintitle.Name == mtStr).one()
        st = self.store.get(Subtitle, stID)
        if mt == None:
            st.maintitle.Name = mtStr
            st.Name = stStr
        elif mt.Name != st.maintitle.Name:
            self.store.find(Subtitle, Subtitle.MainTitleID == st.MainTitleID).set(MainTitleID = mt.ID)
            st.Name = stStr
        else:
            st.Name = stStr
        self.store.commit()
    def remove(self,stID):
        stID = int(stID)
        self.store.remove(self.store.get(Subtitle,stID))
        self.store.commit()
    def removeAll(self):
        sunbtitles = self.store.find(Subtitle)
        for st in sunbtitles:
            self.store.remove(st)
        self.store.commit()
    def printTitle(self):
        self.store.rollback()
        print self.titleList
