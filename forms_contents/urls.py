from django.urls import path

from forms_contents import views

urlpatterns = [

    # Trainer url start
    path('trainer/forms', views.trainer_forms_home,
         name='trainer-forms-home'),

    # Ön Görüşme Formu
    path('trainer/forms/interview/create', views.trainer_interview_create, name='trainer-interview-create'),
    path('corporate/interview/delete/<int:id>', views.corporate_interview_delete, name='corporate-interview-delete'),
    path('trainer/interview/delete/<int:id>', views.trainer_interview_delete, name='trainer-interview-delete'),
    path('personal/interview/delete/<int:id>', views.personal_interview_delete, name='personal-interview-delete'),

    #  Teklif ve Sözleşme Formu
    path('trainer/forms/contract/create', views.trainer_contract_create, name='trainer-contract-create'),
    path('corporate/contract/delete/<int:id>', views.corporate_contract_delete, name='corporate-contract-delete'),
    path('trainer/contract/delete/<int:id>', views.trainer_contract_delete, name='trainer-contract-delete'),
    path('personal/contract/delete/<int:id>', views.personal_contract_delete, name='personal-contract-delete'),

    #  Medikal izin Formu
    path('trainer/forms/medicalForm/create', views.trainer_medicalForm_create, name='trainer-medicalform-create'),
    path('corporate/medical/delete/<int:id>', views.corporate_medical_delete, name='corporate-medical-delete'),
    path('trainer/medical/delete/<int:id>', views.trainer_medical_delete, name='trainer-medical-delete'),
    path('personal/medical/delete/<int:id>', views.personal_medical_delete, name='personal-medical-delete'),

    #  Gönüllü  Rıza Formu
    path('trainer/forms/voluntary/create', views.trainer_voluntary_create, name='trainer-voluntary-create'),
    path('corporate/voluntary/delete/<int:id>', views.corporate_voluntary_delete, name='corporate-voluntary-delete'),
    path('trainer/voluntary/delete/<int:id>', views.trainer_voluntary_delete, name='trainer-voluntary-delete'),
    path('personal/voluntary/delete/<int:id>', views.personal_voluntary_delete, name='personal-voluntary-delete'),

    # PAR-Q Formu
    path('trainer/forms/parq/create', views.trainer_parq_create, name='trainer-parq-create'),
    path('corporate/parq/delete/<int:id>', views.corporate_parq_delete, name='corporate-parq-delete'),
    path('trainer/parq/delete/<int:id>', views.trainer_parq_delete, name='trainer-parq-delete'),
    path('personal/parq/delete/<int:id>', views.personal_parq_delete, name='personal-parq-delete'),

    # Danışan Url
    path('personal/forms_contents/index', views.personal_forms_home, name='personal-forms-home'),

    #  Aile Öyküsü ve Hastalık Geçmişi
    path('personal/forms/family/create', views.personal_family_create, name='personal-family-create'),
    path('corporate/family/delete/<int:id>', views.corporate_family_delete, name='corporate-family-delete'),
    path('trainer/family/delete/<int:id>', views.trainer_family_delete, name='trainer-family-delete'),
    path('personal/family/delete/<int:id>', views.personal_family_delete, name='personal-family-delete'),

    #  Egzersiz Geçmişi ve Yönelimi
    path('personal/forms/exercisehistory/create', views.personal_exercisehistory_create,
         name='personal-exercisehistory-create'),
    path('corporate/exercisehistory/delete/<int:id>', views.corporate_exercisehistory_delete,
         name='corporate-exercisehistory-delete'),
    path('trainer/exercisehistory/delete/<int:id>', views.trainer_exercisehistory_delete,
         name='trainer-exercisehistory-delete'),
    path('personal/exercisehistory/delete/<int:id>', views.personal_exercisehistory_delete,
         name='personal-exercisehistory-delete'),

    # Duygu Durumu – Sosyalite – İş Koşulları Formu
    path('personal/forms/mood/create', views.personal_mood_create, name='personal-mood-create'),
    path('corporate/mood/delete/<int:id>', views.corporate_mood_delete, name='corporate-mood-delete'),
    path('trainer/mood/delete/<int:id>', views.trainer_mood_delete, name='trainer-mood-delete'),
    path('personal/mood/delete/<int:id>', views.personal_mood_delete, name='personal-mood-delete'),

    # Uyku Kalitesi – Zindelik – Ağrı Durumu Formu
    path('personal/forms/sleepquality/create', views.personal_sleepquality_create,
         name='personal-sleepquality-create'),
    path('corporate/sleepquality/delete/<int:id>', views.corporate_sleepquality_delete,
         name='corporate-sleepquality-delete'),
    path('trainer/sleepquality/delete/<int:id>', views.trainer_sleepquality_delete, name='trainer-sleepquality-delete'),
    path('personal/sleepquality/delete/<int:id>', views.personal_sleepquality_delete,
         name='personal-sleepquality-delete'),

    # Beslenme ve Tüketim Alışkanlıkları Formu
    path('personal/forms/nutrition/create', views.personal_nutrition_create, name='personal-nutrition-create'),
    path('corporate/nutrition/delete/<int:id>', views.corporate_nutrition_delete, name='corporate-nutrition-delete'),
    path('trainer/nutrition/delete/<int:id>', views.trainer_nutrition_delete, name='trainer-nutrition-delete'),
    path('personal/nutrition/delete/<int:id>', views.personal_nutrition_delete, name='personal-nutrition-delete'),

    # Beslenme ve Tüketim Alışkanlıkları Formu
    path('personal/forms/eudaimonia/create', views.personal_eudaimonia_create, name='personal-eudaimonia-create'),
    path('corporate/eudaimonia/delete/<int:id>', views.corporate_eudaimonia_delete, name='corporate-eudaimonia-delete'),
    path('trainer/eudaimonia/delete/<int:id>', views.trainer_eudaimonia_delete, name='trainer-eudaimonia-delete'),
    path('personal/eudaimonia/delete/<int:id>', views.personal_eudaimonia_delete, name='personal-eudaimonia-delete'),

    # İzlence Formu
    # personal notifications url
    path('personal/notification/index', views.personal_notification_home, name='personal-notifications-home'),
    path('personal/notification/walkin/create', views.personal_curriculum_walking_create,
         name='personal-curriculum-walking-create'),
   
    path('corporate/curriculum/delete/<int:id>', views.corporate_curriculum_delete, name='corporate-curriculum-delete'),
    path('trainer/curriculum/delete/<int:id>', views.trainer_curriculum_delete, name='trainer-curriculum-delete'),
    path('personal/curriculum/delete/<int:id>', views.personal_curriculum_delete, name='personal-curriculum-delete'),
]
