#coding=utf-8

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def login(request):
    return render_to_response('login.html')
    
def index(request):
    return render_to_response('top.html')
    
def tableview(request):
    return render_to_response('tableview.html')

def mogfs_view(request):
    return render_to_response('mogfs_view.html')
    
    
def addtracker(request):
    return render_to_response('addtracker.html')
    
def admin_mgr(request):
    return render_to_response('admin_mgr.html')
    
def addmogilefs(request):
    return render_to_response('addmogilefs.html')
    
def admin_mofpsw(request):
    return render_to_response('admin_mofpsw.html')
   
def admin_mofpsw(request):
    return render_to_response('admin_mofpsw.html')

def logout(request):
    return render_to_response('logout.html')    