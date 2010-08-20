# -*- coding: cp936 -*-
import string, sys, pickle, cmd,post2db,env,getpass
import os.path,os
class Poster(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ':-)'
        self.intro="""�������(help/? [����]):
================================
login  pdir  pfile  logout quit
��¼    �ļ�   Ŀ¼    �ǳ�   �˳�

================================
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
        if env.g_uid== -1:
            print '���¼��'
            return
        if filename == "":
            filename = raw_input("Enter filename: ")
        if not os.path.isfile(filename):
            print '�ļ�������'
        else:
            pl=[filename]
            #post2db.PostTxt(pl)
            post2db.PostList(pl,env.g_uid)
    def help_pdir(self):
        print '¼���ļ�����vi.duba.net'
    def do_pdir(self,filename):
        if env.g_uid== -1:
            print '���¼��'
            return
        if filename == "": filename = raw_input("Enter filename: ")
        if os.path.isdir(filename):
            li=os.listdir(filename)
            files=[os.path.join(filename, l) for l in li]
            post2db.PostList(files,env.g_uid)
            #post2db.PostTxt(files)
        else:
            print 'Ŀ¼������'
    def help_test(self):
        print 'test'
    def do_test(self,p):
        #env.ReadCfg(p)
        print env.g_user
        print env.g_uid
        print '*'*50+'\n',env.g_ddb
        print '*'*50+'\n',env.g_dtxt
        print '*'*50+'\n',env.g_dsql
        print '*'*10
        for k,v in env.g_ddb.items():
            print k,v
        for k,v in env.g_dtxt.items():
            print k,v
        for k,v in env.g_dsql.items():
            print k,v
    def help_cc(self):
        print 'change cmd'
    def do_cc(self ,filename):
        if filename == "":
            filename = raw_input("Enter filename: ")
        self.prompt='['+filename+']>'
    def help_login(self):
        print '��¼'
    def do_login(self,user):
        if user == "":
            user = raw_input("Enter username: ")
        pwd = getpass.getpass('Enter password: ')
        r = post2db.CheckUser(user,pwd)
        if r>-1 :
            self.prompt='['+user+']>'
            env.g_uid=r
            env.g_user=user
            print user,'�ɹ���¼'
        else :
            #print env.g_uid
            print '�û��������벻ƥ��,��¼ʧ��'
        
    def help_logout(self):
        print '�ǳ�'
    def do_logout(self,filename):
        self.prompt=':-)'
        print '',''
        env.g_uid=-1
        env.g_user=''
if __name__ == '__main__':
    env.ReadCfg('cfg.txt')
    poster = Poster()
    poster.cmdloop()
