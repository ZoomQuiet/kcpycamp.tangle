def check(login,password,selectstatue):
    if _is_valid(login,password): 
	
  	if selectstatue == '1':
		IntervieweePage()
  		
	elif selectstatue == '2':
		Interviewerpage()
	elif selectstatue == '3':
		adminpage()
	else:
		assistantpage()
    else:
        print "Sorry, you are not allowed to access this page"

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
def _is_valid(login,password):
# replace this with a check in the users database
    return login == '' and password == ''
