# -*- coding: cp936 -*-
# Filename: ccrj_main.py

def main(SrcFilename, DestFilename, Option):
    """调用各个判断函数的主程序"""
    print "\n"
    print "\t所操作的文件是%s."%SrcFilename
    if Option == "":
        print "\t默认所有检查所有的条例"
    else:
        print "\t你所选的条例是:%s."%Option
    print "\t程序处理中"
    print "\t完成,结果保存在%s."%DestFilename
    
