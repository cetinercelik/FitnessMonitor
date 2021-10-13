from django.urls import path
from fitness import views

urlpatterns = [
    # Corporate url Start
    path('corporate/index', views.corporate_fitness_home, name='corporate-fitness-home'),
    path('corporate/create', views.corporate_fitness_create, name='corporate-fitness-create'),
    path('corporate/delete/<int:id>', views.corporate_fitness_delete, name='corporate-fitness-delete'),

    # Trainer url start
    path('trainer/index', views.trainer_fitness_home, name='trainer-fitness-home'),
    path('trainer/create', views.trainer_fitness_create, name='trainer-fitness-create'),
    path('trainer/delete/<int:id>', views.trainer_fitness_delete, name='trainer-fitness-delete'),

    path('personal/delete/<int:id>', views.personal_fitness_delete, name='personal-fitness-delete'),

]
