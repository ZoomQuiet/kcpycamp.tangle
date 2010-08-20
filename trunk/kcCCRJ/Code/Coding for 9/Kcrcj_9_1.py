# coding: gbk
#完成9.1部分功能，尚不完整
'''
BUG
1.无法处理像*号（可以当乘号，指针等）等有不同含义的符号，直接忽略。现在知道有*，&， 
2.加减号可以当符号也可以当前缀使用，当前缀使用的时候一般会被处理成错误
3.还有一些未发现，哈哈~~~
'''
import re
regWhiteBlank =re.compile('^\s*$|^\s*//|^\s*/\*')    #匹配空行或者注释行的情况
regRemark =re.compile('.s(//.*)')    #匹配注释的情况
regImport =re.compile('^\s*#')    #匹配#号开始的情况，包括#include和#define

listOperZero = ['++', '--', '->', '::']
listOperOne = ['>=', '<=', '*=', '/=', '%=', '+=', '-=', '^=', '&=', '|=','&&','||','==','!=']
listOperTwo = ['>', '<',  '/', '+', '-', '^', '|', '?']    #*号有歧义

linelist = []
errordata = []
error9_1= '在双目运算符前后必须有空格'


#消除注释
def ReplaceRemark(linecode):
    regRemark = re.compile('.*?(//.*)')    #匹配注释的情况
    if regRemark.match(linecode):
       strDataToR = regRemark.match(linecode).group(1)
     #  print "str:" + strDataToR
       linecode = linecode.replace(strDataToR, '') 
    return linecode


def GetFileData(filefrom):
    f = file(filefrom)
    while True:
        line = f.readline()
        if len(line) == 0: # Zero length indicates EOF
            break
        linelist.append(line)
    f.close() # close the file 

def ShowFileData():
    for i in linelist:
        print i,

def ShowErrorData():
    for i in errordata:
        print i, 

#将错误写进文件
def writeerror(fileto, errorline, errorcode, errortype):
    f = file(fileto, 'a')   #打开文件
    data = '';
    data += '\n错误位置:'
    data += str(errorline)
    data += '\n错误类型:'
    data += errortype
    data += '\n错误代码:'
    data += errorcode
    errordata.append(data)  #写入输出数据
    f.write(data)           #写入文件
    f.close() 

    

#完成 ‘函数体内{}对应’ 功能   
def check2(filefrom, fileto):
    linenum = -1
    for linecode in linelist:
         linenum = linenum + 1
         if regWhiteBlank.match(linecode):
             continue
         if regImport.match(linecode):
             continue

      #   print linenum
         linecode = ReplaceRemark(linecode)
      #   print linecode
         linecode = CheckWithOperZero(linecode)
      #   print linecode
         linecode = CheckWithOperOne(linenum, linecode, fileto)
         linecode = CheckWithOperTwo(linenum, linecode, fileto)

def CheckWithOperZero(linestr,):
    for item in listOperZero:   
        linestr = linestr.replace(item, '@@')
    return linestr




def CheckWithOperOne(linenum, linestr, fileto):
    for item in listOperOne:
        t = linestr.split(item)
        tlen = len(t)
        if tlen == 1:
            continue

        num = -1
        for i in t:
        #     print i
            num=num+1
        #    print num
            if num == 0:
                if not i.endswith(' '):
                    strerror = '第%d行%s符号左空格有错误' % (linenum+1, item)
                    writeerror(fileto, linenum+1, linelist[linenum], strerror)
            elif num == tlen - 1:
                if not i.startswith(' '):
                    strerror = '第%d行%s符号右空格有错误' % (linenum+1, item)
                    writeerror(fileto, linenum+1, linelist[linenum], strerror)
            else:
                if not i.startswith(' '):
                    strerror = '第%d行%s符号右空格有错误' % (linenum+1, item)
                    writeerror(fileto, linenum+1, linelist[linenum], strerror)
                if not i.endswith(' '):
                    strerror = '第%d行%s符号左空格有错误' % (linenum+1, item)
                    writeerror(fileto, linenum+1, linelist[linenum], strerror)
        linestr =linestr.replace(item, '@')
        
    return linestr

def CheckWithOperTwo(linenum, linestr, fileto):
    for item in listOperTwo:
        t = linestr.split(item)
        tlen = len(t)
        if tlen == 1:
            continue

        num = -1
        for i in t:
            num=num+1
            if num == 0:
                if not i.endswith(' '):
                    strerror = '第%d行%s符号左空格有错误' % (linenum+1, item)
                    writeerror(fileto, linenum+1, linelist[linenum], strerror)
            elif num == tlen - 1:
                if not i.startswith(' '):
                    strerror = '第%d行%s符号右空格有错误' % (linenum+1, item)
                    writeerror(fileto, linenum+1, linelist[linenum], strerror)
            else:
                if not i.startswith(' '):
                    strerror = '第%d行%s符号右空格有错误' % (linenum+1, item)
                    writeerror(fileto, linenum+1, linelist[linenum], strerror)
                if not i.endswith(' '):
                    strerror = '第%d行%s符号左空格有错误' % (linenum+1, item)
                    writeerror(fileto, linenum+1, linelist[linenum], strerror)   
        linestr =linestr.replace(item, '@')
        
    return linestr

def check(filefrom, fileto):
    GetFileData(filefrom) #读取文件数据
    flag = False
    flag = check1('4.cpp', 'out.txt')
    if(flag):
        check2('4.cpp', 'out.txt')      
    return flag

GetFileData('KGameUI.cpp')
check2('KGameUI.cpp', 'out.txt')
ShowErrorData()
#ShowFileData()


