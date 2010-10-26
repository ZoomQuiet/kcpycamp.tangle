from Cheetah.Template import Template
from webapps.kcHHD.model.kvhhd_orm import *
from webapps.kcHHD.conf.db import *
from webapps.kcHHD.service.UserServic import *

session = Session()
if not hasattr(session, 'accountID'):
	session.accountID = None
	
class Calender():
	def __init__(self):
		self.DataList = [{'no':1,'time':'2008-8-10','place':'wps'},{'no':2,'time':'2008-8-10','place':'wps'}]
		self.vPool={'CList':self.DataList}
		#self.DataList = []
		#self.vPool= {}
	def printPage(self,ID):
		#self.DataList = getCalendarList_interviewer(ID)
		#self.vPool={'CList':self.DataList}
		Include("../../web/interviewer/interviewerHeader.pih",title="Calendar")
		t=Template(file='../web/interviewer/Calender.tmpl',searchList=[self.vPool])
		print t


	
class IntervieweeList():
	def __init__(self):
		self.DataList = [{'no':1,'ID':'001','name':'may','department':'softEnterprise'},{'no':2,'ID':'002','name':'tan','department':'softEnterprise'}]
		self.vPool= {'CList':self.DataList}
	def printPage(self):
		Include("../../web/interviewer/interviewerHeader.pih",title="IntervieweeList")
		t=Template(file='../web/interviewer/Interviewer_intervieweelist.tmpl',searchList=[self.vPool])
		print t
		
class AppriaseTable():
	def __init__(self):
		self.intervieweeinfo=[{'name':'may','sex':'boy','graduated':'北京师范大学','speciality':'software'}]
		self.vPool = {}

	def printPage(self):
		self.vPool ={'CList':self.intervieweeinfo}
		Include("../../web/interviewer/interviewerHeader.pih",title="IntervieweeList")
		t=Template(file='../web/interviewer/Interviewer_intervieweelist.tmpl',searchList=[self.vPool])
		print t
		
class Quessioninfo():
	def __init__(self):
		self.DataList = [{'no':1,'maintype':'编程能力','type':'开发环境','quession':'没人够你帅'},{'no':2,'maintype':'编程能力','type':'开发环境','quession':'没人要？'}]
		self.vPool={'CList':self.DataList}
		
	def printPage(self):
		Include("../../web/interviewer/interviewerHeader.pih",title="IntervieweeList")
		t=Template(file='../web/interviewer/Quessions.tmpl',searchList=[self.vPool])
		print t	

class Information():
	def __init__(self):
		self.DataList = []
		self.vPool = {'name':'小小','dept':'软件事业部'}
	def printPage(self,accountID):
		self.DataList = getInterviewerInfo(accountID)
		self.vPool = {'CList':self.DataList}
		#print self.DataList
		#raise SCRIPT_END
		
		Include("../../web/interviewer/interviewerHeader.pih",title="IntervieweeList")
		t=Template(file='../web/interviewer/interviewerinfo.tmpl',searchList=[self.vPool])
		print t

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
	session.accountID =accountID
	calendar()

def calendar():
	if session.accountID != None:
		obj = Calender()
		obj.printPage(session.accountID)
def intervieweeList():
	obj = IntervieweeList()
	obj.printPage()
def appriaseTable():
	#Include("../../web/interviewer/interviewerHeader.pih",title="AppriaseTable")
	atable =AppriaseTable()
	atable.printPage()
	#pass
def information():
	obj = Information()
	obj.printPage(session.accountID)
def quessioninfo():
	obj = Quessioninfo()
	obj.printPage()
	