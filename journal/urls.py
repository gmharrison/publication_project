from django.conf.urls import url
from . import views
from zine import settings

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT})
]