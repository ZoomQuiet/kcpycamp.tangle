# -*- coding: cp936 -*-
#模块功能:从文件中解析病毒信息,保存到字典
#conf--
conf ={'\xb2\xa1\xb6\xbe\xc0\xe0\xd0\xcd': 'field_category_value', '\xb2\xa1\xb6\xbe\xd3\xa2\xce\xc4\xc3\xfb\xb3\xc6': 'field_enname_value', '\xd3\xb0\xcf\xec\xcf\xb5\xcd\xb3': '', '\xb2\xa1\xb6\xbe\xd6\xd0\xce\xc4\xc3\xfb\xb3\xc6': '', '\xcd\xfe\xd0\xb2\xbc\xb6\xb1\xf0': 'field_level_value', '\xb9\xd8\xbc\xfc\xb4\xca': '', '\xb2\xa1\xb6\xbe\xbc\xf2\xbd\xe9': '', '\xb8\xd0\xc8\xbe\xcd\xbe\xbe\xb6': '', '\xb2\xa1\xb6\xbe\xb1\xf0\xc3\xfb': '', '\xd0\xd0\xce\xaa\xb7\xd6\xce\xf6': 'field_remark_value', '\xb2\xa1\xb6\xbe\xb3\xa4\xb6\xc8': ''}
dbcon ={'passwd': '123456', 'host': 'localhost', 'db': 'test1', 'user': 'root'}
#--conf
#判断串s中是否以字典dk中的key开头
def HasKey(s, dk):
    for kk in dk:
        if s.startswith(kk):
            return True
    return False

#解析串s中的字段名和值并存入字典dk中
def Token(s,dk):
    a=s.split(':',1)
    if a[0] in dk:
        dk[a[0]]=a[1].strip()

if __name__ == '__main__':
    print 'good'
