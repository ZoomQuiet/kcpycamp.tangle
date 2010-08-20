from operate import *


def check(id,password,selectstatue):
    a = unicode(id)
    b = unicode(password)
    c = unicode(selectstatue)
    store = getStore()
    d = login(store,a,b,c)
    
    #raise SCRIPT_END
    
    if d == 1: 
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
	raise HTTP_REDIRECTION,"../InterviewerAfterLogin.pih"
def IntervieweePage():
	raise HTTP_REDIRECTION,"../mianshi.pih"



def order(Type):
    if not hasattr(Session(),"login"):
        print "Sorry, you are not allowed to access this page"
    else:
        print "Ok %s, you want to order a %s" %(Session().login,Type)
