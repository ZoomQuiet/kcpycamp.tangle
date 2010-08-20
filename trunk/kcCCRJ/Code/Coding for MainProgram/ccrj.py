# -*- coding: cp936 -*-
# Filename: ccrj.py

import sys
from ccrj_help import ccrj_help
from ccrj_main import main
import os
import os.path 
    
def IsIllegalFile(SrcFilename):     # 判断是否是c++类型的文件
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
    if IsIllegalFile(SrcFilename):  # 文件操作
        return False
    else:
        Folder,Filename=os.path.split(SrcFilename);    
        DestFilename = DestFolder[0:] + 'CRJ_' + Filename
                                    # 加上判断标记名
        main(SrcFilename, DestFilename, option)
                                    # 将所获得的参数进行传递
        return True   
    
    
    
    

# 程序开始运行


if len(sys.argv) > 1 and sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]        # 判断输入的是否是帮助命令
    if option == 'help':
        ccrj_help()
    else:
        print '不需要该指令'
    sys.exit()
if len(sys.argv) < 3:
    print '参数不够,详情请看帮助--help'
    sys.exit()

if len(sys.argv) > 2: 
    if not os.path.isdir(sys.argv[2]):  
        print '格式错误:你所输入的目的地不是目录'
        sys.exit()                  # 判断结果目录是否存在
    
option = "" # 默认是全选
if len(sys.argv) > 3 and sys.argv[3].startswith('--'):
    option = sys.argv[3][2:]        # 判断是否有功能选项的输入            

    
if not sys.argv[2].endswith('\\') : # 目的地是文件夹,如果结尾没有"\",自动加上
    sys.argv[2] += "\\"
    
if os.path.isfile(sys.argv[1]):     # 是否是文件?而且是存在的文件
    if FileOperation(sys.argv[1],sys.argv[2], option) == False:
        print '不是合法的文件'        # 不是.c,.cpp,.h类型的文件  
    sys.exit()
elif os.path.isdir(sys.argv[1]):    # 是否是文件夹?
    if not sys.argv[1].endswith("\\"):
        sys.argv[1] += "\\"         # 源地址是文件夹,如果结尾没有"\",自动加上
    for Parent, Folder, Filenames in os.walk(sys.argv[1]):
                                    #遍历文件夹, Filenames存放文件名       
        for SrcFilename in Filenames:
            if not Parent.endswith("\\"):
                Parent += "\\"      # 目的地是文件夹,如果结尾没有"\",自动加上      
            SrcFilename = Parent + SrcFilename
            k = len(sys.argv[1])    #在目的目录里面也建立相应的文件夹
            DestFolder = sys.argv[2] + Parent[k:]       
            FileOperation(SrcFilename, DestFolder, option)
                                    # 传递参数给文件操作函数
    sys.exit()
else:
    print "你所输入源操作数不存在"
    sys.exit()
          


    
    

        
        

    





