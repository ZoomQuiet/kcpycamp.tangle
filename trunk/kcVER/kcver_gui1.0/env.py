# -*- coding: cp936 -*-

import ConfigParser
#ģ�鹦��:���ļ��н���������Ϣ,���浽�ֵ�
#conf--
#conf ={'\xb2\xa1\xb6\xbe\xc0\xe0\xd0\xcd': 'field_category_value', '\xb2\xa1\xb6\xbe\xd3\xa2\xce\xc4\xc3\xfb\xb3\xc6': 'field_enname_value', '\xd3\xb0\xcf\xec\xcf\xb5\xcd\xb3': '', '\xb2\xa1\xb6\xbe\xd6\xd0\xce\xc4\xc3\xfb\xb3\xc6': '', '\xcd\xfe\xd0\xb2\xbc\xb6\xb1\xf0': 'field_level_value', '\xb9\xd8\xbc\xfc\xb4\xca': '', '\xb2\xa1\xb6\xbe\xbc\xf2\xbd\xe9': '', '\xb8\xd0\xc8\xbe\xcd\xbe\xbe\xb6': '', '\xb2\xa1\xb6\xbe\xb1\xf0\xc3\xfb': '', '\xd0\xd0\xce\xaa\xb7\xd6\xce\xf6': 'field_remark_value', '\xb2\xa1\xb6\xbe\xb3\xa4\xb6\xc8': ''}
#dbcon ={'passwd': '123456', 'host': 'localhost', 'db': 'test1', 'user': 'root'}
#--conf
#�жϴ�s���Ƿ����ֵ�dk�е�key��ͷ
def HasKey(s, dk):
    for kk in dk:
        if s.startswith(kk):
            return True
    return False

#������s�е��ֶ�����ֵ�������ֵ�dk��
def Token(s,dk):
    a=s.split(':',1)
    if a[0] in dk:
        dk[a[0]]=a[1].strip()
g_ddb={}#���ݿ����Ӳ���
g_dtxt={}#�ļ��ֶ���ȡ
g_dsql={}#���ݿ���ֶ�
g_uid=-1
g_user=''
#�������ļ�     
def ReadCfg(path):
    global g_ddb,g_dtxt,g_dsql
    cfg = ConfigParser.ConfigParser()
    cfg.read(path)
    s=cfg.sections()
    v=cfg.items('txt_field')
    for vi in v:
        g_dtxt[vi[0]]=vi[1]
    v=cfg.items('db_field')
    for vi in v:
        g_dsql[vi[0]]=vi[1]
    v=cfg.items('dbcon')
    for vi in v:
        g_ddb[vi[0]]=vi[1]
    for k,v in g_ddb.items():
        #print k,v
        pass
if __name__ == '__main__':
    pass
