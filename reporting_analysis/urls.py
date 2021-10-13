from django.urls import path

from reporting_analysis import views

urlpatterns = [

    # Trainer url start
    path('trainer/index', views.trainer_reporting_analysis_home,
         name='trainer-reporting-analysis-home'),

    # Kişisel Form sonuçları sayfası
    path('trainer/forms/results/<int:id>', views.trainer_form_results_home,
         name='trainer-forms-analysis-results-home'),

    # Start Measurements Urls
    path('trainer/measurements/<int:id>', views.trainer_measurements_home,
         name='trainer-measurements-analysis-home'),

    path('trainer/measurements/fitness/results/<int:id>', views.trainer_measurements_fitness_analysis_results,
         name='trainer-measurements-fitness-results-home'),

    path('trainer/measurements/athletic/results/<int:id>', views.trainer_measurements_athletic_analysis_results,
         name='trainer-measurements-athletic-result-home'),

    # Postural Bozulma Danışan analiz sonuşları sayfası
    path('trainer/measurements/postural/ruslts/<int:id>', views.trainer_measurements_postural_analysis_results,
         name='trainer-measurements-postural-results-home'),

    path('trainer/measurements/medical/results/<int:id>', views.trainer_measurement_medical_analysis_results,
         name='trainer-measurements-medical-results-home'),
    # Finish Measurements Urls

    # Start Prescriptions Urls
    path('trainer/prescriptions/<int:id>', views.trainer_prescriptions_home,
         name='trainer-prescriptions-analysis-home'),

    path('trainer/prescriptions/athletic_development', views.trainer_prescriptions_athletic_development_home,
         name='trainer-prescriptions-athletic-development-home'),

    # Düzeltici Egzersiz Analiz Danışan Listesi ve sonuçları
    path('trainer/prescriptions/corrective_exercise/results/<int:id>',
         views.trainer_prescriptions_corrective_exercise_results,
         name='trainer-prescriptions-corrective-exercise-results'),

    # Egzersiz Reçetesi Analiz Danışan Sonuç Listesi
    path('trainer/prescriptions/exercise_prescription/results/<int:id>',
         views.trainer_prescriptions_exercise_prescription_results,
         name='trainer-prescriptions-exercise-prescription-results'),

    path('trainer/prescriptions/personal_training/results/<int:id>',
         views.trainer_prescriptions_pilates_prescription_results,
         name='trainer-prescriptions-pilates-prescription-results'),

    path('trainer/prescriptions/medical_exercise/results/<int:id>',
         views.trainer_prescriptions_medical_exercise_results,
         name='trainer-prescriptions-medical-exercise-results'),

    path('trainer/prescriptions/metabolic_exercise/results/<int:id>',
         views.trainer_metabolic_exercise_results,
         name='trainer-metabolic-exercise-results'),
    # /End Prescriptions Urls
    # /End Trainer

    # Corporate url start
    path('corporate', views.corporate_reporting_analysis_home,
         name='corporate-reporting-analysis-home'),

    # Kurumsal Form Analiz Danışman Sonuçları
    path('corporate/forms/results/<int:id>', views.corporate_forms_analysis_results_home,
         name='corporate-forms-analysis-results-home'),

    # Start Measurements Urls
    path('corporate/measurements/index<int:id>', views.corporate_measurements_home,
         name='corporate-measurements-analysis-home'),

    # Fitness Ölçüm Danışan Analiz Sonuçları
    path('corporate/measurements/fitness/results/<int:id>', views.corp_meas_fitness_analysis_results,
         name='corporate-measurements-fitness-results-home'),

    # Atletic Performans Ölçüm Analiz Danışan Listesi
    path('corporate/measurements/athletic/results/<int:id>', views.corporate_measurements_athletic_results,
         name='corporate-measurements-athletic-results-home'),

    # Postural Ölçüm Analiz Danışan Sonuçları
    path('corporate/measurements/postural/results/<int:id>', views.corporate_measurements_postural_results_home,
         name='corporate-measurements-postural-results-home'),

    # Medical Ölçüm Analiz Danışan Sonuçları
    path('corporate/measurements/medical/results/<int:id>', views.corporate_measurements_medical_results_home,
         name='corporate-measurements-medical-results-home'),
    # Finish Measurements Urls

    # Start Prescriptions Urls
    path('corporate/prescriptions/index/<int:id>', views.corporate_prescriptions_home,
         name='corporate-prescriptions-analysis-home'),

    path('corporate/prescriptions/athletic_development', views.corporate_prescriptions_athletic_development_home,
         name='corporate-prescriptions-athletic-development-home'),

    # Düzeltici Egzersiz Danışan Sonuçları
    path('corporate/prescriptions/corrective_exercise/results/<int:id>',
         views.corporate_prescriptions_corrective_exercise_results,
         name='corporate-prescriptions-corrective-exercise-results-home'),

    # Egzersiz Reçetesi Danışan Spnuçları
    path('corporate/prescriptions/exercise_prescription/results/<int:id>',
         views.corporate_prescriptions_exercise_prescription_results_home,
         name='corporate-exercise-prescription-results-home'),

    path('corpoarate/prescriptions/personal_training/results/<int:id>',
         views.corpoarate_prescriptions_pilates_prescription_results,
         name='corporate-prescriptions-pilates-prescription-results'),

    path('corporate/prescriptions/medical_exercise/results/<int:id>',
         views.corporate_prescriptions_medical_exercise_results,
         name='corporate-prescriptions-medical-exercise-results'),

    path('corporate/prescriptions/metabolic_exercise/results/<int:id>',
         views.corporate_metabolic_exercise_results,
         name='corporate-metabolic-exercise-results'),
    # /End Prescriptions Urls
    # /End Corporate

    # Personal url start
    path('personal', views.personal_reporting_analysis_home,
         name='personal-reporting-analysis-home'),

    path('personal/forms_contents', views.personal_forms_home,
         name='personal-forms-analysis-home'),

    # Start Measurements Urls
    path('personal/measurements', views.personal_measurements_home,
         name='personal-measurements-analysis-home'),

    path('personal/measurements/fitness', views.personal_measurements_fitness_home,
         name='personal-measurements-fitness-home'),

    path('personal/measurements/athletic', views.personal_measurements_athletic_home,
         name='personal-measurements-athletic-home'),

    path('personal/measurements/postural', views.personal_measurements_postural_home,
         name='personal-measurements-postural-home'),

    path('personal/measurements/medical', views.personal_measurements_medical_home,
         name='personal-measurements-medical-home'),
    # Finish Measurements Urls

    # Start Prescriptions Urls
    path('personal/prescriptions', views.personal_prescriptions_home,
         name='personal-prescriptions-analysis-home'),

    path('personal/prescriptions/athletic_development', views.personal_prescriptions_athletic_development_home,
         name='personal-prescriptions-athletic-development-home'),

    path('personal/prescriptions/corrective_exercise', views.personal_prescriptions_corrective_exercise_home,
         name='personal-prescriptions-corrective-exercise-home'),

    path('personal/prescriptions/exercise_prescription', views.personal_prescriptions_exercise_prescription_home,
         name='personal-prescriptions-exercise-prescription-home'),

    path('personal/prescriptions/medical_exercise', views.personal_prescriptions_medical_exercise_results,
         name='personal-prescriptions-medical-exercise-home'),

    path('personal/prescriptions/personal_training/results',
         views.personal_prescriptions_pilates_prescription_results,
         name='personal-prescriptions-pilates-prescription-results'),

    path('personal/prescriptions/metabolic_exercise/results',
         views.personal_metabolic_exercise_results,
         name='personal-metabolic-exercise-results'),
    # /End Prescriptions Urls
    # /End Corporate
]
