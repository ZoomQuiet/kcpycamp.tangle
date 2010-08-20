# -*- coding: utf-8 -*-
from pychartdir import *
from django.http import HttpResponse

import MySQLdb

conn = MySQLdb.connect(host = "localhost",user = "root",passwd = "1234",db = "examonline")
cursor = conn.cursor()
cursor.execute("SELECT sum(Mark)  from judgment where  Date(Grading_Time) >= '2008-07-14' and Date(Grading_Time) <= '2008-07-18' Group by Date(Grading_Time)")
cds=cursor.fetchall()

data0 = [100, 125, 245, 147, 67]
labels = ["星期一", "星期二", "星期三", "星期四", "星期五"]
for i in range(len(cds)):
    data0[i] = cds[i][0]

c = XYChart(700, 480)

c.addTitle("训练营每周成绩统计图", "simsun.ttc", 18,0xff)

c.setPlotArea(80, 70, 540, 370, c.linearGradientColor(0, 55, 0, 335, 0xf9f9ff,
    0x6666ff), -1, 0xffffff, 0xffffff)

c.addLegend(70, 28, 0, "simsun.ttc",10).setBackground(Transparent)

c.xAxis().setLabels(labels)

c.xAxis().setTickOffset(0.5)

c.xAxis().setLabelStyle("simsun.ttc", 10)
c.yAxis().setLabelStyle("simsun.ttc", 10)

c.xAxis().setWidth(2)
c.yAxis().setWidth(2)

c.yAxis().setTitle("KcEAR制作","simsun.ttc",18)

layer = c.addBarLayer2(Stack, 8)
layer.addDataSet(data0, 0xff0000, "当天训练营总分")


layer.setAggregateLabelStyle()


layer.setBorderColor(Transparent, glassEffect(NormalGlare, Left))

layer.setBarGap(0.2, TouchBar)
def makeImage(request):
   return HttpResponse(c.makeChart2(PNG))
