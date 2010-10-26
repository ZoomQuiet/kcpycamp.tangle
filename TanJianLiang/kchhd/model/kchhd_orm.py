from storm.locals import *

"""one DBtable to one class"""

class InterviewInfo(Storm):
    """InitFunParameters:  ID(Int), Result(Unicode), Addr(Unicode),
    Times(Int), DateTime(Unicode), Dept(Unicode), IsOvertime(Int)"""
    __storm_table__ = 'interviewinfo'
    ID = Int(primary = True)
    TableVerID = Int()
    Result = Unicode()
    Addr = Unicode()
    Times = Int()
    DateTime = Unicode()
    Dept = Unicode()
    IsOvertime = Int()
    IntervieweeID = Int()

    interviewee = Reference(IntervieweeID,'User.ID')

    tableversion = Reference(TableVerID,'Tableversion.ID')   

    interviewers = ReferenceSet(ID,
                                'InterviewerInterviewInfo.InterviewInfoID',
                                'InterviewerInterviewInfo.InterviewerID',
                                'User.ID')
    questions = ReferenceSet(ID,
                             'QuestionInterviewInfo.InterviewID',
                             'QuestionInterviewInfo.QestionsID',
                             'Questions.ID')

    def __init__(self, ID, Result, Addr, Times, DateTime, Dept, IsOvertime):
        self.ID = ID
        self.Result = Result
        self.Addr = Addr
        self.Times = Times
        self.DateTime = DateTime
        self.Dept = Dept
        self.IsOvertime = IsOvertime
    
class User(Storm):
    """InitFunParameters:  ID(Int), AccountID(Unicode), Name(Unicode),
    Type(Unicode), Pwd(Unicode), Dept(Unicode)"""
    __storm_table__ = 'user'
    ID = Int(primary = True)
    AccountID = Unicode()
    Name = Unicode()
    Type = Unicode()
    Pwd = Unicode()
    Dept = Unicode()

    interviewee_interviewInfos = ReferenceSet(ID,'InterviewInfo.IntervieweeID')
    
    interviewer_interviewInfos = ReferenceSet(ID,
                                              'InterviewerInterviewInfo.InterviewerID',
                                              'InterviewerInterviewInfo.InterviewInfoID',
                                              'InterviewInfo.ID')
    
    
    def __init__(self, ID, AccountID, Name, Type, Pwd, Dept = u""):       
        self.ID = ID
        self.AccountID = AccountID
        self.Name = Name
        self.Type = Type
        self.Pwd = Pwd
        self.Dept = Dept
    
    
class Tableversion(Storm):
    """InitFunParameters:  ID(Int), UsedCounts(Int), VerNumber(Int)"""
    __storm_table__ = 'tableversion'
    ID = Int(primary = True)
    UsedCounts = Int()
    VerNumber = Int()

    interviewInfos = ReferenceSet(ID,'InterviewInfo.TableVerID')

    subtitles = ReferenceSet(ID,
                             'SubtitleTableversion.TableVerID',
                             'SubtitleTableversion.SubTitleID',
                             'Subtitle.ID')                           
    
    def __init__(self, ID, UsedCounts, VerNumber):
        self.ID = ID
        self.UsedCounts = UsedCounts
        self.VerNumber = VerNumber
    

class Questions(Storm):
    """InitFunParameters:  ID(Int), Description(Unicode)"""
    __storm_table__ = 'questions'
    ID = Int(primary = True)
    Description = Unicode()

    interviewInfos = ReferenceSet(ID,
                                  'QuestionInterviewInfo.QestionsID',
                                  'QuestionInterviewInfo.InterviewID',
                                  'InterviewInfo.ID')
                                     
    def __init__(self, ID, Description):
        self.ID = ID
        self.Description = Description    
    

class Intervieweegroup(Storm):
    """InitFunParameters:  ID(Int), Name(Unicode), Description(Unicode)"""
    __storm_table__ = 'intervieweegroup'
    ID = Int(primary = True)
    Name = Unicode()
    Description = Unicode()

    resumeInfos = ReferenceSet(ID,
                               'IntervieweegroupResumeInfo.GroupID',
                               'IntervieweegroupResumeInfo.ResumeID',
                               'ResumeInfo.ID')                             
    
    def __init__(self, ID, Name, Description = u""):
        self.ID = ID
        self.Name = Name
        self.Description = Description
    

class Subtitle(Storm):
    """InitFunParameters:  ID(Int), Name(Unicode)"""
    __storm_table__ = 'subtitle'
    ID = Int(primary = True)
    Name = Unicode()
    MainTitleID = Int()

    maintitle = Reference(MainTitleID,'Maintitle.ID')

    tableversions = ReferenceSet(ID,
                                 'SubtitleTableversion.SubTitleID',
                                 'SubtitleTableversion.TableVerID',
                                 'Tableversion.ID')
                                 
    
    def __init__(self, ID, Name):
        self.ID = ID
        self.Name = Name
    
class Maintitle(Storm):
    """InitFunParameters:  ID(Int), Name(Unicode)"""
    __storm_table__ = 'maintitle'
    ID = Int(primary = True)
    Name = Unicode()

    subtitles = ReferenceSet(ID,'Subtitle.MainTitleID')    
    
    def __init__(self, ID, Name):
        self.ID = ID
        self.Name = Name
           
class ResumeInfo(Storm):
    """InitFunParameters:  ID(Int), CardID(Unicode), Name(Unicode),Sex(Unicode)"""
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

    user = Reference(UserID,'User.ID')

    intervieweegroups = ReferenceSet(ID,
                                     'IntervieweegroupResumeInfo.ResumeID',
                                     'IntervieweegroupResumeInfo.GroupID',
                                     'Intervieweegroup.ID')
                                           

    def __init__(self, ID, CardID, Name, Sex):
        self.ID = ID
        self.CardID = CardID
        self.Name = Name
        self.Sex = Sex


"""Relation class"""

class InterviewerInterviewInfo(Storm):
    __storm_table__ = 'interviewer_interviewInfo_relation'
    __storm_primary__ = "InterviewInfoID", "InterviewerID"
    InterviewInfoID = Int()
    InterviewerID = Int()

class IntervieweegroupResumeInfo(Storm):
    __storm_table__ = 'intervieweegroup_resumeInfo_relation'
    __storm_primary__ = "GroupID", "ResumeID"
    GroupID = Int()
    ResumeID = Int()

class QuestionInterviewInfo(Storm):
    __storm_table__ = 'question_interviewInfo_relation'
    __storm_primary__ = "QestionsID", "InterviewID"
    QestionsID = Int()
    InterviewID = Int()
    Answer = Unicode()

class SubtitleTableversion(Storm):
    __storm_table__ = 'subtitle_tableversion_relation'
    __storm_primary__ = "SubTitleID", "TableVerID"
    SubTitleID = Int()
    TableVerID = Int()

    
'''
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
                                               InterviewInfo.ID)


InterviewInfo.interviewers = ReferenceSet(InterviewInfo.ID,
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
                                      Subtitle.ID)
    

Subtitle.tableversions = ReferenceSet(Subtitle.ID,
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
'''