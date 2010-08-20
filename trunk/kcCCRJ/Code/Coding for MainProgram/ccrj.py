# -*- coding: cp936 -*-
# Filename: ccrj.py

import sys
from ccrj_help import ccrj_help
from ccrj_main import main
import os
import os.path 
    
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

def FileOperation(SrcFilename, DestFolder, option):
    if IsIllegalFile(SrcFilename):  # �ļ�����
        return False
    else:
        Folder,Filename=os.path.split(SrcFilename);    
        DestFilename = DestFolder[0:] + 'CRJ_' + Filename
                                    # �����жϱ����
        main(SrcFilename, DestFilename, option)
                                    # ������õĲ������д���
        return True   
    
    
    
    

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
        print '��ʽ����:���������Ŀ�ĵز���Ŀ¼'
        sys.exit()                  # �жϽ��Ŀ¼�Ƿ����
    
option = "" # Ĭ����ȫѡ
if len(sys.argv) > 3 and sys.argv[3].startswith('--'):
    option = sys.argv[3][2:]        # �ж��Ƿ��й���ѡ�������            

    
if not sys.argv[2].endswith('\\') : # Ŀ�ĵ����ļ���,�����βû��"\",�Զ�����
    sys.argv[2] += "\\"
    
if os.path.isfile(sys.argv[1]):     # �Ƿ����ļ�?�����Ǵ��ڵ��ļ�
    if FileOperation(sys.argv[1],sys.argv[2], option) == False:
        print '���ǺϷ����ļ�'        # ����.c,.cpp,.h���͵��ļ�  
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
            FileOperation(SrcFilename, DestFolder, option)
                                    # ���ݲ������ļ���������
    sys.exit()
else:
    print "��������Դ������������"
    sys.exit()
          


    
    

        
        

    





