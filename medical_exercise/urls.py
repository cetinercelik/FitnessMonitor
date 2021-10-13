from django.urls import path

from medical_exercise import views

urlpatterns = [
    path('trainer/index', views.trainer_medical_exercise, name='trainer-medical-exercise-home'),

    path('trainer/create', views.trainer_medical_exercise_create_home,
         name='trainer-medical-exercise-create-home'),

    path('trainer/create1', views.trainer_medical_exercise_create1,
         name='trainer-medical-exercise-create1'),



    path('trainer/delete/<int:id>', views.trainer_medical_exercise1_delete,
         name='trainer-medical-exercise-delete'),

    path('corporate/delete/<int:id>', views.corporate_medical_exercise1_delete,
         name='corporate-medical-exercise-delete'),

    path('personal/delete/<int:id>', views.personal_medical_exercise1_delete,
         name='personal-medical-exercise-delete'),
]
