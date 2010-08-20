# -*- coding: cp936 -*-
#check函数，完成8.1功能
from writeerror import writeerror

import re


linelist = []
error8_1= '在{之前只允许有空格，后面可以有注释，但不可以有代码'
error8_2 = '第%d行的{和第%d行的}不对应'

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
    num = -1
    rega = re.compile('^\s*$')              #匹配前缀空格
    regb =re.compile('^\s*//|^\s*/\*.*\*/$')    #匹配在三种合理的情况，全部为空或者出现//或者出现/*并且以*/结尾
    bFlag = False
    for item in linelist:
        num = num + 1
        if regb.match(item):
            continue
        if '{' in item:
            splitStr = item.split('{')
            if rega.match(splitStr[0]) and\
               (rega.match(splitStr[1]) or regb.match(splitStr[1])):
                continue
            else:
                writeerror(fileto, num + 1, linelist[num], error8_1)
                bFlag = True

    return bFlag
    

#完成函数体内{}对应’ 功能   
def check2(filefrom, fileto):  
    listLineNum = []        #存放{符号，下标表示第i个
    listPos = []            #存放{符号对应的前置空格数字
    regb =re.compile('^\s*//|^\s*/\*.*\*/$')    #匹配在三种合理的情况，全部为空或者出现//或者出现/*并且以*/结尾
    num = -1
    bFlag = False
    for i in linelist:      #遍历
        num = num + 1
        if regb.match(i):
            continue        
        if('{' in i):           #遇到{符号，入栈
            t = i.replace('\t', '    ')     #将制表符\t换算成4个空格
            listLineNum.append(num)          
            listPos.append(t.index('{'))    
            
         #   print t,
         #   print 'input:',num, t.index('{')
         #   print '\n'
         
        if('}' in i):
            if(len(listLineNum) > 0):
                linenum = listLineNum.pop() 
                linestr = listPos.pop()
                t = i.replace('\t', '    ')               
                if(t.index('}') != linestr):        #将{与}进行比较，如果前置空格不同，错误
          #          print linestr, t.index('}')
                    writeerror(fileto, num + 1, linelist[num], error8_2 % (linenum + 1, num + 1))
                    bFlag = True
    return bFlag

    

def check(filefrom, fileto):
    GetFileData(filefrom) #读取文件数据
    bFile1 = check1(filefrom, fileto)
    bFile2 = check2(filefrom, fileto)
    return bFile1 or bFile2  


#check('8.1 test_change.h', 'out.txt')



