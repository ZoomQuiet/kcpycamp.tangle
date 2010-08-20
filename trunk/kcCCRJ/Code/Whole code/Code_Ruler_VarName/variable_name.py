# -*- coding: cp936 -*-
# Filename: variable_name.py
from writeerror import writeerror
"""
@author: 邢佳
@license: kcCCRJ
@version：1.0
@tag：判断一个文件中的变量定义是否符合代码规范,
"""


var = {"char":"ch", "TCHAR":"ch", "bool":"b", "BOOL":"b", "int":"n",\
       "__int16":"n", "__int32":"n", "__int64":"n", "unsigned":"u", \
       "long":"l","double":"f","float":"f","BYTE":"by","WORD":"w",\
       "DWORD":"dw","int*":"pn","int**":"ppn","char*":"pch",\
       "char**":"ppch","bool*":"pb","bool**":"ppb"}
not_finish_var ={ "int*":"pn","int**":"ppn","char*":"pch","char**":"ppch", "unsigned long":"ul", "字符串":"sz"}



"""
@param srcfilename  需要检测的文件
@type srcfilename  字符串
@param destfilename 存放结果的文件
@type destfilename 字符串
"""
def variable_name(srcfilename, destfilename):
    """
    0.这个规范是在其他规范合格的基础上判断的,当其他规范不合格的时候,正确性会受到影响,
    1.对于缺省定义变量,将会当做不符合规范
    2.不考虑类、结构、宏、枚举以及联合的类型定义
    3.暂时不考虑多行的情况(不考虑多个逻辑行在一个物理行和一个逻辑行在多个无论行)
    5.字符串无法判断
    6.要求符合规范的变量最短的是类型加名字(前面字母是类型名,类型名过后的第一个字母必须大写),那么i,j等也会报错
    7.可以处理行(//)注释问题,但是不考虑块/**/注释问题
    8.暂时不能处理多种类型结合定义
    9.全局变量和成员变量的名字定义会误判
    10.不考虑自定义类型的变量名
    11.指针判断取只能检测判对第一个类型且*号是在左边的,因此假设用户不会在同一逻辑行定义指针和普通变量.
    """
    srcfile = open(srcfilename,'r')
    T_or_F = False;
    i = 0
    for srcfile_line in srcfile.readlines():
        context = "代码规范关于变量命名的检查:"    
        i = i + 1
        if len(srcfile_line) == 0:
            break
        for key,value in var.items():
            
            if key in srcfile_line:         # 只判断有相关类型的关键字
              #  print key,"is",srcfile_line
                if not findword(srcfile_line, key):
                    context += key
                    writeerror(destfilename, i, srcfile_line, context)
                    T_or_F = True                  
    srcfile.close()
    return T_or_F

"""
@param line  当前文件一行的内容
@type line  字符串
@param key 当前的类型
@type key 字符串
"""    
def findword(line, key): 
    key_flag = 0
    ch = ""
    i = -1
    line_len = len(line) - 1
    while i < line_len:
        i = i + 1
        if ('/' == line[i]) and ('/' == line[i - 1]):
            return True    # 如果遇到注释,便结束
        
        if ('a' <= line[i] <= 'z') or \
           ('A' <= line[i] <= 'Z') or \
           ('0' <= line[i] and line[i] <= '9') or\
           ('_' == line[i]):
            ch += line[i]  # 变量名的有效字符
            continue      
        if '(' == line[i] or ')'== line[i]:
            key_flag = 0   # 有可能定义的是函数,如果是函数的话,"("前面的不算
            ch = ""        # 也有可能是sizeof对该类型取值
            continue
        if  0 == key_flag and "*" == line[i]:
            ch += line[i]
            key_flag = 0   # 有可能定义的是函数,如果是函数的话,"("前面的不算
            continue 
        
        if 1 == key_flag and (':' == line[i]) and ('::' in line):
            ch = ""         
            continue        # 如果变量::操作符,前面的不是变量名        


                            # 如果前面还没有定义类型,现在便判断当前单词是否是定义类型
        if  0 == key_flag and ch == key:
            key_flag = 1
            ch = ""    
            continue
        
        if 1 == key_flag and ch != "":   # 如果前面是定义类型
                                        #这部分是判断是否同一行有其他的类型定义,如在函数里面的参数
            if ch in var:               
                if ch == key:
                    ch = ""
                    continue
                else:
                    key_flag = 0
                    ch = ""
                    continue
                    
                
            if len(ch) <= len(var[key]):
                return False             # 不能少于前缀的长度
            if not ch.startswith(var[key]):
                return False             # 必须是类型对应的前缀
            if ch[len(var[key])] < 'A' or ch[len(var[key])] > 'Z':
                return False             # 类型前缀后的字母必须是大写的
                
            if ',' == line[i]:
                ch = ""
                continue
        if line[i] == ';':
            key_flag = 0
            ch = ""
            continue
    return True

#以下是测试语句
##b = "C:\\Documents and Settings\\kcs0006\\桌面\\CCRJ\\a.h"
##a = "C:\\Documents and Settings\\kcs0006\\桌面\\CCRJ\\b.h"
##variable_name(a, b)

    
