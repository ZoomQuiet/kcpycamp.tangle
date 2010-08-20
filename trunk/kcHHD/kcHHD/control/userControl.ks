﻿#-*- coding:utf-8 -*-
from webapps.kcHHD.model.kchhd_orm import *
from webapps.kcHHD.service.UserServic import *
#from UserServic import *
#from common.exception import *

session = Session()

def login(id, password, userType):
    id = unicode(id, 'utf-8')
    pwd = unicode(password, 'utf-8')
    uType = unicode(userType,'utf-8')
    user = loginValidate(id, pwd, uType)
    if user:
        #session = Session()
        #session.UserID = user.ID
        #name = user.ID
        if uType == u'interviewee':
            #print session.UserID
            #raise SCRIPT_END
            temp = "../interviewee.ks/index?accountID=%s&id=%s"%(user.AccountID,user.ID)
            raise HTTP_REDIRECTION,temp
            #Include("../../web/intervieweeHeader.pih")
        elif uType == u'interviewer':
            temp_url = "../interviewer.ks/index?accountID=" +user.AccountID
            raise HTTP_REDIRECTION,temp_url
        elif uType == u'admin':
            temp = "../admin.ks/index?accountID=%s"%user.AccountID
            raise HTTP_REDIRECTION,temp
        else:
            temp = "../assistant.ks/index?accountID=%s"%user.AccountID
            raise HTTP_REDIRECTION,temp
    else:
        Include("/kcHHD/web/error.pih")



def register(userID, userName, password, password1):
    accountID = unicode(userID,'utf-8')
    pwd = unicode(password,'utf-8')
    name = unicode(userName,'utf-8')
    if(checkUserNameUsed(accountID)):
        print "用户名已存在"        
    else:
        try:
            user = addInterviewee(accountID, name, pwd)
        except:
            print "添加失败"
        else:
            temp = "../interviewee.ks/index?accountID=%s&id=%s"%(user.AccountID,user.ID)
            raise HTTP_REDIRECTION,temp
            
