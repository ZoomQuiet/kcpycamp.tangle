from django.conf.urls.defaults import *
import settings

urlpatterns = patterns('',
    # Example:
    # (r'^web_project/', include('web_project.foo.urls')),

    (r'^$', 'web_project.Url_control.login'),
    (r'^login/', 'web_project.Url_control.login'),
    (r'^Check_Login/', 'web_project.Login.Checklogin'),
    (r'^index/', 'web_project.FrontPage.index'),
    (r'^admin_mofpsw/', 'web_project.Url_control.admin_mofpsw'),
    (r'^Check_admin_mofpsw/', 'web_project.MdfAdminPsw.modify'),
    (r'^logout/', 'web_project.Logout.logout'),



    (r'^admin_mgr/', 'web_project.Url_control.admin_mgr'),    
    (r'^Check_admin_mgr/', 'web_project.AdminManage.adminManage'),


    (r'^tableview/', 'web_project.url_control.tableview'),
    (r'^mogfs_view/', 'web_project.url_control.mogfs_view'),
    (r'^addmogilefs/', 'web_project.url_control.addmogilefs'),
    (r'^addtracker/', 'web_project.url_control.addtracker'),

    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_IMAGE_PATH }),

# Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
