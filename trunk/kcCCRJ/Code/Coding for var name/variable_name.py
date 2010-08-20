# -*- coding: cp936 -*-
# Filename: variable_name.py

"""
@author: 邢佳
@license: kcCCRJ
@version：1.0
@tag：判断一个文件中的变量定义是否符合代码规范,

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

other_var ={"*":"p", "unsigned long":"ul", "字符串":"sz"}

def judge_othercase(key,word,line):
    if "*" not in line:
        return True    
# pointer类型是 *,不考虑:function,object



def variable_name(srcfilename, destfilename):
    """
    0.这个规范是在其他规范合格的基础上判断的,当其他规范不合格的时候,正确性会受到影响,
    1.对于缺省定义变量,将会当做不符合规范
    2.不考虑类、结构、宏、枚举以及联合的类型定义
    3.暂时不考虑多行的情况
    4.假设操作符号后面得跟上空格
    5.字符串和指针还没有判断
    6.要求符合规范的变量最短得是类型加名字(头个字母大写,一个大写字母也符合)
    7.可以处理行(//)注释问题,但是不考虑块/**/注释问题
    8.暂时不能处理多种类型结合定义
    9.全局变量和成员变量暂时不判断
    """
    srcfile = open(srcfilename,'r')
    destfile= open(destfilename,'a')
    context = ""
    T_or_F = True;
    
    for i in range(80):
        context += "="
    
    context += "\n\n\t\t代码规范关于变量命名的检查\n"    
    destfile.writelines(context)
    i = 0
    for srcfile_line in srcfile.readlines():
        i = i + 1
        if len(srcfile_line) == 0:
            break
        for key,value in var.items():                
            if key in srcfile_line:         # 只判断有相关类型的关键字
               if not findword(srcfile_line, key):
                   context = """第%s行:"""%i
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
            key_flag = 0   #有可能定义的是函数,如果是函数的话,"("前面的不算
            ch = ""
            continue
        if "//" == ch:
            return True

                            #如果前面还没有定义类型,现在便判断当前单词是否是定义类型
        if  0 == key_flag and ch == key:
            key_flag = 1
            ch = ""    
            continue
        if 1 == key_flag and ch != "":   #如果前面是定义类型
            if len(ch) <= len(var[key]):
                return False             #不能少于前缀的长度
            if not ch.startswith(var[key]):
                return False             #必须是类型对应的前缀
            if ch[len(var[key])] < 'A' or ch[len(var[key])] > 'Z':
                return False             #前缀后的字母必须是大写的
                
            if ',' == line[i]:
                ch = ""
                continue
                
        ch = ""
        if line[i] == ';':
            key_flag = 0            
            continue
    return True

#以下是测试语句
#a = "C:\\Python25\\CCRJ\\a.h"
#b = "C:\\Python25\\CCRJ\\AA.H"
#variable_name(a, b)

    
