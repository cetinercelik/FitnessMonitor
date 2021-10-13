from django.urls import path

from metabolic import views

urlpatterns = [
    path('corporate/delete/<int:id>', views.corporate_metabolic_exercise_delete,
         name='corporate-metabolic-exercise-delete'),

    path('trainer/index', views.trainer_metabolic_exercise_home, name='trainer-metabolic-exercise-home'),
    path('trainer/create', views.trainer_metabolic_exercise_create, name='trainer-metabolic-exercise-create'),

    path('trainer/delete/<int:id>', views.trainer_metabolic_exercise_delete,
         name='trainer-metabolic-exercise-delete'),

    path('personal/delete/<int:id>', views.personal_metbolic_exercise_delete,
         name='personal-metabolic-exercise-delete'),
]
