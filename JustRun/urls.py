from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from dash.views import home_view, run
from logs.views import log_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('run/', run, name='run'),
    path('log/', log_view, name='logs'),
] 
# + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)