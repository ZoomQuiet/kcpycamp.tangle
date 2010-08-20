from Cheetah.Template import Template
from webapps.kcHHD.model.kchhd_orm import *
from webapps.kcHHD.conf.db import *
from webapps.kcHHD.service.UserServic import *
import random

session = Session()
if not hasattr(session, u'accountID'):
	session.accountID = None

if not hasattr(session, u'interviewee'):
	session.interviewee = None
		
#**************************************************************************************************
##**************************************************************************************************	
class Calender():
	def __init__(self):
		#self.DataList = [{'no':1,'time':'2008-8-10','place':'wps'},{'no':2,'time':'2008-8-10','place':'wps'}]
		#self.vPool={'CList':self.DataList}
		self.DataList = []
		self.vPool= {}
	def printPage(self,ID):
		self.DataList = getCalendarList_interviewer(ID)
		self.vPool={u'CList':self.DataList}
		Include("../../web/interviewer/interviewerHeader.pih",title="日程")
		t=Template(file='../web/interviewer/Calender.tmpl',searchList=[self.vPool])
		print t

def getInterviewerInterviweInfo(store,id,usrtype):
	if usrtype == u"interviewer":
		interviewer = store.find(User,User.AccountID == id,User.IsEffect != 0).one()
		#print interviewer.ID
		#print id
		#raise SCRIPT_END
		interviewSet = interviewer.interviewer_interviewInfos
		#print interviewSet
		return interviewSet
	else:
		return None
		
def getCalendarList_interviewer(accountID):
	store = getStore()
	store.rollback()
	id = accountID.decode('UTF-8')
	resultSet = getInterviewerInterviweInfo(store,id,u"interviewer")
	i = 1
	list = []
	for result in resultSet:
		if result.IsOvertime == 1:
			pass
		else:
			interviewee = store.find(User,User.ID == result.IntervieweeID).one()
			list.append({u'no':i,u'time':result.DateTime,u'place':result.Addr,u'person':interviewee.Name})
			i = i+1
	return list


class ResultList():
	def __init__(self):
		self.DataList = []
		self.vPool= {}
	def printPage(self,accountID):
		self.DataList = getIntervieweeList(accountID)
		self.vPool = {u'CList':self.DataList}
		Include("../../web/interviewer/interviewerHeader.pih",title="面试者列表")
		t=Template(file='../web/interviewer/Interviewer_intervieweelist.tmpl',searchList=[self.vPool])
		print t

"""def getInterviewedList():
	store = getStore()
	store.rollback()
	id = accountID.decode('UTF-8')
	interviewer = store.find(User,User.AccountID == id).one()
	#intervieweeSet = store.find(User,User.Type == u"interviewee",User.Dept == interviewer.Dept,User.IsEffect != 0)
	interviewSet = interviewer.interviewer_interviewInfos
	for interview in interviewSet:
		list = []
		if(interview.IsOvertime == 1):
			interviewer = store.find(User, User.AccountID == interview.IntervieweeID).one()
			list.append({u'name':interviewer.Name})

	return list

"""

def fillResult(intervieweeID):
	store.rollback()
	usr = store.find(User,User.Name == unicode(intervieweeID,'utf-8')).one()
	session.interviewee = usr.ID
	Include("../../web/interviewer/interviewerHeader.pih",title="填写面试结果")
	Include("../../web/interviewer/fillResult.pih",user = usr)

def setResult(result):
	ID = session.interviewee
	res = unicode(result,'utf-8')
	store.rollback
	store.find(InterviewInfo,InterviewInfo.IntervieweeID == ID).set(Result = res,IsOvertime = 1)
	store.commit()
	Include("../../web/interviewer/interviewerHeader.pih",title="FillResult")
	print "<div align = 'center'>"
	print "<h1>"
	print "success"
	print"</h1></div>"


#**************************************************************************************************
##**************************************************************************************************
class IntervieweeList():
	def __init__(self):
		self.DataList = [{u'no':1,u'ID':u'001',u'name':u'may',u'department':u'softEnterprise'},{u'no':2,u'ID':u'002',u'name':u'tan',u'department':u'softEnterprise'}]
		self.vPool= {u'CList':self.DataList}
	def printPage(self,accountID):
		self.DataList = getIntervieweeList(accountID)
		self.vPool = {u'CList':self.DataList}
		Include("../../web/interviewer/interviewerHeader.pih",title="面试者列表")
		t=Template(file='../web/interviewer/Interviewer_intervieweelist.tmpl',searchList=[self.vPool])
		print t

def getIntervieweeList(accountID):
	store = getStore()
	store.rollback()
	id = accountID.decode('UTF-8')
	interviewer = store.find(User,User.AccountID == id).one()
	intervieweeSet = store.find(User,User.Type == u"interviewee",User.Dept == interviewer.Dept,User.IsEffect != 0)
	
	#resultSet =getInterviewerInterviweInfo(store,id,u"interviewer")
	#i = 1
	list = []
	for interviewee in intervieweeSet:
		b = False
		listtemp = []
		#resultSet = interviewee.interviewee_interviewInfos
		interview = store.find(InterviewInfo,InterviewInfo.IntervieweeID== interviewee.ID)
		
		for result in interview:
			if result==[]:
				pass
			elif result.IsOvertime == 1:
				listtemp.append({u'no':interviewee.ID,u'ID':interviewee.AccountID,u'name':interviewee.Name,u'department':interviewee.Dept})
				#i = i+1
			else:
				pass
		if listtemp != []:
			b = True
			
		if b:
			for itemp in range(len(listtemp)):
				list.append(listtemp[itemp])
		else:
			list.append({u'no':interviewee.ID,u'ID':interviewee.AccountID,u'name':interviewee.Name,u'department':interviewee.Dept})
			#i = i + 1
	return list
#**************************************************************************************************
#
#**************************************************************************************************
def seeResume(resumeId):
	intervieweeID = int(resumeId)
	t = getUserResume(intervieweeID)
	if t == False:
		Include("../../web/interviewer/interviewerHeader.pih",title="查看简历出错")
		print "<div align = 'center'>"
		print "<h1>"
		print " NO RESUME"
		print"</h1></div>"
	else:
		Include("../../web/interviewer/interviewerHeader.pih",title="查看简历")
		Include("../../web/interviewer/seeresume.pih",userID=intervieweeID)
#**************************************************************************************************
def downResume(intervieweeID):
	intervieweeid = int(intervieweeID)
	t = getUserResume(intervieweeid)
	if t == False:
		Include("../../web/interviewer/interviewerHeader.pih",title="查看简历出错")
		print "<div align = 'center'>"
		print "<h1>"
		print " NO RESUME"
		print"</h1></div>"
	else:
		store = getStore()
		resume = store.find(ResumeInfo,ResumeInfo.UserID == intervieweeid).one()
		dir = r'../uploadFiles/'
		fl_dir = resume.ResumePath
		(filedir,filename) = os.path.split(fl_dir)
		dir_src = os.path.join(dir,filename)
		Include("../../web/interviewer/interviewerHeader.pih",title="下载简历")
		Include("../../web/interviewer/downresume.pih",srcdir=dir_src)

		
	
#**************************************************************************************************		
class AppriaseTable():
	def __init__(self):
		self.intervieweeinfo=[]
		self.vPool = {}

	def printPage(self):
		self.vPool ={u'CList':self.intervieweeinfo}
		Include("../../web/interviewer/interviewerHeader.pih",title="填写评议表")
		t=Template(file='../web/interviewer/Interviewer_intervieweelist.tmpl',searchList=[self.vPool])
		print t
		
class Quessioninfo():
	def __init__(self):
		self.DataList = []
		self.vPool={u'CList':self.DataList}
		
	def printPage(self):
		Include("../../web/interviewer/interviewerHeader.pih",title="问题信息")
		t=Template(file='../web/interviewer/Quessions.tmpl',searchList=[self.vPool])
		print t	

class Information():
	def __init__(self):
		self.DataList = []
		self.vPool = {}
	def printPage(self,accountID):
		self.DataList = getInterviewerInfo(accountID)
		self.vPool = {u'CList':self.DataList}
		#print self.DataList
		#raise SCRIPT_END
		
		Include("../../web/interviewer/interviewerHeader.pih",title="个人信息")
		t=Template(file='../web/interviewer/interviewerinfo.tmpl',searchList=[self.vPool])
		print t

class Homepage():
	def __init__(self):
		self.vPool={}
	
	def printPage(self,accountID):
		self.vPool={'AccountID':accountID}
		Include("../../web/interviewer/interviewerHeader.pih",title="主页")
		t=Template(file='../web/interviewer/interviewerHomePage.tmpl',searchList=[self.vPool])
		print t

def bookInterveiw(intervieweeID):
	session.interviewee = intervieweeID
	Include("../../web/interviewer/interviewerHeader.pih",title="预约面试")
	Include("../../web/interviewer/yudingmianshi.pih")

def addInterview(time,place):
	if time == None or place == None:
		Include("../../web/interviewer/interviewerHeader.pih",title="主页")
		print "<div align = 'center'>"
		print "<h1>"
		print "You must Fill the blank"
		print"</h1></div>"
	else:
		accountID = unicode(session.accountID,'utf-8')
		interviewer = store.find(User,User.AccountID == accountID).one()
		dept = interviewer.Dept
		Time = unicode(time)
		Place = unicode(place)
		ID = random.randrange(1000,9999)
		store.rollback()
		interview = InterviewInfo(ID,u'',Place,0,Time,dept,0)
		interview.IntervieweeID = int(session.interviewee)
		store.add(interview)

		interviewer.interviewer_interviewInfos.add(interview)
		#*************************************************
		#
		#*************************************************
		

		store.commit()
		Include("../../web/interviewer/interviewerHeader.pih",title="主页")
		print "<div align = 'center'>"
		print "<h1>"
		print "success"
		print"</h1></div>"
		session.interviewee = None
	
def getInterviewerInfo(accountID):
	store = getStore()
	store.rollback()
	aID = accountID.decode('UTF-8')
	interviewerinfo = store.find(User,User.AccountID == aID).one()
	list = []
	list.append({'name':interviewerinfo.Name,'dept': interviewerinfo.Dept})
	
	return list

def index(accountID):
	#print accountID
	#raise SCRIPT_END
	
	session.accountID = accountID
	obj = Homepage()
	obj.printPage(session.accountID)
	

def calendar():
	if session.accountID != None:
		obj = Calender()
		obj.printPage(session.accountID)
def intervieweeList():
	if session.accountID != None:
		obj = IntervieweeList()
		obj.printPage(session.accountID)
def appriaseTable():
	Include("../../web/interviewer/interviewerHeader.pih",title="填写评议表")
	print "<div align = 'center'>"
	print "<h1>"
	print "on Building"
	print"</h1></div>"
	
def information():
	obj = Information()
	obj.printPage(session.accountID)
def quessioninfo():
	obj = Quessioninfo()
	obj.printPage()

def exit():
	session.close()
	raise HTTP_REDIRECTION,"../../web/login.pih"

def editPassword():
	Include("../../web/interviewer/interviewerHeader.pih",title="修改密码")
	Include("../../web/interviewer/editPassword.pih")


def resetPassword(pwd1,pwd2, pwd3):
	id = unicode(session.accountID,'utf-8')
	user = store.find(User,User.AccountID == id).one()
	password1 = unicode(pwd1,'utf-8')
	password2 = unicode(pwd2,'utf-8')
	if pwd2 != pwd3:
		Include("../../web/interviewer/interviewerHeader.pih",title="修改密码")
		print "<div align = 'center'>"
		print "<h1>"
		print "the twice password you filled are different"
		print"</h1></div>"
	else:
		if user.Pwd == password1:
			store.find(User,User.AccountID == id).set(Pwd = password2)
			store.commit()
			Include("../../web/interviewer/interviewerHeader.pih",title="主页")
			print "<div align = 'center'>"
			print "<h1>"
			print "success"
			print"</h1></div>"
		else:
			Include("../../web/interviewer/interviewerHeader.pih",title="主页")
			print "<div align = 'center'>"
			print "<h1>"
			print u"The old password is wrong"
			print"</h1></div>"

	