# -*- coding: cp936 -*-
# Filename: variable_name.py

"""
@author: �ϼ�
@license: kcCCRJ
@version��1.0
@tag���ж�һ���ļ��еı��������Ƿ���ϴ���淶,

@param 
@type 
@param 
@type 
@param 
@type 
@return: 
@rtype 
"""
var = {"char":"ch","TCHAR":"ch","bool":"b","BOOL":"b",\
"int":"n","__int16":"n","__int32":"n","__int64":"n","unsigned":"u",\
"long":"l","double":"f","float":"f","BYTE":"by","WORD":"w","DWORD":"dw"}

other_var ={"*":"p", "unsigned long":"ul", "�ַ���":"sz"}

def judge_othercase(key,word,line):
    if "*" not in line:
        return True    
# pointer������ *,������:function,object



def variable_name(srcfilename, destfilename):
    """
    0.����淶���������淶�ϸ�Ļ������жϵ�,�������淶���ϸ��ʱ��,��ȷ�Ի��ܵ�Ӱ��,
    1.����ȱʡ�������,���ᵱ�������Ϲ淶
    2.�������ࡢ�ṹ���ꡢö���Լ����ϵ����Ͷ���
    3.��ʱ�����Ƕ��е����
    4.����������ź���ø��Ͽո�
    5.�ַ�����ָ�뻹û���ж�
    6.Ҫ����Ϲ淶�ı�����̵������ͼ�����(ͷ����ĸ��д,һ����д��ĸҲ����)
    7.���Դ�����(//)ע������,���ǲ����ǿ�/**/ע������
    8.��ʱ���ܴ���������ͽ�϶���
    9.ȫ�ֱ����ͳ�Ա������ʱ���ж�
    """
    srcfile = open(srcfilename,'r')
    destfile= open(destfilename,'a')
    context = ""
    T_or_F = True;
    
    for i in range(80):
        context += "="
    
    context += "\n\n\t\t����淶���ڱ��������ļ��\n"    
    destfile.writelines(context)
    i = 0
    for srcfile_line in srcfile.readlines():
        i = i + 1
        if len(srcfile_line) == 0:
            break
        for key,value in var.items():                
            if key in srcfile_line:         # ֻ�ж���������͵Ĺؼ���
               if not findword(srcfile_line, key):
                   context = """��%s��:"""%i
                   context += srcfile_line
                   T_or_F = False
                   #print srcfile_line
                   destfile.writelines(context)
    srcfile.close()
    destfile.close()
    return T_or_F
    
def findword(line, key): 
    key_flag = 0
    ch = ""
    i = -1
    line_len = len(line) - 1
    while i < line_len:
        i = i + 1
        if 'a' <= line[i] <= 'z':
            ch += line[i]
            continue
        
        if 'A' <= line[i] <= 'Z':
            ch += line[i]
            continue
        
        if '0' <= line[i] and line[i] <= '9':
            ch += line[i]
            continue
        
        if '_' == line[i]:
            ch += line[i]
            continue
        
        if '(' == line[i]:
            key_flag = 0   #�п��ܶ�����Ǻ���,����Ǻ����Ļ�,"("ǰ��Ĳ���
            ch = ""
            continue
        if "//" == ch:
            return True

                            #���ǰ�滹û�ж�������,���ڱ��жϵ�ǰ�����Ƿ��Ƕ�������
        if  0 == key_flag and ch == key:
            key_flag = 1
            ch = ""    
            continue
        if 1 == key_flag and ch != "":   #���ǰ���Ƕ�������
            if len(ch) <= len(var[key]):
                return False             #��������ǰ׺�ĳ���
            if not ch.startswith(var[key]):
                return False             #���������Ͷ�Ӧ��ǰ׺
            if ch[len(var[key])] < 'A' or ch[len(var[key])] > 'Z':
                return False             #ǰ׺�����ĸ�����Ǵ�д��
                
            if ',' == line[i]:
                ch = ""
                continue
                
        ch = ""
        if line[i] == ';':
            key_flag = 0            
            continue
    return True

#�����ǲ������
#a = "C:\\Python25\\CCRJ\\a.h"
#b = "C:\\Python25\\CCRJ\\AA.H"
#variable_name(a, b)

    
