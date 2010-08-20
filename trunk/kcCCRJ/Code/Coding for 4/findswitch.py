# coding: UTF-8
#!/usr/bin/python
# Filename: FindSwitch.py

"""
@author: 方正圆
@license: kcCCRJ
@version：1.0
@tag：从一行字符串中查找关键字switch，若找到则返回紧接switch的下一个文位置，否则返回-1

@param CodeLine：需检测的字符串 
@type CodeLine: 字符串
@param Start: 从该行字符串的第几个位置开始检测
@type Start: 整型
@return: 若找到则返回switch的h所在位置，否则返回-1
@rtype i: 整型
"""

def findswitch(CodeLine, Start):
    i = Start - 1
    found = 0
    while i < len(CodeLine) - 6:
        i = i + 1
        szTemp = CodeLine[i:i+6]
        if szTemp == 'switch':
            if i + 6 < len(CodeLine):#检测switch是否某个变量的前缀，若是则found = 1并继续循环
                if 'a' <= CodeLine[i+6] <= 'z':
                    found = 1
                    continue
                if 'A' <= CodeLine[i+6] <= 'Z':
                    found = 1
                    continue
                if '0' <= CodeLine[i+6] <= '9':
                    found = 1
                    continue
                if '_' == CodeLine[i+6]:
                    found = 1
                    continue
            if found == 0:#找到了switch。后续更改位置
                return i + 5
                #print CodeLine
                #print 'found switch'
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
#f = file('BAService.cpp')
#print '''start'''
#while True:
#    line = f.readline()
#    if len(line) == 0: # Zero length indicates EOF
#        break
#    FindSwitch(line, 0)
#f.close()
#print '''fin'''
