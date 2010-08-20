from webapps.kcHHD.model.kvhhd_orm import *
#from webapps.kcHHD.model.operate import *
from webapps.kcHHD.model.db import *


def check(id,password,selectstatue):
    a = unicode(id)
    b = unicode(password)
    c = unicode(selectstatue)
    store = getStore()
    d = login(store,a,b,c)
    #session = Session()
    #session.AccountID = id
    #print session.AccountID
    #raise SCRIPT_END
    
    if d == 1:
        #session = Session()
        #session.UserId= a
        if selectstatue == 'interviewee':
            IntervieweePage()  		
        elif selectstatue == 'interviewer':
            Interviewerpage()
        elif selectstatue == 'admin':
            adminpage()
        else:
            assistantpage()
    elif d == 2:
        print "please input the right type"
    elif d == 3:
        print "please input the right password"
    elif d == 4:
        print "the ID is not exists"
    elif d == 0:
        print "Please input the right ID"
    else:
        print "<h1>ERROR<h1>"

def assistantpage():
	raise HTTP_REDIRECTION,"../AssistantPage.pih"
def adminpage():
	raise HTTP_REDIRECTION,"../AdminPage.pih"
def Interviewerpage():
	raise HTTP_REDIRECTION,"../interviewer.ks/index"
def IntervieweePage():
	raise HTTP_REDIRECTION,"../interviewee.ks/index"



def order(Type):
    if not hasattr(Session(),"login"):
        print "Sorry, you are not allowed to access this page"
    else:
        print "Ok %s, you want to order a %s" %(Session().login,Type)


#µÇÂ½
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

