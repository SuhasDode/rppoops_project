from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = 'index'),
    path('register',views.register,name = 'register'),
    path('login',views.login,name = 'login'),
    path('logout',views.logout,name = 'logout'),
    path('services',views.services,name = 'services'),
    path('about',views.about,name = 'about'),
    path('contact',views.contact,name = 'contact'),
]