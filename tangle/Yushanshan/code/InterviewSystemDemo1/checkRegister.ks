def check(login,password,selectstatue):
    if _is_valid(login,password):
#check the database if the username is exits
        Session().login = login
        print "Hello",login,"<br>"
        print "%s" %_selectstatue
        print '<div align="center">'
        print '<br><a href="../AdminPage.pih">Admin</a>'
        print '<br><a href="../InterviewerPage.pih">Interviewer</a>'
        print '<br><a href="../AssistantPage.pih">Candidatet</a>'
        print '<br><a href="../IntervieweePage.pih">Candidatet</a>'
        print '</div>'
    else:
        print "Sorry, you are not allowed to access this page"
def order(Type):
    if not hasattr(Session(),"login"):
        print "Sorry, you are not allowed to access this page"
    else:
        print "Ok %s, you want to order a %s" %(Session().login,Type)
def _is_valid(login,password):
# replace this with a check in the users database
    return login == 'login' and password == 'password'
