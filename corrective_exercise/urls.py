from django.urls import path
from corrective_exercise import views

urlpatterns = [
    # Corporate url Start
    path('corporate/index', views.cororate_cor_exercise_home,
         name='corporate-corrective_exercise-home'),
    path('corporate/create', views.corporate_cor_exercise_create,
         name='corporate-corrective_exercise-create'),
    path('corporate/delete/<int:id>', views.corporate_corrective_exercise_delete,
         name='corporate-corrective_exercise-delete'),

    # Trainer url start
    path('trainer/index', views.trainer_cor_exercise_home,
         name='trainer-corrective_exercise-home'),
    path('trainer/create', views.trainer_cor_exercise_create,
         name='trainer-corrective_exercise-create'),
    path('trainer/delete/<int:id>', views.trainer_corrective_exercise_delete,
         name='trainer-corrective_exercise-delete'),

    path('personal/delete/<int:id>', views.personal_corrective_exercise_delete,
         name='personal-corrective_exercise-delete'),
]
