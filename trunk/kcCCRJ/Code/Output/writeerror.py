# -*- coding: cp936 -*-
# �������


#������д���ļ�
def writeerror(fileto, errorline, errorcode, errortype):
    f = file(fileto, 'a')   #���ļ�
    data = '';
    data += '\n����λ��:'
    data += str(errorline)
    data += '\n��������:'
    data += errortype
    data += '\n�������:'
    data += errorcode
    
    f.write(data)           #д���ļ�
    f.close() 
