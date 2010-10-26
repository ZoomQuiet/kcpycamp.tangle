from Cheetah.Template import Template
class Calender:
	def __init__(self):
		self.DataList = [{'no':1,'time':'2008-8-10','place':'wps'},{'no':2,'time':'2008-8-10','place':'wps'}]
		self.vPool={'CList':self.DataList}
	def printPage(self):
		Include("../interviewerHeader.pih",title="Calendar")
		t=Template(file='Calender.tmpl',searchList=[self.vPool])
		print t	
class IntervieweeList():
	def __init__(self):
		self.DataList = [{'no':1,'ID':'001','name':'may','department':'softEnterprise'},{'no':2,'ID':'002','name':'tan','department':'softEnterprise'}]
		self.vPool={'CList':self.DataList}
	def printPage(self):
		Include("../interviewerHeader.pih",title="IntervieweeList")
		t=Template(file='Interviewer_intervieweelist.tmpl',searchList=[self.vPool])
		print t	
class AppriaseTable():
	def __init__(self):
		self.intervieweeinfo=[{'name':'may','sex':'boy','graduated':'����ʦ����ѧ','speciality':'software'}]
	

	def printPage(self):
		Include("../interviewerHeader.pih",title="IntervieweeList")
		t=Template(file='Interviewer_intervieweelist.tmpl',searchList=[self.vPool])
		print t	
class Quessioninfo():
	def __init__(self):
		self.DataList = [{'no':1,'maintype':'�������','type':'��������','quession':'û�˹���˧'},{'no':2,'maintype':'�������','type':'��������','quession':'û��Ҫ��'}]
		self.vPool={'CList':self.DataList}
	def printPage(self):
		Include("../interviewerHeader.pih",title="IntervieweeList")
		t=Template(file='Quessions.tmpl',searchList=[self.vPool])
		print t	

class Information():
	def __init__(self):
		self.vPool = {'name':'СС','dept':'�����ҵ��','job':'�������ʦ'}
	def printPage(self):
		Include("../interviewerHeader.pih",title="IntervieweeList")
		t=Template(file='interviewerinfo.tmpl',searchList=[self.vPool])
		print t	
	

def index():
	calendar()

def calendar():
	obj = Calender()
	obj.printPage()
def intervieweeList():
	obj = IntervieweeList()
	obj.printPage()
def appriaseTable():
	Include("../interviewerHeader.pih",title="AppriaseTable")
	pass
def information():
	obj = Information()
	obj.printPage()
def quessioninfo():
	obj = Quessioninfo()
	obj.printPage()
	