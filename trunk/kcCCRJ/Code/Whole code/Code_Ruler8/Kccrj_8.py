# -*- coding: cp936 -*-
#check���������8.1����
from writeerror import writeerror

import re


linelist = []
error8_1= '��{֮ǰֻ�����пո񣬺��������ע�ͣ����������д���'
error8_2 = '��%d�е�{�͵�%d�е�}����Ӧ'

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


    

#��� ����{֮ǰֻ�����пո񣬺��������ע�ͣ����������д��롯 ����
def check1(filefrom, fileto):
    num = -1
    rega = re.compile('^\s*$')              #ƥ��ǰ׺�ո�
    regb =re.compile('^\s*//|^\s*/\*.*\*/$')    #ƥ�������ֺ���������ȫ��Ϊ�ջ��߳���//���߳���/*������*/��β
    bFlag = False
    for item in linelist:
        num = num + 1
        if regb.match(item):
            continue
        if '{' in item:
            splitStr = item.split('{')
            if rega.match(splitStr[0]) and\
               (rega.match(splitStr[1]) or regb.match(splitStr[1])):
                continue
            else:
                writeerror(fileto, num + 1, linelist[num], error8_1)
                bFlag = True

    return bFlag
    

#��ɺ�������{}��Ӧ�� ����   
def check2(filefrom, fileto):  
    listLineNum = []        #���{���ţ��±��ʾ��i��
    listPos = []            #���{���Ŷ�Ӧ��ǰ�ÿո�����
    regb =re.compile('^\s*//|^\s*/\*.*\*/$')    #ƥ�������ֺ���������ȫ��Ϊ�ջ��߳���//���߳���/*������*/��β
    num = -1
    bFlag = False
    for i in linelist:      #����
        num = num + 1
        if regb.match(i):
            continue        
        if('{' in i):           #����{���ţ���ջ
            t = i.replace('\t', '    ')     #���Ʊ��\t�����4���ո�
            listLineNum.append(num)          
            listPos.append(t.index('{'))    
            
         #   print t,
         #   print 'input:',num, t.index('{')
         #   print '\n'
         
        if('}' in i):
            if(len(listLineNum) > 0):
                linenum = listLineNum.pop() 
                linestr = listPos.pop()
                t = i.replace('\t', '    ')               
                if(t.index('}') != linestr):        #��{��}���бȽϣ����ǰ�ÿո�ͬ������
          #          print linestr, t.index('}')
                    writeerror(fileto, num + 1, linelist[num], error8_2 % (linenum + 1, num + 1))
                    bFlag = True
    return bFlag

    

def check(filefrom, fileto):
    GetFileData(filefrom) #��ȡ�ļ�����
    bFile1 = check1(filefrom, fileto)
    bFile2 = check2(filefrom, fileto)
    return bFile1 or bFile2  


#check('8.1 test_change.h', 'out.txt')



