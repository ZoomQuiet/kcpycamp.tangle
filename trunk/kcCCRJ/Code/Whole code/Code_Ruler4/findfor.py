# -*- coding: cp936 -*-
#!/usr/bin/python
# Filename: FindIf.py

"""
@author: ����Բ
@license: kcCCRJ
@version��1.0
@tag����һ���ַ����в��ҹؼ���for�����ҵ��򷵻�for��r����λ�ã����򷵻�-1

@param CodeLine��������ַ��� 
@type CodeLine: �ַ���
@param Start: �Ӹ����ַ����ĵڼ���λ�ÿ�ʼ���
@type Start: ����
@return: ���ҵ��򷵻�for��r����λ�ã����򷵻�-1
@rtype i: ����
"""

def findfor(CodeLine,Start):
    i = Start - 1
    found = 0
    while i < len(CodeLine) - 3:
        i = i + 1
        szTemp = CodeLine[i:i+3]
        if szTemp == 'for':
            if i+3 < len(CodeLine):#���for�Ƿ�ĳ��������ǰ׺��������found = 1������ѭ��
                if 'a' <= CodeLine[i+3] <= 'z':
                    found = 1
                    continue
                if 'A' <= CodeLine[i+3] <= 'Z':
                    found = 1
                    continue
                if '0' <= CodeLine[i+3] <= '9':
                    found = 1
                    continue
                if '_' == CodeLine[i+3]:
                    found = 1
                    continue
            if found == 0:#�ҵ���for����������λ��
                return i + 2
                #print CodeLine
                #print 'found if'
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
#f = file('KCheatMaster.cpp')
#while True:
#    line = f.readline()
#    if len(line) == 0: # Zero length indicates EOF
#        break
#    FindIf(line, 0)
#f.close()
#
# ��ȡһ�кͳ�ʼ����λ�ã���������м����ҵ�if
#found = 0������if�Ŀ�ʼ��������' ', ';', '\t', '('��
#found = 1��������if�Ŀ�ʼ������
# done
# ͨ���˳�������
