# -*- coding: cp936 -*-
# check函数，完成1功能
from writeerror import writeerror
import re
"""
@author: 林哲
@license: kcCCRJ
@version：1.0
@tag：判断在{之前只允许有空格，后面可以有注释，但不可以有代码,{}左右符号要对应
"""

linelist = []
error1= '文件头注释信息不足,必须包括文件名，创建人，创建时间，功能描述4种信息'


"""
@tag：从文件中读内容并存放到linelist中
@param filefrom：读取的文件名字 
@type filefrom: 字符串
"""
def GetFileData(filefrom):
    f = file(filefrom)
    # if no mode is specified, 'r'ead mode is assumed by default
    while True:
        line = f.readline()
        if len(line) == 0: # Zero length indicates EOF
            break
        linelist.append(line)
        # Notice comma to avoid automatic newline added by Python
    f.close() # close the file 

    
"""
@tag：判断是否有正确的文件头注释
@param filefrom：读取的文件名字 
@type filefrom: 字符串
@param fileto：写出的文件名字 
@type fileto: 字符串
"""
def check1(filefrom, fileto):

    GetFileData(filefrom)
    #标志文件起始处的4个必要注释片段是否存在
    bFlieName = True       #文件名
    bCreator = True        #创建人
    bDate = True           #创建时间
    bComment = True        #功能描述

    #判读注释片段的正则表达式,可用中文或英文，英文忽略大小写
    regFlieName = re.compile('(^//|^/\*)\s*(FlieName|文件名)',re.IGNORECASE)
    regCreator = re.compile('(^//|^/\*)\s*(Creator|创建者)',re.IGNORECASE)
    regDate = re.compile('(^//|^/\*)\s*(Date|创建时间)',re.IGNORECASE)
    regComment = re.compile('(^//|^/\*)\s*(Comment|功能描述)',re.IGNORECASE)

    nRemarkLineNum = 6   # 标志自动生成的文件开始处注释行数
    if len(linelist) < nRemarkLineNum:   #根据宏生成的文件头注释至少6行
        writeerror(fileto, 1, '', error1) 
        return True


    num = -1
    for item in linelist:
        num = num + 1
        

        if item.startswith('/*') or item.startswith('//'):

            if regFlieName.match(item):
                bFlieName = False
            elif regCreator.match(item):
                bCreator = False
            elif regDate.match(item):
                bDate = False
            elif regComment.match(item):
                bComment = False                    
        else:
            break

    if bFlieName == False and bCreator == False and bDate == False and bComment == False:
        return False
    else:
        writeerror(fileto, 1, '', error1) 
        return True
    







