from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from gallery.views import Register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/success/',TemplateView.as_view(template_name="registration/success.html"), name ='register-success'),
    path('register/', Register.as_view(), name='register'),
    path('gallery/', include('gallery.urls')),
    path('', include('django.contrib.auth.urls')),
    path('', include('gallery.urls')),
    # url(r'^register/', views.UserFormView.as_view(), name='register'),
    # url(r'^login/', views.LoginView, name='login'),
    # url(r'^system/', include('gallery.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )