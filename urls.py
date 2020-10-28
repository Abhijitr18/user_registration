from django.conf.urls import url

from . import views
from django.urls import path

urlpatterns = [
    path('register/',views.register_view,name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('admin_page/', views.admin_page, name='admin_page'),
    #...
]