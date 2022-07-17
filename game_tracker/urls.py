from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('gallery/', include('gallery.urls')),
    path('register/', views.UserFormView.as_view(), name='register'),
    # url(r'^register/', views.UserFormView.as_view(), name='register'),
    # url(r'^login/', views.LoginView, name='login'),
    # url(r'^system/', include('gallery.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )