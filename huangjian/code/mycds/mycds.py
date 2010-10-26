import db
cds = db.read('mycds.db)'
for(artist, title) in cds
	print artist,title