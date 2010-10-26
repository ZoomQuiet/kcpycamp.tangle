import datetime
import calendar

so = Session()
if not hasattr(so, 'countmonth'):
    so.countmonth = 0

class mycalendar():
    def __init__(self):
        self.today = datetime.date.today()
        self.setcurrentdate(self.today.year,self.today.month,self.today.day)
        self.daydict={2008:{8:{9:0,8:2,7:3},7:{1:4,2:5,5:6,8:7,7:8}},2007:{8:{8:9,9:10}}}
    def setcurrentdate(self, year, month, day):
        self.currentyear = year
        self.currentmonth = month
        self.currentday = day
    def setcurrentsessiondate(self, cm):
        self.setcurrentdate(self.today.year,self.today.month,self.today.day)
        self.currentmonth += int(cm)
        self.currentyear += self.currentmonth/12+1
        self.currentmonth = self.currentmonth%12+1
    def daystatus(self,y=None,m=None,d=None):
        if self.daydict.get(y) == None:
            return -2 #No year
        if self.daydict[y].get(m) == None:
            return -1 #No month
        if d == None:
            return 2  #have month
        if self.daydict[y][m].get(m) == None:
            return 0  #No day
        else:
            return 1  #yes get datetime
    def addcalendar(self,y=0,m=0,d=0):
        staus = self.daystatus(y,m,d)
        if staus == 1:
            return False
        elif staus == 0:
            self.daydict[y][m].append(d)
            self.daydict[y][m].sort()
        elif staus == -1:
            self.daydict[y][m]=[]
            self.daydict[y][m].append(d)
        elif staus == -2:
            self.daydict[y]={}
            self.daydict[y][m]=[d]
            self.daydict[y][m]=[]
            self.daydict[y][m].append(d)
    def removecalendar(self,y=0,m=0,d=0):
        if self.daystatus(y,m,d) == 1:
            self.daydict[y][m].remove(d)
            return True
        else:
            return False
    def printcalendar(self):
        dayList = []
        if self.daystatus(self.currentyear,self.currentmonth) == 2:
            dayList = self.daydict[self.currentyear][self.currentmonth].keys()

        print '''<style type="text/css">
                span.today
                {
                background-color:#FF3064
                }
                span.calendarday 
                {
                color : #FFFFFF;
                background-color : #001F64;
                }
                </style>
                <meta http-equiv="Content-Type" content="text/html; charset=windows-1252">
                <table cellspacing="10">
                <tr><td valign="top">
                '''
        print '<pre>'
        print '<a href="setcurrentmonth?monthtemp=-12"><</a>%s<a href="setcurrentmonth?monthtemp=12">></a>    <a href="setcurrentmonth?monthtemp=-1"><=</a>%s<a href="setcurrentmonth?monthtemp=1">=></a>'%(self.currentyear,self.currentmonth)
        print '<span class="calendarday"> Mon Tue Wed Thu Fri <span class="today">Sat Sun </span></span>'
        for week in calendar.monthcalendar(self.currentyear, self.currentmonth):
            ws = ''
            for day in week:
                if day == 0:
                    ws += '    '
                elif self.currentyear == self.today.year and self.currentmonth==self.today.month and day == self.currentday:
                    ws += '<span class="today">%3s </span>'%day
                elif dayList.count(day) > 0:
                    ws += '<a href="delday?y=%s&m=%s&d=%s"><span class="calendarday">%3s </span></a>'%(self.currentyear,self.currentmonth,day,day)
                else:
                    ws += '<a href="addday?y=%s&m=%s&d=%s">%3s </a>'%(self.currentyear,self.currentmonth,day,day)
            print ws
        print '</pre>'
        print self.daydict
obj = mycalendar()
def index(count=0):
    obj.setcurrentsessiondate(int(so.countmonth))
    obj.printcalendar()
def setcurrentmonth(monthtemp = 0):
    so.countmonth = int(so.countmonth)
    so.countmonth += int(monthtemp)
    raise HTTP_REDIRECTION,"index?count=%s"%monthtemp
def addday(y=None, m=None, d=None):
    y=int(y)
    m=int(m)
    d=int(d)
    obj.addcalendar(y,m,d)
    raise HTTP_REDIRECTION,"index"    
def delday(y=None, m=None, d=None):
    y=int(y)
    m=int(m)
    d=int(d)
    obj.removecalendar(y,m,d)
    raise HTTP_REDIRECTION,"index"
       