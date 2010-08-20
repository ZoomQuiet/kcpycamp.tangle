# -*- coding: cp936 -*-
# Filename: variable_name.py
from writeerror import writeerror
"""
@author: �ϼ�
@license: kcCCRJ
@version��1.0
@tag���ж�һ���ļ��еı��������Ƿ���ϴ���淶,
"""


var = {"char":"ch", "TCHAR":"ch", "bool":"b", "BOOL":"b", "int":"n",\
       "__int16":"n", "__int32":"n", "__int64":"n", "unsigned":"u", \
       "long":"l","double":"f","float":"f","BYTE":"by","WORD":"w",\
       "DWORD":"dw","int*":"pn","int**":"ppn","char*":"pch",\
       "char**":"ppch","bool*":"pb","bool**":"ppb"}
not_finish_var ={ "int*":"pn","int**":"ppn","char*":"pch","char**":"ppch", "unsigned long":"ul", "�ַ���":"sz"}



"""
@param srcfilename  ��Ҫ�����ļ�
@type srcfilename  �ַ���
@param destfilename ��Ž�����ļ�
@type destfilename �ַ���
"""
def variable_name(srcfilename, destfilename):
    """
    0.����淶���������淶�ϸ�Ļ������жϵ�,�������淶���ϸ��ʱ��,��ȷ�Ի��ܵ�Ӱ��,
    1.����ȱʡ�������,���ᵱ�������Ϲ淶
    2.�������ࡢ�ṹ���ꡢö���Լ����ϵ����Ͷ���
    3.��ʱ�����Ƕ��е����(�����Ƕ���߼�����һ�������к�һ���߼����ڶ��������)
    5.�ַ����޷��ж�
    6.Ҫ����Ϲ淶�ı�����̵������ͼ�����(ǰ����ĸ��������,����������ĵ�һ����ĸ�����д),��ôi,j��Ҳ�ᱨ��
    7.���Դ�����(//)ע������,���ǲ����ǿ�/**/ע������
    8.��ʱ���ܴ���������ͽ�϶���
    9.ȫ�ֱ����ͳ�Ա���������ֶ��������
    10.�������Զ������͵ı�����
    11.ָ���ж�ȡֻ�ܼ���жԵ�һ��������*��������ߵ�,��˼����û�������ͬһ�߼��ж���ָ�����ͨ����.
    """
    srcfile = open(srcfilename,'r')
    T_or_F = False;
    i = 0
    for srcfile_line in srcfile.readlines():
        context = "����淶���ڱ��������ļ��:"    
        i = i + 1
        if len(srcfile_line) == 0:
            break
        for key,value in var.items():
            
            if key in srcfile_line:         # ֻ�ж���������͵Ĺؼ���
              #  print key,"is",srcfile_line
                if not findword(srcfile_line, key):
                    context += key
                    writeerror(destfilename, i, srcfile_line, context)
                    T_or_F = True                  
    srcfile.close()
    return T_or_F

"""
@param line  ��ǰ�ļ�һ�е�����
@type line  �ַ���
@param key ��ǰ������
@type key �ַ���
"""    
def findword(line, key): 
    key_flag = 0
    ch = ""
    i = -1
    line_len = len(line) - 1
    while i < line_len:
        i = i + 1
        if ('/' == line[i]) and ('/' == line[i - 1]):
            return True    # �������ע��,�����
        
        if ('a' <= line[i] <= 'z') or \
           ('A' <= line[i] <= 'Z') or \
           ('0' <= line[i] and line[i] <= '9') or\
           ('_' == line[i]):
            ch += line[i]  # ����������Ч�ַ�
            continue      
        if '(' == line[i] or ')'== line[i]:
            key_flag = 0   # �п��ܶ�����Ǻ���,����Ǻ����Ļ�,"("ǰ��Ĳ���
            ch = ""        # Ҳ�п�����sizeof�Ը�����ȡֵ
            continue
        if  0 == key_flag and "*" == line[i]:
            ch += line[i]
            key_flag = 0   # �п��ܶ�����Ǻ���,����Ǻ����Ļ�,"("ǰ��Ĳ���
            continue 
        
        if 1 == key_flag and (':' == line[i]) and ('::' in line):
            ch = ""         
            continue        # �������::������,ǰ��Ĳ��Ǳ�����        


                            # ���ǰ�滹û�ж�������,���ڱ��жϵ�ǰ�����Ƿ��Ƕ�������
        if  0 == key_flag and ch == key:
            key_flag = 1
            ch = ""    
            continue
        
        if 1 == key_flag and ch != "":   # ���ǰ���Ƕ�������
                                        #�ⲿ�����ж��Ƿ�ͬһ�������������Ͷ���,���ں�������Ĳ���
            if ch in var:               
                if ch == key:
                    ch = ""
                    continue
                else:
                    key_flag = 0
                    ch = ""
                    continue
                    
                
            if len(ch) <= len(var[key]):
                return False             # ��������ǰ׺�ĳ���
            if not ch.startswith(var[key]):
                return False             # ���������Ͷ�Ӧ��ǰ׺
            if ch[len(var[key])] < 'A' or ch[len(var[key])] > 'Z':
                return False             # ����ǰ׺�����ĸ�����Ǵ�д��
                
            if ',' == line[i]:
                ch = ""
                continue
        if line[i] == ';':
            key_flag = 0
            ch = ""
            continue
    return True

#�����ǲ������
##b = "C:\\Documents and Settings\\kcs0006\\����\\CCRJ\\a.h"
##a = "C:\\Documents and Settings\\kcs0006\\����\\CCRJ\\b.h"
##variable_name(a, b)

    
