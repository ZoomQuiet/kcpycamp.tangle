# -*- coding: cp936 -*-
import string, sys, pickle, cmd,post2db,env,getpass
import os.path,os
class Poster(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = ':-)'
        self.intro="""命令帮助(help/? [命令]):
================================
login  pdir  pfile  logout quit
登录    文件   目录    登出   退出

================================
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
        if env.g_uid== -1:
            print '请登录先'
            return
        if filename == "":
            filename = raw_input("Enter filename: ")
        if not os.path.isfile(filename):
            print '文件不存在'
        else:
            pl=[filename]
            #post2db.PostTxt(pl)
            post2db.PostList(pl,env.g_uid)
    def help_pdir(self):
        print '录入文件夹至vi.duba.net'
    def do_pdir(self,filename):
        if env.g_uid== -1:
            print '请登录先'
            return
        if filename == "": filename = raw_input("Enter filename: ")
        if os.path.isdir(filename):
            li=os.listdir(filename)
            files=[os.path.join(filename, l) for l in li]
            post2db.PostList(files,env.g_uid)
            #post2db.PostTxt(files)
        else:
            print '目录不存在'
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
        print '登录'
    def do_login(self,user):
        if user == "":
            user = raw_input("Enter username: ")
        pwd = getpass.getpass('Enter password: ')
        r = post2db.CheckUser(user,pwd)
        if r>-1 :
            self.prompt='['+user+']>'
            env.g_uid=r
            env.g_user=user
            print user,'成功登录'
        else :
            #print env.g_uid
            print '用户名和密码不匹配,登录失败'
        
    def help_logout(self):
        print '登出'
    def do_logout(self,filename):
        self.prompt=':-)'
        print '',''
        env.g_uid=-1
        env.g_user=''
if __name__ == '__main__':
    env.ReadCfg('cfg.txt')
    poster = Poster()
    poster.cmdloop()
