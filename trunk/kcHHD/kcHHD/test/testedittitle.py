#!/usr/bin/env python
#coding=utf-8
#coding=gbk
#RESPONSE['Content-Type'] = "text/html; charset=utf-8"
#----------------------------------------------------------------------------
# Name:         testedittitle.py
# Purpose:      测试Title模块
# Author:       chenhuayong  
# Date:         2008-8-25
#----------------------------------------------------------------------------

import unittest
from webapps.kcHHD.test.testedittitleData import TestData
from webapps.kcHHD.control.edittitle import Title
#插入标题测试类
class InsettitleTestCase(unittest.TestCase):
    def setUp(self):
        mt = '[+]'
        st = '[-]'
        self.testData = TestData(mt,st,'teststr')
        self.Title = Title(mt,st)
        self.testinfo = ''
    def tearDown(self):
        pass
    def testStrToList(self):
        self.testData.updateStrToListData()
        for item in self.testData.testDataList:#对StrToList进行测试
            titlestr,resultList, self.testinfo = item
            self.Title.setTitleStr(titlestr)
            assert self.Title.strToList() == resultList ,\
             '\nInfo =%s\nTestStr=%s\nRealResult=%s\nTestResult=%s'\
            %(self.testinfo,titlestr,self.Title.strToList(),resultList)
    def testListToStr(self):
        self.testData.updateListToStrData()
        for item in self.testData.testDataList:
            titleList,resultStr, self.testinfo = item
            self.Title.setTitleList(titleList)
            assert self.Title.listToStr() == resultStr ,\
            '\nInfo =%s\nTestList=%s\nRealResult=%s\nTestResult=%s'\
            %(self.testinfo,titleList,self.Title.listToStr(),resultStr)
        
#if __name__ == "__main__":
#    suite = unittest.TestSuite()
#    suite.addTest(InsettitleTestCase("testStrToList"))
#    suite.addTest(InsettitleTestCase("testListToStr"))
#    
#    runner = unittest.TextTestRunner()
#    runner.run(suite)

