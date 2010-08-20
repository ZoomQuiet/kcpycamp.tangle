# -*- coding: cp936 -*-
#!/usr/bin/python
# Filename: CodeRule4.py

"""
@author:方正圆
@license: kcCCRJ
@version：1.0
@tag：代码规范第4条的实现
"""

from findif import findif
from findfor import findfor
from findwhile import findwhile
from findswitch import findswitch
from findcase import findcase
from finddefault import finddefault
from findelse import findelse
from bracketjudge import bracketjudge
from judgebehindbracket import judgebehindbracket
from behindcolon import behindcolon
from writeerror import writeerror

"""
@param FileName: 输入文件
@type FileName: 字符串 
@param Destination: 输出文件
@type Destination: 字符串
@return: 是否成功执行这个函数
@rtype v: bool
"""
def coderule4(FileName,Destination):
    f = file(FileName)#输入文件
    filejudge = False#False表示文没找到不符合代码规范4的
    lineNum = 0
    mistakeNum = 0
    while True:
        line = f.readline()
        lineNum = lineNum + 1
        if len(line) == 0: # Zero length indicates EOF
            break

        Place = findif(line,0)#查找if,while,switch,for
        if -1 == Place:
            Place = findwhile(line,0)
        if -1 == Place:
            Place = findswitch(line,0)
        if -1 == Place:
            Place = findfor(line,0)

        judge = True#默认为符合代码规范的
        if -1 != Place:#若查找到if,while或switch
    #        print Place
    #        print 'if,while,switch'
            BracketInfo = bracketjudge(line, 0, 0, Place + 1)#查找成功后对后面的()进行匹配扫描
            while False == BracketInfo[2]:
                left = BracketInfo[0]
                right = BracketInfo[1]
                line = f.readline()
                if len(line) == 0: # Zero length indicates EOF
                    break                
                lineNum = lineNum + 1
                BracketInfo = bracketjudge(line, left, right, 0)

            i = BracketInfo[3] - 1
            judge = judgebehindbracket(line, i)#()后是否有控制行
        else:#试图查找case或default
            Place = findcase(line,0)
            if -1 == Place:
                Place = finddefault(line,0)

            if -1 != Place:#查找到case或default
                judge = behindcolon(line,Place)
            else:
                Place = findelse(line,0)
                if -1 != Place:
                    judge = judgebehindbracket(line, Place)#()后是否有控制行

        if False == judge:#不符合规范
            mistakeNum = mistakeNum + 1
            filejudge = True
            writeerror(Destination, lineNum, line, "循环，分支代码和执行代码不能在同一行上")
            #调用输出函数
            #print mistakeNum
            #print lineNum
            #print line
            #print '''***********************'''
            
    #f.close()#关闭输入文件
    return filejudge
#print """fin"""
