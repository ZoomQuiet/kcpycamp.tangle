from os.path import walk, join, normpath
import sys
import os.path
from os import getcwd
def visit(arg, dirname, names):
     #print "\n".join(dirname)
     print names
     files=[normpath(join(dirname, file)) for file in names]
     #count = 0
     for i in files:
         if os.path.isdir(i):
             #count += 1
             #print i
             pass

if __name__=="__main__":
     '''
     if len(sys.argv)==1:
         path=getcwd()
     else:
         path=sys.argv[1]
     '''
     path = 'd:test11'
     walk(path, visit, 0)


