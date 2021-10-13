from django.urls import path
from pilates import views

urlpatterns = [

    # Aşağıda urlde verilen personal_trainin ve Views ve name de verilen pilates aynı şeydir modul adı değiştiğinden sadece url kısmında değişiklik yapıldı.
    path('corporate/delete/<int:id>', views.corporate_pilates_delete,
         name='corporate-pilates-delete'),

    # Trainer url start
    path('trainer/index', views.trainer_pilates_home,
         name='trainer-pilates-home'),
    path('trainer/create', views.trainer_pilates_create, name='trainer-pilates-create'),

    path('trainer/delete/<int:id>', views.trainer_pilates_delete,
         name='trainer-pilates-delete'),

    path('personal/delete/<int:id>', views.personal_pilates_delete,
         name='personal-pilates-delete'),
]
