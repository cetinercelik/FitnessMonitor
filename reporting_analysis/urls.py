from django.urls import path

from reporting_analysis import views, pdfmaker

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

    # Pdf maker fields***********************************
    # Trains form pdf maker
    # Interview form Pdf Maker field
    path('trainer/forms/interview/pdf/<int:id>/', pdfmaker.trainer_interview_forms_pdf_view,
         name='trainer-forms-interview-pdf'),

    # medikal form Pdf Maker field
    path('trainer/forms/medikal/pdf/<int:id>/', pdfmaker.trainer_medikalInpt_forms_pdf_view,
         name='trainer-forms-medikalInpt-pdf'),

    # contract form Pdf Maker field
    path('trainer/forms/contract/pdf/<int:id>/', pdfmaker.trainer_contractInput_forms_pdf_view,
         name='trainer-forms-contractInput-pdf'),

    # voluntary form Pdf Maker field
    path('trainer/forms/voluntary/pdf/<int:id>/', pdfmaker.trainer_voluntaryInput_forms_pdf_view,
         name='trainer-forms-voluntaryInput-pdf'),

    # Interview form Pdf Maker field
    path('trainer/forms/familyInput/pdf/<int:id>/', pdfmaker.trainer_familyInput_forms_pdf_view,
         name='trainer-forms-familyInput-pdf'),

    # exercisehistory form Pdf Maker field
    path('trainer/forms/exercisehistory/pdf/<int:id>/', pdfmaker.trainer_exercisehistoryInput_forms_pdf_view,
         name='trainer-forms-exercisehistoryInput-pdf'),

    # parq form Pdf Maker field
    path('trainer/forms/parq/pdf/<int:id>/', pdfmaker.trainer_parqInput_forms_pdf_view,
         name='trainer-forms-parqInput-pdf'),

    # mood form Pdf Maker field
    path('trainer/forms/mood/pdf/<int:id>/', pdfmaker.trainer_moodInput_forms_pdf_view,
         name='trainer-forms-moodInput-pdf'),

    # sleepquality form Pdf Maker field
    path('trainer/forms/sleepquality/pdf/<int:id>/', pdfmaker.trainer_sleepqualityInput_forms_pdf_view,
         name='trainer-forms-sleepqualityInput-pdf'),

    # nutrition form Pdf Maker field
    path('trainer/forms/nutrition/pdf/<int:id>/', pdfmaker.trainer_nutritionInput_forms_pdf_view,
         name='trainer-forms-nutritionInput-pdf'),

    # eudaimonia form Pdf Maker field
    path('trainer/forms/eudaimonia/pdf/<int:id>/', pdfmaker.trainer_eudaimoniaInput_forms_pdf_view,
         name='trainer-forms-eudaimoniaInput-pdf'),

    # curriculum form Pdf Maker field
    path('trainer/forms/curriculum/pdf/<int:id>/', pdfmaker.trainer_curriculum_forms_pdf_view,
         name='trainer-forms-curriculum-pdf'),



    # Mesurements Pdf Maker field
    # Athletic Measuremnt Pdf make url
    path('trainer/measurements/athletic/pdf/<int:id>/', pdfmaker.trainer_measurements_athletic_pdf_view,
         name='trainer-measurements-athletic-pdf'),

    # Fitness Measurements pdf make url
    path('trainer/measurements/fitness/pdf/<int:id>/', pdfmaker.trainer_measurements_fitness_pdf_view,
         name='trainer-measurements-fitness-pdf'),

    # Medical Measurements pdf make url
    path('trainer/measurements/medical/pdf/<int:id>/', pdfmaker.trainer_measurements_medical_pdf_view,
         name='trainer-measurements-medical-pdf'),

    # Postural Measurements pdf make url
    path('trainer/measurements/postural/pdf/<int:id>/', pdfmaker.trainer_measurements_postural_pdf_view,
         name='trainer-measurements-postural-pdf'),

    # Prescriptions pdf Make field
    # Exercise Prescriptions pdf make url
    path('trainer/prescriptions/exercise/pdf/<int:id>/', pdfmaker.trainer_prescriptions_exercise_pdf_view,
         name='trainer-prescriptions-exercise-pdf'),

    # Exercise Prescriptions pdf make url
    path('trainer/prescriptions/mdical/pdf/<int:id>/', pdfmaker.trainer_prescriptions_medical_pdf_view,
         name='trainer-prescriptions-mdical-pdf'),

    # Exercise Prescriptions pdf make url
    path('trainer/prescriptions/metabolic/pdf/<int:id>/', pdfmaker.trainer_prescriptions_metabolic_pdf_view,
         name='trainer-prescriptions-metabolic-pdf'),

    # personalTraining Prescriptions pdf make url
    path('trainer/prescriptions/personalTraining/pdf/<int:id>/', pdfmaker.trainer_prescriptions_personalTraining_pdf_view,
         name='trainer-prescriptions-personalTraining-pdf'),

    # Corporate form pdf maker
    # Corporate Interview form Pdf Maker field
    path('corporate/forms/interview/pdf/<int:id>/', pdfmaker.corporate_interview_forms_pdf_view,
         name='corporate-forms-interview-pdf'),

    # medikal form Pdf Maker field
    path('corporate/forms/medikal/pdf/<int:id>/', pdfmaker.corporate_medikalInpt_forms_pdf_view,
         name='corporate-forms-medikalInpt-pdf'),

    # contract form Pdf Maker field
    path('corporate/forms/contract/pdf/<int:id>/', pdfmaker.corporate_contractInput_forms_pdf_view,
         name='corporate-forms-contractInput-pdf'),

    # voluntary form Pdf Maker field
    path('corporate/forms/voluntary/pdf/<int:id>/', pdfmaker.corporate_voluntaryInput_forms_pdf_view,
         name='corporate-forms-voluntaryInput-pdf'),

    # Interview form Pdf Maker field
    path('corporate/forms/familyInput/pdf/<int:id>/', pdfmaker.corporate_familyInput_forms_pdf_view,
         name='corporate-forms-familyInput-pdf'),

    # exercisehistory form Pdf Maker field
    path('corporate/forms/exercisehistory/pdf/<int:id>/', pdfmaker.corporate_exercisehistoryInput_forms_pdf_view,
         name='corporate-forms-exercisehistoryInput-pdf'),

    # parq form Pdf Maker field
    path('corporate/forms/parq/pdf/<int:id>/', pdfmaker.corporate_parqInput_forms_pdf_view,
         name='corporate-forms-parqInput-pdf'),

    # mood form Pdf Maker field
    path('corporate/forms/mood/pdf/<int:id>/', pdfmaker.corporate_moodInput_forms_pdf_view,
         name='corporate-forms-moodInput-pdf'),

    # sleepquality form Pdf Maker field
    path('corporate/forms/sleepquality/pdf/<int:id>/', pdfmaker.corporate_sleepqualityInput_forms_pdf_view,
         name='corporate-forms-sleepqualityInput-pdf'),

    # nutrition form Pdf Maker field
    path('corporate/forms/nutrition/pdf/<int:id>/', pdfmaker.corporate_nutritionInput_forms_pdf_view,
         name='corporate-forms-nutritionInput-pdf'),

    # eudaimonia form Pdf Maker field
    path('corporate/forms/eudaimonia/pdf/<int:id>/', pdfmaker.corporate_eudaimoniaInput_forms_pdf_view,
         name='corporate-forms-eudaimoniaInput-pdf'),

    # curriculum form Pdf Maker field
    path('corporate/forms/curriculum/pdf/<int:id>/', pdfmaker.corporate_curriculum_forms_pdf_view,
         name='corporate-forms-curriculum-pdf'),

    # Mesurements Pdf Maker field
    # Athletic Measuremnt Pdf make url
    path('corporate/measurements/athletic/pdf/<int:id>/', pdfmaker.corporate_measurements_athletic_pdf_view,
         name='corporate-measurements-athletic-pdf'),

    # Fitness Measurements pdf make url
    path('corporate/measurements/fitness/pdf/<int:id>/', pdfmaker.corporate_measurements_fitness_pdf_view,
         name='corporate-measurements-fitness-pdf'),

    # Medical Measurements pdf make url
    path('corporate/measurements/medical/pdf/<int:id>/', pdfmaker.corporate_measurements_medical_pdf_view,
         name='corporate-measurements-medical-pdf'),

    # Postural Measurements pdf make url
    path('corporate/measurements/postural/pdf/<int:id>/', pdfmaker.corporate_measurements_postural_pdf_view,
         name='corporate-measurements-postural-pdf'),

    # Prescriptions pdf Make field
    # Exercise Prescriptions pdf make url
    path('corporate/prescriptions/exercise/pdf/<int:id>/', pdfmaker.corporate_prescriptions_exercise_pdf_view,
         name='corporate-prescriptions-exercise-pdf'),

    # Exercise Prescriptions pdf make url
    path('corporate/prescriptions/mdical/pdf/<int:id>/', pdfmaker.corporate_prescriptions_medical_pdf_view,
         name='corporate-prescriptions-mdical-pdf'),

    # Exercise Prescriptions pdf make url
    path('corporate/prescriptions/metabolic/pdf/<int:id>/', pdfmaker.corporate_prescriptions_metabolic_pdf_view,
         name='corporate-prescriptions-metabolic-pdf'),

    # personalTraining Prescriptions pdf make url
    path('corporate/prescriptions/personalTraining/pdf/<int:id>/',pdfmaker.corporate_prescriptions_personalTraining_pdf_view,
         name='corporate-prescriptions-personalTraining-pdf'),

    # Corrective Prescriptions pdf make url
    path('corporate/prescriptions/corrective/pdf/<int:id>/', pdfmaker.corporate_prescriptions_corrective_pdf_view,
         name='corporate-prescriptions-corrective-pdf'),

    # Corporate form pdf maker
    # Corporate Interview form Pdf Maker field
    path('personal/forms/interview/pdf/<int:id>/', pdfmaker.personal_interview_forms_pdf_view,
         name='personal-forms-interview-pdf'),

    # medikal form Pdf Maker field
    path('personal/forms/medikal/pdf/<int:id>/', pdfmaker.personal_medikalInpt_forms_pdf_view,
         name='personal-forms-medikalInpt-pdf'),

    # contract form Pdf Maker field
    path('personal/forms/contract/pdf/<int:id>/', pdfmaker.personal_contractInput_forms_pdf_view,
         name='personal-forms-contractInput-pdf'),

    # voluntary form Pdf Maker field
    path('personal/forms/voluntary/pdf/<int:id>/', pdfmaker.personal_voluntaryInput_forms_pdf_view,
         name='personal-forms-voluntaryInput-pdf'),

    # Interview form Pdf Maker field
    path('personal/forms/familyInput/pdf/<int:id>/', pdfmaker.personal_familyInput_forms_pdf_view,
         name='personal-forms-familyInput-pdf'),

    # exercisehistory form Pdf Maker field
    path('personal/forms/exercisehistory/pdf/<int:id>/', pdfmaker.personal_exercisehistoryInput_forms_pdf_view,
         name='personal-forms-exercisehistoryInput-pdf'),

    # parq form Pdf Maker field
    path('personal/forms/parq/pdf/<int:id>/', pdfmaker.personal_parqInput_forms_pdf_view,
         name='personal-forms-parqInput-pdf'),

    # mood form Pdf Maker field
    path('personal/forms/mood/pdf/<int:id>/', pdfmaker.personal_moodInput_forms_pdf_view,
         name='personal-forms-moodInput-pdf'),

    # sleepquality form Pdf Maker field
    path('personal/forms/sleepquality/pdf/<int:id>/', pdfmaker.personal_sleepqualityInput_forms_pdf_view,
         name='personal-forms-sleepqualityInput-pdf'),

    # nutrition form Pdf Maker field
    path('personal/forms/nutrition/pdf/<int:id>/', pdfmaker.personal_nutritionInput_forms_pdf_view,
         name='personal-forms-nutritionInput-pdf'),

    # eudaimonia form Pdf Maker field
    path('personal/forms/eudaimonia/pdf/<int:id>/', pdfmaker.personal_eudaimoniaInput_forms_pdf_view,
         name='personal-forms-eudaimoniaInput-pdf'),

    # curriculum form Pdf Maker field
    path('personal/forms/curriculum/pdf/<int:id>/', pdfmaker.personal_curriculum_forms_pdf_view,
         name='personal-forms-curriculum-pdf'),

    # Mesurements Pdf Maker field
    # Athletic Measuremnt Pdf make url
    path('personal/measurements/athletic/pdf/<int:id>/', pdfmaker.personal_measurements_athletic_pdf_view,
         name='personal-measurements-athletic-pdf'),

    # Fitness Measurements pdf make url
    path('personal/measurements/fitness/pdf/<int:id>/', pdfmaker.personal_measurements_fitness_pdf_view,
         name='personal-measurements-fitness-pdf'),

    # Medical Measurements pdf make url
    path('personal/measurements/medical/pdf/<int:id>/', pdfmaker.personal_measurements_medical_pdf_view,
         name='personal-measurements-medical-pdf'),

    # Postural Measurements pdf make url
    path('personal/measurements/postural/pdf/<int:id>/', pdfmaker.personal_measurements_postural_pdf_view,
         name='personal-measurements-postural-pdf'),

    # Prescriptions pdf Make field
    # Exercise Prescriptions pdf make url
    path('personal/prescriptions/exercise/pdf/<int:id>/', pdfmaker.personal_prescriptions_exercise_pdf_view,
         name='personal-prescriptions-exercise-pdf'),

    # Exercise Prescriptions pdf make url
    path('personal/prescriptions/mdical/pdf/<int:id>/', pdfmaker.personal_prescriptions_medical_pdf_view,
         name='personal-prescriptions-mdical-pdf'),

    # Exercise Prescriptions pdf make url
    path('personal/prescriptions/metabolic/pdf/<int:id>/', pdfmaker.personal_prescriptions_metabolic_pdf_view,
         name='personal-prescriptions-metabolic-pdf'),

    # personalTraining Prescriptions pdf make url
    path('personal/prescriptions/personalTraining/pdf/<int:id>/',
         pdfmaker.personal_prescriptions_personalTraining_pdf_view,
         name='personal-prescriptions-personalTraining-pdf'),

    # Corrective Prescriptions pdf make url
    path('personal/prescriptions/corrective/pdf/<int:id>/', pdfmaker.personal_prescriptions_corrective_pdf_view,
         name='personal-prescriptions-corrective-pdf'),

]
