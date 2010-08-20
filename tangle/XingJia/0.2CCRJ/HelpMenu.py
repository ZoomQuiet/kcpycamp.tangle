# -*- coding: cp936 -*-
# Filename: HelpMenu.py
def HelpMenu():
    print """
    *********************************************
                    主菜单中:
            File    [FileName]  单个文件命令
            注意:不包括"[]"
            例如：File C:\VC++\TEST.cpp
            或者：File TEST.h       (当前文件夹下的文件）

            Folder   [Path]     整个目录命令  
            例如：Folder C:\VC++\
            或者：Folder C:\VC++      (自动加上"\\")

            H(help)             帮助命令 
            Q(Quit)             退出命令

                        子菜单：
            默认（所有选项都匹配）
            default  

            自定义 （列出所有选项由用户选择）
            custom


                    自定义子菜单
            A. 文件起始处的说明
            B. 关于注释
            C. 每行代码长度
            D. 合并行的问题
            E. 指针中*号的位置
            F. 全局函数的调用
            G. 关于if...else if
            H. 与“{”、“}”有关的各项规定
            I. 与空格有关的各项规定
            J. 与缩进有关的各项规定
            K. 关于出错处理
            L. 与类相关的.h文件与.cpp文件
            M. 注释书写与自动生成帮助文档规范
            N. 命名规范

            例如：AN   (只检查AN两项）
    *********************************************
"""
# End of HelpMenu.py



















