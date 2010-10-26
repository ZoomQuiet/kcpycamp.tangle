import unittest
from kchhd_orm import*
import storm_conf

DB = storm_conf.getStore()
class RelationTestCase(unittest.TestCase):
    def setUp(self):
        self.user_1 = DB.add(User(1,u"user_1",u"user_1",u"user_1",u"user_1",u"user_1"))
        self.user_2 = DB.add(User(2,u"user_2",u"user_2",u"user_2",u"user_2",u"user_2"))        
        self.interviewInfo_1 = DB.add(InterviewInfo(1,1,u"interviewInfo_1",
            u"interviewInfo_1",1,u"interviewInfo_1",u"interviewInfo_1",1,1))       
        self.interviewInfo_2 = DB.add(InterviewInfo(2,2,u"interviewInfo_2",
            u"interviewInfo_2",2,u"interviewInfo_2",u"interviewInfo_2",2,2))
    def tearDown(self):
        DB.remove(self.user_1)
        DB.remove(self.user_2)
        DB.remove(self.interviewInfo_1)
        DB.remove(self.interviewInfo_2)
        DB.commit()
    def testRelationship(self):
        '''test one-to-many '''
        self.user_1.interviewee_interviewInfos.add(self.interviewInfo_1)
        self.user_1.interviewee_interviewInfos.add(self.interviewInfo_2)
        assert self.user_1.interviewee_interviewInfos.count() == 2, 'incorrect count'
        
'''
class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User(1,u"test",u"test",u"test",u"test",u"test")
        DB.add(self.user)
    def tearDown(self):
        DB.remove(self.user)
        DB.commit()
    def testDefaultValue(self):
        assert self.user.ID == 1 , 'incorrect default ID'
        assert self.user.AccountID == u"test" , 'incorrect default AccountID'
        assert self.user.Name == u"test" , 'incorrect default Name'
        assert self.user.Type == u"test" , 'incorrect default Type'
        assert self.user.Pwd == u"test" , 'incorrect default Pwd'
        assert self.user.Dept == u"test" , 'incorrect default Dept'
    def testDBValue(self):
        self.user.ID = 123
        self.user.AccountID = u"DBtest"
        self.user.Name = u"DBtest"
        self.user.Type = u"DBtest"
        self.user.Pwd = u"DBtest"
        self.user.Dept = u"DBtest"
        DB.commit()
        assert DB.find(User,User.ID == 123).one(), "wrong ID after evaluate"
        assert DB.find(User,User.AccountID == u"DBtest").one(), "wrong AccountID after evaluate"
        assert DB.find(User,User.Name == u"DBtest").one(), "wrong Name after evaluate"
        assert DB.find(User,User.Type == u"DBtest").one(), "wrong Type after evaluate"
        assert DB.find(User,User.Pwd == u"DBtest").one(), "wrong Pwd after evaluate"
        assert DB.find(User,User.Dept == u"DBtest").one(), "wrong Dept after evaluate"
      
class InterviewInfoTestCase(unittest.TestCase):
    def setUp(self):
        self.interviewInfo = InterviewInfo(1,1,u"test",u"test",1,u"test",u"test",1,1)
        DB.add(self.interviewInfo)        
    def tearDown(self):
        DB.remove(self.interviewInfo)
        DB.commit()       
    def testDefaultValue(self):
        assert self.interviewInfo.ID == 1 , 'incorrect default ID'
        assert self.interviewInfo.TableVerID == 1 , 'incorrect default TableVerID'
        assert self.interviewInfo.Result == u"test" , 'incorrect default Result'
        assert self.interviewInfo.Addr == u"test" , 'incorrect `default Addr'
        assert self.interviewInfo.Times == 1 , 'incorrect default Times'
        assert self.interviewInfo.DateTime == u"test" , 'incorrect default DateTime'
        assert self.interviewInfo.Dept == u"test" , 'incorrect default Dept'
        assert self.interviewInfo.IsOvertime == 1 , 'incorrect default IsOvertime'
        assert self.interviewInfo.IntervieweeID == 1 , 'incorrect default IntervieweeID'

    def testDBValue(self):
        self.interviewInfo.ID = 123
        #DB.commit()

        self.interviewInfo.TableVerID = 123
        self.interviewInfo.Result = u"DBtest"
        self.interviewInfo.Addr = u"DBtest"
        self.interviewInfo.Times = 123
        self.interviewInfo.DateTime = u"DBtest"
        self.interviewInfo.Dept = u"DBtest"
        self.interviewInfo.IntervieweeID = 123
        
        DB.commit()0
        '''
        #assert DB.find(InterviewInfo,InterviewInfo.ID == 123).one(), "wrong ID after evaluate"
        '''
        assert DB.find(InterviewInfo,InterviewInfo.TableVerID == 123).one(), "wrong TableVerID after evaluate"
        assert DB.find(InterviewInfo,InterviewInfo.Result == u"DBtest").one(), "wrong Result after evaluate"
        assert DB.find(InterviewInfo,InterviewInfo.Addr == u"DBtest").one(), "wrong Addr after evaluate"
        assert DB.find(InterviewInfo,InterviewInfo.Times == 123).one(), "wrong Times after evaluate"
        assert DB.find(InterviewInfo,InterviewInfo.DateTime == u"DBtest").one(), "wrong DateTime after evaluate"
        #assert DB.find(User,interviewInfo.Dept == u"DBtest").one(), "wrong Dept after evaluate"
        assert DB.find(InterviewInfo,InterviewInfo.IntervieweeID == 123).one(), "wrong IntervieweeID after evaluate"


   ''' 
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(RelationTestCase,'test'))
    #suite.addTest(unittest.makeSuite(UserTestCase,'test'))
    #suite.addTest(unittest.makeSuite(InterviewInfoTestCase,'test'))
    return suite
if __name__ == '__main__':
    unittest.main()