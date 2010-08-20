#-*- coding:utf-8 -*-
"""Copy the uploaded file on the script directory"""
from webapps.kcHHD.model.kchhd_orm import *
from webapps.kcHHD.conf.db import *
from webapps.kcHHD.service.UserServic import *
import os
#print "uploading file %s" %_myfile.filename

# uncomment the following lines to copy the uploaded file 
# to the current directory

""""""
file_dir = ""

def uploadfile():
   # print "accountID is %d" %int(_accountID)
    
    f = _myfile.file # file-like object
    #print f
    global file_dir 

    dest_name = os.path.basename(_myfile.filename)
    name =dest_name.decode('utf-8')
    #获取服务器保存文件的路径
    currentdir = os.getcwd()
    file_dir = os.path.join(currentdir,name)
    #print file_dir
    #将路径写入数据库中
   
    writeDirInDB()

    #print name
    out = open(name,'wb')
       # copy file
    import shutil
    shutil.copyfileobj(f,out)
    out.close()
    

def writeDirInDB():
    userID = int(_accountID)
    
    #print file_dir
    store = getStore()
    t = getUserResume(userID)
    if t== True:
        store.find(ResumeInfo,ResumeInfo.UserID == userID).set(ResumePath = file_dir)
        store.commit()
        
    else:
        number = random.randrange(1000,9999);
        interviewee = store.find(User,User.ID == userID).one()
        
        resume = ResumeInfo(number,unicode(' '),interviewee.Name,unicode(" "))
        resume.UserID = userID
        store.add(resume)
        store.commit()
        
        
        

uploadfile()



