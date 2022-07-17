from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/', views.UserFormView.as_view(), name='register'),
    url(r'^login/', views.LoginView, name='login'),
    url(r'^system/', include('gallery.urls')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )