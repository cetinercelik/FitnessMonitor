from django.urls import path
from athletic import views

urlpatterns = [
    path('corporate/index', views.corporate_athletic_home, name='corporate-athletic-home'),
    path('corporate/athletic/delete/<int:id>', views.corporate_athletic_delete, name='corporate-athletic-delete'),

    path('trainer/index', views.trainer_athletic_home, name='trainer-athletic-home'),
    path('trainer/create/index', views.trainer_athletic_create_home, name="trainer-athletic-create-home"),
    path('trainer/create', views.trainer_athletic_create, name='trainer-athletic-create'),
    path('trainer/delete/<int:id>', views.trainer_athletic_delete, name='trainer-athletic-delete'),

    path('personal/delete/<int:id>', views.personal_athletic_delete, name='personal-athletic-delete'),
]
