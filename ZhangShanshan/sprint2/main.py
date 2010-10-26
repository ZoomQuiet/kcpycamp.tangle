# -*- coding: cp936 -*-
import string, sys, pickle, cmd,post2db
import os.path,os
class Poster(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ':-)'
        self.intro="""命令帮助(help/? [命令]):
=========================
pdir  pfile  quit
文件   目录   退出

=========================
"""
        #self.misc_header='*******************'
        #self.ruler ='*'
        #self.doc_header ='commands'
        #self.undoc_header=''
        #初始化代码
        #self.lipath=[]
        #self.lifile=[]
    if 0:
        def help_add(self):
            print "添加文件or目录"
        def do_add(self, name):
            if name == "": name = raw_input("Enter Name: ")
            phone = raw_input("Enter Phone Number for "+ name+": ")
            self.people[name] = phone   # add phone number for name
    
    def help_quit(self):
        print "退出"
    def do_quit(self, line):
        sys.exit()
    def help_pfile(self):
        print "录入单个文件至vi.duba.net"
    def do_pfile(self, filename):
        if filename == "":
            filename = raw_input("Enter filename: ")
        if not os.path.isfile(filename):
            print '文件不存在'
        else:
            pl=[filename]
            post2db.PostTxt(pl)
    def help_pdir(self):
        print '录入文件夹至vi.duba.net'
    def do_pdir(self,filename):
        if filename == "": filename = raw_input("Enter filename: ")
        if os.path.isdir(filename):
            li=os.listdir(filename)
            files=[os.path.join(filename, l) for l in li]
            post2db.PostTxt(files)
        else:
            print '目录不存在'
if __name__ == '__main__':
    poster = Poster()
    poster.cmdloop()
