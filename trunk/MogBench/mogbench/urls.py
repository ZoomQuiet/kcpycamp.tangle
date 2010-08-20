#coding: utf-8	
from django.conf.urls.defaults import *
import settings

urlpatterns = patterns('',
    # Example:
    # (r'^mogbench/', include('mogbench.foo.urls')),
  
    (r'^mogbench//item/$', 'mogbench.login.Checklogin'),
    (r'^mogbench//item/viewlog/$', 'mogbench.admin_manage.ViewLog'),
    (r'^mogbench//item/login/$', 'mogbench.login.Checklogin'),
    (r'^mogbench//item/index/$', 'mogbench.index.index'), # by toontong
    (r'^mogbench//item/mogfs_view/$', 'mogbench.mogfs_view.index'),   # bytoontong
    (r'^mogbench//item/deltracker/$', 'mogbench.delete.delTracker'),   # bytoontong
    (r'^mogbench//item/delmogilefs/', 'mogbench.delete.delMogileFS'),   # bytoontong
    (r'^mogbench//item/dellog/', 'mogbench.delete.delLog'),   # bytoontong
    (r'^mogbench//item/logout/$', 'mogbench.logout.logout'),
    (r'^mogbench//item/admin_mgr/$', 'mogbench.admin_manage.adminManage'),    
    (r'^mogbench//item/addtracker/$', 'mogbench.add_tracker.AddTracker'),
    (r'^mogbench//item/addmogilefs/$', 'mogbench.add_moggroup.AddMogGroup'), 
    (r'^mogbench//item/tableview/$', 'mogbench.url_control.tableview'),
    (r'^mogbench//item/site_media/(?P<path>.*)$', 'django.views.static.serve',\
    {'document_root': settings.STATIC_IMAGE_PATH }),
#*************************************************************************************
    (r'^mogbench//$', 'mogbench.login.Checklogin'),
    (r'^mogbench//viewlog/$', 'mogbench.admin_manage.ViewLog'),
    (r'^mogbench//login/$', 'mogbench.login.Checklogin'),
    (r'^mogbench//index/$', 'mogbench.index.index'), # by toontong
    (r'^mogbench//mogfs_view/$', 'mogbench.mogfs_view.index'),   # bytoontong
    (r'^mogbench//deltracker/$', 'mogbench.delete.delTracker'),   # bytoontong
    (r'^mogbench//delmogilefs/', 'mogbench.delete.delMogileFS'),   # bytoontong
    (r'^mogbench//dellog/', 'mogbench.delete.delLog'),   # bytoontong
    (r'^mogbench//logout/$', 'mogbench.logout.logout'),
    (r'^mogbench//admin_mgr/$', 'mogbench.admin_manage.adminManage'),    
    (r'^mogbench//addtracker/$', 'mogbench.add_tracker.AddTracker'),
    (r'^mogbench//addmogilefs/$', 'mogbench.add_moggroup.AddMogGroup'), 
    (r'^mogbench//tableview/$', 'mogbench.url_control.tableview'),
    (r'^mogbench//site_media/(?P<path>.*)$', 'django.views.static.serve',\
    {'document_root': settings.STATIC_IMAGE_PATH }),
  #*************************************************************************************

    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_IMAGE_PATH }),
    (r'^$', 'mogbench.login.Checklogin'),
    (r'^login/', 'mogbench.login.Checklogin'),
    (r'^viewlog/$', 'mogbench.admin_manage.ViewLog'),
    (r'^index/', 'mogbench.index.index'), # by toontong
    (r'^mogfs_view/', 'mogbench.mogfs_view.index'),   # bytoontong
    (r'^deltracker/', 'mogbench.delete.delTracker'),   # bytoontong
    (r'^delmogilefs/', 'mogbench.delete.delMogileFS'),   # bytoontong
    (r'^dellog/', 'mogbench.delete.delLog'),   # bytoontong
    (r'^logout/', 'mogbench.logout.logout'),
    (r'^admin_mgr/', 'mogbench.admin_manage.adminManage'),    
    (r'^addtracker/', 'mogbench.add_tracker.AddTracker'),
    (r'^addmogilefs/', 'mogbench.add_moggroup.AddMogGroup'), 
    (r'^tableview/', 'mogbench.url_control.tableview'),
    #(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',\
    #{'document_root': settings.STATIC_IMAGE_PATH }),

# Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
