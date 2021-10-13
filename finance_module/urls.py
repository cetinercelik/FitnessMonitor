from django.urls import path

from finance_module import views

urlpatterns = [
    # Corporate url start
    path('corporate', views.corporate_finance_module_home,
         name='corporate-finance-module-home'),
    path('trainer', views.trainer_finance_module_home,
         name='trainer-finance-module-home'),
    path('personal', views.personal_finance_module_home,
         name='personal-finance-module-home'),

]
