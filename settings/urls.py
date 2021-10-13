from django.urls import path

from settings import views

urlpatterns = [
    # Kurumsal bilgiler(Kurucu,Felsefe,Kurumsal Çözümlemeler)
    path('home/about', views.about, name='home-about'),
    path('home/founder', views.founder, name='home-founder'),
    path('home/philosophy', views.philosophy, name='home-philosophy'),
    path('home/corpsolve', views.corpsolve, name='home-corpsolve'),
    path('home/contact', views.contact, name='home-contact'),
    path('home/create', views.contactcreate, name='contact-create'),
    path('home/fitnessmonitor<int:id>', views.fitnessMonitor, name='home-fitnessmonitor'),
]
