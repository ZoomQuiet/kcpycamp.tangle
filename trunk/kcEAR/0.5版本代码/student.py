# -*- coding: utf-8 -*-
from pychartdir import *
from django.http import HttpResponse
import MySQLdb
conn = MySQLdb.connect(host = "localhost",user = "root",passwd = "1234",db = "examonline")
cursor = conn.cursor()

cursor.execute("select Mark from judgment where User_ID = 1")

cds=cursor.fetchall()

data0 = [42, 49, 49, 49,89]
labels = ["星期一", "星期二", "星期三", "星期四", "星期五"]

for i in range(0,5):
    data0[i] = cds[i][0]
    
c = XYChart(600, 375)

s = "学生每周成绩曲线图"

c.addTitle(s, "simsun.ttc", 18,0xff)

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

layer.setDataLabelFormat("{value|0}")

def makeImage(request):
   return HttpResponse(c.makeChart2(PNG))
