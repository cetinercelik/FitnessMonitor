from django.urls import path

from exercise_tracking import views

urlpatterns = [
    path('corporate/exercise_tracking/index', views.corporate_exercise_tracking_home,
         name='corporate-exercise-tracking-home'),
    # Trainer url start
    path('trainer/exercise_tracking/index', views.trainer_exercise_tracking_home,
         name='trainer-exercise-tracking-home'),
]
