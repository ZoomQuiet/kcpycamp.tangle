# -*- coding: cp936 -*-
#!/usr/bin/python
# Filename: BehindColon.py

"""
@author: ����Բ
@license: kcCCRJ
@version��1.0
@tag���ж�case,default��:���Ƿ���ע�ͣ��ո�����Ķ���

@param CodeLine��������ַ��� 
@type CodeLine: �ַ���
@param Start: �Ӹ����ַ����ĵڼ���λ�ÿ�ʼ���
@type Start: ����
@return: ����ע�ͣ��ո�����Ķ����򷵻�False�����򷵻�True
@rtype : bool
"""
def behindcolon(CodeLine,start):
    k = len(CodeLine)
    i = start
    markColon = False
    markRemark = False
    while i < k - 2:
        i = i + 1
        if i < k - 1:
            sTemp = CodeLine[i:i+2]
            if '//' == sTemp:
                return (True == markColon)
            elif '/*' == sTemp:
                markRemark = True
        if False == markRemark:
            if False == markColon:
                if ':' == CodeLine[i]:
                    markColon = True
            elif ' ' != CodeLine[i]:
                if '\t' != CodeLine[i]:
#                    print '? ',CodeLine[i]
                    return False
        if i < k - 1:
            sTemp = CodeLine[i:i+2]
            if '*/' == sTemp:
                markRemark = False
                i = i + 1
    return True

# ��ȡһ�кͳ�ʼ����λ�ã���������м����ҵ�if
#found = 0������if�Ŀ�ʼ��������' ', ';', '\t', '('��
#found = 1��������if�Ŀ�ʼ������
# done
# ͨ���˳�������
