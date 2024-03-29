# -*- coding: cp936 -*-
import time
import env
StrSqlOrg="""INSERT INTO `node` (`nid`,`vid`,`type`,`title`,`uid`,`promote`,`sticky`,`created`,`changed`)
VALUES (id_node,id_node_ver,'virus','病毒英文名称','1','1','0',post,post);

INSERT INTO `content_type_virus` (`vid`,`nid`,`field_alias_value`,`field_length_value`,`field_category_value`,`field_brief_value`,`field_brief_format`,`field_remark_format`,`field_level_value`,`field_platform_value`)
VALUES (id_node_ver,id_node,'病毒别名','病毒长度','病毒类型','病毒简介','1','1','威胁级别','影响系统');

INSERT INTO `content_field_cnname` (`nid`,`vid`,`field_cnname_value`)
 VALUES (id_node,id_node_ver,'病毒中文名称');

INSERT INTO `term_data` (`tid`,`vid`,`name`,`weight`)
 VALUES (id_term,'1','','0');

INSERT INTO `term_node` (`nid`,`tid`)
VALUES (id_node,id_term);

INSERT INTO `nodewords` (`type`,`id`,`name`,`content`)
 VALUES ('node',id_node,'description','kword0');

INSERT INTO `nodewords` (`type`,`id`,`name`,`content`)
 VALUES ('node',id_node,'keywords','kword0');

INSERT INTO `node_revisions` (`nid`,`vid`,`uid`,`title`,`body`,`teaser`,`log`,`format`,`timestamp`)
 VALUES (id_node,id_node_ver,'1','病毒英文名称','行为分析','teaser','log','1',post) ;

UPDATE `sequences` SET `id`=id_node
WHERE (`name`='node_nid' );

UPDATE `sequences` SET `id`=id_node_ver
 WHERE (`name`='node_revisions_vid' );

UPDATE `sequences` SET `id`=id_term
WHERE (`name`='term_data_tid' );

DELETE FROM cache_page"""
#补充uid 变量,变量统一加前缀var_
#vars:var_nid,var_vid,var_uid,var_time
#var_teaser,var_body需要在配置文件中补充
#var_time最好取服务器时间,可以SQL查询时间
StrAddNode="""INSERT INTO `node` (`nid`,`vid`,`type`,`title`,`uid`,`promote`,`sticky`,`created`,`changed`)
VALUES ('var_nid','var_vid','virus','var_title','var_uid','1','0','var_time','var_time');

INSERT INTO `content_type_virus` (`vid`,`nid`,`field_alias_value`,`field_length_value`,`field_category_value`,
                                `field_brief_value`,`field_brief_format`,`field_remark_format`,
                                `field_level_value`,`field_platform_value`)
VALUES ('var_vid','var_nid','var_field_alias_value','var_field_length_value','var_field_category_value',
'var_field_brief_value','1','1',
'var_field_level_value','var_field_platform_value');

INSERT INTO `content_field_cnname` (`nid`,`vid`,`field_cnname_value`)
VALUES ('var_nid','var_vid','var_field_cnname_value');

INSERT INTO `node_revisions` (`nid`,`vid`,`uid`,`title`,`body`,`teaser`,`log`,`format`,`timestamp`)
VALUES ('var_nid','var_vid','var_uid','var_title','var_body','var_teaser','','1','var_time');

UPDATE `sequences` SET `id`='var_nid' WHERE (`name`='node_nid');

UPDATE `sequences` SET `id`='var_vid' WHERE (`name`='node_revisions_vid');

DELETE FROM cache_page"""

StrAddTerm="""INSERT INTO `term_data` (`tid`,`vid`,`name`,`weight`)
VALUES (id_term,'1','','0');

INSERT INTO `term_node` (`nid`,`tid`)
VALUES (id_node,id_term);

UPDATE `sequences` SET `id`=id_term
WHERE (`name`='term_data_tid' );"""

def GetPlatform(s0 , platform):
    sp=platform.replace('/',' ')
    index = s0.lower().find(sp.lower())
    return s0[index:index+len(sp)]

def AddNodeSql(var_nid,var_vid,var_uid,var_time,dinfo,platformtxt):
    StrObj=''+StrAddNode
    StrObj=StrObj.replace('var_nid',`var_nid`)
    StrObj=StrObj.replace('var_vid',`var_vid`)
    StrObj=StrObj.replace('var_uid',`var_uid`)
    StrObj=StrObj.replace('var_time',`var_time`)
    for k ,v in env.g_dsql.items():
        if k == 'var_field_level_value':#危险级别
            StrObj=StrObj.replace(k,MakeStars(dinfo[v]))
        elif k == 'var_field_platform_value':
            StrObj=StrObj.replace(k,GetPlatform(platformtxt,dinfo[v]))
        else:
            StrObj=StrObj.replace(k,dinfo[v])
    return StrObj

def MakeStars(star):
    return (star+'☆'*((5*2-len(star))/2))
def MakeSql(nid,vid,tid,dinfo):
    id_node = nid
    id_node_ver=vid
    id_term=tid
    post=int(time.time())
    StrSqlObj= ''+StrSqlOrg
    StrSqlObj= StrSqlObj.replace('id_node_ver',("'"+`id_node_ver`+"'"))
    StrSqlObj= StrSqlObj.replace('id_node',("'"+`id_node`+"'"))
    StrSqlObj= StrSqlObj.replace('id_term',("'"+`id_term`+"'"))
    StrSqlObj= StrSqlObj.replace('post',("'"+`post`+"'"))
    for key,value in dinfo.items():
        if key == '威胁级别':
            StrSqlObj = StrSqlObj.replace(key,MakeStars(value))
        else:
            StrSqlObj = StrSqlObj.replace(key,value)
    return StrSqlObj
if 0:
    if __name__ == '__main__':
        print '=-----------------------'
        print StrSqlOrg
        print '=========================='
