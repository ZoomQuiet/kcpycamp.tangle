# -*- coding: cp936 -*-
# Filename: ccrj.py
"""
@author: �ϼ�
@license: kcCCRJ
@version��2.0
@tag��CCRJ������
"""
import sys
from ccrj_help import ccrj_help
from ccrj_main import main
import os
import os.path

import time
begin = int(time.strftime('%H%M%S'))
                                    #��¼��ʼʱ��

"""
@param srcfilename  ��Ҫ�����ļ�
@type srcfilename  �ַ���
@tag���жϸ��ļ��Ƿ���CCRJ�еĲ��Ϸ��ļ�
@return: True���Ϸ��ļ�
"""    
def IsIllegalFile(SrcFilename):     # �ж��Ƿ���c++���͵��ļ�
    if SrcFilename.endswith('.h') or \
       SrcFilename.endswith('.H') or \
       SrcFilename.endswith('.c') or \
       SrcFilename.endswith('.C') or \
       SrcFilename.endswith('.cpp') or \
       SrcFilename.endswith('.CPP'):
        return False
    else:        
        return True    

"""
@param SrcFilename  ��Ҫ�����ļ�
@type SrcFilename  �ַ���

@param DestFolder  ��ŵ�Ŀ���ļ�
@type DestFolder  �ַ���

@param option  ��Ҫ�����ļ�
@type option  �ַ���

@tag���жϸ��ļ��Ƿ���CCRJ�еĲ��Ϸ��ļ�
@return: True���Ϸ��ļ�
""" 
def FileOperation(SrcFilename, DestFolder, option):
    if IsIllegalFile(SrcFilename):  # �ļ�����
        return False
    else:
        Folder,Filename=os.path.split(SrcFilename);
        point = Filename.rfind(".")
        DestFilename = DestFolder[0:]
        i = 0
        while i < len(Filename):
            if i == point:
                DestFilename += "_"
            else:
                DestFilename +=  Filename[i]
            i += 1
        DestFilename += ".txt"  
      
                                    # �����жϱ����
        main(SrcFilename, DestFilename, option)
                                    # ������õĲ������д���
        return True   
    
def MakeFolder(DestFolder):         #�ж����û��Ŀ¼�㽨��
    paths = ""
    i = 0    
    while i < len(DestFolder):
        paths += DestFolder[i]
        i = i + 1
        if paths.endswith("\\") and  (not os.path.exists(DestFolder)):
            os.mkdir(DestFolder)
    
    

# ����ʼ����


if len(sys.argv) > 1 and sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]        # �ж�������Ƿ��ǰ�������
    if option == 'help':
        ccrj_help()
    else:
        print '����Ҫ��ָ��'
    sys.exit()
if len(sys.argv) < 3:
    print '��������,�����뿴����--help'
    sys.exit()
    


if len(sys.argv) > 2: 
    if not os.path.isdir(sys.argv[2]):  
        print '��ʽ����:��������Ĳ���Ŀ¼'
        sys.exit()                  # �жϽ��Ŀ¼�Ƿ����
    
option = "" # Ĭ����ȫѡ
if len(sys.argv) > 3 and sys.argv[3].startswith('--'):
    option = sys.argv[3][2:]        # �ж��Ƿ��й���ѡ�������            
if not sys.argv[2].endswith('\\') : # Ŀ�ĵ����ļ���,�����βû��"\",�Զ�����
    sys.argv[2] += "\\"
MakeFolder(sys.argv[2])             #����Ŀ¼  


    
if os.path.isfile(sys.argv[1]):     # �Ƿ����ļ�?�����Ǵ��ڵ��ļ�
    if FileOperation(sys.argv[1],sys.argv[2], option) == False:
        print '���ǺϷ����ļ�'        # ����.c,.cpp,.h���͵��ļ�
    else:
        print "\t�������"
    end = int(time.strftime('%H%M%S'))
                                    #��¼����ʱ��    
    sys.exit()
elif os.path.isdir(sys.argv[1]):    # �Ƿ����ļ���?
    if not sys.argv[1].endswith("\\"):
        sys.argv[1] += "\\"         # Դ��ַ���ļ���,�����βû��"\",�Զ�����
    for Parent, Folder, Filenames in os.walk(sys.argv[1]):
                                    #�����ļ���, Filenames����ļ���       
        for SrcFilename in Filenames:
            if not Parent.endswith("\\"):
                Parent += "\\"      # Ŀ�ĵ����ļ���,�����βû��"\",�Զ�����      
            SrcFilename = Parent + SrcFilename
            k = len(sys.argv[1])    #��Ŀ��Ŀ¼����Ҳ������Ӧ���ļ���
            DestFolder = sys.argv[2] + Parent[k:]
              #���û��Ŀ¼���Զ�����
            if not os.path.exists(DestFolder):
                os.mkdir(DestFolder)
            
            FileOperation(SrcFilename, DestFolder, option)
                                    # ���ݲ������ļ���������
    print "\t�������"
    
    end = int(time.strftime('%H%M%S'))
                                    #��¼����ʱ��
    sys.exit()
else:
    print "��������Դ������������"
    sys.exit()
          


    
    

        
        

    





