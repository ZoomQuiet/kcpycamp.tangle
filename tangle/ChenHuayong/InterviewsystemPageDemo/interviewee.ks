from Cheetah.Template import Template
class Calendar:
	def __init__(self):
		self.DataList = [{'no':1,'time':'2008-8-10','place':'wps'},{'no':2,'time':'2008-8-10','place':'wps'}]
		self.vPool={'CList':self.DataList}
	def printPage(self):
		Include("../intervieweeHeader.pih",title="Calendar")
		t=Template(file='Calender.tmpl',searchList=[self.vPool])
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
	#def ResetResume(ID=0,Name=0,CardID=0,Sex=0,School=0,Subject=0,Grade=0,Telephone=0,Native=0,Addr=0,
	#			    AddrPhone=0,Email=0,QQ=0,ForeignLanguage=0,Character=0,Programming=0,Character=0,
	#			    Programming=0,MathAndPhysics=0,Scholarships=0,Project=0,SchoolDuty=0,MoreInfo=0,
	#				Advice=0,ResumePath=0,PhotoPath=0,UserID=0):		
	def printRestPage(self):
		Include("../intervieweeHeader.pih",title="Resume")
		t=Template(file='resetresume.tmpl',searchList=[self.vPool])
		print t	
	def printPage(self):
		Include("../intervieweeHeader.pih",title="Resume")
		t=Template(file='resume.tmpl',searchList=[self.vPool])
		print t	
def index():
	calendar()

def calendar():
	obj = Calendar()
	obj.printPage()
def resume():
	obj = Resume()
        obj.printPage()
def resetresume():
	obj = Resume()
	obj.printRestPage()
def uploadresume():
	Include("../intervieweeHeader.pih",title="UpLoad Resume")
	Include("../Uploadfile.pih")

def result():
	Include("../intervieweeHeader.pih",title="Result")
	print "pass"

	