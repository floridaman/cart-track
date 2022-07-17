from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'gallery'
urlpatterns = [
    path('', views.SystemView.as_view(), name='defaultgallery'),
    path('collection', login_required(views.CollectionView.as_view()), name='collection'),
    path('system/<str:system_name>', views.SystemView.as_view(), name='systemgallery'),
    path('<int:game_id>/add/', views.add, name='add'),
    path('<int:game_id>/remove/', views.remove, name='remove')
]
