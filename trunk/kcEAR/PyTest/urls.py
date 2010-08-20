from django.conf.urls.defaults import *
from PyTest import settings
urlpatterns = patterns('',
    # Example:
    # (r'^PyTest/', include('PyTest.foo.urls')),
    #(r'^$', 'PyTest.helloworld.index'),
    (r'^$', 'PyTest.index.index'),
    (r'^kcmap/$', 'PyTest.kcmap.showmap'),
    (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_PATH}),

    # Uncomment this for admin:
#     (r'^admin/', include('django.contrib.admin.urls')),
)
