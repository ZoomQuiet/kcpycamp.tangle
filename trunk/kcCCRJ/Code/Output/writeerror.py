# -*- coding: cp936 -*-
# 输出函数


#将错误写进文件
def writeerror(fileto, errorline, errorcode, errortype):
    f = file(fileto, 'a')   #打开文件
    data = '';
    data += '\n错误位置:'
    data += str(errorline)
    data += '\n错误类型:'
    data += errortype
    data += '\n错误代码:'
    data += errorcode
    
    f.write(data)           #写入文件
    f.close() 
