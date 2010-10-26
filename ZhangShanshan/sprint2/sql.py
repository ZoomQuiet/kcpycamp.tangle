# -*- coding: cp936 -*-
import time
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
