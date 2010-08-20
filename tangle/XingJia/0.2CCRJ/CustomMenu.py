# -*- coding: cp936 -*-
# Filename: CustomMenu.py
def CustomMenu():
    print """
    *********************************************
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
    *********************************************
    """
    szCmd = raw_input()
    return szCmd
# End of CustomMenu.py
