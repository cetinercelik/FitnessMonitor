from django.urls import path
from postural import views

# Corporate Urls
urlpatterns = [
    path('corporate/index', views.corporate_postural_home, name='corporate-postural-home'),
    path('corporate/create', views.corporate_postural_create, name='corporate-postural-create'),
    path('corporate/delete/<int:id>', views.corporate_postural_delete, name='corporate-postural-delete'),

    # Trainer Urls
    path('trainer/index', views.trainer_postural_home, name='trainer-postural-home'),
    path('trainer/create', views.trainer_postural_create, name='trainer-postural-create'),
    path('trainer/delete/<int:id>', views.trainer_postural_delete, name='trainer-postural-delete'),

    path('personal/delete/<int:id>', views.personal_postural_delete, name='personal-postural-delete'),
]
