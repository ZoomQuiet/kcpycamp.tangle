from storm.locals import *


"""one DBtable to one class"""

class InterviewerInterviewInfo(Storm):
    __storm_table__ = 'interviewer_interviewInfo_relation'
    __storm_primary__ = "InterviewInfoID", "InterviewerID"
    InterviewInfoID = Int()
    InterviewerID = Int()
    def __init__(self, InterviewInfoID = 0, InterviewerID = 0):
        self.InterviewInfoID = InterviewInfoID
        self.InterviewerID = InterviewerID

class IntervieweegroupResumeInfo(object):
    __storm_table__ = 'intervieweegroup_resumeInfo_relation'
    __storm_primary__ = "GroupID", "ResumeID"
    GroupID = Int()
    ResumeID = Int()
    def __init__(self, GroupID = 0, ResumeID = 0):
        self.GroupID = GroupID
        self.ResumeID = ResumeID

class QuestionInterviewInfo(Storm):
    __storm_table__ = 'question_interviewInfo_relation'
    __storm_primary__ = "QestionsID", "InterviewID"
    QestionsID = Int()
    InterviewID = Int()
    Answer = Unicode()
    def __init__(self, QestionsID = 0, InterviewID = 0, Answer = u""):
        self.QestionsID = QestionsID
        self.InterviewID = InterviewID
        self.Answer = Answer

class SubtitleTableversion(Storm):
    __storm_table__ = 'subtitle_tableversion_relation'
    __storm_primary__ = "SubTitleID", "TableVerID"
    SubTitleID = Int()
    TableVerID = Int()
    def __init__(self, SubTitleID = 0, TableVerID = 0):
        self.SubTitleID = SubTitleID
        self.TableVerID = TableVerID
    
class InterviewInfo(Storm):
    __storm_table__ = 'interviewinfo'
    ID = Int(primary = True)
    TableVerID = Int()
    Result = Unicode()
    Addr = Unicode()
    Times = Int()
    DateTime = Unicode()
    IntervieweeID = Int()

    def __init__(self, ID = 0, TableVerID = 0, Result = u"", Addr = u"",
                 Times = 0, DateTime = u"", IntervieweeID = u""):
        self.ID = ID
        self.TableVerID = TableVerID
        self.Result = Result
        self.Addr = Addr
        self.Times = Times
        self.DateTime = DateTime
        self.IntervieweeID = IntervieweeID
    
    
class User(Storm):
    __storm_table__ = 'user'
    ID = Int(primary = True)
    AccountID = Unicode()
    Name = Unicode()
    Type = Unicode()
    Pwd = Unicode()
    Dept = Unicode()
    
    def __init__(self, ID, Name, Type, Pwd,AccountID, Dept = None):
        self.ID = ID
        self.AccountID = AccountID
        self.Name = Name
        self.Type = Type
        self.Pwd = Pwd
        self.Dept = Dept

    
class Tableversion(Storm):
    __storm_table__ = 'tableversion'
    ID = Int(primary = True)
    UsedCounts = Int()
    VerNumber = Int()
    
    def __init__(self, UsedCounts = 0, VerNumber = 0):
        self.UsedCounts = UsedCounts
        self.VerNumber = VerNumber
    
class Subtitle(Storm):
    __storm_table__ = 'subtitle'
    ID = Int(primary = True)
    Name = Unicode()
    MainTitleID = Int()

    def __init__(self, ID = 0, Name = u"", MainTitleID = 0):
        self.ID = ID
        self.Name = Name
        self.MainTitleID = MainTitleID


class Questions(Storm):
    __storm_table__ = 'questions'
    ID = Int(primary = True)
    Description = Unicode()

    def __init__(self, ID = 0, Description = u""):
        self.ID = ID
        self.Description = Description    


class Intervieweegroup(Storm):
    __storm_table__ = 'intervieweegroup'
    ID = Int(primary = True)
    Name = Unicode()
    Description = Unicode()

    def __init__(self, ID = 0,Name = u"", Description = u""):
        self.ID = ID
        self.Name = Name
        self.Description = Description

class Maintitle(object):
    __storm_table__ = 'maintitle'
    ID = Int(primary = True)
    Name = Unicode()

    def __init__(self, ID = 0,Name = u""):
        self.ID = ID
        self.Name = Name
        
class ResumeInfo(Storm):
    __storm_table__ = 'resumeinfo'
    ID = Unicode(primary = True)
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

    def __init__(self, ID = 0, CardID = u"", Name = u"", Sex = u"", School = u"",
                 Subject = u"", Grade = u"", Telephone = u"", Native = u"", Addr = u"",
                 AddrPhone = u"", Email = u"", QQ = u"", ForeignLanguage = u"",
                 Character = u"", Programming = u"", MathAndPhysics = u"", Scholarships = u"",
                 Project = u"", SchoolDuty = u"", MoreInfo = u"", Advice = u"",
                 ResumePath = u"", PhotoPath = u"", UserID = 0):
        self.ID = ID
        self.CardID = CardID
        self.Name = Name
        self.Sex = Sex
        self.School = School
        self.Subject = Subject
        self.Grade = Grade
        self.Telephone = Telephone
        self.Native = Native
        self.Addr = Addr
        self.AddrPhone = AddrPhone
        self.Email = Email
        self.QQ = QQ
        self.ForeignLanguage = ForeignLanguage
        self.Character = Character
        self.Programming = Programming
        self.MathAndPhysics = MathAndPhysics
        self.Scholarships = Scholarships
        self.Project = Project
        self.SchoolDuty = SchoolDuty
        self.MoreInfo = MoreInfo
        self.Advice = Advice
        self.ResumePath = ResumePath
        self.PhotoPath = PhotoPath
        self.UserID = UserID


"""One-to-One reference"""
ResumeInfo.user = Reference(ResumeInfo.UserID,User.ID)

"""Many-to-one reference sets"""

User.interviewee_interviewInfos = ReferenceSet(User.ID,InterviewInfo.IntervieweeID)

Maintitle.subtitles = ReferenceSet(Maintitle.ID,Subtitle.MainTitleID)

Tableversion.interviewInfos = ReferenceSet(Tableversion.ID,InterviewInfo.TableVerID)

"""Many-to-Many reference sets"""

User.interviewer_interviewInfos = ReferenceSet(User.ID,
                                               InterviewerInterviewInfo.InterviewerID,
                                               InterviewerInterviewInfo.InterviewInfoID,
                                               InterviewInfo.IntervieweeID)


InterviewInfo.interviewers = ReferenceSet(InterviewInfo.IntervieweeID,
                                          InterviewerInterviewInfo.InterviewInfoID,
                                          InterviewerInterviewInfo.InterviewerID,
                                          User.ID)
    
InterviewInfo.questions = ReferenceSet(InterviewInfo.ID,
                                       QuestionInterviewInfo.InterviewID,
                                       QuestionInterviewInfo.QestionsID,
                                       Questions.ID)

Questions.interviewInfos = ReferenceSet(Questions.ID,
                                        QuestionInterviewInfo.QestionsID,
                                        QuestionInterviewInfo.InterviewID,
                                        InterviewInfo.ID)


Tableversion.subtitles = ReferenceSet(Tableversion.ID,
                                      SubtitleTableversion.TableVerID,
                                      SubtitleTableversion.SubTitleID,
                                      Subtitle.MainTitleID)
    

Subtitle.tableversions = ReferenceSet(Subtitle.MainTitleID,
                                      SubtitleTableversion.SubTitleID,
                                      SubtitleTableversion.TableVerID,
                                      Tableversion.ID)


Intervieweegroup.resumeInfos = ReferenceSet(Intervieweegroup.ID,
                                            IntervieweegroupResumeInfo.GroupID,
                                            IntervieweegroupResumeInfo.ResumeID,
                                            ResumeInfo.ID)

ResumeInfo.intervieweegroups = ReferenceSet(ResumeInfo.ID,
                                           IntervieweegroupResumeInfo.ResumeID,
                                           IntervieweegroupResumeInfo.GroupID,
                                           Intervieweegroup.ID)