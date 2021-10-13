from django.urls import path
from athletic_development import views

urlpatterns = [
    # Corporate url Start
    path('corporate/exercise_prescription/index', views.corporate_athletic_development_home,
         name='corporate-athletic-development-home'),

    path('trainer/exercise_prescription/index', views.trainer_athletic_development_home,
         name='trainer-athletic-development-home'),

]
