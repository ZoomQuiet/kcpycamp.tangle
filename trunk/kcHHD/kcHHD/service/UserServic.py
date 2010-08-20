from webapps.kcHHD.model.kchhd_orm import *
from webapps.kcHHD.conf.db import *
import random

store = getStore()

def addInterviewee(accountID,name,password):
    if checkUserNameUsed(accountID):
        return False
    userType = u'interviewee'
    UserDept = None
    ID = random.randrange(1000,9999)
    user = User(ID,accountID,name,userType,password,UserDept)
    store.add(user)
    store.commit()
    return user
    
        
def checkUserNameUsed(name):
    if store.find(User,User.AccountID == name).one():
        return True
    else:
        return False


def loginValidate(UID,password,userType):
    usr = store.find(User,User.AccountID == UID, User.Pwd == password, User.Type == userType, User.IsEffect != 0).one()
    if usr:
        return usr
    else:
        return False


def getIntervieweeInterviewInfo(id, userType):
    if userType == u'interviewee':
        interviewee = store.get(User,id)
        #print interviewee.Name
        interviewSet = interviewee.interviewee_interviewInfos
        #print [result.Addr for result in interviewSet]
        return interviewSet
    else:
        return None

def getUserResume(id):
    #userID = id.decode('UTF-8')
    """user = store.find(User, User.AccountID == accountID).one()
    if user == None:
        return False
    userID = int(user.ID)
    print userID"""
    #userID = int(id)
    resume = store.find(ResumeInfo, ResumeInfo.UserID == id).one()
    if resume == None:
        return False
    return True
