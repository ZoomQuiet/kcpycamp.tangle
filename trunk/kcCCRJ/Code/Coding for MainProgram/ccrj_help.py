# -*- coding: cp936 -*-
# Filename: ccrj_help.py

def ccrj_help():
    print    """
    在DOS窗口下:
    对照DOS,

    C:\Python25\CCRJ\CCRJ.PY C:\TEST.CPP C:\
    (单个文件后缀命必须是.C,.CPP,.H,否则默认成输入的的目录)
    直接判断文件TEST.CPP  是否符合所有的代码规范
    并将检查结果放到C盘下(结果是CRJ_TEST.TXT)

    C:\Python25\CCRJ\CCRJ.PY C:\VC++ C:\
    只要后缀名不是.C,.CPP,.H,则当成目录判断
     
    C:\Python25\CCRJ\CCRJ.PY --help
    显示帮助

    如果只想检查某些匹配选择
    那么可以这样  C:\Python25\CCRJ\CCRJ.PY  C:\TEST.CPP  C:\  -ABC
    第四个参数就是 说明匹配ABC项目
    而结果文件则放在C盘下,每个文件名分别是CRE_x.TXT(x为原来判定文件的名字)
    (具体匹配项目可以从"帮助"里面查询)

    ps:参数1为CCRJ主程序,由于时间原因,暂时无法直接设计CCRJ为启动命令,只能用绝对路径,
       参数2为源文件(或帮助命令)
       参数3为目的文件
       参数4为选项
       程序容错功能,将放到后期实现

    整个过程只需要用户输入一次命令:方便.
    """







