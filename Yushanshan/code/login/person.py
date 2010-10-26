#write by sara_yu
from storm.locals import *

class InterviewInfo(Storm):
    __storm_table__ = 'interviewInfo'
    ID = Int(primary = True)
    TableVerID = Int()
    Result = Unicode()
    Addr = Unicode()
    Times = Int()
    IntervieweeID = Int()

class User(Storm):
    __storm_table__ = 'user'
    ID = Int(primary = True)
    AccountID = Unicode()
    Name = Unicode()
    Type = Unicode()
    Pwd = Unicode()
    Dept = Unicode()

    interviews = ReferenceSet(ID, InterviewInfo.IntervieweeID)

    def __repr__(self):
        return "<User('%s','%s','%s','%s','%s')>"  % (self.AccountID, self.Name, self.Type, self.Pwd, self.Dept)
    
    def __init__(self, ID):
        self.ID = ID



