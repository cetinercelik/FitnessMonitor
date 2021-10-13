"""MedicalEgzersiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from MedicalEgzersiz import views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('',views.homepage,name='home-page'),
                  path('home/dashboard', views.home, name='home-dashboard'),

                  path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
                  path('logout/', auth_views.LogoutView.as_view(template_name='pages/logout.html'), name='logout'),
                  path('personal_register/', auth_views.LoginView.as_view(template_name='pages/personal_register.html'),
                       name='personal_register'),
                  path('registration/', include('registration.urls')),
                  path('fitness/', include('fitness.urls')),
                  path('postural/', include('postural.urls')),
                  path('medical/', include('medical.urls')),
                  path('athletic/', include('athletic.urls')),
                  path('exercise_prescription/', include('exercise_prescription.urls')),
                  path('corrective_exercise/', include('corrective_exercise.urls')),
                  path('medical_exercise/', include('medical_exercise.urls')),
                  path('athletic_development/', include('athletic_development.urls')),
                  path('exercise_tracking/', include('exercise_tracking.urls')),
                  path('finance_module/', include('finance_module.urls')),
                  path('reporting_analysis/', include('reporting_analysis.urls')),
                  path('forms_contents/', include('forms_contents.urls')),
                  path('settings/', include('settings.urls')),
                  path('pilates/', include('pilates.urls')),
                  path('metabolic/', include('metabolic.urls')),

              ] \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
