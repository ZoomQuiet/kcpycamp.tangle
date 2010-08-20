from Cheetah.Template import Template
from webapps.kcHHD.model.kchhd_orm import *
from webapps.kcHHD.conf.db import *
from webapps.kcHHD.service.UserServic import *

sess = Session()
if not hasattr(sess, 'accountID'):
	sess.accountID = None

def index(accountID):
	#print accountID
	#raise SCRIPT_END
	sess.accountID =accountID
	Include("../../web/admin/adminHeader.pih",title="管理者主页")

class AllUser():
	def __init__(self):
		self.DataList =[]
		self.vPool={}	
	def printPage(self):
		self.DataList = getAllUserList()
		self.vPool={'CList':self.DataList}
		Include("../../web/admin/adminHeader.pih",title="所有用户列表")
		t = Template(file='../web/admin/alluser.tmpl',searchList = [self.vPool])
		print t

def getAllUserList():
	store = getStore()
	store.rollback()	
	user = store.find(User)
	i = 1
	list = []
	for result in user:
		list.append({'ID':i,'AccountID':result.AccountID,'Name':result.Name})
		i = i + 1
	#store.close()
	return list

def AllUserFunction():
	obj = AllUser()
	obj.printPage()



class AllInterviewee():
	def __init__(self):
		self.DataList =[]
		self.vPool={}
	def printPage(self):
		self.DataList = getAllIntervieweeList()
		self.vPool={'CList':self.DataList}
		Include("../../web/admin/adminHeader.pih",title="面试者列表")
		t = Template(file='../web/admin/alluser.tmpl',searchList = [self.vPool])
		print t

def getAllIntervieweeList():
	store = getStore()
	store.rollback()	
	user = store.find(User, User.Type == u'interviewee',User.IsEffect != 0)
	i = 1
	list = []
	for result in user:
		list.append({'ID':i,'AccountID':result.AccountID,'Name':result.Name})
		i = i + 1
	#store.close()
	return list

def getAllIntervieweeFunction():
	obj = AllInterviewee()
	obj.printPage()




class AllInterviewer():
	def __init__(self):
		self.DataList =[]
		self.vPool={}
		
	def printPage(self):
		self.DataList = getAllInterviewer()
		self.vPool={'CList':self.DataList}
		Include("../../web/admin/adminHeader.pih",title="面试官列表")
		t = Template(file='../web/admin/alluser.tmpl',searchList = [self.vPool])
		print t

def getAllInterviewer():
	store = getStore()
	store.rollback()	
	user = store.find(User, User.Type == u'interviewer',User.IsEffect != 0)
	i = 1
	list = []
	for result in user:
		list.append({'ID':i,'AccountID':result.AccountID,'Name':result.Name})
		i = i + 1
	#store.close()
	return list

def getAllInterviewerFunction():
	obj = AllInterviewer()
	obj.printPage()

class AllAssistant():
	def __init__(self):
		self.DataList =[]
		self.vPool={}
	def printPage(self):
		self.DataList = getAllAssistant()
		self.vPool={'CList':self.DataList}
		Include("../../web/admin/adminHeader.pih",title="助理")
		t = Template(file='../web/admin/alluser.tmpl',searchList = [self.vPool])
		print t

def getAllAssistant():
	store = getStore()
	store.rollback()	
	user = store.find(User, User.Type == u'assistant',User.IsEffect != 0)
	i = 1
	list = []
	for result in user:
		list.append({'ID':i,'AccountID':result.AccountID,'Name':result.Name})
		i = i + 1
	#store.close()
	return list

def getAllAssistantFunction():
	obj = AllAssistant()
	obj.printPage()

def exit():
	sess.close()
	raise HTTP_REDIRECTION,"../../web/login.pih"

def edit(AccountID):
	store = getStore()
	store.rollback()
	user = store.find(User, User.AccountID == unicode(AccountID, 'utf-8')).one()
	Include("../../web/admin/edit.pih",user = user)

def editPwd():
	Include("../../web/admin/adminHeader.pih",title="修改密码")
	Include("../../web/admin/editPassword.pih")

def resetPassword(pwd1,pwd2, pwd3):
	id = unicode(sess.accountID,'utf-8')
	user = store.find(User,User.AccountID == id).one()
	password1 = unicode(pwd1,'utf-8')
	password2 = unicode(pwd2,'utf-8')
	password3 = unicode(pwd3,'utf-8')
	if password3 != password2:
		Include("../../web/admin/adminHeader.pih",title=u"修改密码")
		print "<div align = 'center'>"
		print "<h1>"
		print "两次密码输入不相同"
		print"</h1></div>"
	else:
		if user.Pwd == password1:
			store.find(User,User.AccountID == id).set(Pwd = password2)
			store.commit()
			Include("../../web/admin/adminHeader.pih",title=u"修改密码")
			print "<div align = 'center'>"
			print "<h1>"
			print "修改密码成功"
			print"</h1></div>"
		else:
			Include("../../web/admin/adminHeader.pih",title=u"修改密码")
			print "<div align = 'center'>"
			print "<h1>"
			print u"初始密码输入错误"
			print"</h1></div>"

###############################################################################################
def modify_userinfo(userID,userName,password,password1):
	store = getStore()
	store.find(User,User.AccountID == unicode(userID,'utf')).set(Name = userName.decode("utf"), Pwd = password.decode("utf"))
	store.commit()
	user = store.find(User,User.AccountID == unicode(userID,'utf')).one()
	if user.Type == u'interviewee':
		temp = "getAllIntervieweeFunction"
	if user.Type == u'interviewer':
		temp = "getAllInterviewerFunction"
	if user.Type == u'assistant':
		temp = "getAllAssistantFunction"
	raise HTTP_REDIRECTION,temp

def add(accountID,name,type,password):
	if checkUserNameUsed(accountID):
		return False
	UserDept = None
	ID = random.randrange(1000,9999)
	user = User(ID,accountID,name,type,password,UserDept)
	store.add(user)
	store.commit()
	return user
	
def adduser(userID,userName,userType,password,password1):
	accountID = unicode(userID,'utf-8')
	name = unicode(userName,'utf-8')
	type = unicode(userType,'utf-8')
	pwd = unicode(password,'utf-8')
	if(checkUserNameUsed(accountID)):
		print "用户名已存在"
	else:
		try:
			user = add(accountID, name, type, pwd)
		except:
			print "添加失败"
		else:
			if user.Type == u'interviewee':
				temp = "getAllIntervieweeFunction"
			if user.Type == u'interviewer':
				temp = "getAllInterviewerFunction"
			if user.Type == u'assistant':
				temp = "getAllAssistantFunction"
			raise HTTP_REDIRECTION,temp

#########################################################################################

def removeInterviewee(AccountID):
	store.rollback()
	id = unicode(AccountID,'utf-8')
	store.find(User,User.AccountID == id).set(IsEffect = 0)
	user = store.find(User,User.AccountID == id).one()
	userID = user.ID
	interview = store.find(InterviewInfo, InterviewInfo.IntervieweeID == userID, InterviewInfo.IsOvertime != 1)
	if interview != None:
		interview.set(IsOvertime = 1)
	store.commit()
	Include("../../web/admin/adminHeader.pih",title="删除面试者")
	print "<div align = 'center'>"
	print "<br><br><br><br><br><br><br><br><h1>"
	print "删除面试者成功"
	print"</h1></div>"

def remove(AccountID):
	store.rollback()
	id = unicode(AccountID,'utf-8')
	store.find(User,User.AccountID == id).set(IsEffect = 0)
	store.commit()
	user = store.find(User,User.AccountID == id).one()
	userID = user.ID	
	if user.Type == u'interviewee':
			interview = store.find(InterviewInfo, InterviewInfo.IntervieweeID == userID, InterviewInfo.IsOvertime != 1)
			if interview != None:
				interview.set(IsOvertime = 1)
			store.commit()
			temp = "getAllIntervieweeFunction"

	if user.Type == u'interviewer':
			temp = "getAllInterviewerFunction"
	if user.Type == u'assistant':
			temp = "getAllAssistantFunction"
	raise HTTP_REDIRECTION,temp






	