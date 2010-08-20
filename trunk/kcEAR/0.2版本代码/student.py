# -*- coding: utf-8 -*-
from pychartdir import *
import MySQLdb
conn = MySQLdb.connect(host = "localhost",user = "root",passwd = "1234",db = "mydb")
cursor = conn.cursor()
cursor.execute("select user_id from user")
cds=cursor.fetchall()

data0 = [42, 49, 33, 38, 64]
labels = ["周一", "周二", "周三", "周四", "周五"]
for i in range(len(cds)):
    data0[i] = cds[0][i]
    
c = XYChart(600, 375)

c.addTitle("学生每周成绩曲线图", "simsun.ttc", 18,0xff)

c.setPlotArea(50, 55, 500, 280, c.linearGradientColor(0, 55, 0, 335, 0xf9f9ff,
    0x6666ff), -1, 0xffffff, 0xffffff)

c.addLegend(50, 28, 0, "simsun.ttc", 10).setBackground(Transparent)

c.xAxis().setLabels(labels)

c.yAxis().setTickDensity(30)

c.xAxis().setLabelStyle("simsun.ttc", 12)
c.yAxis().setLabelStyle("simsun.ttc", 12)

c.xAxis().setWidth(2)
c.yAxis().setWidth(2)

c.yAxis().setTitle("KCEAR小组制作", "simsun.ttc", 12)

layer = c.addLineLayer2()

layer.setLineWidth(3)

layer.addDataSet(data0, 0xff0000, "考试成绩").setDataSymbol(CircleSymbol, 9)

c.makeChart("symbolline2.png")
