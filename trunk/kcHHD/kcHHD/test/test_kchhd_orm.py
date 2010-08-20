#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Name:         test_kchhd_orm.py
# Purpose:      测试数据库读写
#
# Author:       LongChunhua <longchunhua@gmail.com>
#
# Date:         2008-8-21
#----------------------------------------------------------------------------


from webapps.kcHHD.conf import db #数据库连接
from webapps.kcHHD.model import kchhd_orm #被测试模块
#import storm_conf #数据库连接
#import kchhd_orm #被测试模块
from init import * #初始化模块
import unittest

db = db.getStore() #连接数据


    
class kchhd_ormTestCase(unittest.TestCase):#测试kchhd_ormTestCase模块
    def setUp(self):
        #申明并初始化对象
        self.mainTitle = init_maintitle(101)
        self.subTitle = init_subtitle(102)
        self.tableVersion = init_tableversion(103)
        self.question = init_questions(104)
        self.interviewinfo = init_interviewinfo(105)
        self.intervieweeGroup = init_intervieweegroup(106)
        self.resume = init_resumeinfo(107)
        self.userStudent = init_user(111)

        l = [
                self.mainTitle,
                self.subTitle,
                self.tableVersion,
                self.question,
                self.interviewinfo,
                self.intervieweeGroup,
                self.resume,
                self.userStudent,             
            ]
                
        for i in l:
            db.add(i)
        db.commit()


    def tearDown(self):
        db.remove(self.mainTitle)
        db.remove(self.subTitle)
        db.remove(self.tableVersion)
        db.remove(self.question)
        db.remove(self.interviewinfo)
        db.remove(self.intervieweeGroup)
        db.remove(self.resume)
        db.remove(self.userStudent)
        db.commit()



    def testMaintitle(self):#测试Maintitle类
##        db.invalidate(self.mainTitle)
##        #del self.mainTitle
##        import gc
##        collected = gc.collect()
        mainTitleTemp = init_maintitle(101)#实例化一个临时变量，将其与从数据库中读出的数据做比较
        mainTitleOut = db.find(kchhd_orm.Maintitle, kchhd_orm.Maintitle.ID == 101).one()#从数据库中去出刚读入的那条数据。      
        #print mainTitleOut, self.mainTitle
        #这里原来想将mainTitleOut.name与self.mainTitle.Name作比较的，但发现mainTitleOut与self.mainTitle指向同一内存地址，所以只有重新实例化一个临时对象。
        self.assertEqual(mainTitleTemp.Name, mainTitleOut.Name)#将读入数据库后再取出的数据与原数据是否一致
        

##
    def testSubtitle(self):#测试Subtitle类
        subTitleTemp = init_subtitle(102)
        subTitleOut = db.find(kchhd_orm.Subtitle, kchhd_orm.Subtitle.ID == 102).one()
        self.assertEqual(subTitleTemp.Name, subTitleOut.Name)

##
    def testTableversion(self):#测试Tableversion类
        tbVerTemp = init_tableversion(103)
        tbVerOut = db.find(kchhd_orm.Tableversion, kchhd_orm.Tableversion.ID == 103).one()
        self.assertEqual(tbVerTemp.VerNumber, tbVerOut.VerNumber)
        self.assertEqual(tbVerTemp.UsedCounts, tbVerOut.UsedCounts)

##
    def testQuestions(self):#测试Questions类
        questionTemp = init_questions(104)
        questionOut = db.find(kchhd_orm.Questions, kchhd_orm.Questions.ID == 104).one()
        self.assertEqual(questionTemp.Description, questionOut.Description)

    def testInterviewInfo(self):#测试InterviewInfo类
        interviewInfoTemp = init_interviewinfo(105)
        interviewInfoOut = db.find(kchhd_orm.InterviewInfo, kchhd_orm.InterviewInfo.ID == 105).one()
        self.assertEqual(interviewInfoTemp.Addr, interviewInfoOut.Addr)
        self.assertEqual(interviewInfoTemp.DateTime, interviewInfoOut.DateTime)
        self.assertEqual(interviewInfoTemp.Dept, interviewInfoOut.Dept)
        self.assertEqual(interviewInfoTemp.Result, interviewInfoOut.Result)


    def testIntervieweegroup(self):#测试Intervieweegroup类
        intervieweeGroupTemp = init_intervieweegroup(106)
        intervieweeGroupOut = db.find(kchhd_orm.Intervieweegroup, kchhd_orm.Intervieweegroup.ID == 106).one()
        self.assertEqual(intervieweeGroupTemp.Name, intervieweeGroupOut.Name)
        self.assertEqual(intervieweeGroupTemp.Description, intervieweeGroupOut.Description)

        
    def testResumeInfo(self):#测试ResumeInfo类
        resumeTemp = init_resumeinfo(107)
        resumeOut = db.find(kchhd_orm.ResumeInfo, kchhd_orm.ResumeInfo.ID == 107).one()
        self.assertEqual(resumeTemp.CardID, resumeOut.CardID)
        self.assertEqual(resumeTemp.Name, resumeOut.Name)
        self.assertEqual(resumeTemp.Sex, resumeOut.Sex)

        

##        
    def testUser(self):#此时User类
        #声明一个临时对象
        studentTemp = init_user(111)

        studentOut = db.find(kchhd_orm.User, kchhd_orm.User.ID == 111).one()

        self.assertEqual(studentTemp.AccountID, studentOut.AccountID)
        self.assertEqual(studentTemp.Name, studentOut.Name)
        self.assertEqual(studentTemp.Type, studentOut.Type)
        self.assertEqual(studentTemp.Pwd, studentOut.Pwd)
        self.assertEqual(studentTemp.Dept, studentOut.Dept)




        
   
##def suite():
##    suite = unittest.TestSuite()   
##    suite.addTest(unittest.makeSuite(kchhd_ormTestCase, 'test'))
##    
##    return suite
##
##
##def myRun():
##    # 构造测试集
##    suite = unittest.TestSuite()
##    suite.addTest(kchhd_ormTestCase("testMaintitle"))
##    suite.addTest(kchhd_ormTestCase("testSubtitle"))
##    suite.addTest(kchhd_ormTestCase("testTableversion"))
##    suite.addTest(kchhd_ormTestCase("testQuestions"))
##    suite.addTest(kchhd_ormTestCase("testInterviewInfo"))
##    suite.addTest(kchhd_ormTestCase("testIntervieweegroup"))
##    suite.addTest(kchhd_ormTestCase("testResumeInfo"))
##    suite.addTest(kchhd_ormTestCase("testUser"))
##
##    
##    
##    # 执行测试
##    runner = unittest.TextTestRunner()
##    runner.run(suite)
##
##    
##if __name__ == '__main__':
##    unittest.main()#执行suite()函数
##    myRun()#用myRun()函数执行测试,执行后不会要求你关闭窗口
