from django.urls import path
from . import views

app_name = 'gallery'
urlpatterns = [
    path('system/<str:system_name>', views.SystemView.as_view(), name='systemgallery')
]
