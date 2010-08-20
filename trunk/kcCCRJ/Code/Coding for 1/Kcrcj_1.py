# -*- coding: cp936 -*-
# check���������1����
from writeerror import writeerror
import re
"""
@author: ����
@license: kcCCRJ
@version��1.0
@tag���ж���{֮ǰֻ�����пո񣬺��������ע�ͣ����������д���,{}���ҷ���Ҫ��Ӧ
"""

linelist = []
error1= '�ļ�ͷע����Ϣ����,��������ļ����������ˣ�����ʱ�䣬��������4����Ϣ'


"""
@tag�����ļ��ж����ݲ���ŵ�linelist��
@param filefrom����ȡ���ļ����� 
@type filefrom: �ַ���
"""
def GetFileData(filefrom):
    f = file(filefrom)
    # if no mode is specified, 'r'ead mode is assumed by default
    while True:
        line = f.readline()
        if len(line) == 0: # Zero length indicates EOF
            break
        linelist.append(line)
        # Notice comma to avoid automatic newline added by Python
    f.close() # close the file 

    
"""
@tag���ж��Ƿ�����ȷ���ļ�ͷע��
@param filefrom����ȡ���ļ����� 
@type filefrom: �ַ���
@param fileto��д�����ļ����� 
@type fileto: �ַ���
"""
def check1(filefrom, fileto):

    GetFileData(filefrom)
    #��־�ļ���ʼ����4����Ҫע��Ƭ���Ƿ����
    bFlieName = True       #�ļ���
    bCreator = True        #������
    bDate = True           #����ʱ��
    bComment = True        #��������

    #�ж�ע��Ƭ�ε�������ʽ,�������Ļ�Ӣ�ģ�Ӣ�ĺ��Դ�Сд
    regFlieName = re.compile('(^//|^/\*)\s*(FlieName|�ļ���)',re.IGNORECASE)
    regCreator = re.compile('(^//|^/\*)\s*(Creator|������)',re.IGNORECASE)
    regDate = re.compile('(^//|^/\*)\s*(Date|����ʱ��)',re.IGNORECASE)
    regComment = re.compile('(^//|^/\*)\s*(Comment|��������)',re.IGNORECASE)

    nRemarkLineNum = 6   # ��־�Զ����ɵ��ļ���ʼ��ע������
    if len(linelist) < nRemarkLineNum:   #���ݺ����ɵ��ļ�ͷע������6��
        writeerror(fileto, 1, '', error1) 
        return True


    num = -1
    for item in linelist:
        num = num + 1
        

        if item.startswith('/*') or item.startswith('//'):

            if regFlieName.match(item):
                bFlieName = False
            elif regCreator.match(item):
                bCreator = False
            elif regDate.match(item):
                bDate = False
            elif regComment.match(item):
                bComment = False                    
        else:
            break

    if bFlieName == False and bCreator == False and bDate == False and bComment == False:
        return False
    else:
        writeerror(fileto, 1, '', error1) 
        return True
    







