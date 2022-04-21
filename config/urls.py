
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('', user.views.homepage, name='homepage'),
    path('social/', include('allauth.urls')),
    path('social/logout/', user.views.home, name='socialout')

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
