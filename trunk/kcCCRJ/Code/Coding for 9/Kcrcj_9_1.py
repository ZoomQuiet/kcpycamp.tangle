# coding: gbk
#���9.1���ֹ��ܣ��в�����
'''
BUG
1.�޷�������*�ţ����Ե��˺ţ�ָ��ȣ����в�ͬ����ķ��ţ�ֱ�Ӻ��ԡ�����֪����*��&�� 
2.�Ӽ��ſ��Ե�����Ҳ���Ե�ǰ׺ʹ�ã���ǰ׺ʹ�õ�ʱ��һ��ᱻ����ɴ���
3.����һЩδ���֣�����~~~
'''
import re
regWhiteBlank =re.compile('^\s*$|^\s*//|^\s*/\*')    #ƥ����л���ע���е����
regRemark =re.compile('.s(//.*)')    #ƥ��ע�͵����
regImport =re.compile('^\s*#')    #ƥ��#�ſ�ʼ�����������#include��#define

listOperZero = ['++', '--', '->', '::']
listOperOne = ['>=', '<=', '*=', '/=', '%=', '+=', '-=', '^=', '&=', '|=','&&','||','==','!=']
listOperTwo = ['>', '<',  '/', '+', '-', '^', '|', '?']    #*��������

linelist = []
errordata = []
error9_1= '��˫Ŀ�����ǰ������пո�'


#����ע��
def ReplaceRemark(linecode):
    regRemark = re.compile('.*?(//.*)')    #ƥ��ע�͵����
    if regRemark.match(linecode):
       strDataToR = regRemark.match(linecode).group(1)
     #  print "str:" + strDataToR
       linecode = linecode.replace(strDataToR, '') 
    return linecode


def GetFileData(filefrom):
    f = file(filefrom)
    while True:
        line = f.readline()
        if len(line) == 0: # Zero length indicates EOF
            break
        linelist.append(line)
    f.close() # close the file 

def ShowFileData():
    for i in linelist:
        print i,

def ShowErrorData():
    for i in errordata:
        print i, 

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
    errordata.append(data)  #д���������
    f.write(data)           #д���ļ�
    f.close() 

    

#��� ����������{}��Ӧ�� ����   
def check2(filefrom, fileto):
    linenum = -1
    for linecode in linelist:
         linenum = linenum + 1
         if regWhiteBlank.match(linecode):
             continue
         if regImport.match(linecode):
             continue

      #   print linenum
         linecode = ReplaceRemark(linecode)
      #   print linecode
         linecode = CheckWithOperZero(linecode)
      #   print linecode
         linecode = CheckWithOperOne(linenum, linecode, fileto)
         linecode = CheckWithOperTwo(linenum, linecode, fileto)

def CheckWithOperZero(linestr,):
    for item in listOperZero:   
        linestr = linestr.replace(item, '@@')
    return linestr




def CheckWithOperOne(linenum, linestr, fileto):
    for item in listOperOne:
        t = linestr.split(item)
        tlen = len(t)
        if tlen == 1:
            continue

        num = -1
        for i in t:
        #     print i
            num=num+1
        #    print num
            if num == 0:
                if not i.endswith(' '):
                    strerror = '��%d��%s������ո��д���' % (linenum+1, item)
                    writeerror(fileto, linenum+1, linelist[linenum], strerror)
            elif num == tlen - 1:
                if not i.startswith(' '):
                    strerror = '��%d��%s�����ҿո��д���' % (linenum+1, item)
                    writeerror(fileto, linenum+1, linelist[linenum], strerror)
            else:
                if not i.startswith(' '):
                    strerror = '��%d��%s�����ҿո��д���' % (linenum+1, item)
                    writeerror(fileto, linenum+1, linelist[linenum], strerror)
                if not i.endswith(' '):
                    strerror = '��%d��%s������ո��д���' % (linenum+1, item)
                    writeerror(fileto, linenum+1, linelist[linenum], strerror)
        linestr =linestr.replace(item, '@')
        
    return linestr

def CheckWithOperTwo(linenum, linestr, fileto):
    for item in listOperTwo:
        t = linestr.split(item)
        tlen = len(t)
        if tlen == 1:
            continue

        num = -1
        for i in t:
            num=num+1
            if num == 0:
                if not i.endswith(' '):
                    strerror = '��%d��%s������ո��д���' % (linenum+1, item)
                    writeerror(fileto, linenum+1, linelist[linenum], strerror)
            elif num == tlen - 1:
                if not i.startswith(' '):
                    strerror = '��%d��%s�����ҿո��д���' % (linenum+1, item)
                    writeerror(fileto, linenum+1, linelist[linenum], strerror)
            else:
                if not i.startswith(' '):
                    strerror = '��%d��%s�����ҿո��д���' % (linenum+1, item)
                    writeerror(fileto, linenum+1, linelist[linenum], strerror)
                if not i.endswith(' '):
                    strerror = '��%d��%s������ո��д���' % (linenum+1, item)
                    writeerror(fileto, linenum+1, linelist[linenum], strerror)   
        linestr =linestr.replace(item, '@')
        
    return linestr

def check(filefrom, fileto):
    GetFileData(filefrom) #��ȡ�ļ�����
    flag = False
    flag = check1('4.cpp', 'out.txt')
    if(flag):
        check2('4.cpp', 'out.txt')      
    return flag

GetFileData('KGameUI.cpp')
check2('KGameUI.cpp', 'out.txt')
ShowErrorData()
#ShowFileData()


