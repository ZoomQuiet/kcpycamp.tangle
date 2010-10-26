from HTMLTags import *
import PyDbLite
from pythontemplate import *
db=PyDbLite.Base('records.pdl')
db.create("title","artist",mode="open")

class IntervieweeList_Template(DictionaryTemplate):
    _template = """
                <h1>My record collection</h1>
                <table class="main" cellpadding="3" cellspacing="0">
                
                <tr><th>Title</th><th>Artist</th>
                %(lst|li|li1)s
                </table>
                """

class Interviewee_Template(ListTemplate):
    _template = """
                <tr>
                <td class="main">%(title)s</td><td class="main">%(artist)s</td>
                <td class="main"><a href="removeRecord?recordId=%(record)s">
                Remove</a></td>
                <td class="main"><a href="editRecord?recordId=%(record)s">
                Edit</a></td>
                </tr>"""
def index():
    articles=[]
    if len(db):
        Include("../recordsHeader.pih",title="My record collection")
        print A(_("Start new thread"), href='record')
        for record in db:
            dirt = {"title": record['title'],"artist": record['artist'],"record": record['__id__'],"record": record['__id__']}
            articles.append(dirt)
        print IntervieweeList_Template(lst=articles, li=Interviewee_Template)	
    else:
        print "No record in this collection"
    print '<p><a href="editRecord?recordId=-1">New record</a>' 
def editRecord(recordId):
    recordId=int(recordId)
    if recordId>-1:
        record=db[recordId]
        title,artist=record['title'],record['artist']
        Include("../recordsHeader.pih",title="Editing record %s" %recordId)
        print "<h1>Editing a record</h1>"
    else:
        title,artist='',''
        Include("../recordsHeader.pih",title="New record")
        print "<h1>New record</h1>"
    
    print '<form action="insertRecord">'
    print '<input type="hidden" name="recordId" value="%s">' %recordId
    print '<table>'
    print '<tr><td>Title</td><td><input name="title" size="40" value="%s"></td></tr>' %title
    print '<tr><td>Artist</td><td><input name="artist" size="40" value="%s"></td></tr>' %artist
    print '</table>'
    print '<input type="submit" value="Ok">'
    print '</form>'
    print '</body>\n</html>'

def insertRecord(recordId,title,artist):
    recordId=int(recordId)
    if recordId==-1:
        db.insert(title=title,artist=artist)
    else:
        db.update(db[recordId],title=title,artist=artist)
    db.commit()
    raise HTTP_REDIRECTION,"index"

def removeRecord(recordId):
    del db[int(recordId)]
    db.commit()
    raise HTTP_REDIRECTION,"index"
def record():
    raise HTTP_REDIRECTION,"index" 
