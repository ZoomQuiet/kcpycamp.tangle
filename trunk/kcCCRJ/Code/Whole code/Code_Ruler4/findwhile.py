# -*- coding: cp936 -*-
#!/usr/bin/python
# Filename: FindWhile.py

"""
@author: ����Բ
@license: kcCCRJ
@version��1.0
@tag����һ���ַ����в��ҹؼ���while�����ҵ��򷵻ؽ���while����һ����λ�ã����򷵻�-1

@param CodeLine��������ַ��� 
@type CodeLine: �ַ���
@param Start: �Ӹ����ַ����ĵڼ���λ�ÿ�ʼ���
@type Start: ����
@return: ���ҵ��򷵻�while��e����λ�ã����򷵻�-1
@rtype i: ����
"""

def findwhile(CodeLine, Start):
#   global k
    i = Start - 1
    found = 0
    while i < len(CodeLine) - 5:
        i = i + 1
        szTemp = CodeLine[i:i+5]
        if szTemp == 'while':
            if i + 5 < len(CodeLine):#��while�Ƿ�ĳ��������ǰ׺��������found = 1������ѭ��
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
            if found == 0:#�ҵ���while����������λ��
                return i + 4
#               k = k + 1
#               print CodeLine
#               print 'found while', k
        found = 0
        if CodeLine[i] == ' ':#����Ƿ���Ͻ���found 0����
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
