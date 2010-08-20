import os
print "uploading file %s" %_myfile.filename
"""
f = _myfile.file # file-like object
dest_name = os.path.basename(_myfile.filename)
out = open(dest_name,'wb')
import shutil
shutil.copyfileobj(f,out)
out.close()
"""
print ' <a href="mianshi.pih"> Back to Index</a>'
