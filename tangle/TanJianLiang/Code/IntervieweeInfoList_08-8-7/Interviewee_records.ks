import PyDbLite

db=PyDbLite.Base('Interviewee_records.pdl')
db.create("Name","ID",mode="open")

def index():
    if len(db):
        Include("../Interviewee_recordsHeader.pih",title="My record collection")
        print '<h1>IntervieweeInfoList</h1>'
        print '<table class="main" cellpadding="3" cellspacing="0">'
        print '<tr><th>Name</th><th>ID</th>'
        print '<th>&nbsp;</th><th>&nbsp;</th></tr>\n'
        for record in db:
            print '<tr>'
            print '<td class="main">%s</td><td class="main">%s</td>' %(record['Name'],record['ID'])
            print '<td class="main"><a href="removeRecord?recordId=%s">' %record['__id__']
            print 'Remove</a></td>'
            print '<td class="main"><a href="editRecord?recordId=%s">' %record['__id__']
            print 'Edit</a></td>'
            print '</tr>'
        print '</table>'
    else:
        print "No record in this collection"

    print '<p><a href="editRecord?recordId=-1">Add New Interviewee</a>'
    print '</body>\n</html>'

def editRecord(recordId):
    recordId=int(recordId)
    if recordId>-1:
        record=db[recordId]
        name,id=record['Name'],record['ID']
        Include("../Interviewee_recordsHeader.pih",title="Editing record %s" %recordId)
        print "<h1>Editing a record</h1>"
    else:
        name,id='',''
        Include("../Interviewee_recordsHeader.pih",title="New Interviewee")
        print "<h1>New Interviewee</h1>"
    
    print '<form action="insertRecord">'

    print '<input type="hidden" name="recordId" value="%s">' %recordId
    print '<table>'
    print '<tr><td>Name</td><td><input name="title" size="40" value="%s"></td></tr>' %name
    print '<tr><td>ID</td><td><input name="artist" size="40" value="%s"></td></tr>' %id
    print '</table>'
    print '<input type="submit" value="Ok">'
    print '</form>'
    print '</body>\n</html>'

def insertRecord(recordId,title,artist):
    recordId=int(recordId)
    if recordId==-1:
        db.insert(Name=title,ID=artist)
    else:
        db.update(db[recordId],Name=title,ID=artist)
    db.commit()
    raise HTTP_REDIRECTION,"index"

def removeRecord(recordId):
    del db[int(recordId)]
    db.commit()
    raise HTTP_REDIRECTION,"index"
