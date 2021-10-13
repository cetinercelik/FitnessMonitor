from django.urls import path
from exercise_prescription import views

urlpatterns = [
    # Corporate url Start
    path('corporate/index', views.corporate_exercise_prescription_home,
         name='corporate-exercise_prescription-home'),
    path('corporate/create', views.corporate_exercise_prescription_create,
         name='corporate-exercise_prescription-create'),
    path('corporate/delete/<int:id>', views.corporate_exercise_prescription_delete,
         name='corporate-exercise_prescription-delete'),
    # Trainer url start
    path('trainer/index', views.trainer_exercise_prescription_home,
         name='trainer-exercise_prescription-home'),
    path('trainer/create', views.trainer_exercise_prescription_create,
         name='trainer-exercise_prescription-create'),
    path('trainer/delete/<int:id>', views.trainer_exercise_prescription_delete,
         name='trainer-exercise_prescription-delete'),
    # Pesonal Urls
    path('personal/delete/<int:id>', views.personal_exercise_prescription_delete,
         name='personal-exercise_prescription-delete'),
]
