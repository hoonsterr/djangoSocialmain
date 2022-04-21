
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('join/', views.join, name='join'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),
    path('mypage/', views.mypage, name='mypage'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('trial/', views.trial, name='trial'),
    path('result/', views.result, name='result'),
    path('dbconn/', views.dbconn),
    path('upload/', views.upload, name='upload'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )