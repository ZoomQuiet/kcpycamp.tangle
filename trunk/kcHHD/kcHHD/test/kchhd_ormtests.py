import unittest
from webapps.kcHHD.model.kchhd_orm import*
from webapps.kcHHD.test.init import*
from webapps.kcHHD.conf.db import *

DB = getStore()

IDlist = [320,321,322,323,324,325,326,327,328,329]

class UserInterviewInfoRelationTestCase(unittest.TestCase):
    def setUp(self):
        '''check ID Used'''
        for id in IDlist:
            if DB.find(User,User.ID == id).one():
                raise 'UserID %s is existed'%id

        '''create object'''            
        self.user_1 = init_user(IDlist[1])
        DB.add(self.user_1)
        self.user_2 = init_user(IDlist[2])
        DB.add(self.user_2)
        
        '''check ID Used'''
        for id in IDlist:
            if DB.find(InterviewInfo,InterviewInfo.ID == id).one():
                raise 'InterviewInfoID %s is existed'%id
            
        '''create object''' 
        self.interviewInfo_1 = init_interviewinfo(IDlist[1])
        DB.add(self.interviewInfo_1)
        self.interviewInfo_2 = init_interviewinfo(IDlist[2])
        DB.add(self.interviewInfo_2)

        DB.commit()

        '''build one-to-many relationship'''
        self.user_1.interviewee_interviewInfos.add(self.interviewInfo_1)
        self.user_1.interviewee_interviewInfos.add(self.interviewInfo_2)
        DB.commit()
        
        '''build many-to-many relationship'''
        self.user_1.interviewer_interviewInfos.add(self.interviewInfo_1)
        self.user_1.interviewer_interviewInfos.add(self.interviewInfo_2)
        self.interviewInfo_1.interviewers.add(self.user_2)
        self.interviewInfo_2.interviewers.add(self.user_2)
        DB.commit()
        
    def tearDown(self):
        
        '''remove one-to-many relationship'''
        self.user_1.interviewee_interviewInfos.remove(self.interviewInfo_1)
        self.user_1.interviewee_interviewInfos.remove(self.interviewInfo_2)
        DB.commit()
        
        '''remove many-to-many relationship'''
        self.user_1.interviewer_interviewInfos.remove(self.interviewInfo_1)
        self.user_1.interviewer_interviewInfos.remove(self.interviewInfo_2)
        self.interviewInfo_1.interviewers.remove(self.user_2)
        self.interviewInfo_2.interviewers.remove(self.user_2)
        DB.commit()
        
        '''remove object'''
        DB.remove(self.user_1)
        DB.remove(self.user_2)
        DB.remove(self.interviewInfo_1)
        DB.remove(self.interviewInfo_2)
        DB.commit()
    def testRelationship(self):
        '''test one-to-many'''
        u_1 = DB.get(User,IDlist[1])
        i_1 = DB.get(InterviewInfo,IDlist[1])
        i_2 = DB.get(InterviewInfo,IDlist[2])
        assert u_1.interviewee_interviewInfos.count() == 2 , 'incorrect count many-to-one user_1'
        assert i_1.interviewee is self.user_1 , 'incorrect  interviewInfo_1 many-to-one user_1'
        assert i_2.interviewee is self.user_1 , 'incorrect  interviewInfo_2 many-to-one user_1'
        
        
        '''test many-to-many'''
        i_1 = DB.get(InterviewInfo,IDlist[1])
        i_2 = DB.get(InterviewInfo,IDlist[2])
        u_1 = DB.get(User,IDlist[1])
        u_2 = DB.get(User,IDlist[2])       
        assert u_1.interviewer_interviewInfos.count() == 2 , 'incorrect count many-to-many user_1'
        assert u_2.interviewer_interviewInfos.count() == 2 , 'incorrect count many-to-many user_2'
        assert i_1.interviewers.count() == 2 , 'incorrect count many-to-many interviewInfo_1'
        assert i_2.interviewers.count() == 2 , 'incorrect count many-to-many interviewInfo_2'
        assert u_1.interviewer_interviewInfos.find(InterviewInfo,InterviewInfo.ID == IDlist[1]) ,\
               'incorrect  user_1 many-to-many InterviewInfo_1'
        assert u_1.interviewer_interviewInfos.find(InterviewInfo,InterviewInfo.ID == IDlist[2]) ,\
               'incorrect  user_1 many-to-many InterviewInfo_2'
        assert u_2.interviewer_interviewInfos.find(InterviewInfo,InterviewInfo.ID == IDlist[1]) ,\
               'incorrect  user_2 many-to-many InterviewInfo_1'
        assert u_2.interviewer_interviewInfos.find(InterviewInfo,InterviewInfo.ID == IDlist[2]) ,\
               'incorrect  user_2 many-to-many InterviewInfo_2'
        assert i_1.interviewers.find(User,User.ID == IDlist[1]) ,\
               'incorrect  interviewInfos_1 many-to-many User_1'
        assert i_1.interviewers.find(User,User.ID == IDlist[2]) ,\
               'incorrect  interviewInfos_1 many-to-many User_2'
        assert i_2.interviewers.find(User,User.ID == IDlist[1]) ,\
               'incorrect  interviewInfos_2 many-to-many User_1'
        assert i_2.interviewers.find(User,User.ID == IDlist[2]) ,\
               'incorrect  interviewInfos_2 many-to-many User_2' 

class QuestionsInterviewInfoRelationTestCase(unittest.TestCase):
    def setUp(self):
        '''check ID Used'''
        for id in IDlist:
            if DB.find(Questions,Questions.ID == id).one():
                raise 'QuestionsID %s is existed'%id

        '''create object'''            
        self.questions_1 = init_questions(IDlist[3])
        DB.add(self.questions_1)
        self.questions_2 = init_questions(IDlist[4])
        DB.add(self.questions_2)
        
        '''check ID Used'''
        for id in IDlist:
            if DB.find(InterviewInfo,InterviewInfo.ID == id).one():
                raise 'InterviewInfoID %s is existed'%id
            
        '''create object''' 
        self.interviewInfo_1 = init_interviewinfo(IDlist[3])
        DB.add(self.interviewInfo_1)
        self.interviewInfo_2 = init_interviewinfo(IDlist[4])
        DB.add(self.interviewInfo_2)

        DB.commit()
        
        '''build many-to-many relationship'''
        self.questions_1.interviewInfos.add(self.interviewInfo_1)
        self.questions_1.interviewInfos.add(self.interviewInfo_2)
        self.interviewInfo_1.questions.add(self.questions_2)
        self.interviewInfo_2.questions.add(self.questions_2)
        DB.commit()
        
    def tearDown(self):
               
        '''remove many-to-many relationship'''
        self.questions_1.interviewInfos.remove(self.interviewInfo_1)
        self.questions_1.interviewInfos.remove(self.interviewInfo_2)
        self.interviewInfo_1.questions.remove(self.questions_2)
        self.interviewInfo_2.questions.remove(self.questions_2)
        DB.commit()
        
        '''remove object'''
        DB.remove(self.questions_1)
        DB.remove(self.questions_2)
        DB.remove(self.interviewInfo_1)
        DB.remove(self.interviewInfo_2)
        DB.commit()
    def testRelationship(self):      
        
        '''test many-to-many'''
        i_1 = DB.get(InterviewInfo,IDlist[3])
        i_2 = DB.get(InterviewInfo,IDlist[4])
        q_1 = DB.get(Questions,IDlist[3])
        q_2 = DB.get(Questions,IDlist[4])       
        assert q_1.interviewInfos.count() == 2 , 'incorrect count many-to-many questions_1'
        assert q_2.interviewInfos.count() == 2 , 'incorrect count many-to-many questions_2'
        assert i_1.questions.count() == 2 , 'incorrect count many-to-many interviewInfo_1'
        assert i_2.questions.count() == 2 , 'incorrect count many-to-many interviewInfo_2'
        
        assert q_1.interviewInfos.find(InterviewInfo,InterviewInfo.ID == IDlist[3]) ,\
               'incorrect  questions_1 many-to-many InterviewInfo_1'
        assert q_1.interviewInfos.find(InterviewInfo,InterviewInfo.ID == IDlist[4]) ,\
               'incorrect  questions_1 many-to-many InterviewInfo_2'
        assert q_2.interviewInfos.find(InterviewInfo,InterviewInfo.ID == IDlist[3]) ,\
               'incorrect  questions_2 many-to-many InterviewInfo_1'
        assert q_2.interviewInfos.find(InterviewInfo,InterviewInfo.ID == IDlist[4]) ,\
               'incorrect  questions_2 many-to-many InterviewInfo_2'
        assert i_1.questions.find(Questions,Questions.ID == IDlist[3]) ,\
               'incorrect  interviewInfos_1 many-to-many questions_1'
        assert i_1.questions.find(Questions,Questions.ID == IDlist[4]) ,\
               'incorrect  interviewInfos_1 many-to-many questions_2'
        assert i_2.questions.find(Questions,Questions.ID == IDlist[3]) ,\
               'incorrect  interviewInfos_2 many-to-many questions_1' 
        assert i_2.questions.find(Questions,Questions.ID == IDlist[4]) ,\
               'incorrect  interviewInfos_2 many-to-many questions_2'

class TableversionSubtitleRelationTestCase(unittest.TestCase):
    def setUp(self):
        '''check ID Used'''
        for id in IDlist:
            if DB.find(Tableversion,Tableversion.ID == id).one():
                raise 'TableversionID %s is existed'%id

        '''create object'''            
        self.tableversion_1 = init_tableversion(IDlist[5])
        DB.add(self.tableversion_1)
        self.tableversion_2 = init_tableversion(IDlist[6])
        DB.add(self.tableversion_2)
        
        '''check ID Used'''
        for id in IDlist:
            if DB.find(Subtitle,Subtitle.ID == id).one():
                raise 'SubtitleID %s is existed'%id
            
        '''create object''' 
        self.subtitle_1 = init_subtitle(IDlist[5])
        DB.add(self.subtitle_1)
        self.subtitle_2 = init_subtitle(IDlist[6])
        DB.add(self.subtitle_2)

        DB.commit()
        
        '''build many-to-many relationship'''
        self.tableversion_1.subtitles.add(self.subtitle_1)
        self.tableversion_1.subtitles.add(self.subtitle_2)
        self.subtitle_1.tableversions.add(self.tableversion_2)
        self.subtitle_2.tableversions.add(self.tableversion_2)
        DB.commit()
        
    def tearDown(self):
               
        '''remove many-to-many relationship'''
        self.tableversion_1.subtitles.remove(self.subtitle_1)
        self.tableversion_1.subtitles.remove(self.subtitle_2)
        self.subtitle_1.tableversions.remove(self.tableversion_2)
        self.subtitle_2.tableversions.remove(self.tableversion_2)
        DB.commit()
        
        '''remove object'''
        DB.remove(self.tableversion_1)
        DB.remove(self.tableversion_2)
        DB.remove(self.subtitle_1)
        DB.remove(self.subtitle_2)
        DB.commit()
    def testRelationship(self):      
        
        '''test many-to-many'''
        t_1 = DB.get(Tableversion,IDlist[5])
        t_2 = DB.get(Tableversion,IDlist[6])
        s_1 = DB.get(Subtitle,IDlist[5])
        s_2 = DB.get(Subtitle,IDlist[6])       
        assert t_1.subtitles.count() == 2 , 'incorrect count many-to-many tableversion_1'
        assert t_2.subtitles.count() == 2 , 'incorrect count many-to-many tableversion_2'
        assert s_1.tableversions.count() == 2 , 'incorrect count many-to-many subtitle_1'
        assert s_2.tableversions.count() == 2 , 'incorrect count many-to-many subtitle_2'
        
        assert t_1.subtitles.find(Subtitle,Subtitle.ID == IDlist[5]) ,\
               'incorrect  tableversion_1 many-to-many subtitle_1'
        assert t_1.subtitles.find(Subtitle,Subtitle.ID == IDlist[6]) ,\
               'incorrect  tableversion_1 many-to-many subtitle_2'
        assert t_2.subtitles.find(Subtitle,Subtitle.ID == IDlist[5]) ,\
               'incorrect  tableversion_2 many-to-many subtitle_1'
        assert t_2.subtitles.find(Subtitle,Subtitle.ID == IDlist[6]) ,\
               'incorrect  tableversion_2 many-to-many subtitle_2'
        assert s_1.tableversions.find(Tableversion,Tableversion.ID == IDlist[5]) ,\
               'incorrect  subtitle_1 many-to-many tableversion_1'
        assert s_1.tableversions.find(Tableversion,Tableversion.ID == IDlist[6]) ,\
               'incorrect  subtitle_1 many-to-many tableversion_2'
        assert s_2.tableversions.find(Tableversion,Tableversion.ID == IDlist[5]) ,\
               'incorrect  subtitle_2 many-to-many tableversion_1' 
        assert s_2.tableversions.find(Tableversion,Tableversion.ID == IDlist[6]) ,\
               'incorrect  subtitle_2 many-to-many tableversion_2'


class ResumeInfoIntervieweegroupRelationTestCase(unittest.TestCase):
    def setUp(self):
        '''check ID Used'''
        for id in IDlist:
            if DB.find(Intervieweegroup,Intervieweegroup.ID == id).one():
                raise 'IntervieweegroupID %s is existed'%id

        '''create object'''            
        self.intervieweegroup_1 = init_intervieweegroup(IDlist[7])
        DB.add(self.intervieweegroup_1)
        self.intervieweegroup_2 = init_intervieweegroup(IDlist[8])
        DB.add(self.intervieweegroup_2)
        
        '''check ID Used'''
        for id in IDlist:
            if DB.find(ResumeInfo,ResumeInfo.ID == id).one():
                raise 'ResumeInfoID %s is existed'%id
            
        '''create object''' 
        self.resumeinfo_1 = init_resumeinfo(IDlist[7])
        DB.add(self.resumeinfo_1)
        self.resumeinfo_2 = init_resumeinfo(IDlist[8])
        DB.add(self.resumeinfo_2)

        DB.commit()
        
        '''build many-to-many relationship'''
        self.intervieweegroup_1.resumeInfos.add(self.resumeinfo_1)
        self.intervieweegroup_1.resumeInfos.add(self.resumeinfo_2)
        self.resumeinfo_1.intervieweegroups.add(self.intervieweegroup_2)
        self.resumeinfo_2.intervieweegroups.add(self.intervieweegroup_2)
        DB.commit()
        
    def tearDown(self):
               
        '''remove many-to-many relationship'''
        self.intervieweegroup_1.resumeInfos.remove(self.resumeinfo_1)
        self.intervieweegroup_1.resumeInfos.remove(self.resumeinfo_2)
        self.resumeinfo_1.intervieweegroups.remove(self.intervieweegroup_2)
        self.resumeinfo_2.intervieweegroups.remove(self.intervieweegroup_2)
        DB.commit()
        
        '''remove object'''
        DB.remove(self.intervieweegroup_1)
        DB.remove(self.intervieweegroup_2)
        DB.remove(self.resumeinfo_1)
        DB.remove(self.resumeinfo_2)
        DB.commit()
    def testRelationship(self):      
        
        '''test many-to-many'''
        g_1 = DB.get(Intervieweegroup,IDlist[7])
        g_2 = DB.get(Intervieweegroup,IDlist[8])
        r_1 = DB.get(ResumeInfo,IDlist[7])
        r_2 = DB.get(ResumeInfo,IDlist[8])       
        assert g_1.resumeInfos.count() == 2 , 'incorrect count many-to-many intervieweegroup_1'
        assert g_2.resumeInfos.count() == 2 , 'incorrect count many-to-many intervieweegroup_2'
        assert r_1.intervieweegroups.count() == 2 , 'incorrect count many-to-many resumeinfo_1'
        assert r_2.intervieweegroups.count() == 2 , 'incorrect count many-to-many resumeinfo_2'
        
        assert g_1.resumeInfos.find(ResumeInfo,ResumeInfo.ID == IDlist[7]) ,\
               'incorrect  intervieweegroup_1 many-to-many resumeinfo_1'
        assert g_1.resumeInfos.find(ResumeInfo,ResumeInfo.ID == IDlist[8]) ,\
               'incorrect  intervieweegroup_1 many-to-many resumeinfo_2'
        assert g_2.resumeInfos.find(ResumeInfo,ResumeInfo.ID == IDlist[7]) ,\
               'incorrect  intervieweegroup_2 many-to-many resumeinfo_1'
        assert g_2.resumeInfos.find(ResumeInfo,ResumeInfo.ID == IDlist[8]) ,\
               'incorrect  intervieweegroup_2 many-to-many resumeinfo_2'
        assert r_1.intervieweegroups.find(Intervieweegroup,Intervieweegroup.ID == IDlist[7]) ,\
               'incorrect  resumeinfo_1 many-to-many intervieweegroup_1'
        assert r_1.intervieweegroups.find(Intervieweegroup,Intervieweegroup.ID == IDlist[8]) ,\
               'incorrect  resumeinfo_1 many-to-many intervieweegroup_2'
        assert r_2.intervieweegroups.find(Intervieweegroup,Intervieweegroup.ID == IDlist[7]) ,\
               'incorrect  resumeinfo_2 many-to-many intervieweegroup_1' 
        assert r_2.intervieweegroups.find(Intervieweegroup,Intervieweegroup.ID == IDlist[8]) ,\
               'incorrect  resumeinfo_2 many-to-many intervieweegroup_2'

class MaintitleSubtitleRelationTestCase(unittest.TestCase):
    def setUp(self):
        '''check ID Used'''
        for id in IDlist:
            if DB.find(Maintitle,Maintitle.ID == id).one():
                raise 'MaintitleID %s is existed'%id

        '''create object'''            
        self.maintitle = init_maintitle(IDlist[1])
        DB.add(self.maintitle)
        
        '''check ID Used'''
        for id in IDlist:
            if DB.find(Subtitle,Subtitle.ID == id).one():
                raise 'SubtitleID %s is existed'%id
            
        '''create object''' 
        self.subtitle_1 = init_subtitle(IDlist[1])
        DB.add(self.subtitle_1)
        self.subtitle_2 = init_subtitle(IDlist[2])
        DB.add(self.subtitle_2)

        DB.commit()

        '''build one-to-many relationship'''
        self.maintitle.subtitles.add(self.subtitle_1)
        self.maintitle.subtitles.add(self.subtitle_2)
        DB.commit()

    def tearDown(self):
        
        '''remove one-to-many relationship'''
        self.maintitle.subtitles.remove(self.subtitle_1)
        self.maintitle.subtitles.remove(self.subtitle_2)
        DB.commit()
               
        '''remove object'''
        DB.remove(self.maintitle)
        DB.remove(self.subtitle_1)
        DB.remove(self.subtitle_2)
        DB.commit()

    def testRelationship(self):
        '''test one-to-many'''
        m_1 = DB.get(Maintitle,IDlist[1])
        s_1 = DB.get(Subtitle,IDlist[1])
        s_2 = DB.get(Subtitle,IDlist[2])
        assert m_1.subtitles.count() == 2 , 'incorrect count many-to-one maintitle'
        assert s_1.maintitle is self.maintitle , 'incorrect  subtitle_1 many-to-one maintitle'
        assert s_2.maintitle is self.maintitle , 'incorrect  subtitle_2 many-to-one maintitle'


class TableversionInterviewInfoRelationTestCase(unittest.TestCase):
    def setUp(self):
        '''check ID Used'''
        for id in IDlist:
            if DB.find(Tableversion,Tableversion.ID == id).one():
                raise 'TableversionID %s is existed'%id

        '''create object'''            
        self.tableversion = init_tableversion(IDlist[1])
        DB.add(self.tableversion)
        
        '''check ID Used'''
        for id in IDlist:
            if DB.find(InterviewInfo,InterviewInfo.ID == id).one():
                raise 'InterviewInfoID %s is existed'%id
            
        '''create object''' 
        self.interviewInfo_1 = init_interviewinfo(IDlist[1])
        DB.add(self.interviewInfo_1)
        self.interviewInfo_2 = init_interviewinfo(IDlist[2])
        DB.add(self.interviewInfo_2)

        DB.commit()

        '''build one-to-many relationship'''
        self.tableversion.interviewInfos.add(self.interviewInfo_1)
        self.tableversion.interviewInfos.add(self.interviewInfo_2)
        DB.commit()
                
    def tearDown(self):
        
        '''remove one-to-many relationship'''
        self.tableversion.interviewInfos.remove(self.interviewInfo_1)
        self.tableversion.interviewInfos.remove(self.interviewInfo_2)
        DB.commit()      
        
        '''remove object'''
        DB.remove(self.tableversion)
        DB.remove(self.interviewInfo_1)
        DB.remove(self.interviewInfo_2)
        DB.commit()
    def testRelationship(self):
        '''test one-to-many'''
        t_1 = DB.get(Tableversion,IDlist[1])
        i_1 = DB.get(InterviewInfo,IDlist[1])
        i_2 = DB.get(InterviewInfo,IDlist[2])
        assert t_1.interviewInfos.count() == 2 , 'incorrect count many-to-one tableversion'
        assert i_1.tableversion is self.tableversion , 'incorrect  interviewInfo_1 many-to-one tableversion'
        assert i_2.tableversion is self.tableversion , 'incorrect  interviewInfo_2 many-to-one tableversion'    

       
def suite():
                                                    
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(UserInterviewInfoRelationTestCase,'test'))
    suite.addTest(unittest.makeSuite(QuestionsInterviewInfoRelationTestCase,'test'))
    suite.addTest(unittest.makeSuite(TableversionSubtitleRelationTestCase,'test'))
    suite.addTest(unittest.makeSuite(ResumeInfoIntervieweegroupRelationTestCase,'test'))
    suite.addTest(unittest.makeSuite(MaintitleSubtitleRelationTestCase,'test'))
    suite.addTest(unittest.makeSuite(TableversionInterviewInfoRelationTestCase,'test'))
    
    return suite
                                                    
if __name__ == '__main__':
    unittest.main()