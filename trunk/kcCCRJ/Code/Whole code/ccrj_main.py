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
        bFile = True      # �ļ�ͷע�ͼ��
    if Code_Ruler8.check(SrcFilename, DestFilename):
        bFile = True      # ����{}����
    if Code_Ruler4.coderule4(SrcFilename, DestFilename):
        bFile = True      # �ϲ�������
    if Code_Ruler9.check1(SrcFilename, DestFilename):
        bFile = True      # �ո�����
    if Code_Ruler_VarName.variable_name(SrcFilename, DestFilename):
        bFile = True      # �����������淶
    
    if False == bFile:
        print "\n%s\n���ϴ���淶"%SrcFilename
    else:
        print "\n%s\n�����ϴ���淶"%SrcFilename

    
       
    
    
