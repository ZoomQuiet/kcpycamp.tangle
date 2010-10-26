#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Name:         MyDBTest2.py
# Purpose:      just for test bitten
#
# Author:       LongChunhua <longchunhua@gmail.com>
#
#----------------------------------------------------------------------------

from kchhd.conf import storm_conf
from kchhd.model import kchhd_orm

db = storm_conf.getStore() #连接数据库

question = kchhd_orm.Questions()  #实例化一个对象
question.Description = u'问题2'

db.add(question) is db
#db.flush()
db.commit()

print "write ok!"
questionsList = []
def Output():
    retQuestion = db.get(kchhd_orm.Questions, 14)
    i = 15
    while None != retQuestion:
        list = [retQuestion.ID,retQuestion.Description]
        questionsList.append(list)
        
        retQuestion = db.get(kchhd_orm.Questions, i)
        i = i + 1
    else:
        print "While End!"


