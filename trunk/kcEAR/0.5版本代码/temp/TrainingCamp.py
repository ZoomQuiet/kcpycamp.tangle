# -*- coding: utf-8 -*-
from pychartdir import *

import MySQLdb

conn = MySQLdb.connect(host = "localhost",user = "root",passwd = "1234",db = "mydb")
cursor = conn.cursor()
cursor.execute("select user_code from user")
cds=cursor.fetchall()
data0 = [100, 125, 245, 147, 67]
data1 = [85, 156, 179, 211, 123]
data2 = [97, 87, 56, 267, 157]
labels = ["星期一", "星期二", "星期三", "星期四", "星期五"]
for i in range(len(cds)):
    data0[i] = cds[i][0]
    print data0[i]

c = XYChart(800, 600)

c.addTitle("学生每周成绩统计图", "simsun.ttc", 18,0xff)

c.setPlotArea(80, 70, 540, 380, c.linearGradientColor(0, 55, 0, 335, 0xf9f9ff,
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
layer.addDataSet(data0, 0xff0000, "作业一")
layer.addDataSet(data1, 0x00ff00, "作业二")
layer.addDataSet(data2, 0xff8800, "作业三")

layer.setAggregateLabelStyle()

layer.setDataLabelStyle()

layer.setBorderColor(Transparent, glassEffect(NormalGlare, Left))

layer.setBarGap(0.2, TouchBar)

c.makeChart("chartdirector.png")
