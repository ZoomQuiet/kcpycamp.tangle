# -*- coding: cp936 -*-
#check���������9.2����
from writeerror import writeerror
import re

"""
@author: ����
@license: kcCCRJ
@version��1.0
@tag���ж�while,if,for������һ���ո�
"""
linelist = []
listSpecialStr = ['for','if','while']

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
@tag���ж�while,if,for������һ���ո�
@param filefrom����ȡ���ļ����� 
@type filefrom: �ַ���
@param fileto��д�����ļ����� 
@type fileto: �ַ���
"""
def check1(filefrom, fileto):
    bFlag = False
    GetFileData(filefrom)
    rega = re.compile('\W+')              #�ָ�ʵı��ʽ
    regb = re.compile(' \S+')
    regSkip =re.compile('^\s*//|^\s*/\*')    #ƥ����л���ע���е����


    num = -1;  
    for item in linelist:
        num = num + 1
        if regSkip.match(item):
            continue
        
        strTemp = rega.split(item)
        for subitem in strTemp:
       #     print subitem
            if subitem in listSpecialStr:
        #        print subitem
                strSplited = item.split(subitem)
                if regb.match(strSplited[1]):
                    continue
                else:
                    writeerror(fileto, num + 1, linelist[num], subitem+'�ź���Ӧ��ֻ��һ���ո�')
                    bFlag = True

    return bFlag




