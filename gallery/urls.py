from django.urls import path
from . import views

app_name = 'gallery'
urlpatterns = [
    path('', views.SystemView.as_view(), name='defaultgallery'),
    path('system/<str:system_name>', views.SystemView.as_view(), name='systemgallery'),
    path('<int:game_id>/add/', views.add, name='add')
]
