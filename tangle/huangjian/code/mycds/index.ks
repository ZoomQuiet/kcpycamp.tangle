import db
def index():
    print "<h1>My record collection</h1>"
    
    # login / logout
    logged = hasattr(Session(),"user") and Session().user is not None
    if logged:
        print 'Logged in as %s<br>' %Session().user
        print '<a href="logout">Logout</a><p>'
    else:
        print '<a href="login">Login</a><p>'

    # print existing records
    cds = db.read('mycds.db')
    if cds:
	print '<table border="1">'
	print '<tr><th>Artist</th><th>Title'
	print '</th></tr>'*2
	for num,(artist,title) in enumerate(cds):
		print '<tr><td>%s</td><td>%s</td>' %(artist, title)
		if logged:
			print '<td><a href="edit?num=%s">Edit</a></td>' %num
			print '<td><a href="remove?num=%s">Remove</a></td>' %num
		print '</tr>'
        #for (artist,title) in cds:
        	#print '<tr><td>%s</td><td>%s</td></tr>' %(artist, title)
	print '</table><p>'
    else:
        print "No CD in the collection<p>"

    # prompt logged in users to enter a new record
    if logged:
        print '<a href="new_cd">Enter new CD</a><p>'

    # page counter
    Include('../counter.py',counter_file='counter.txt')

def login():
	print '<h1>Login</h1>'
	print '<form action = "check_login" method = "post">'
	print 'Login<input name = "login"><br>'
	print 'Password<input type = "password" name = "password"><br>'
	print '<input type= "submit" value ="ok">'
	print '</from>'

def check_login(login,password):
    if login=="huang" and password=="huang":
	Session().user = login
	print "Hello ",login
	print "logged in"
	raise HTTP_REDIRECTION,"index"
    else:
        print "try again"

def logout():
    Session().user = None
    raise HTTP_REDIRECTION,"index"

def new_cd():
	print '<h1>ADD new CD'
	print '<form action = "add_new_cd" method = "post">'
	print 'Artist<input name = "artist">'
	print 'Title<input name = "title"><br>'
	print '<input type = "submit" value = "ok">'
	print '</form>'

def add_new_cd(artist, title):
	cds = db.read('mycds,db')
	cds.append((artist, title))
	db.save(cds,'mycds.db')
	raise HTTP_REDIRECTION, 'index'

def edit(num):
    cds = db.read('mycds.db')
    artist,title = cds[int(num)]
    print '<h1>New CD</h1>'
    print '<form action="update_cd" method="post">'
    print '<input name="num" type="hidden" value="%s">' %num
    print 'Artist <input name="artist" value="%s"><br>' %artist
    print 'Title <input name="title" value="%s"><br>' %title
    print '<input type="submit" value="Ok">'
    print '</form>'

def update_cd(num,artist,title):
    cds = db.read('mycds.db')
    cds[int(num)] = (artist,title)
    db.edit(cds,'mycds.db')
    raise HTTP_REDIRECTION,"index"

def remove(num):
    cds = db.read('mycds.db')
    del cds[int(num)]
    db.edit(cds,'mycds.db')
    raise HTTP_REDIRECTION,"index"