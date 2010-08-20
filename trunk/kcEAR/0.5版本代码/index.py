from django.shortcuts import render_to_response
# -*- coding: utf-8 -*-
import MySQLdb

conn = MySQLdb.connect(host = "localhost",user = "root",passwd = "1234",db = "examonline")
cursor = conn.cursor()
cursor.execute("SET character_set_results='utf8';")

cursor.execute("select User_Code, User_Name from user")
cds = cursor.fetchall()
#list = [{'id':'0001', 'name':'kkkkkk'}]
list = []

value = {}

for record in cds:
    value['name'] = record[1]
    value['id'] = record[0]
    list.append(value.copy())

def index(request):
   return render_to_response('kcear.html',{'list': list})
