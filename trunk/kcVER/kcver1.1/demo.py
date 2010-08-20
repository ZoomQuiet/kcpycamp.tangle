# -*- coding: cp936 -*-
import string, sys, pickle, cmd,post2db,env,getpass
import os.path,os
import wx
from wx import xrc
#import login
#import dlg
ACCT = u'帐号'
PWD = u'密码password'
LOGIN =u'登录'
LOGOUT = u'注销'
import threading
import random
class MyApp(wx.App):

    def OnInit(self):
        self.res = xrc.XmlResource('demo.xrc')
        assert self.res
        self.init_dialog()
        self.lifile=[]
        self.workth=None
        return True
    
    def init_dialog(self):
        self.dlg = self.res.LoadFrame(None, 'ID_DLG')
        assert self.dlg
        self.panel = xrc.XRCCTRL(self.dlg, 'ID_PANEL')

        #login
        self.acct = xrc.XRCCTRL(self.panel, 'ID_ACCT')
        self.pwd = xrc.XRCCTRL(self.panel, 'ID_PWD')
        self.pwd.SetValue(PWD)
        self.login =xrc.XRCCTRL(self.panel, 'ID_LOGIN')
        
        self.btn_dir = xrc.XRCCTRL(self.panel, 'ID_DIR')
        self.btn_file = xrc.XRCCTRL(self.panel, 'ID_FILE')
        self.btn_submit = xrc.XRCCTRL(self.panel, 'ID_SUBMIT')
        
        #output
        self.succ = xrc.XRCCTRL(self.panel, 'ID_SUCC')
        self.process = xrc.XRCCTRL(self.panel, 'ID_PROCESS')
        self.process.SetLabel('hello,world')
        self.fail =xrc.XRCCTRL(self.panel, 'ID_FAIL')

        #ID_PROCTXT
        self.labproc = xrc.XRCCTRL(self.panel,'ID_PROCTXT')
        #event band
        self.dlg.Bind(wx.EVT_BUTTON, self.OnLogin, id=xrc.XRCID('ID_LOGIN'))
        self.dlg.Bind(wx.EVT_BUTTON, self.OnFile, id=xrc.XRCID('ID_FILE'))
        self.dlg.Bind(wx.EVT_BUTTON, self.OnDir, id = xrc.XRCID('ID_DIR'))
        self.dlg.Bind(wx.EVT_BUTTON, self.OnSubmit, id = xrc.XRCID('ID_SUBMIT'))
        self.dlg.Bind(wx.EVT_BUTTON, self.OnEmpty, id = xrc.XRCID('ID_EMPTY'))
        
        #show dialog
        self.panel.Bind(wx.EVT_LEFT_DOWN,self.OnClickPanel,id=xrc.XRCID('ID_PANEL'))
        self.acct.Bind(wx.EVT_LEFT_UP,self.OnClickAcct,id = xrc.XRCID('ID_ACCT'))
        self.acct.Bind(wx.EVT_SET_FOCUS,self.OnSetAcct , id = xrc.XRCID('ID_ACCT'))
        self.acct.Bind(wx.EVT_KILL_FOCUS,self.OnLostAcct , id = xrc.XRCID('ID_ACCT'))

        self.pwd.Bind(wx.EVT_LEFT_UP,self.OnClickPwd,id = xrc.XRCID('ID_PWD'))
        self.pwd.Bind(wx.EVT_SET_FOCUS,self.OnSetPwd , id = xrc.XRCID('ID_PWD'))
        self.pwd.Bind(wx.EVT_KILL_FOCUS,self.OnLostPwd , id = xrc.XRCID('ID_PWD'))
        
        self.acct.SelectAll()
        self.dlg.Show()

    def OnEmpty(self,evt):
        if env.g_uid == -1:
            self.fail.AppendText(u'请先登录\n')
            return
        self.lifile = []
        self.succ.AppendText(u'文件列表已清空\n')
        self.labproc.SetLabel('')
        self.process.SetValue(0)
        pass
    def OnClickPanel(self,evt):
        self.process.SetFocus()
    def OnClickPwd(self, evt):
        self.pwd.SelectAll()
        evt.Skip()    
    def OnClickAcct(self, evt):
        self.acct.SelectAll()
        evt.Skip()
    def OnSetAcct(self, evt):
        if self.acct.GetValue() == ACCT:
            self.acct.SetValue('')
        else:
            self.acct.SelectAll()
    def OnLostAcct(self ,evt):
        if self.acct.GetValue()=='':
            self.acct.SetValue(ACCT)
    def OnSetPwd(self, evt):
        if self.pwd.GetValue() == PWD:
            self.pwd.SetValue('')
    def OnLostPwd(self ,evt):
         if self.pwd.GetValue()=='':
            self.pwd.SetValue(PWD)
    def OnLogin(self, evt):
        if env.g_uid == -1:
            user = self.acct.GetValue()
            pwd = self.pwd.GetValue()
            r = post2db.CheckUser(user,pwd)
            if r>-1 :
                self.prompt='['+user+']>'
                env.g_uid=r
                env.g_user=user
                self.login.SetLabel(LOGOUT)
                self.acct.SetEditable(0)
                self.pwd.SetEditable(0)
                self.succ.AppendText(u'%s 成功登录\n'%(user))
            else :
                self.fail.AppendText(u'用户名和密码不匹配,登录失败\n')
        else:
           self.fail.AppendText(u'%s 已注销\n'%(env.g_user))
           env.g_uid =-1
           env.g_user = ''
           self.login.SetLabel(LOGIN)
           self.acct.SetEditable(1)
           self.pwd.SetEditable(1)
           self.acct.SetValue(ACCT)
           self.pwd.SetValue(PWD)
           
    def OnDir(self ,evt):
        if env.g_uid == -1:
            self.fail.AppendText(u'请先登录\n')
            return
            pass
        if self.workth != None:
            self.fail.AppendText('录入数据中...')
            return
        self.process.SetValue(0)
        dirdlg = wx.DirDialog(None,'Choose dir',
                style = wx.DD_DEFAULT_STYLE)
        r = dirdlg.ShowModal()
        if r == wx.ID_OK:
            strPath = dirdlg.GetPath()
            strpath=strPath.encode('cp936')
            li=os.listdir(strPath)
            files=[os.path.join(strPath, l) for l in li]
            self.lifile = list(set(self.lifile + files))
            self.succ.AppendText(u'共添加了 %d 个文件\n'%(len(self.lifile)))
        else:
            dirdlg.Destroy()
            
    def OnFile(self ,evt):
        if env.g_uid == -1:
            self.fail.AppendText(u'请先登录\n')
            return
            pass
        if self.workth != None:
            self.fail.AppendText('录入数据中...')
            return
        dlg = wx.FileDialog(None, message=u'添加文件夹', defaultDir="",
        defaultFile="", wildcard="*.*", style=wx.MULTIPLE,
        pos=wx.DefaultPosition)
        r = dlg.ShowModal()
        if r == wx.ID_OK:
            li = dlg.GetPaths()
            self.lifile = list(set(self.lifile + li))
            self.succ.AppendText(u'共添加了 %d 个文件\n'%(len(self.lifile)))
        else:
            dlg.Destroy()
        pass
    def OnSubmit(self,evt):
        if env.g_uid == -1:
            self.fail.AppendText(u'请先登录\n')
            return
            pass
        #post2db.PostList(self.lifile,env.g_uid,self)
        #self.lifile = []
        if self.workth == None:
            self.workth = WorkerThread(self,self.lifile,env.g_uid)
            self.workth.start()
            self.lifile=[]
            pass
        else:
            self.fail.AppendText('录入数据中...\n')
    def PostAll(self,msg):
        self.workth=None
        pass
    def showmsg(self,m1,m2):
        self.succ.AppendText(m1)
        self.fail.AppendText(m2)
    def SetRange(self,var):
        self.process.SetRange(var)
        pass
    def SetValue(self,var):
        self.process.SetValue(var)
    def SetLabel(self,var):
        self.labproc.SetLabel(var)
    def AppendText(self,bsucc,txt):
        if bsucc:
            self.succ.AppendText(txt)
        else:
            self.fail.AppendText(txt)
    def SetText(self,bsucc,txt):
        if bsucc:
            self.succ.SetValue(txt)
        else:
            self.fail.SetValue(txt)

class WorkerThread(threading.Thread):
    def __init__(self,app,lifile,gid):
        threading.Thread.__init__(self)
        self.app = app
        self.li=lifile
        self.gid=gid
        self.timeToQuit = threading.Event()
        self.timeToQuit.clear()

    def run(self):
        post2db.PostList(self.li,self.gid,self.app,self.timeToQuit)
        self.timeToQuit.set()
        wx.CallAfter(self.app.PostAll,'all done')
    
if __name__ == '__main__':
    env.ReadCfg('cfg.txt')
    app = MyApp(0)
    app.MainLoop()
