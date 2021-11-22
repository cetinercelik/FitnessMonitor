from django.shortcuts import render, get_object_or_404
from django.contrib import messages
# Create your views here.
# pdf library/
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# /
from athletic.models import AthleticInpt
from corrective_exercise.models import corrective_exercise
from exercise_prescription.models import exercise_prescription
from fitness.models import FitnessInputs

from forms_contents.models import InterviewInput, ContractInput, MedikalInpt, VoluntaryInput, FamilyInput, \
    ExercisehistoryInput, ParqInput, MoodInput, SleepqualityInput, NutritionInput, EudaimoniaInput, CurriculumWalking1
from medical.models import MedicalInputModel1
from medical_exercise.models import medical_exercise1

from metabolic.models import Metabolic
from pilates.models import personalTrainingInput1
from postural.models import PosturInputs
from registration.models import Trainer, Personal
from registration.views import user_checking

corporate_content_template_path = 'modules/corporate_content/analyzes/'
trainer_content_template_path = 'modules/trainer_content/analyzes/'
personal_content_template_path = 'modules/personel_content/analyzes/'

"""Corporate"""


def corporate_reporting_analysis_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    corporate_id = user_control_data['corporate_info'].id
    trainers_data = Trainer.objects.filter(corporate_id=corporate_id)
    trainer_ids = [trainers.id for trainers in trainers_data]
    personal_data = Personal.objects.filter(trainer_id__in=trainer_ids).all()
    template = corporate_content_template_path + 'reporting_analysis/reporting_analysis.html'
    context = {
        'personals': personal_data,
        'trainers': trainers_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def corporate_forms_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    corporate_id = user_control_data['corporate_info'].id
    trainers_data = Trainer.objects.filter(corporate_id=corporate_id)
    trainer_ids = [trainers.id for trainers in trainers_data]
    personal_data = Personal.objects.filter(trainer_id__in=trainer_ids).all()
    template = corporate_content_template_path + 'reporting_analysis/forms/forms.html'
    context = {
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def corporate_forms_analysis_results_home(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    personal_data = Personal.objects.filter(id=id).all()
    it_data = InterviewInput.objects.filter(personal_id=id).all()  # Ön Görüşme Formu
    ct_data = ContractInput.objects.filter(personal_id=id).all()  # Teklif ve Sözleşme Formu
    mc_data = MedikalInpt.objects.filter(personal_id=id).all()  # Medikal izin Formu
    vt_data = VoluntaryInput.objects.filter(personal_id=id).all()  # Gönüllü  Rıza Formu
    fi_data = FamilyInput.objects.filter(personal_id=id).all()  # Aile Öyküsü ve Hastalık Geçmişi
    ex_data = ExercisehistoryInput.objects.filter(personal_id=id).all()  # Egzersiz Geçmişi ve Yönelimi
    pq_data = ParqInput.objects.filter(personal_id=id).all()  # PAR-Q Formu
    md_data = MoodInput.objects.filter(personal_id=id).all()  # Duygu Durumu – Sosyalite – İş Koşulları Formu
    sp_data = SleepqualityInput.objects.filter(personal_id=id).all()  # Uyku Kalitesi – Zindelik – Ağrı Durumu Formu
    nt_data = NutritionInput.objects.filter(personal_id=id).all()  # Beslenme ve Tüketim Alışkanlıkları Formu
    ed_data = EudaimoniaInput.objects.filter(personal_id=id).all()  # Eudaimonia Sağlıklı Yaşam Semptom Formu
    ci_data = CurriculumWalking1.objects.filter(personal_id=id).all()  # İzlence Formu
    template = corporate_content_template_path + 'reporting_analysis/forms/form_results.html'

    context = {
        'personals': personal_data,
        'interviews': it_data,
        'contracts': ct_data,
        'medicals': mc_data,
        'voluntarys': vt_data,
        'familys': fi_data,
        'exercises': ex_data,
        'parqs': pq_data,
        'moods': md_data,
        'sleeps': sp_data,
        'nutritions': nt_data,
        'eudaimonias': ed_data,
        'curriculums': ci_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


"""Start Measurement Field"""


def corporate_measurements_home(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    template = corporate_content_template_path + 'reporting_analysis/measurements/measurements.html'
    context = {
        'id': id,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def corp_meas_fitness_analysis_results(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    personal_data = Personal.objects.filter(id=id).all()
    ft_data = FitnessInputs.objects.filter(personal_id=id).all()
    template = corporate_content_template_path + 'reporting_analysis/measurements/fitness/fitness_analysis_results.html'
    context = {
        'id': id,
        'personals': personal_data,
        'fitness': ft_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def corporate_measurements_athletic_results(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    personal_data = Personal.objects.filter(id=id).all()
    at_data = AthleticInpt.objects.filter(personal_id=id).all()
    template = corporate_content_template_path + 'reporting_analysis/measurements/athletic_performance/athletic_performance_results.html'
    context = {
        'id': id,
        'athletics': at_data,
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def corporate_measurements_postural_results_home(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    personal_data = Personal.objects.filter(id=id).all()
    pst_data = PosturInputs.objects.filter(personal_id=id).all()
    template = corporate_content_template_path + 'reporting_analysis/measurements/postural/postural_results.html'
    context = {
        'id': id,
        'posturals': pst_data,
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def corporate_measurements_medical_results_home(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    personal_data = Personal.objects.filter(id=id).all()
    mdc_data = MedikalInpt.objects.filter(personal_id=id).all()
    template = corporate_content_template_path + 'reporting_analysis/measurements/medical/medical_results.html'
    context = {
        'id': id,
        'medicals': mdc_data,
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


"""/End Measurement Field"""

"""Start precriptions Field"""


def corporate_prescriptions_home(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    template = corporate_content_template_path + 'reporting_analysis/prescriptions/prescriptions.html'
    context = {
        'id': id,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def corporate_prescriptions_athletic_development_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    corporate_id = user_control_data['corporate_info'].id
    trainers_data = Trainer.objects.filter(corporate_id=corporate_id)
    trainer_ids = [trainers.id for trainers in trainers_data]
    personal_data = Personal.objects.filter(trainer_id__in=trainer_ids).all()
    template = corporate_content_template_path + 'reporting_analysis/prescriptions/athletic_development/athletic_development.html'
    context = {
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def corporate_prescriptions_corrective_exercise_results(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    cor_data = corrective_exercise.objects.filter(personal_id=id).all()
    personal_data = Personal.objects.filter(id=id).all()
    template = corporate_content_template_path + 'reporting_analysis/prescriptions/corrective_exercise/corrective_exercise_result.html'
    context = {
        'id': id,
        'correctives': cor_data,
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def corporate_prescriptions_exercise_prescription_results_home(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    ex_data = exercise_prescription.objects.filter(personal_id=id).all()
    personal_data = Personal.objects.filter(id=id).all()
    template = corporate_content_template_path + 'reporting_analysis/prescriptions/exercise_prescription/exercise_prescription_results.html'
    context = {
        'id': id,
        'exercises': ex_data,
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def corpoarate_prescriptions_pilates_prescription_results(request, id):
    user = request.user
    user_control_dt = user_checking(user.id)
    pt_data = personalTrainingInput1.objects.filter(personal_id=id).all()
    personal_data = Personal.objects.filter(id=id).all()
    template = corporate_content_template_path + 'reporting_analysis/prescriptions/pilates_prescription/pilates_prescription_results.html'
    context = {
        'id': id,
        'pilates': pt_data,
        'personals': personal_data,
        'user_control_data': user_control_dt
    }

    return render(request=request, template_name=template, context=context)


def corporate_prescriptions_medical_exercise_results(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    mdcl_data1 = medical_exercise1.objects.filter(personal_id=id).all()
    personal_data = Personal.objects.filter(id=id).all()
    template = corporate_content_template_path + 'reporting_analysis/prescriptions/medical_exercise/medical_exercise.html'
    context = {
        'id': id,
        'medical1': mdcl_data1,
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def corporate_metabolic_exercise_results(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    mtblc_data = Metabolic.objects.filter(personal_id=id).all()
    personal_data = Personal.objects.filter(id=id).all()
    template = corporate_content_template_path + 'reporting_analysis/prescriptions/metabolic_exercise/metabolic_exercise.html'
    context = {
        'id': id,
        'metabolic': mtblc_data,
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


"""/End Prescriptions Field"""

"""/Corporate"""

"""Trainer"""


def trainer_reporting_analysis_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    user_control_data = user_checking(user.id)
    trainer_id = user_control_data['trainer_info'].id
    personal_data = Personal.objects.filter(trainer_id=trainer_id).all()
    template = trainer_content_template_path + 'reporting_analysis/reporting_analysis.html'
    context = {
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


# Kişisel Form sonuçları sayfası
def trainer_form_results_home(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    prs_data = Personal.objects.filter(id=id).all()
    it_data = InterviewInput.objects.filter(personal_id=id).all()  # Ön Görüşme Formu
    ct_data = ContractInput.objects.filter(personal_id=id).all()  # Teklif ve Sözleşme Formu
    mc_data = MedikalInpt.objects.filter(personal_id=id).all()  # Medikal izin Formu
    vt_data = VoluntaryInput.objects.filter(personal_id=id).all()  # Gönüllü  Rıza Formu
    fi_data = FamilyInput.objects.filter(personal_id=id).all()  # Aile Öyküsü ve Hastalık Geçmişi
    ex_data = ExercisehistoryInput.objects.filter(personal_id=id).all()  # Egzersiz Geçmişi ve Yönelimi
    pq_data = ParqInput.objects.filter(personal_id=id).all()  # PAR-Q Formu
    md_data = MoodInput.objects.filter(personal_id=id).all()  # Duygu Durumu – Sosyalite – İş Koşulları Formu
    sp_data = SleepqualityInput.objects.filter(personal_id=id).all()  # Uyku Kalitesi – Zindelik – Ağrı Durumu Formu
    nt_data = NutritionInput.objects.filter(personal_id=id).all()  # Beslenme ve Tüketim Alışkanlıkları Formu
    ed_data = EudaimoniaInput.objects.filter(personal_id=id).all()  # Eudaimonia Sağlıklı Yaşam Semptom Formu
    ci_data = CurriculumWalking1.objects.filter(personal_id=id).all()  # İzlence Formu
    template = trainer_content_template_path + 'reporting_analysis/forms/form_results.html'

    context = {
        'interviews': it_data,
        'contracts': ct_data,
        'medicals': mc_data,
        'voluntaris': vt_data,
        'familys': fi_data,
        'exercises': ex_data,
        'parqs': pq_data,
        'moods': md_data,
        'sleeps': sp_data,
        'nutritions': nt_data,
        'eudaimonias': ed_data,
        'curriculums': ci_data,
        'personals': prs_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


"""Start Measurement Field"""


def trainer_measurements_home(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    personal_data = Personal.objects.filter().all()
    template = trainer_content_template_path + 'reporting_analysis/measurements/measurements.html'
    context = {
        'id': id,
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_measurements_fitness_analysis_results(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    pt_data = Personal.objects.filter(id=id).all()
    fitness_data = FitnessInputs.objects.filter(personal_id=id).all()
    template = trainer_content_template_path + 'reporting_analysis/measurements/fitness/fitness_analysis_results.html'

    context = {
        'id': id,
        'personals': pt_data,
        'fitness': fitness_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)




def trainer_measurements_athletic_analysis_results(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    pt_data = Personal.objects.filter(id=id).all()
    athletic_data = AthleticInpt.objects.filter(personal_id=id).all()
    template = trainer_content_template_path + 'reporting_analysis/measurements/athletic_performance/athletic_performance_results.html'

    context = {
        'id': id,
        'athletics': athletic_data,
        'personals': pt_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


# Postural Bozulma Danışan analiz sonuşları sayfası
def trainer_measurements_postural_analysis_results(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    pt_data = Personal.objects.filter(id=id).all()
    postural_data = PosturInputs.objects.filter(personal_id=id).all()
    template = trainer_content_template_path + 'reporting_analysis/measurements/postural/postural_results.html'

    context = {
        'id': id,
        'personals': pt_data,
        'posturals': postural_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_measurement_medical_analysis_results(request, id):
    user = request.user
    user_control = user_checking(user.id)
    pt_data = Personal.objects.filter(id=id).all()
    medical_data = MedicalInputModel1.objects.filter(personal_id=id).all()
    template = trainer_content_template_path + 'reporting_analysis/measurements/medical/medical_results.html'

    context = {
        'id': id,
        'medicals': medical_data,
        'personals': pt_data,
        'user_control_data': user_control
    }
    return render(request, template_name=template, context=context)


"""/End Measurement Field"""

"""Start precriptions Field"""


def trainer_prescriptions_home(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    template = trainer_content_template_path + 'reporting_analysis/prescriptions/prescriptions.html'
    context = {
        'id': id,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_prescriptions_athletic_development_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    trainers_data = Trainer.objects.filter().all()
    trainer_ids = [trainers.id for trainers in trainers_data]
    personal_data = Personal.objects.filter(trainer_id__in=trainer_ids).all()
    template = trainer_content_template_path + 'reporting_analysis/prescriptions/athletic_development/athletic_development.html'
    context = {
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


# Düzeltici Egzersiz Analiz danışan sonuçları ve listesi
def trainer_prescriptions_corrective_exercise_results(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    pt_data = Personal.objects.filter(id=id).all()
    cor_data = corrective_exercise.objects.filter(personal_id=id).all()
    template = trainer_content_template_path + 'reporting_analysis/prescriptions/corrective_exercise/corrective_exercise_result.html'

    context = {
        'id': id,
        'correctives': cor_data,
        'personals': pt_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_prescriptions_exercise_prescription_results(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    pt_data = Personal.objects.filter(id=id).all()
    ex_data = exercise_prescription.objects.filter(personal_id=id).all()
    template = trainer_content_template_path + 'reporting_analysis/prescriptions/exercise_prescription/exercise_prescription_results.html'
    context = {
        'id': id,
        'exercises': ex_data,
        'personals': pt_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_prescriptions_pilates_prescription_results(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    pl_data = personalTrainingInput1.objects.filter(personal_id=id).all()
    pt_data = Personal.objects.filter(id=id).all()
    template = trainer_content_template_path + 'reporting_analysis/prescriptions/pilates_prescription/pilates_prescription_results.html'
    context = {
        'id': id,
        'pilates': pl_data,
        'personals': pt_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_prescriptions_medical_exercise_results(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    pt_data = Personal.objects.filter(id=id).all()
    mdcl_data1 = medical_exercise1.objects.filter(personal_id=id).all()
    template = trainer_content_template_path + 'reporting_analysis/prescriptions/medical_exercise/medical_exercise.html'
    context = {
        'id': id,
        'personals': pt_data,
        'medical1': mdcl_data1,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_metabolic_exercise_results(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    pt_data = Personal.objects.filter(id=id).all()
    mtblc_data = Metabolic.objects.filter(personal_id=id).all()
    template = trainer_content_template_path + 'reporting_analysis/prescriptions/metabolic_exercise/metabolic_exercise.html'
    context = {
        'id': id,
        'metabolic': mtblc_data,
        'personals': pt_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


"""/End Prescriptions Field"""

"""/Trainer"""

"""Personal"""


def personal_reporting_analysis_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    template = personal_content_template_path + 'reporting_analysis/reporting_analysis.html'
    context = {
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def personal_forms_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    id = user_control_data['personal_info'].id
    fm_data = FamilyInput.objects.filter(personal_id=id).all()
    exhis_data = ExercisehistoryInput.objects.filter(personal_id=id).all()
    md_data = MoodInput.objects.filter(personal_id=id).all()
    sp_data = SleepqualityInput.objects.filter(personal_id=id).all()
    nt_data = NutritionInput.objects.filter(personal_id=id).all()
    ed_data = EudaimoniaInput.objects.filter(personal_id=id).all()
    cr_data = CurriculumWalking1.objects.filter(personal_id=id).all()
    template = personal_content_template_path + 'reporting_analysis/forms/forms.html'
    context = {
        'familys': fm_data,
        'exercises': exhis_data,
        'moods': md_data,
        'sleeps': sp_data,
        'nutritions': nt_data,
        'eudaimonias': ed_data,
        'curriculums': cr_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


"""Start Measurement Field"""


def personal_measurements_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    template = personal_content_template_path + 'reporting_analysis/measurements/measurements.html'
    context = {
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def personal_measurements_fitness_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    id = user_control_data['personal_info'].id
    ft_data = FitnessInputs.objects.filter(personal_id=id).all()
    template = personal_content_template_path + 'reporting_analysis/measurements/fitness/fitness.html'
    context = {
        'fitness': ft_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def personal_measurements_athletic_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    id = user_control_data['personal_info'].id
    at_data = AthleticInpt.objects.filter(personal_id=id).all()
    template = personal_content_template_path + 'reporting_analysis/measurements/athletic_performance/athletic_performance.html'
    context = {
        'athletics': at_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def personal_measurements_postural_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    id = user_control_data['personal_info'].id
    pt_data = PosturInputs.objects.filter(personal_id=id).all()
    template = personal_content_template_path + 'reporting_analysis/measurements/postural/postural.html'
    context = {
        'posturals': pt_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def personal_measurements_medical_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    id = user_control_data['personal_info'].id
    md_data = MedikalInpt.objects.filter(personal_id=id).all()
    template = personal_content_template_path + 'reporting_analysis/measurements/medical/medical.html'
    context = {
        'medicals': md_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


"""/End Measurement Field"""

"""Start precriptions Field"""


def personal_prescriptions_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    template = personal_content_template_path + 'reporting_analysis/prescriptions/prescriptions.html'
    context = {
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def personal_prescriptions_athletic_development_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    template = personal_content_template_path + 'reporting_analysis/prescriptions/athletic_development/athletic_development.html'
    context = {
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def personal_prescriptions_corrective_exercise_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    id = user_control_data['personal_info'].id
    cex_data = corrective_exercise.objects.filter(personal_id=id).all()
    template = personal_content_template_path + 'reporting_analysis/prescriptions/corrective_exercise/corrective_exercise.html'
    context = {
        'correctives': cex_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def personal_prescriptions_exercise_prescription_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    id = user_control_data['personal_info'].id
    exp_data = exercise_prescription.objects.filter(personal_id=id).all()
    template = personal_content_template_path + 'reporting_analysis/prescriptions/exercise_prescription/exercise_prescription.html'
    context = {
        'exercises': exp_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def personal_prescriptions_medical_exercise_results(request):
    user = request.user
    user_control_data = user_checking(user.id)
    id = user_control_data['personal_info'].id
    mdcl_data1 = medical_exercise1.objects.filter(personal_id=id).all()
    template = personal_content_template_path + 'reporting_analysis/prescriptions/medical_exercise/medical_exercise.html'
    context = {
        'medical1': mdcl_data1,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def personal_prescriptions_pilates_prescription_results(request):
    user = request.user
    user_control_data = user_checking(user.id)
    id = user_control_data['personal_info'].id
    pl_data = personalTrainingInput1.objects.filter(personal_id=id).all()
    template = personal_content_template_path + 'reporting_analysis/prescriptions/pilates_prescription/pilates_prescription_results.html'
    context = {
        'pilates': pl_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def personal_metabolic_exercise_results(request):
    user = request.user
    user_control_data = user_checking(user.id)
    id = user_control_data['personal_info'].id
    mtblc_data = Metabolic.objects.filter(personal_id=id).all()
    template = personal_content_template_path + 'reporting_analysis/prescriptions/metabolic_exercise/metabolic_exercise.html'
    context = {
        'metabolic': mtblc_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


"""/End Prescriptions Field"""

"""/Personal"""
