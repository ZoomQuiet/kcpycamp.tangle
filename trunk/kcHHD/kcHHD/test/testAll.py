#coding=utf-8
import unittest
from webapps.kcHHD.test.testedittitle import *
from webapps.kcHHD.test.kchhd_ormtests import *
from webapps.kcHHD.test.test_kchhd_orm import *

if __name__ == "__main__":
    
    suite = unittest.TestSuite()
#--kchhd_ormtests 
    suite.addTest(unittest.makeSuite(UserInterviewInfoRelationTestCase,'test'))
    suite.addTest(unittest.makeSuite(QuestionsInterviewInfoRelationTestCase,'test'))
    suite.addTest(unittest.makeSuite(TableversionSubtitleRelationTestCase,'test'))
    suite.addTest(unittest.makeSuite(ResumeInfoIntervieweegroupRelationTestCase,'test'))
    suite.addTest(unittest.makeSuite(MaintitleSubtitleRelationTestCase,'test'))
    suite.addTest(unittest.makeSuite(TableversionInterviewInfoRelationTestCase,'test'))

#--testedittitle
    suite.addTest(InsettitleTestCase("testStrToList"))
    suite.addTest(InsettitleTestCase("testListToStr"))

#--kchhd_ormtests
    suite.addTest(kchhd_ormTestCase("testMaintitle"))
    suite.addTest(kchhd_ormTestCase("testSubtitle"))
    suite.addTest(kchhd_ormTestCase("testTableversion"))
    suite.addTest(kchhd_ormTestCase("testQuestions"))
    suite.addTest(kchhd_ormTestCase("testInterviewInfo"))
    suite.addTest(kchhd_ormTestCase("testIntervieweegroup"))
    suite.addTest(kchhd_ormTestCase("testResumeInfo"))
    suite.addTest(kchhd_ormTestCase("testUser"))

#run 
    runner = unittest.TextTestRunner()
    runner.run(suite)
