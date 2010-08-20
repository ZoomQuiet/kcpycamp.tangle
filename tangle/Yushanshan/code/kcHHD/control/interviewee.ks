from Cheetah.Template import Template
from webapps.kcHHD.model.kvhhd_orm import *
from webapps.kcHHD.model.db import *

class Calendar:
	def __init__(self):
		self.DataList =[]
		self.vPool={}
	def printPage(self):
		self.DataList = getCalendarList()
		self.vPool={'CList':self.DataList}
		Include("../../web/intervieweeHeader.pih",title="Calendar")
		t=Template(file='../web/Calender.tmpl',searchList=[self.vPool])
		print t

class Result:
	def __init__(self):
		self.DataList =[]
		self.vPool={}
	def printPage(self):
		self.DataList = getResultList()
		self.vPool={'CList':self.DataList}
		Include("../../web/intervieweeHeader.pih",title="Result")
		t=Template(file='../web/Result.tmpl',searchList=[self.vPool])
		print t
	
		
class Resume():
	def __init__(self):
		self.vPool={'ID':123,'Name':'name','CardID':1232,'Sex':'boy',\
				    'School':'asd','Subject':'asdf','Grade':'asdf',\
					'Telephone':'asdf','Native':'asdf','Addr':'asdf',\
				    'AddrPhone':'asdf','Email':'asdf','QQ':'asdf',\
				    'ForeignLanguage':'asdf','Character':'asdf',\
					'Programming':'asdf','Character':'asdf',\
				    'Programming':'asdf','MathAndPhysics':'asdf',\
				    'Scholarships':'asdf','Project':'asdf','SchoolDuty':'asdf',\
				    'MoreInfo':'asdf','Advice':'asdf','ResumePath':'asdf',\
				    'PhotoPath':'asdf','UserID':'asdf'}
	
	def printPage(self):
		Include("../../web/intervieweeHeader.pih",title="Resume")
		t=Template(file='../web/resume.tmpl',searchList=[self.vPool])
		print t

		

class Homepage():
	def __init__(self):
		self.vPool={'AccountID':'sara'}
	def printPage(self):
		Include("../../web/intervieweeHeader.pih",title="Homepage")
		t=Template(file='../web/intervieweeHomePage.tmpl',searchList=[self.vPool])
		print t

def index():
	obj = Homepage()
	obj.printPage()

def calendar():
	obj = Calendar()
	obj.printPage()
def resume():
	#obj = Resume()
	#obj.printPage()
	Include("../../web/intervieweeHeader.pih",title="FillResume")
	Include("../../web/resume.pih")

def uploadresume():
	Include("../../web/intervieweeHeader.pih",title="UpLoad Resume")
	Include("../../web/Uploadfile.pih")

def result():
	obj = Result()
	obj.printPage()

#面试者查看日程
#返回该面试者所有日程的tuple

def modifyResume():
	Include("../../web/intervieweeHeader.pih",title="Modify Resume")
	Include("../../web/modifyresume.pih")
def showResume():
	Include("../../web/intervieweeHeader.pih",title="Show Resume")
	Include("../../web/seeresume.pih")


def getIntervieweeInterviewInfo(store, id, userType):
    if userType == u'interviewee':
        interviewee = store.find(User, User.AccountID == id).one()
        #print interviewee.Name
        interviewSet = interviewee.interviewee_interviewInfos
        #print [result.Addr for result in interviewSet]
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


def getCalendarList():
	store = getStore()
	store.rollback()
	resultSet = getIntervieweeInterviewInfo(store, u'sara',u'interviewee')
	i = 1
	list = []
	for result in resultSet:
		list.append({'no':i,'time':result.DateTime,'place':result.Addr})
		i = i + 1
	#store.close()
	return list


def getResultList():
	store = getStore()
	store.rollback()
	resultSet = getIntervieweeInterviewInfo(store, u'sara',u'interviewee')
	i = 1
	list = []
	for result in resultSet:
		list.append({'no':i,'time':result.DateTime,'place':result.Addr,'result':result.Result})
		i = i + 1
	return list