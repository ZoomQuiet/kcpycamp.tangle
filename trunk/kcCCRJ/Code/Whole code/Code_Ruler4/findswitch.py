# -*- coding: cp936 -*-
#!/usr/bin/python
# Filename: FindSwitch.py

"""
@author: ����Բ
@license: kcCCRJ
@version��1.0
@tag����һ���ַ����в��ҹؼ���switch�����ҵ��򷵻ؽ���switch����һ����λ�ã����򷵻�-1

@param CodeLine��������ַ��� 
@type CodeLine: �ַ���
@param Start: �Ӹ����ַ����ĵڼ���λ�ÿ�ʼ���
@type Start: ����
@return: ���ҵ��򷵻�switch��h����λ�ã����򷵻�-1
@rtype i: ����
"""

def findswitch(CodeLine, Start):
    i = Start - 1
    found = 0
    while i < len(CodeLine) - 6:
        i = i + 1
        szTemp = CodeLine[i:i+6]
        if szTemp == 'switch':
            if i + 6 < len(CodeLine):#���switch�Ƿ�ĳ��������ǰ׺��������found = 1������ѭ��
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
            if found == 0:#�ҵ���switch����������λ��
                return i + 5
                #print CodeLine
                #print 'found switch'
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
#f = file('BAService.cpp')
#print '''start'''
#while True:
#    line = f.readline()
#    if len(line) == 0: # Zero length indicates EOF
#        break
#    FindSwitch(line, 0)
#f.close()
#print '''fin'''
