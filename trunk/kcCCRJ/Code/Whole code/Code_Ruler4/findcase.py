# -*- coding: cp936 -*-
#!/usr/bin/python
# Filename: FindCase.py

"""
@author: ����Բ
@license: kcCCRJ
@version��1.0
@tag����һ���ַ����в��ҹؼ���case�����ҵ��򷵻ؽ���case����һ����λ�ã����򷵻�-1

@param CodeLine��������ַ��� 
@type CodeLine: �ַ���
@param Start: �Ӹ����ַ����ĵڼ���λ�ÿ�ʼ���
@type Start: ����
@return: ���ҵ��򷵻�case��e����λ�ã����򷵻�-1
@rtype i: ����
"""

def findcase(CodeLine,Start):
#    global k
    i = Start - 1
    found = 0
    while i < len(CodeLine) - 4:
        i = i + 1
        szTemp = CodeLine[i:i+4]
        if szTemp == 'case':
            if i+4 < len(CodeLine):#���case�Ƿ�ĳ��������ǰ׺��������found = 1������ѭ��
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
            if found == 0:#�ҵ���case����������λ��
                return i + 3
                #k = k + 1
                #print k
                #print CodeLine
                #print 'found case'
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
#k = 0
#f = file('BAService.cpp')
#while True:
#    line = f.readline()
#    if len(line) == 0: # Zero length indicates EOF
#        break
#    FindCase(line, 0)
#f.close()
# ��ȡһ�кͳ�ʼ����λ�ã���������м����ҵ�if
#found = 0������if�Ŀ�ʼ��������' ', ';', '\t', '('��
#found = 1��������if�Ŀ�ʼ������
# done
# ͨ���˳�������