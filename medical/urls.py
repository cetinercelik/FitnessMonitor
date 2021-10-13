from django.urls import path
from django.contrib.auth import views as auth_views
from medical import views

# Corporate Urls
urlpatterns = [
    path('corporate/index', views.corporate_medical_home, name='corporate-medical-home'),
    path('corporate/create', views.corporate_medical_create, name='corporate-medical-create'),
    path('corporate/delete/<int:id>', views.corporate_medical_delete, name='corporate-measurement_medical-delete'),

    # Trainer Urls
    path('trainer/index', views.trainer_medical_home, name='trainer-medical-home'),
    path('trainer/create', views.trainer_medical_create, name='trainer-medical-create'),
    path('trainer/delete/<int:id>', views.trainer_medical_delete, name='trainer-measurement_medical-delete'),
    # Personel Urls
    path('personal/delete/<int:id>', views.personal_medical_delete, name='personal-measurement_medical-delete'),
]
