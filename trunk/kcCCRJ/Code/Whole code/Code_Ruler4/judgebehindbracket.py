# -*- coding: cp936 -*-
#!/usr/bin/python
# Filename: JudgeBehindBracket.py

"""
@author: ����Բ
@license: kcCCRJ
@version��1.0
@tag���ж�if,switch,while��()���Ƿ���ע�ͣ��ո�����Ķ���

@param CodeLine��������ַ��� 
@type CodeLine: �ַ���
@param Start: �Ӹ����ַ����ĵڼ���λ�ÿ�ʼ���
@type Start: ����
@return: ����ע�ͣ��ո�����Ķ����򷵻�False�����򷵻�True
@rtype : bool
"""

def judgebehindbracket(line, i):
    judge = True
    remark = False
#    print '''len(line)''', len(line)
#    print '''i''',i
#    print line[i:len(line)]
    while i < len(line) - 1:
        i = i + 1
#        print '''line[i]:''', line[i]
#            print line[i:i+2]
           # print line[i]
           # print line[i+1]
        if ' ' == line[i]:
            continue
        if '\t' == line[i]:
            continue
        if '\n' == line[i]:
            continue
        if ';' == line[i]:
            continue
        
        if i < len(line) - 1:
            if '/' == line[i]:
                if '/' == line[i+1]:
#                    print '?'
                    break
            if '/' == line[i]:
                if '*' == line[i+1]:
                    remark = True

        if False == remark:
           # print '''line[i:len(line)]:''',line[i:len(line)]
            judge = False
            break
        
        if i < len(line) - 1:
            if '*' == line[i]:
                if '/' == line[i+1]:
                    remark = False
                    i = i + 1
                    
    return judge                    
