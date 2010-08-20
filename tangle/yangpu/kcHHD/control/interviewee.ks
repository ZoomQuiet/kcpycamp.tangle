from Cheetah.Template import Template
from webapps.kcHHD.model.kvhhd_orm import *
from webapps.kcHHD.conf.db import *
from webapps.kcHHD.service.UserServic import *

sess = Session()
if not hasattr(sess, 'accountID'):
	sess.accountID = None
if not hasattr(sess, 'ID'):
	sess.ID = None

class Calendar():
	def __init__(self):
		self.DataList =[]
		self.vPool={}
	def printPage(self,accountID):
		self.DataList = getCalendarList(accountID)
		self.vPool={'CList':self.DataList}
		Include("../../web/interviewee/intervieweeHeader.pih",title="Calendar")
		t=Template(file='../web/interviewee/Calender.tmpl',searchList=[self.vPool])
		print t


class Result():
	def __init__(self):
		self.DataList =[]
		self.vPool={}
	def printPage(self,accountID):
		self.DataList = getResultList(accountID)
		self.vPool={'CList':self.DataList}
		Include("../../web/interviewee/intervieweeHeader.pih",title="Result")
		t=Template(file='../web/interviewee/Result.tmpl',searchList=[self.vPool])
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
		self.vPool={}
		
	def printPage(self,accountID):
		self.vPool={'AccountID':accountID}
		Include("../../web/interviewee/intervieweeHeader.pih",title="HomePage")
		t=Template(file='../web/interviewee/intervieweeHomePage.tmpl',searchList=[self.vPool])
		print t
		

def index(accountID,id):
	sess.accountID = accountID
	sess.ID = id
	obj = Homepage()
	obj.printPage(accountID)
	#print sess.accountID

def calendar():
	if sess.accountID != None:
		obj = Calendar()
		obj.printPage(sess.accountID)
	else:
		print"��û��½"
def resume():
	#obj = Resume()
	#obj.printPage()
	id = int(sess.ID)	
	t = getUserResume(id)
	if t == True:
		Include("../../web/interviewee/intervieweeHeader.pih",title="FillResume")
		print "<div align = 'center'>"
		print "<h1>"
		print "YOU HAVE FILLED YOUR RESUME"
		print"</h1></div>"
	else:
		Include("../../web/interviewee/intervieweeHeader.pih",title="FillResume")
		Include("../../web/interviewee/resume.pih",userID=sess.ID)

def uploadresume():
	Include("../../web/interviewee/intervieweeHeader.pih",title="UpLoad Resume")
	Include("../../web/interviewee/Uploadfile.pih")

def result():
	obj = Result()
	obj.printPage(sess.accountID)

#面试者查看日程
#返回该面试者所有日程的tuple

def modifyResume():
	id = int(sess.ID)
	t = getUserResume(id)
	if t == False:
		Include("../../web/interviewee/intervieweeHeader.pih",title="Modify Resume")
		print "<div align = 'center'>"
		print "<h1>"
		print "YOU HAVE NOT FILLED YOUR RESUME"
		print"</h1></div>"
	else:
		Include("../../web/interviewee/intervieweeHeader.pih",title="Modify Resume")
		Include("../../web/interviewee/modifyresume.pih",userID=sess.ID)
def showResume():
	id = int(sess.ID)
	t = getUserResume(id)
	if t == False:
		Include("../../web/interviewee/intervieweeHeader.pih",title="Modify Resume")
		print "<div align = 'center'>"
		print "<h1>"
		print "YOU HAVE NOT FILLED YOUR RESUME"
		print"</h1></div>"
	else:
		Include("../../web/interviewee/intervieweeHeader.pih",title="Show Resume")
		Include("../../web/interviewee/seeresume.pih",userID=sess.ID)

def exit():
	sess.close()
	raise HTTP_REDIRECTION,"../../web/login.pih"


def getIntervieweeInterviewInfo(store, id, userType):
    if userType == u'interviewee':
        interviewee = store.find(User, User.AccountID == id).one()
        interviewSet = interviewee.interviewee_interviewInfos
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


def getCalendarList(accountID):
	store = getStore()
	store.rollback()
	id = accountID.decode("UTF-8")	
	resultSet = getIntervieweeInterviewInfo(store, id,u'interviewee')
	i = 1
	list = []
	for result in resultSet:
		list.append({'no':i,'time':result.DateTime,'place':result.Addr})
		i = i + 1
	#store.close()
	return list


def getResultList(accountID):
	store = getStore()
	store.rollback()
	id = accountID.decode('UTF-8')
	resultSet = getIntervieweeInterviewInfo(store, id,u'interviewee')
	i = 1
	list = []
	for result in resultSet:
		list.append({'no':i,'time':result.DateTime,'place':result.Addr,'result':result.Result})
		i = i + 1
	return list


def logout():
    session.close()

    
def check_resume(CardID,Name,Sex,School,Subject,Grade,Telephone,Native,Addr,AddrPhone,Email,QQ,ForeignLanguage,Character,Programming,MathAndPhysics,Scholarships,Project,SchoolDuty,MoreInfo,Advice):
	store = getStore()
	id = CardID.decode("UTF-8") 			#1
	name = Name.decode("UTF-8")   			#21
	sex = Sex.decode("UTF-8")   			#2
	school = School.decode("UTF-8")			#3
	subject = Subject.decode("UTF-8")		#4	
	grade = Grade.decode("UTF-8")			#5	
	telephone = Telephone.decode("UTF-8")		#6
	native = Native.decode("UTF-8")			#7
	addr = Addr.decode("UTF-8")			#8
	addrphone = AddrPhone.decode("UTF-8")		#9
	email = Email.decode("UTF-8")			#10
	qq = QQ.decode("UTF-8")				#11
	foreignLanguage = ForeignLanguage.decode("UTF-8")#12
	character = Character.decode("UTF-8")		#13
	programming = Programming.decode("UTF-8")	#14
	mathAndPhysics = MathAndPhysics.decode("UTF-8")	#15
	scholarships = Scholarships.decode("UTF-8")	#16
	project = Project.decode("UTF-8")		#17
	schoolDuty = SchoolDuty.decode("UTF-8")		#18
	moreInfo = MoreInfo.decode("UTF-8")		#19
	advice = Advice.decode("UTF-8")			#20

	number = random.randrange(1000,9999);
	#user = store.find(User, User.AccountID == session.UserID).one()

	t = ResumeInfo()
	t.ID = number
	t.CardID = id
	t.Name = name
	t.Sex = sex
	t.School = school
	t.Subject = subject
	t.Grade = grade
	t.Telephone = telephone
	t.Native = native
	t.Addr = addr
	t.AddrPhone = addrphone
	t.Email = email
	t.QQ = qq
	t.ForeignLanguage = foreignLanguage
	t.Character = character
	t.Programming = programming
	t.MathAndPhysics = mathAndPhysics
	t.Scholarships = scholarships
	t.Project = project
	t.SchoolDuty = schoolDuty
	t.MoreInfo = moreInfo
	t.Advice = advice
	t.UserID = session.UserID
#	t =ResumeInfo(number,id,name,sex,school,subject,grade,telephone,native,addr,addrphone,email,qq,foreignLanguage,character,programming,mathAndPhysics,scholarships,project,schoolDuty,moreInfo,advice,userid)

	#t = ResumeInfo(9,u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9',u'10',u'11',u'12',u'13',u'14',u'15',u'16',u'17',u'18',u'19',u'20',584)
	store.add(t)
	store.commit()
	Include("../../web/interviewee/intervieweeHeader.pih",flash= '����ɹ�')

def modify_resume(CardID,Name,Sex,School,Subject,Grade,Telephone,Native,Addr,AddrPhone,Email,QQ,ForeignLanguage,Character,Programming,MathAndPhysics,Scholarships,Project,SchoolDuty,MoreInfo,Advice):
	store = getStore()
	id = CardID.decode("UTF-8") 			#1
	name = Name.decode("UTF-8")   			#21
	sex = Sex.decode("UTF-8")   			#2
	school = School.decode("UTF-8")			#3
	subject = Subject.decode("UTF-8")		#4	
	grade = Grade.decode("UTF-8")			#5	
	telephone = Telephone.decode("UTF-8")		#6
	native = Native.decode("UTF-8")			#7
	addr = Addr.decode("UTF-8")			#8
	addrphone = AddrPhone.decode("UTF-8")		#9
	email = Email.decode("UTF-8")			#10
	qq = QQ.decode("UTF-8")				#11
	foreignLanguage = ForeignLanguage.decode("UTF-8")#12
	character = Character.decode("UTF-8")		#13
	programming = Programming.decode("UTF-8")	#14
	mathAndPhysics = MathAndPhysics.decode("UTF-8")	#15
	scholarships = Scholarships.decode("UTF-8")	#16
	project = Project.decode("UTF-8")		#17
	schoolDuty = SchoolDuty.decode("UTF-8")		#18
	moreInfo = MoreInfo.decode("UTF-8")		#19
	advice = Advice.decode("UTF-8")			#20
	store.find(ResumeInfo, ResumeInfo.UserID == int(sess.ID)).set(Name = name,Sex = sex,School = school,Subject = subject, CardID = id, Grade= grade,Telephone = telephone,QQ = qq, Native = native,Addr = addr,AddrPhone =addrphone,Email = email,ForeignLanguage = foreignLanguage, Character = character,Programming = programming, MathAndPhysics = mathAndPhysics,Scholarships = scholarships, Project = project,SchoolDuty = schoolDuty,MoreInfo = moreInfo,Advice = advice)
	store.commit()
	Include("../../web/interviewee/intervieweeHeader.pih",title="HomePage")

    
