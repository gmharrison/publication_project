from django.conf.urls import url
from django.conf import settings
from django.conf.urls import patterns

from . import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
]

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)