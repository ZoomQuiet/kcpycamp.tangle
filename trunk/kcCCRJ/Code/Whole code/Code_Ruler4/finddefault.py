# -*- coding: cp936 -*-
#!/usr/bin/python
# Filename: FindDefault.py

"""
@author: ����Բ
@license: kcCCRJ
@version��1.0
@tag����һ���ַ����в��ҹؼ���default�����ҵ��򷵻ؽ���default����һ����λ�ã����򷵻�-1

@param CodeLine��������ַ��� 
@type CodeLine: �ַ���
@param Start: �Ӹ����ַ����ĵڼ���λ�ÿ�ʼ���
@type Start: ����
@return: ���ҵ��򷵻�default��t����λ�ã����򷵻�-1
@rtype i: ����
"""

def finddefault(CodeLine,Start):
#    global k
    i = Start - 1
    found = 0
    while i < len(CodeLine) - 7:
        i = i + 1
        szTemp = CodeLine[i:i+7]
        if szTemp == 'default':
            if i+6 < len(CodeLine):#���default�Ƿ�ĳ��������ǰ׺��������found = 1������ѭ��
                if 'a' <= CodeLine[i+7] <= 'z':
                    found = 1
                    continue
                if 'A' <= CodeLine[i+7] <= 'Z':
                    found = 1
                    continue
                if '0' <= CodeLine[i+7] <= '9':
                    found = 1
                    continue
                if '_' == CodeLine[i+7]:
                    found = 1
                    continue
            if found == 0:#�ҵ���default����������λ��
                return i + 6
#                k = k + 1
#                print k
#                print CodeLine
#                print 'found case'
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
#print 'start'
#k = 0
#f = file('poem.txt')
#while True:
#    line = f.readline()
#    if len(line) == 0: # Zero length indicates EOF
#        break
#    FindDefault(line, 0)
#f.close()
#print 'fin'
# ��ȡһ�кͳ�ʼ����λ�ã���������м����ҵ�if
#found = 0������if�Ŀ�ʼ��������' ', ';', '\t', '('��
#found = 1��������if�Ŀ�ʼ������
# done
# ͨ���˳�������
