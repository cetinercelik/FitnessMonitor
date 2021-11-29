from django.urls import path
from athletic_development import views

urlpatterns = [
    # Corporate url Start
    path('corporate/athletic_development/index', views.corporate_athletic_development_home,
         name='corporate-athletic-development-home'),

    path('trainer/athletic_development/index', views.trainer_athletic_development_home,
         name='trainer-athletic-development-home'),

    path('trainer/athletic_development/create', views.trainer_athletic_development_create,
         name='trainer-athletic-development-create'),

    path('trainer/athletic_development/home/create', views.trainer_athltc_dvlpmnt_create_home,
         name='trainer-athletic-development-home-create'),

]
