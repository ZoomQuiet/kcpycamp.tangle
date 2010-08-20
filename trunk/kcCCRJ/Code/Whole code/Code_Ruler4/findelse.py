# -*- coding: cp936 -*-
#!/usr/bin/python
# Filename: FindElse.py

"""
@author: 方正圆
@license: kcCCRJ
@version：1.0
@tag：从一行字符串中查找关键字else，若找到则返回紧接else的下一个文位置，否则返回-1

@param CodeLine：需检测的字符串 
@type CodeLine: 字符串
@param Start: 从该行字符串的第几个位置开始检测
@type Start: 整型
@return: 若找到则返回else的e所在位置，否则返回-1
@rtype i: 整型
"""

def findelse(CodeLine,Start):
 #   global k
    i = Start - 1
    found = 0
    while i < len(CodeLine) - 4:
        i = i + 1
        szTemp = CodeLine[i:i+4]
        if szTemp == 'else':
            if i+4 < len(CodeLine):#检测else是否某个变量的前缀，若是则found = 1并继续循环
                if 'a' <= CodeLine[i+4] <= 'z':
                    found = 1
                    continue
                if 'A' <= CodeLine[i+4] <= 'Z':
                    found = 1
                    continue
                if '0' <= CodeLine[i+4] <= '9':
                    found = 1
                    continue
                if '_' == CodeLine[i+4]:
                    found = 1
                    continue
            if found == 0:#找到了else。后续更改位置
                return i + 3
                #k = k + 1
                #print k
                #print CodeLine
                #print 'found else'
        found = 0
        if CodeLine[i] == ' ':#检测是否符合进入found 0条件
            continue
        if CodeLine[i] == ';':
            continue
        if CodeLine[i] == '\t':
            continue
        if CodeLine[i] == '(':
            continue
        found = 1
    return -1
#k = 0
#f = file('NumberGame2.4.cpp')
#while True:
#    line = f.readline()
#    if len(line) == 0: # Zero length indicates EOF
#        break
#    FindElse(line, 0)
#f.close()

# 获取一行和初始查找位置，返输出该行假如找到if
#found = 0：符合if的开始条件。（' ', ';', '\t', '('）
#found = 1：不符合if的开始条件。
# done
# 通过了初步测试
