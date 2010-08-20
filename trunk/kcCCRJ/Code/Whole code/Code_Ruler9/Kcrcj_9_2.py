# -*- coding: cp936 -*-
#check函数，完成9.2功能
from writeerror import writeerror
import re


linelist = []

listSpecialStr = ['for','if','while']

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



#完成 ‘在{之前只允许有空格，后面可以有注释，但不可以有代码’ 功能
def check1(filefrom, fileto):
    bFlag = False
    GetFileData(filefrom)
    rega = re.compile('\W+')              #分割单词的表达式
    regb = re.compile(' \S+')
    regSkip =re.compile('^\s*//|^\s*/\*')    #匹配空行或者注释行的情况


    num = -1;  
    for item in linelist:
        num = num + 1
        if regSkip.match(item):
            continue
        
        strTemp = rega.split(item)
        for subitem in strTemp:
       #     print subitem
            if subitem in listSpecialStr:
        #        print subitem
                strSplited = item.split(subitem)
                if regb.match(strSplited[1]):
                    continue
                else:
                    writeerror(fileto, num + 1, linelist[num], subitem+'号后面应该只有一个空格')
                    bFlag = True

    return bFlag




