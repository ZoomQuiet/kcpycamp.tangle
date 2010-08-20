from Cheetah.Template import Template
from webapps.kcHHD.model.kchhd_orm import *
from webapps.kcHHD.conf.db import *
from webapps.kcHHD.service.UserServic import *
from webapps.kcHHD.control.edittitle import *
import random

sess = Session()
if not hasattr(sess, 'accountID'):
	sess.accountID = None

if not hasattr(sess, 'intervieweeID'):
	sess.intervieweeID = None
	
store = getStore()

class IntervieweeList():
	def __init__(self):
		self.DataList = [{'no':1,'ID':'001','name':'may','department':'softEnterprise'},{'no':2,'ID':'002','name':'tan','department':'softEnterprise'}]
		self.vPool={'CList':self.DataList}
	def printPage(self):
		self.DataList = getIntervieweeList()
		self.vPool={'CList':self.DataList}
		Include("../../web/assistant/assistantHeader.pih",title="面试者列表")
		t=Template(file='../web/assistant/intervieweelist.tmpl',searchList=[self.vPool])
		print t	
class InterviewerAccounts:
	def __init__(self):
		self.DataList = []
		self.vPool={}
	def printPage(self):
		self.DataList = getInterviewerList()
		self.vPool={'CList':self.DataList}
		Include("../../web/assistant/assistantHeader.pih",title="面试官列表")
		t=Template(file='../web/assistant/intervieweraccounts.tmpl',searchList=[self.vPool])
		print t	
class AppriaseTable():
	def __init__(self):
		self.mTitle = Title('[+]','[-]')
		self.dataControl = TitleDataControl()
	def EditAllTitle(self,str):
		pass
	def AddManyTitle(self,str):
		self.mTitle.titleStr = str
		self.mTitle.strToList()
		for tt in self.mTitle.titleList:
			for st in tt:
				if st == tt[0]:
					strMt = st
				else:
					self.dataControl.add(strMt, st)
	def delOne(self,stID):
		self.dataControl.remove(stID)
	def delAll(self):
		self.dataControl.removeAll()
	def printStrTitle(self,Tag):
		self.mTitle.titleList = [[st[1] for st in tt] for tt in self.dataControl.titleList]
		Str=''
		Tag = int(Tag)
		TTName = '批量添加'
		if Tag == 0:
			self.mTitle.listToStr()
			Str = self.mTitle.titleStr
			TTName = '批量编辑'
		#self.mTitle.printTT()
		Include("../../web/assistant/assistantHeader.pih",title=TTName)
		self.printTitle()
		print '''<div align='center'>
		        <form name="form1" method="post" action="editAllTitle">
				<input type="hidden" name="Tag" value="%s">
				<textarea name="textarea" cols="30" rows="30">%s</textarea>
				<input type="submit" value="Ok">
				</form>'''%(Tag,Str)
		print u'''注释：<br>[+]:为主标题<br>[-]:次标题<br>例子：<br>[+]主标题<br>[-]副标题一<br>[-]副标题二<br>[+]主标题一<br>[-]副标题三<br>[-]副标题四<br>
		<table width="75%" border="1"><tr> <td colspan="2" rowspan="2">主标题一</td><td>副标题一</td></tr><tr> <td>副标题二</td></tr><tr>
		<td colspan="2" rowspan="2">主标题二</td><td>副标题三</td></tr><tr><td>副标题四</td></tr></table></div>	'''
	def printTitle(self):
		Pool = {'TTList':self.dataControl.titleList}
		t=Template(file='../web/assistant/appriaseTablet.tmpl',searchList=[Pool])
		#print '%s'%self.dataControl.titleList
		print t	
	def printPage(self):
		Include("../../web/assistant/assistantHeader.pih",title="定制评议表")
		self.printTitle()
		print u'''<div align='center'><td class="main"><a href="../../control/assistant.ks/showEditTitle?Tag=0">编辑All Title</a></td>
				<td class="main"><a href="../../control/assistant.ks/showEditTitle?Tag=1">批量添加Title</a></td></div>'''

class Information():
	def __init__(self):
		self.vPool={}
	def printPage(self):
		self.vPool = getAssistantInfo()
		Include("../../web/assistant/assistantHeader.pih",title="Information")
		t=Template(file='../web/assistant/assistantinfo.tmpl',searchList=[self.vPool])
		print t	
	

def index(accountID):
	sess.accountID = accountID
	wel = "Welcom to the System:" + sess.accountID
	Include("../../web/assistant/assistantHeader.pih",title=u"HomePage")
	print "<div align = 'center'>"
	print "<h1>"
	print wel
	print"</h1></div>"
def intervieweeList():
	obj = IntervieweeList()
	obj.printPage()
def interviewerList():
	obj = InterviewerAccounts()
	obj.printPage()
def appriaseTable():
	appriaseTable = AppriaseTable()
	appriaseTable.printPage()
def information():
	obj = Information()
	obj.printPage()
def addInterviewee():
	Include("../../web/assistant/assistantHeader.pih",title="添加面试者")
	Include("../../web/assistant/addInterviewee.pih")

def addInterviewer():
	Include("../../web/assistant/assistantHeader.pih",title="添加面试官")
	Include("../../web/assistant/addInterviewer.pih")

def editPassword():
	Include("../../web/assistant/assistantHeader.pih",title="修改密码")
	Include("../../web/assistant/editPassword.pih")	
	
def exit():
	sess.close()
	raise HTTP_REDIRECTION,"../../web/login.pih"

def getIntervieweeList():
	store.rollback()	
	user = store.find(User,User.Type == u'interviewee', User.IsEffect != 0)
	i = 1
	list = []
	for result in user:
		list.append({'no':i,'ID':result.ID,'AccountID':result.AccountID,'name':result.Name,'department':result.Dept})
		i = i + 1
	#store.close()
	return list

def getInterviewerList():
	store.rollback()	
	user = store.find(User,User.Type == u'interviewer', User.IsEffect != 0)
	i = 1
	list = []
	for result in user:
		list.append({'no':i,'ID':result.ID,'AccountID':result.AccountID,'name':result.Name,'department':result.Dept})
		i = i + 1
	#store.close()
	return list


def getAssistantInfo():
	store.rollback()
	accountID = sess.accountID.decode('utf-8')
	user = store.find(User,User.AccountID == accountID,User.IsEffect != 0).one()
	info = {'name':user.Name, 'AccountID':user.AccountID,'Dept':user.Dept}
	return info

def showResume(ID):
	#IntervieweeID = AccountID
	id = int(ID)
	t = getUserResume(id)
	if t == False:
		Include("../../web/assistant/assistantHeader.pih",title="查看简历")
		print "<div align = 'center'>"
		print "<h1>"
		print "此面试者没有填写简历"
		print"</h1></div>"
	else:
		Include("../../web/assistant/assistantHeader.pih",title="查看简历")
		Include("../../web/assistant/seeresume.pih",userID=id)

def editIntervieweeInfo(ID):
	store.rollback()
	user = store.get(User,int(ID))
	sess.intervieweeID = int(ID)
	Include("../../web/assistant/assistantHeader.pih",title="修改面试者面试部门")
	Include("../../web/assistant/editIntervieweeInfo.pih",user = user)

def editIntervieweeDept(dept):
	store.rollback()
	deptartment = None
	if dept != None:
		deptartment = dept.decode('utf-8')
	store.find(User,User.ID == sess.intervieweeID).set(Dept = deptartment)
	store.commit()
	sess.intervieweeID = None
	Include("../../web/assistant/assistantHeader.pih",title="主页")
	print "<div align = 'center'>"
	print "<h1>"
	print "修改成功"
	print"</h1></div>"

def addIntervieweeInfo(AccountID,Name,Pwd,Dept):
	account = AccountID.decode("utf-8")
	if checkUserNameUsed(account):
		Include("../../web/assistant/assistantHeader.pih",title="主页")
		print "<div align = 'center'>"
		print "<h1>"
		print "此账号已存在"
		print"</h1></div>"
	else:
		ID = random.randrange(1000,9999)
		
		name = Name.decode('utf-8')
		pwd = Pwd.decode('utf-8')
		dept = Dept.decode('utf-8')
		user = User(ID,account,name,u'interviewee',pwd,dept)
		store.rollback()
		store.add(user)
		store.commit()
		Include("../../web/assistant/assistantHeader.pih",title="HomePage")
		print "<div align = 'center'>"
		print "<h1>"
		print "添加面试者成功"
		print"</h1></div>"
		
def addInterviewerInfo(AccountID,Pwd,Dept):
	account = AccountID.decode("utf-8")
	if checkUserNameUsed(account):
		Include("../../web/assistant/assistantHeader.pih",title="主页")
		print "<div align = 'center'>"
		print "<h1>"
		print "此账号已存在"
		print"</h1></div>"
	else:
		ID = random.randrange(1000,9999)
		name = u''
		pwd = Pwd.decode('utf-8')
		dept = Dept.decode('utf-8')
		user = User(ID,account,name,u'interviewer',pwd,dept)
		store.rollback()
		store.add(user)
		store.commit()
		Include("../../web/assistant/assistantHeader.pih",title="主页")
		print "<div align = 'center'>"
		print "<h1>"
		print "添加面试官成功"
		print"</h1></div>"

def resetPassword(pwd1,pwd2, pwd3):
	id = unicode(sess.accountID,'utf-8')
	user = store.find(User,User.AccountID == id).one()
	password1 = unicode(pwd1,'utf-8')
	password2 = unicode(pwd2,'utf-8')
	if pwd2 != pwd3:
		Include("../../web/assistant/assistantHeader.pih",title="修改密码")
		print "<div align = 'center'>"
		print "<h1>"
		print "两次输入的密码不相同"
		print"</h1></div>"
	else:
		if user.Pwd == password1:
			store.find(User,User.AccountID == id).set(Pwd = password2)
			store.commit()
			Include("../../web/assistant/assistantHeader.pih",title="主页")
			print "<div align = 'center'>"
			print "<h1>"
			print "修改密码成功"
			print"</h1></div>"
		else:
			Include("../../web/assistant/assistantHeader.pih",title="主页")
			print "<div align = 'center'>"
			print "<h1>"
			print u"初始密码输入错误"
			print"</h1></div>"


def removeInterviewee(ID):
	id = int(ID)
	store.rollback()
	store.find(User, User.ID == id).set(IsEffect = 0)
	interview = store.find(InterviewInfo, InterviewInfo.IntervieweeID == id, InterviewInfo.IsOvertime != 1)
	if interview != None:
		interview.set(IsOvertime = 1)
	store.commit()
	Include("../../web/assistant/assistantHeader.pih",title="删除面试者")
	print "<div align = 'center'>"
	print "<br><br><br><br><br><br><br><br><h1>"
	print "删除面试者成功"
	print"</h1></div>"

	
def removeInterviewer(ID):
	id = int(ID)
	store.rollback()
	store.find(User, User.ID == id).set(IsEffect = 0)
	
	store.commit()
	Include("../../web/assistant/assistantHeader.pih",title="删除面试官")
	print "<div align = 'center'>"
	print "<br><br><br><br><br><br><br><br><h1>"
	print "删除面试官成功"
	print"</h1></div>"
	
def showEditTitle(Tag):
	appriaseTable = AppriaseTable()
	appriaseTable.printStrTitle(Tag)	
def editAllTitle(Tag,textarea=''):
	Tag=int(Tag)
	appriaseTable = AppriaseTable()
	if Tag == 0:
		appriaseTable.delAll()
	appriaseTable.AddManyTitle(textarea)
	raise HTTP_REDIRECTION,"appriaseTable"		
def removeTitle(ID = 0):
	appriaseTable = AppriaseTable()
	appriaseTable.delOne(ID)
	raise HTTP_REDIRECTION,"appriaseTable"	

	id = int(ID)
	store.rollback()
	store.find(User, User.ID == id).set(IsEffect = 0)
	
	store.commit()
	Include("../../web/assistant/assistantHeader.pih",title="删除面试官")
	print "<div align = 'center'>"
	print "<br><br><br><br><br><br><br><br><h1>"
	print "删除面试官成功"
	print"</h1></div>"

	