# -*- coding: cp936 -*-
#!/usr/bin/python
# Filename: CodeRule4.py

"""
@author:����Բ
@license: kcCCRJ
@version��1.0
@tag������淶��4����ʵ��
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
@param FileName: �����ļ�
@type FileName: �ַ��� 
@param Destination: ����ļ�
@type Destination: �ַ���
@return: �Ƿ�ɹ�ִ���������
@rtype v: bool
"""
def coderule4(FileName,Destination):
    f = file(FileName)#�����ļ�
    filejudge = False#False��ʾ��û�ҵ������ϴ���淶4��
    lineNum = 0
    mistakeNum = 0
    while True:
        line = f.readline()
        lineNum = lineNum + 1
        if len(line) == 0: # Zero length indicates EOF
            break

        Place = findif(line,0)#����if,while,switch,for
        if -1 == Place:
            Place = findwhile(line,0)
        if -1 == Place:
            Place = findswitch(line,0)
        if -1 == Place:
            Place = findfor(line,0)

        judge = True#Ĭ��Ϊ���ϴ���淶��
        if -1 != Place:#�����ҵ�if,while��switch
    #        print Place
    #        print 'if,while,switch'
            BracketInfo = bracketjudge(line, 0, 0, Place + 1)#���ҳɹ���Ժ����()����ƥ��ɨ��
            while False == BracketInfo[2]:
                left = BracketInfo[0]
                right = BracketInfo[1]
                line = f.readline()
                if len(line) == 0: # Zero length indicates EOF
                    break                
                lineNum = lineNum + 1
                BracketInfo = bracketjudge(line, left, right, 0)

            i = BracketInfo[3] - 1
            judge = judgebehindbracket(line, i)#()���Ƿ��п�����
        else:#��ͼ����case��default
            Place = findcase(line,0)
            if -1 == Place:
                Place = finddefault(line,0)

            if -1 != Place:#���ҵ�case��default
                judge = behindcolon(line,Place)
            else:
                Place = findelse(line,0)
                if -1 != Place:
                    judge = judgebehindbracket(line, Place)#()���Ƿ��п�����

        if False == judge:#�����Ϲ淶
            mistakeNum = mistakeNum + 1
            filejudge = True
            writeerror(Destination, lineNum, line, "ѭ������֧�����ִ�д��벻����ͬһ����")
            #�����������
            #print mistakeNum
            #print lineNum
            #print line
            #print '''***********************'''
            
    #f.close()#�ر������ļ�
    return filejudge
#print """fin"""
