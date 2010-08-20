from storm.locals import *
from webapps.kcHHD.model.kvhhd_orm import *
from webapps.kcHHD.model.db import *
import random
	
class Test(object):
	__storm_table__ = 'test'
	id = Int(primary = True)
	name = Unicode()
	def __init__(self,name):
		self.name = name



def check_register(id, name, password,cpassword, UserDept = None):
	store = getStore()
	number = random.randrange(0,1001)
	id = id.decode("UTF-8")
	n  = name.decode("UTF-8")
	type = u"interviewee"
	#psw = unicode(password)
	psw =password.decode("UTF-8")
	#p = User(number,id,n,type,psw,UserDept)
	p = User(number,n,type,psw,id,UserDept)
	store.add(p)
	store.commit()
	Session().user = name
	raise HTTP_REDIRECTION,"../interviewee.ks/index"

def check_resume(CardID,Name,Sex,School,Subject,Grade,Telephone,Native,Addr,AddrPhone,Email,QQ, \
		ForeignLanguage,Character,Programming,MathAndPhysics,Scholarships,Project,SchoolDuty,MoreInfo,Advice):
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

	number = random.randrange(0,1001);
	user = store.find(User, User.Name == name).one()

	userid = user.ID
	
	t =Interviewee(number,id,name,sex,school,subject,grade,telephone,native,addr,addrphone,email,qq,foreignLanguage,character,programming,mathAndPhysics,scholarships,project,schoolDuty,moreInfo,advice,userid)
	store.add(t)

#	t = Interviewee(u'89',u'2',u'3',u'4',u'5',u'6',u'7',u'8',u'9',u'10',u'11',u'12',u'13',u'14',u'15',u'16',u'17',u'18',u'19',u'20',u'21')
	store.add(t)
	store.commit()

	user = store.find(User, User.ID == 353).one()
	
	
	


	
def check_modify_resume(CardID,Name,Sex,School,Subject,Grade,Telephone,Native,Addr,AddrPhone,Email,QQ, \
		ForeignLanguage,Character,Programming,MathAndPhysics,Scholarships,Project,SchoolDuty,MoreInfo,Advice):
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
	store.find(ResumeInfo, ResumeInfo.UserID == 54).set(Name = name,Sex = sex, School = school,Subject = subject, CardID = id, Grade= grade, Telephone = telephone,QQ = qq, Native = native, Addr = addr,AddrPhone =addrphone,Email = email, ForeignLanguage = foreignLanguage, Character = character,Programming = programming, MathAndPhysics = mathAndPhysics, Scholarships = scholarships, Project = project, SchoolDuty = schoolDuty,MoreInfo = moreInfo,Advice = advice)
	store.commit()

	
	raise HTTP_REDIRECTION,"../interviewee.ks/index"



