# coding: UTF-8
#!/usr/bin/python
# Filename: FindWhile.py

"""
@author: 方正圆
@license: kcCCRJ
@version：1.0
@tag：从一行字符串中查找关键字while，若找到则返回紧接while的下一个文位置，否则返回-1

@param CodeLine：需检测的字符串 
@type CodeLine: 字符串
@param Start: 从该行字符串的第几个位置开始检测
@type Start: 整型
@return: 若找到则返回while的e所在位置，否则返回-1
@rtype i: 整型
"""

def findwhile(CodeLine, Start):
#   global k
    i = Start - 1
    found = 0
    while i < len(CodeLine) - 5:
        i = i + 1
        szTemp = CodeLine[i:i+5]
        if szTemp == 'while':
            if i + 5 < len(CodeLine):#检瞱hile是否某个变量的前缀，若是则found = 1并继续循环
                if 'a' <= CodeLine[i+5] <= 'z':
                    found = 1
                    continue
                if 'A' <= CodeLine[i+5] <= 'Z':
                    found = 1
                    continue
                if '0' <= CodeLine[i+5] <= '9':
                    found = 1
                    continue
                if '_' == CodeLine[i+5]:
                    found = 1
                    continue
            if found == 0:#找到了while。后续更改位置
                return i + 4
#               k = k + 1
#               print CodeLine
#               print 'found while', k
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

#f = file('NumberGame2.4.cpp')
#print '''start'''
#k = 0
#while True:
#    line = f.readline()
#    if len(line) == 0: # Zero length indicates EOF
#        break
 #   FindWhile(line, 0)
#f.close()
#print '''fin'''
