# -*- coding: cp936 -*-
import string, sys, pickle, cmd,post2db
import os.path,os
class Poster(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ':-)'
        self.intro="""�������(help/? [����]):
=========================
pdir  pfile  quit
�ļ�   Ŀ¼   �˳�

=========================
"""
        #self.misc_header='*******************'
        #self.ruler ='*'
        #self.doc_header ='commands'
        #self.undoc_header=''
        #��ʼ������
        #self.lipath=[]
        #self.lifile=[]
    if 0:
        def help_add(self):
            print "����ļ�orĿ¼"
        def do_add(self, name):
            if name == "": name = raw_input("Enter Name: ")
            phone = raw_input("Enter Phone Number for "+ name+": ")
            self.people[name] = phone   # add phone number for name
    
    def help_quit(self):
        print "�˳�"
    def do_quit(self, line):
        sys.exit()
    def help_pfile(self):
        print "¼�뵥���ļ���vi.duba.net"
    def do_pfile(self, filename):
        if filename == "":
            filename = raw_input("Enter filename: ")
        if not os.path.isfile(filename):
            print '�ļ�������'
        else:
            pl=[filename]
            post2db.PostTxt(pl)
    def help_pdir(self):
        print '¼���ļ�����vi.duba.net'
    def do_pdir(self,filename):
        if filename == "": filename = raw_input("Enter filename: ")
        if os.path.isdir(filename):
            li=os.listdir(filename)
            files=[os.path.join(filename, l) for l in li]
            post2db.PostTxt(files)
        else:
            print 'Ŀ¼������'
if __name__ == '__main__':
    poster = Poster()
    poster.cmdloop()
