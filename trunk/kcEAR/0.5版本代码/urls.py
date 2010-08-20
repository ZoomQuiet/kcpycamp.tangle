from django.conf.urls.defaults import *
import settings
urlpatterns = patterns('',
    # Example:
    # (r'^kcear/', include('kcear.foo.urls')),
     #(r'^kcmap/$', 'kcear.dbdemo1.loadmap'),
     (r'^trainingcamp/$', 'kcear.trainingcamp.makeImage'),
     (r'^student/$', 'kcear.student.makeImage'),
                       
     (r'^$', 'kcear.index.index'),
     (r'^kcmap/$', 'kcear.kcmap.showmap'),
     (r'^kcstu/$', 'kcear.kcstu.showmap'),
     (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH}),
    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
