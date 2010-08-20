# -*- coding: utf-8 -*-
from person import *
from storm import *
from storm.locals import *


db_url = 'mysql://root:123456@localhost:3306/kchhd'
database = None
store = None
#session = Session()
def getStore():
    global store
    if store == None:
        store = Store(getDatabase())
    return store


def getDatabase():
    global database
    if database == None:
        database = create_database(db_url)
    return database

#登陆
def login(store, id, pwd, tt):
    user = store.find(User, User.AccountID == id).one()
    if user != None:
        if user.Pwd != None:
            if user.Pwd == pwd:
                if user.Type != None:
                    if user.Type == tt:
                        #sessionObj = Session()
                        #session.AccountID = id
                        return 1
                    else:
                        return 2
                return 2
            else:
                return 3
        else:
            return 3
    return 4

#User.interviewee = ReferenceSet(User.AccountID, Interviewinfo.ID)

#面试者查看日程
#返回该面试者所有日程的tuple
def getIntervieweeCalendar(store, id, userType):
    if userType == u'interviewee':
        interviewee = store.find(User, User.AccountID == id).one()
        interviewSet = interviewee.interviews
        return interviewSet
    else:
        return None


#面试者查看相应面试的面试结果
#返回该面试者所有面试的tuple
def getIntervieweeResult(store, id, userType, interviewID):
    if userType == u'interviewee':
        interviewee = store.find(User, User.AccountID == id).one()
        interviewSet = interviewee.interviews
        for result in interviewSet:
            if result.ID == interviewID:
                return result.Result
    else:
        return None


#面试官查看面试者列表
#面试官只能查看自己部门的面试者
#返回的是user表中
def getIntervieweeList(store, ueseType, userDept):
    if ueseType == u'interviewer':
        intervieweeSet = store.find(User, User.Dept == userDept, User.Type == u'interviewee')
        return intervieweeSet
    else:
        return None





#=========================TEST========================
#store.close()
store = getStore()


#result = getIntervieweeCalendar(store, u'sara')

#print result
#print [[ss.IntervieweeID, ss.Addr] for ss in result]

#result = getIntervieweeResult(store, u'sara', u'interviewee', 1)
#print result

results = getIntervieweeList(store, u'interviewer', u'develop')
print [result.AccountID for result in results]
    #print result.AccountID
#one = User(u'003', u'sara',u'interviewee',u'123',u'123')
#store.add(one)
#store.commit()
#test = store.get(User, u'003')
#print test
#b = login(store, u'sara',u'123',u'interviewee')
#print b

#if b == 1:
#    print "welcom to login"
#else:
#    print "error ID or password"



