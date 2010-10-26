from storm.locals import *


"""one DBtable to one class"""


class Maintitle(object):
    __storm_table__ = 'maintitle'
    ID = Int(primary = True)
    Name = Unicode()

#    def __init__(self, ID = 0,Name = u""):
#        self.ID = ID
#        self.Name = Name



class Subtitle(Storm):
    __storm_table__ = 'subtitle'
    ID = Int(primary = True)
    Name = Unicode()
    MainTitleID = Int()

#    def __init__(self, ID = 0, Name = u"", MainTitleID = 0):
#        self.ID = ID
#        self.Name = Name
#        self.MainTitleID = MainTitleID



class Tableversion(Storm):
    __storm_table__ = 'tableversion'
    ID = Int(primary = True)
    UsedCounts = Int()
    VerNumber = Int()
    
#    def __init__(self, UsedCounts = 0, VerNumber = 0):
#        self.UsedCounts = UsedCounts
#        self.VerNumber = VerNumber
    


class SubtitleTableversion(Storm):
    __storm_table__ = 'subtitle_tableversion_relation'
    __storm_primary__ = "SubTitleID", "TableVerID"
    SubTitleID = Int()
    TableVerID = Int()
#    def __init__(self, SubTitleID = 0, TableVerID = 0):
#        self.SubTitleID = SubTitleID
#        self.TableVerID = TableVerID



class Intervieweegroup(Storm):
    __storm_table__ = 'intervieweegroup'
    ID = Int(primary = True)
    Name = Unicode()
    Description = Unicode()

#    def __init__(self, ID = 0,Name = u"", Description = u""):
#        self.ID = ID
#        self.Name = Name
#        self.Description = Description


class ResumeInfo(Storm):
    __storm_table__ = 'resumeinfo'
    ID = Int(primary = True)
    CardID = Unicode()
    Name = Unicode()
    Sex = Unicode()
    School = Unicode()
    Subject = Unicode()
    Grade = Unicode()
    Telephone = Unicode()
    Native = Unicode()
    Addr = Unicode()
    AddrPhone = Unicode()
    Email = Unicode()
    QQ = Unicode()
    ForeignLanguage = Unicode()
    Character = Unicode()
    Programming = Unicode()
    MathAndPhysics = Unicode()
    Scholarships = Unicode()
    Project = Unicode()
    SchoolDuty = Unicode()
    MoreInfo = Unicode()
    Advice = Unicode()
    ResumePath = Unicode()
    PhotoPath = Unicode()
    UserID = Int()

#    def __init__(self, ID = 0, CardID = u"", Name = u"", Sex = u"", School = u"",
#                 Subject = u"", Grade = u"", Telephone = u"", Native = u"", Addr = u"",
#                 AddrPhone = u"", Email = u"", QQ = u"", ForeignLanguage = u"",
#                 Character = u"", Programming = u"", MathAndPhysics = u"", Scholarships = u"",
#                 Project = u"", SchoolDuty = u"", MoreInfo = u"", Advice = u"",
#                 ResumePath = u"", PhotoPath = u"", UserID = 0):
#        self.ID = ID
#        self.CardID = CardID
#        self.Name = Name
#        self.Sex = Sex
#        self.School = School
#        self.Subject = Subject
#        self.Grade = Grade
#        self.Telephone = Telephone
#        self.Native = Native
#        self.Addr = Addr
#        self.AddrPhone = AddrPhone
#        self.Email = Email
#        self.QQ = QQ
#        self.ForeignLanguage = ForeignLanguage
#        self.Character = Character
#        self.Programming = Programming
#        self.MathAndPhysics = MathAndPhysics
#        self.Scholarships = Scholarships
#        self.Project = Project
#        self.SchoolDuty = SchoolDuty
#        self.MoreInfo = MoreInfo
#        self.Advice = Advice
#        self.ResumePath = ResumePath
#        self.PhotoPath = PhotoPath
#        self.UserID = UserID



class IntervieweegroupResumeInfo(object):
    __storm_table__ = 'intervieweegroup_resumeInfo_relation'
    __storm_primary__ = "GroupID", "ResumeID"
    GroupID = Int()
    ResumeID = Int()
#    def __init__(self, GroupID = 0, ResumeID = 0):
#        self.GroupID = GroupID
#        self.ResumeID = ResumeID



class User(Storm):
    __storm_table__ = 'user'
    ID = Int(primary = True)
    AccountID = Unicode()
    Name = Unicode()
    Type = Unicode()
    Pwd = Unicode()
    Dept = Unicode()
    
#    def __init__(self, ID = 0, Name = u"", Type = u"", Pwd = u"",
#                 AccountID = u"", Dept = u""):
#        self.ID = ID
#        self.AccountID = AccountID
#        self.Name = Name
#        self.Type = Type
#        self.Pwd = Pwd
#        self.Dept = Dept


class InterviewInfo(Storm):
    __storm_table__ = 'interviewinfo'
    ID = Int(primary = True)
    Times = Int()
    Addr = Unicode()
    DateTime = Unicode()
    Dept = Unicode()
    IsInterviewed = Unicode()
    Result = Unicode()
    TableVerID = Int()
    IntervieweeID = Int()

#    def __init__(self, ID = 0, TableVerID = 0, Result = u"", Addr = u"",
#                 Times = 0, DateTime = u"", IntervieweeID = u""):
#        self.ID = ID
#        self.TableVerID = TableVerID
#        self.Result = Result
#        self.Addr = Addr
#        self.Times = Times
#        self.DateTime = DateTime
#        self.IntervieweeID = IntervieweeID
    
    
class InterviewerInterviewInfo(Storm):
    __storm_table__ = 'interviewer_interviewInfo_relation'
    __storm_primary__ = "InterviewInfoID", "InterviewerID"
    InterviewInfoID = Int()
    InterviewerID = Int()
#    def __init__(self, InterviewInfoID = 0, InterviewerID = 0):
#        self.InterviewInfoID = InterviewInfoID
#        self.InterviewerID = InterviewerID


      
class Questions(Storm):
    __storm_table__ = 'questions'
    ID = Int(primary = True)
    Description = Unicode()

#    def __init__(self, ID = 0, Description = u""):
#        self.ID = ID
#        self.Description = Description    

       


class QuestionInterviewInfo(Storm):
    __storm_table__ = 'question_interviewInfo_relation'
    __storm_primary__ = "QuestionsID", "InterviewID"
    QuestionsID = Int()
    InterviewID = Int()
    Answer = Unicode()
#    def __init__(self, QuestionsID = 0, InterviewID = 0, Answer = u""):
#        self.QuestionsID = QuestionsID
#        self.InterviewID = InterviewID
#        self.Answer = Answer







"""Many-to-one reference sets"""

#User.interviewee_interviewInfos = ReferenceSet(User.ID,InterviewInfo.ID)

#Maintitle.subtitles = ReferenceSet(Maintitle.ID,Subtitle.ID)
Subtitle.MainTitleName = ReferenceSet(Subtitle.MainTitleID, Maintitle.ID)

#Tableversion.interviewInfos = ReferenceSet(Tableversion.ID,InterviewInfo.ID)
SubtitleTableversion.SubTitleName = ReferenceSet(SubtitleTableversion.SubTitleID,
                                                 Subtitle.ID)
SubtitleTableversion.TableVer = ReferenceSet(SubtitleTableversion.TableVerID,
                                             Tableversion.ID)
###-------------------
ResumeInfo.interviewee = Reference(ResumeInfo.UserID,
                                   User.ID)
IntervieweegroupResumeInfo.Group = ReferenceSet(IntervieweegroupResumeInfo.GroupID,
                                                Intervieweegroup.ID)
IntervieweegroupResumeInfo.Resume = ReferenceSet(IntervieweegroupResumeInfo.ResumeID,
                                                 ResumeInfo.ID)
InterviewInfo.Interviewee = ReferenceSet(InterviewInfo.IntervieweeID,
                                         User.ID)
InterviewInfo.TableVer = ReferenceSet(InterviewInfo.TableVerID,
                                      Tableversion.ID)
InterviewerInterviewInfo.InterviewInfo = ReferenceSet(InterviewerInterviewInfo.InterviewInfoID,
                                                      InterviewInfo.ID)
InterviewerInterviewInfo.InterviewerID = ReferenceSet(InterviewerInterviewInfo.InterviewerID,
                                                      User.ID)
QuestionInterviewInfo.Interview = ReferenceSet(QuestionInterviewInfo.InterviewID,
                                               InterviewInfo.ID)
QuestionInterviewInfo.Question = ReferenceSet(QuestionInterviewInfo.QuestionsID,
                                             Questions.ID)

###---------------------
"""Many-to-Many reference sets"""

User.interviewer_interviewInfos = ReferenceSet(User.ID,
                                              InterviewerInterviewInfo.InterviewerID,
                                              InterviewerInterviewInfo.InterviewInfoID,
                                              InterviewInfo.ID)


InterviewInfo.interviewers = ReferenceSet(InterviewInfo.ID,
                                          InterviewerInterviewInfo.InterviewInfoID,
                                          InterviewerInterviewInfo.InterviewerID,
                                          User.ID)
    
InterviewInfo.questions = ReferenceSet(InterviewInfo.ID,
                                       QuestionInterviewInfo.InterviewID,
                                       QuestionInterviewInfo.QuestionsID,
                                       Questions.ID)


Tableversion.subtitles = ReferenceSet(Tableversion.ID,
                                      SubtitleTableversion.TableVerID,
                                      SubtitleTableversion.SubTitleID,
                                      Subtitle.ID)
    

Subtitle.tableversions = ReferenceSet(Subtitle.ID,
                                      SubtitleTableversion.SubTitleID,
                                      SubtitleTableversion.TableVerID,
                                      Tableversion.ID)

Questions.interviewInfos = ReferenceSet(Questions.ID,
                                        QuestionInterviewInfo.QuestionsID,
                                        QuestionInterviewInfo.InterviewID,
                                        InterviewInfo.ID)

Intervieweegroup.resumeInfos = ReferenceSet(Intervieweegroup.ID,
                                            IntervieweegroupResumeInfo.GroupID,
                                            IntervieweegroupResumeInfo.ResumeID,
                                            ResumeInfo.ID)

ResumeInfo.intervieweeterms = ReferenceSet(ResumeInfo.ID,
                                           IntervieweegroupResumeInfo.ResumeID,
                                           IntervieweegroupResumeInfo.GroupID,
                                           Intervieweegroup.ID)


