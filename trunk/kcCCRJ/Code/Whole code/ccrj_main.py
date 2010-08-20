# -*- coding: cp936 -*-
# Filename: ccrj_main.py

import Code_Ruler4
import Code_Ruler1
import Code_Ruler8
import Code_Ruler9
import Code_Ruler_VarName


    
def main(SrcFilename, DestFilename, Option):
    bFile = False

    if Code_Ruler1.check1(SrcFilename, DestFilename):
        bFile = True      # 文件头注释检测
    if Code_Ruler8.check(SrcFilename, DestFilename):
        bFile = True      # 关于{}问题
    if Code_Ruler4.coderule4(SrcFilename, DestFilename):
        bFile = True      # 合并行问题
    if Code_Ruler9.check1(SrcFilename, DestFilename):
        bFile = True      # 空格问题
    if Code_Ruler_VarName.variable_name(SrcFilename, DestFilename):
        bFile = True      # 变量名命名规范
    
    if False == bFile:
        print "\n%s\n符合代码规范"%SrcFilename
    else:
        print "\n%s\n不符合代码规范"%SrcFilename

    
       
    
    
