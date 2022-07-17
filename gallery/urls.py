from django.conf.urls import url
from . import views

app_name = 'gallery'

urlpatterns = [
    url(r'^(?P<system_name>[\w]+)/$', views.SystemView.as_view(), name='systemgallery'),
]
