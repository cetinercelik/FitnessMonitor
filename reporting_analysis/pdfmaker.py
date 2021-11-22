# Create your views here.
# pdf library/
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from xhtml2pdf import pisa

# /
from athletic.models import AthleticInpt
from corrective_exercise.models import corrective_exercise
from exercise_prescription.models import exercise_prescription
from fitness.models import FitnessInputs
from forms_contents.models import InterviewInput, ContractInput, MedikalInpt, VoluntaryInput, FamilyInput, \
    ExercisehistoryInput, ParqInput, MoodInput, NutritionInput, EudaimoniaInput, CurriculumWalking1, \
    CurriculumMorning, CurriculumNoon, CurriculumEvening, CurriculumSnack, SleepqualityInput
from medical.models import MedicalInputModel1
from medical_exercise.models import medical_exercise1
from metabolic.models import Metabolic
from pilates.models import personalTrainingInput3, personalTrainingInput1
from postural.models import PosturInputs

corporate_content_template_path = 'modules/corporate_content/analyzes/'
trainer_content_template_path = 'modules/trainer_content/analyzes/'
personal_content_template_path = 'modules/personel_content/analyzes/'


# Form field
# Trainer InterviewInput Form Pdf Makers
def trainer_interview_forms_pdf_view(request, id):
    # interview = InterviewInput.objects.filter(id=id).all()
    interview = get_object_or_404(InterviewInput, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/forms/interview_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = interview.personal.user.first_name + '_' + interview.personal.user.last_name + '_öngörüşme_formu_' + str(
        interview.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'interviews': interview,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Trainer InterviewInput Form Pdf Makers
def trainer_medikalInpt_forms_pdf_view(request, id):
    # interview = InterviewInput.objects.filter(id=id).all()
    medikal = get_object_or_404(MedikalInpt, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/forms/medical_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = medikal.personal.user.first_name + '_' + medikal.personal.user.last_name + '_medikal_izin_' + str(
        medikal.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'medikal': medikal,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Trainer ContractInput Form Pdf Makers
def trainer_contractInput_forms_pdf_view(request, id):
    # contract = ContractInput.objects.filter(id=id).all()
    contract = get_object_or_404(ContractInput, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/forms/contractInput_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = contract.personal.user.first_name + '_' + contract.personal.user.last_name + '_teklif_sözleşme' + str(
        contract.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'contracts': contract,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Trainer VoluntaryInput Form Pdf Makers
def trainer_voluntaryInput_forms_pdf_view(request, id):
    # voluntaryInput = VoluntaryInput.objects.filter(id=id).all()
    voluntaryInput = get_object_or_404(VoluntaryInput, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/forms/voluntaryInput_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = voluntaryInput.personal.user.first_name + '_' + voluntaryInput.personal.user.last_name + '_gönüllü_formu_' + str(
        voluntaryInput.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'voluntarys': voluntaryInput,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Trainer VoluntaryInput Form Pdf Makers
def trainer_familyInput_forms_pdf_view(request, id):
    # familyInput = FamilyInput.objects.filter(id=id).all()
    familyInput = get_object_or_404(FamilyInput, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/forms/familyInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = familyInput.personal.user.first_name + '_' + familyInput.personal.user.last_name + '_aile_öyküsü_' + str(
        familyInput.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'familys': familyInput,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Trainer ExercisehistoryInput Form Pdf Makers
def trainer_exercisehistoryInput_forms_pdf_view(request, id):
    # exercise = ExercisehistoryInput.objects.filter(id=id).all()
    exercise = get_object_or_404(ExercisehistoryInput, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/forms/exercisehistoryInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = exercise.personal.user.first_name + '_' + exercise.personal.user.last_name + '_egzersiz_geçmişi_' + str(
        exercise.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'exercises': exercise,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Trainer ParqInput Form Pdf Makers
def trainer_parqInput_forms_pdf_view(request, id):
    # parq = ParqInput.objects.filter(id=id).all()
    parq = get_object_or_404(ParqInput, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/forms/parqInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = parq.personal.user.first_name + '_' + parq.personal.user.last_name + '_parq_' + str(parq.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'parqs': parq,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Trainer ExercisehistoryInput Form Pdf Makers
def trainer_moodInput_forms_pdf_view(request, id):
    # moodInput = MoodInput.objects.filter(id=id).all()
    moodInput = get_object_or_404(MoodInput, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/forms/moodInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = moodInput.personal.user.first_name + '_' + moodInput.personal.user.last_name + '_duygu_durumu_' + str(
        moodInput.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'moodInputs': moodInput,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Trainer SleepqualityInput Form Pdf Makers
def trainer_sleepqualityInput_forms_pdf_view(request, id):
    # sleep = MoodInput.objects.filter(id=id).all()
    sleep = get_object_or_404(SleepqualityInput, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/forms/sleepqualityInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = sleep.personal.user.first_name + '_' + sleep.personal.user.last_name + '_uyku_kalitesi_' + str(sleep.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'sleeps': sleep,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Trainer NutritionInput Form Pdf Makers
def trainer_nutritionInput_forms_pdf_view(request, id):
    # nutrition = NutritionInput.objects.filter(id=id).all()
    nutrition = get_object_or_404(NutritionInput, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/forms/nutritionInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = nutrition.personal.user.first_name + '_' + nutrition.personal.user.last_name + '_beslenme_' + str(
        nutrition.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'nutritions': nutrition,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Trainer EudaimoniaInput Form Pdf Makers
def trainer_eudaimoniaInput_forms_pdf_view(request, id):
    # eudaimonia = EudaimoniaInput.objects.filter(id=id).all()
    eudaimonia = get_object_or_404(EudaimoniaInput, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/forms/eudaimoniaInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = eudaimonia.personal.user.first_name + '_' + eudaimonia.personal.user.last_name + '_eudaimonia_' + str(
        eudaimonia.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'eudaimonias': eudaimonia,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Trainer Curriculum Form Pdf Makers
def trainer_curriculum_forms_pdf_view(request, id):
    # curriculummorning = CurriculumMorning.objects.filter(id=id).all()
    # curriculumnoon = CurriculumNoon.objects.filter(id=id).all()
    # curriculumevening = CurriculumEvening.objects.filter(id=id).all()
    # curriculummsnack = CurriculumSnack.objects.filter(id=id).all()
    # # curriculumwalk = CurriculumWalking1.objects.filter(id=id).all()
    curriculummorning = get_object_or_404(CurriculumMorning, id=id)
    curriculumnoon = get_object_or_404(CurriculumNoon, id=id)
    curriculumevening = get_object_or_404(CurriculumEvening, id=id)
    curriculummsnack = get_object_or_404(CurriculumSnack, id=id)
    curriculumwalk = get_object_or_404(CurriculumWalking1, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/forms/curriculum_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = curriculumwalk.personal.user.first_name + '_' + curriculumwalk.personal.user.last_name + '_izlence_' + str(
        curriculumwalk.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'curriculummornings': curriculummorning,
        'curriculumnoons': curriculumnoon,
        'curriculumevenings': curriculumevening,
        'curriculummsnacks': curriculummsnack,
        'curriculumwalks': curriculumwalk,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Trainer Measurements Athletic Pdf Makers
def trainer_measurements_athletic_pdf_view(request, id):
    athletic = get_object_or_404(AthleticInpt, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/measurements/measurements_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = athletic.personal.user.first_name + '_' + athletic.personal.user.last_name + '_atletik_' + str(
        athletic.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'athletics': athletic,
        'fnames': fname,
    }
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Trainer Fittness Model Pdf Makers
def trainer_measurements_fitness_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    fitness = get_object_or_404(FitnessInputs, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/measurements/measurements_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = fitness.personal.user.first_name + '_' + fitness.personal.user.last_name + '_fitness_' + str(
        fitness.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'fitness': fitness,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Trainer Medical Model Pdf Makers
def trainer_measurements_medical_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    medicalmes = get_object_or_404(MedicalInputModel1, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/measurements/measurements_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = medicalmes.personal.user.first_name + '_' + medicalmes.personal.user.last_name + '_medikal_ölçüm_' + str(
        medicalmes.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'mdcls': medicalmes,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Trainer Medical Model Pdf Makers
def trainer_measurements_postural_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    postural = get_object_or_404(PosturInputs, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/measurements/measurements_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = postural.personal.user.first_name + '_' + postural.personal.user.last_name + '_postural_ölçüm_' + str(
        postural.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'posturals': postural,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Trainer Prescriptions
# Trainer Prescriptions Athletic development Model Pdf Makers
def trainer_prescriptions_athletic_development_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    postural = get_object_or_404(PosturInputs, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/measurements/prescriptions_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = postural.personal.user.first_name + '_' + postural.personal.user.last_name + '_postural_ölçüm_' + str(
        postural.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'posturals': postural,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Trainer Prescriptions Athletic development Model Pdf Makers
def trainer_prescriptions_corrective_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    corr = get_object_or_404(corrective_exercise, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/prescriptions/prescriptions_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = corr.personal.user.first_name + '_' + corr.personal.user.last_name + '_düzeltici_egzersiz_' + str(
        corr.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'corrctives': corr,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Trainer Prescriptions Athletic development Model Pdf Makers
def trainer_prescriptions_exercise_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    exercise = get_object_or_404(exercise_prescription, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/prescriptions/prescriptions_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = exercise.personal.user.first_name + '_' + exercise.personal.user.last_name + '_egzersiz_reçetesi_' + str(
        exercise.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'exercises': exercise,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Trainer Medical Prescription Model Pdf Makers
def trainer_prescriptions_medical_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    medical = get_object_or_404(medical_exercise1, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/prescriptions/prescriptions_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = medical.personal.user.first_name + '_' + medical.personal.user.last_name + '_medikal_reçetesi_' + str(
        medical.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'medicals': medical,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Trainer Metabolic Athletic development Model Pdf Makers
def trainer_prescriptions_metabolic_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    metabolic = get_object_or_404(Metabolic, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/prescriptions/prescriptions_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = metabolic.personal.user.first_name + '_' + metabolic.personal.user.last_name + '_metabolik_reçetesi_' + str(
        metabolic.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'metabolics': metabolic,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Trainer Metabolic Athletic development Model Pdf Makers
def trainer_prescriptions_personalTraining_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    ptrain = get_object_or_404(personalTrainingInput1, id=id)
    template_path = trainer_content_template_path + 'reporting_analysis/prescriptions/prescriptions_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = ptrain.personal.user.first_name + '_' + ptrain.personal.user.last_name + '_metabolik_reçetesi_' + str(
        ptrain.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'ptrains': ptrain,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Corporate pdf Maker Filed
# Corporate Form Make pdf Field
# Corporate Interview Form pdf field
def corporate_interview_forms_pdf_view(request, id):
    # interview = InterviewInput.objects.filter(id=id).all()
    interview = get_object_or_404(InterviewInput, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/forms/interview_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = interview.personal.user.first_name + '_' + interview.personal.user.last_name + '_öngörüşme_formu_' + str(
        interview.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'interviews': interview,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Corporate InterviewInput Form Pdf Makers
def corporate_medikalInpt_forms_pdf_view(request, id):
    # interview = InterviewInput.objects.filter(id=id).all()
    medikal = get_object_or_404(MedikalInpt, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/forms/medical_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = medikal.personal.user.first_name + '_' + medikal.personal.user.last_name + '_medikal_izin_' + str(
        medikal.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'medikal': medikal,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Corporate ContractInput Form Pdf Makers
def corporate_contractInput_forms_pdf_view(request, id):
    # contract = ContractInput.objects.filter(id=id).all()
    contract = get_object_or_404(ContractInput, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/forms/contractInput_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = contract.personal.user.first_name + '_' + contract.personal.user.last_name + '_teklif_sözleşme' + str(
        contract.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'contracts': contract,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Corporate VoluntaryInput Form Pdf Makers
def corporate_voluntaryInput_forms_pdf_view(request, id):
    # voluntaryInput = VoluntaryInput.objects.filter(id=id).all()
    voluntaryInput = get_object_or_404(VoluntaryInput, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/forms/voluntaryInput_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = voluntaryInput.personal.user.first_name + '_' + voluntaryInput.personal.user.last_name + '_gönüllü_formu_' + str(
        voluntaryInput.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'voluntarys': voluntaryInput,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Corporate VoluntaryInput Form Pdf Makers
def corporate_familyInput_forms_pdf_view(request, id):
    # familyInput = FamilyInput.objects.filter(id=id).all()
    familyInput = get_object_or_404(FamilyInput, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/forms/familyInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = familyInput.personal.user.first_name + '_' + familyInput.personal.user.last_name + '_aile_öyküsü_' + str(
        familyInput.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'familys': familyInput,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Corporate ExercisehistoryInput Form Pdf Makers
def corporate_exercisehistoryInput_forms_pdf_view(request, id):
    # exercise = ExercisehistoryInput.objects.filter(id=id).all()
    exercise = get_object_or_404(ExercisehistoryInput, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/forms/exercisehistoryInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = exercise.personal.user.first_name + '_' + exercise.personal.user.last_name + '_egzersiz_geçmişi_' + str(
        exercise.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'exercises': exercise,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response



# Corporate ParqInput Form Pdf Makers
def corporate_parqInput_forms_pdf_view(request, id):
    # parq = ParqInput.objects.filter(id=id).all()
    parq = get_object_or_404(ParqInput, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/forms/parqInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = parq.personal.user.first_name + '_' + parq.personal.user.last_name + '_parq_' + str(parq.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'parqs': parq,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Corporate ExercisehistoryInput Form Pdf Makers
def corporate_moodInput_forms_pdf_view(request, id):
    # moodInput = MoodInput.objects.filter(id=id).all()
    moodInput = get_object_or_404(MoodInput, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/forms/moodInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = moodInput.personal.user.first_name + '_' + moodInput.personal.user.last_name + '_duygu_durumu_' + str(
        moodInput.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'moodInputs': moodInput,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Corporate SleepqualityInput Form Pdf Makers
def corporate_sleepqualityInput_forms_pdf_view(request, id):
    # sleep = MoodInput.objects.filter(id=id).all()
    sleep = get_object_or_404(SleepqualityInput, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/forms/sleepqualityInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = sleep.personal.user.first_name + '_' + sleep.personal.user.last_name + '_uyku_kalitesi_' + str(sleep.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'sleeps': sleep,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response



# Corporate NutritionInput Form Pdf Makers
def corporate_nutritionInput_forms_pdf_view(request, id):
    # nutrition = NutritionInput.objects.filter(id=id).all()
    nutrition = get_object_or_404(NutritionInput, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/forms/nutritionInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = nutrition.personal.user.first_name + '_' + nutrition.personal.user.last_name + '_beslenme_' + str(
        nutrition.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'nutritions': nutrition,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Corporate EudaimoniaInput Form Pdf Makers
def corporate_eudaimoniaInput_forms_pdf_view(request, id):
    # eudaimonia = EudaimoniaInput.objects.filter(id=id).all()
    eudaimonia = get_object_or_404(EudaimoniaInput, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/forms/eudaimoniaInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = eudaimonia.personal.user.first_name + '_' + eudaimonia.personal.user.last_name + '_eudaimonia_' + str(
        eudaimonia.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'eudaimonias': eudaimonia,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response



# Corporate Curriculum Form Pdf Makers
def corporate_curriculum_forms_pdf_view(request, id):
    # curriculummorning = CurriculumMorning.objects.filter(id=id).all()
    # curriculumnoon = CurriculumNoon.objects.filter(id=id).all()
    # curriculumevening = CurriculumEvening.objects.filter(id=id).all()
    # curriculummsnack = CurriculumSnack.objects.filter(id=id).all()
    # # curriculumwalk = CurriculumWalking1.objects.filter(id=id).all()
    curriculummorning = get_object_or_404(CurriculumMorning, id=id)
    curriculumnoon = get_object_or_404(CurriculumNoon, id=id)
    curriculumevening = get_object_or_404(CurriculumEvening, id=id)
    curriculummsnack = get_object_or_404(CurriculumSnack, id=id)
    curriculumwalk = get_object_or_404(CurriculumWalking1, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/forms/curriculum_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = curriculumwalk.personal.user.first_name + '_' + curriculumwalk.personal.user.last_name + '_izlence_' + str(
        curriculumwalk.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'curriculummornings': curriculummorning,
        'curriculumnoons': curriculumnoon,
        'curriculumevenings': curriculumevening,
        'curriculummsnacks': curriculummsnack,
        'curriculumwalks': curriculumwalk,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# Corporate Measurements Athletic Pdf Makers
def corporate_measurements_athletic_pdf_view(request, id):
    athletic = get_object_or_404(AthleticInpt, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/measurements/measurements_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = athletic.personal.user.first_name + '_' + athletic.personal.user.last_name + '_atletik_' + str(
        athletic.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'athletics': athletic,
        'fnames': fname,
    }
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Corporate Fittness Model Pdf Makers
def corporate_measurements_fitness_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    fitness = get_object_or_404(FitnessInputs, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/measurements/measurements_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = fitness.personal.user.first_name + '_' + fitness.personal.user.last_name + '_fitness_' + str(
        fitness.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'fitness': fitness,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Corporate Medical Model Pdf Makers
def corporate_measurements_medical_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    medicalmes = get_object_or_404(MedicalInputModel1, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/measurements/measurements_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = medicalmes.personal.user.first_name + '_' + medicalmes.personal.user.last_name + '_medikal_ölçüm_' + str(
        medicalmes.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'mdcls': medicalmes,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# Corporate Medical Model Pdf Makers
def corporate_measurements_postural_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    postural = get_object_or_404(PosturInputs, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/measurements/measurements_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = postural.personal.user.first_name + '_' + postural.personal.user.last_name + '_postural_ölçüm_' + str(
        postural.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'posturals': postural,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Corporate Prescriptions
# Corporate Prescriptions Athletic development Model Pdf Makers
def corporate_prescriptions_athletic_development_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    postural = get_object_or_404(PosturInputs, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/measurements/prescriptions_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = postural.personal.user.first_name + '_' + postural.personal.user.last_name + '_postural_ölçüm_' + str(
        postural.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'posturals': postural,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Corporate Prescriptions Athletic development Model Pdf Makers
def corporate_prescriptions_corrective_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    corr = get_object_or_404(corrective_exercise, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/prescriptions/prescriptions_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = corr.personal.user.first_name + '_' + corr.personal.user.last_name + '_düzeltici_egzersiz_' + str(
        corr.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'corrctives': corr,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Corporate Prescriptions Athletic development Model Pdf Makers
def corporate_prescriptions_exercise_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    exercise = get_object_or_404(exercise_prescription, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/prescriptions/prescriptions_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = exercise.personal.user.first_name + '_' + exercise.personal.user.last_name + '_egzersiz_reçetesi_' + str(
        exercise.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'exercises': exercise,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# Corporate Medical Prescription Model Pdf Makers
def corporate_prescriptions_medical_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    medical = get_object_or_404(medical_exercise1, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/prescriptions/prescriptions_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = medical.personal.user.first_name + '_' + medical.personal.user.last_name + '_medikal_reçetesi_' + str(
        medical.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'medicals': medical,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# Corporate Metabolic Athletic development Model Pdf Makers
def corporate_prescriptions_metabolic_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    metabolic = get_object_or_404(Metabolic, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/prescriptions/prescriptions_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = metabolic.personal.user.first_name + '_' + metabolic.personal.user.last_name + '_metabolik_reçetesi_' + str(
        metabolic.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'metabolics': metabolic,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# Corporate Metabolic Athletic development Model Pdf Makers
def corporate_prescriptions_personalTraining_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    ptrain = get_object_or_404(personalTrainingInput1, id=id)
    template_path = corporate_content_template_path + 'reporting_analysis/prescriptions/prescriptions_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = ptrain.personal.user.first_name + '_' + ptrain.personal.user.last_name + '_metabolik_reçetesi_' + str(
        ptrain.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'ptrains': ptrain,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Personal pdf Maker Filed
# Personal Form Make pdf Field
# Personal Interview Form pdf field
def personal_interview_forms_pdf_view(request, id):
    # interview = InterviewInput.objects.filter(id=id).all()
    interview = get_object_or_404(InterviewInput, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/forms/interview_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = interview.personal.user.first_name + '_' + interview.personal.user.last_name + '_öngörüşme_formu_' + str(
        interview.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'interviews': interview,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Personal InterviewInput Form Pdf Makers
def personal_medikalInpt_forms_pdf_view(request, id):
    # interview = InterviewInput.objects.filter(id=id).all()
    medikal = get_object_or_404(MedikalInpt, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/forms/medical_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = medikal.personal.user.first_name + '_' + medikal.personal.user.last_name + '_medikal_izin_' + str(
        medikal.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'medikal': medikal,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response

# Personal ContractInput Form Pdf Makers
def personal_contractInput_forms_pdf_view(request, id):
    # contract = ContractInput.objects.filter(id=id).all()
    contract = get_object_or_404(ContractInput, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/forms/contractInput_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = contract.personal.user.first_name + '_' + contract.personal.user.last_name + '_teklif_sözleşme' + str(
        contract.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'contracts': contract,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response



# Personal VoluntaryInput Form Pdf Makers
def personal_voluntaryInput_forms_pdf_view(request, id):
    # voluntaryInput = VoluntaryInput.objects.filter(id=id).all()
    voluntaryInput = get_object_or_404(VoluntaryInput, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/forms/voluntaryInput_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = voluntaryInput.personal.user.first_name + '_' + voluntaryInput.personal.user.last_name + '_gönüllü_formu_' + str(
        voluntaryInput.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'voluntarys': voluntaryInput,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response

# Personal VoluntaryInput Form Pdf Makers
def personal_familyInput_forms_pdf_view(request, id):
    # familyInput = FamilyInput.objects.filter(id=id).all()
    familyInput = get_object_or_404(FamilyInput, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/forms/familyInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = familyInput.personal.user.first_name + '_' + familyInput.personal.user.last_name + '_aile_öyküsü_' + str(
        familyInput.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'familys': familyInput,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Personal ParqInput Form Pdf Makers
def personal_parqInput_forms_pdf_view(request, id):
    # parq = ParqInput.objects.filter(id=id).all()
    parq = get_object_or_404(ParqInput, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/forms/parqInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = parq.personal.user.first_name + '_' + parq.personal.user.last_name + '_parq_' + str(parq.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'parqs': parq,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response

# Personal MoodInput Form Pdf Makers
def personal_moodInput_forms_pdf_view(request, id):
    # moodInput = MoodInput.objects.filter(id=id).all()
    moodInput = get_object_or_404(MoodInput, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/forms/moodInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = moodInput.personal.user.first_name + '_' + moodInput.personal.user.last_name + '_duygu_durumu_' + str(
        moodInput.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'moodInputs': moodInput,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Personal ExercisehistoryInput Form Pdf Makers
def personal_exercisehistoryInput_forms_pdf_view(request, id):
    # exercise = ExercisehistoryInput.objects.filter(id=id).all()
    exercise = get_object_or_404(ExercisehistoryInput, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/forms/exercisehistoryInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = exercise.personal.user.first_name + '_' + exercise.personal.user.last_name + '_egzersiz_geçmişi_' + str(
        exercise.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'exercises': exercise,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response

# Corporate SleepqualityInput Form Pdf Makers
def personal_sleepqualityInput_forms_pdf_view(request, id):
    # sleep = MoodInput.objects.filter(id=id).all()
    sleep = get_object_or_404(SleepqualityInput, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/forms/sleepqualityInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = sleep.personal.user.first_name + '_' + sleep.personal.user.last_name + '_uyku_kalitesi_' + str(sleep.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'sleeps': sleep,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Personal NutritionInput Form Pdf Makers
def personal_nutritionInput_forms_pdf_view(request, id):
    # nutrition = NutritionInput.objects.filter(id=id).all()
    nutrition = get_object_or_404(NutritionInput, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/forms/nutritionInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = nutrition.personal.user.first_name + '_' + nutrition.personal.user.last_name + '_beslenme_' + str(
        nutrition.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'nutritions': nutrition,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# Personal EudaimoniaInput Form Pdf Makers
def personal_eudaimoniaInput_forms_pdf_view(request, id):
    # eudaimonia = EudaimoniaInput.objects.filter(id=id).all()
    eudaimonia = get_object_or_404(EudaimoniaInput, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/forms/eudaimoniaInput_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = eudaimonia.personal.user.first_name + '_' + eudaimonia.personal.user.last_name + '_eudaimonia_' + str(
        eudaimonia.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'eudaimonias': eudaimonia,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response



# Personal Curriculum Form Pdf Makers
def personal_curriculum_forms_pdf_view(request, id):
    # curriculummorning = CurriculumMorning.objects.filter(id=id).all()
    # curriculumnoon = CurriculumNoon.objects.filter(id=id).all()
    # curriculumevening = CurriculumEvening.objects.filter(id=id).all()
    # curriculummsnack = CurriculumSnack.objects.filter(id=id).all()
    # # curriculumwalk = CurriculumWalking1.objects.filter(id=id).all()
    curriculummorning = get_object_or_404(CurriculumMorning, id=id)
    curriculumnoon = get_object_or_404(CurriculumNoon, id=id)
    curriculumevening = get_object_or_404(CurriculumEvening, id=id)
    curriculummsnack = get_object_or_404(CurriculumSnack, id=id)
    curriculumwalk = get_object_or_404(CurriculumWalking1, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/forms/curriculum_pdf.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if you download pdf
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if you attachment browser
    fname = curriculumwalk.personal.user.first_name + '_' + curriculumwalk.personal.user.last_name + '_izlence_' + str(
        curriculumwalk.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    # find the template and render it.
    template = get_template(template_path)
    context = {
        'id': id,
        'curriculummornings': curriculummorning,
        'curriculumnoons': curriculumnoon,
        'curriculumevenings': curriculumevening,
        'curriculummsnacks': curriculummsnack,
        'curriculumwalks': curriculumwalk,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Personal Measurements Athletic Pdf Makers
def personal_measurements_athletic_pdf_view(request, id):
    athletic = get_object_or_404(AthleticInpt, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/measurements/measurements_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = athletic.personal.user.first_name + '_' + athletic.personal.user.last_name + '_atletik_' + str(
        athletic.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'athletics': athletic,
        'fnames': fname,
    }
    html = template.render(context)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('Bir hata ile karşılaşıldı <pre>' + html + '</pre>')
    return response


# Personal Fittness Model Pdf Makers
def personal_measurements_fitness_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    fitness = get_object_or_404(FitnessInputs, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/measurements/measurements_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = fitness.personal.user.first_name + '_' + fitness.personal.user.last_name + '_fitness_' + str(
        fitness.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'fitness': fitness,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Personal Medical Model Pdf Makers
def personal_measurements_medical_pdf_view(request, id):
    medicalmes = get_object_or_404(MedicalInputModel1, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/measurements/measurements_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = medicalmes.personal.user.first_name + '_' + medicalmes.personal.user.last_name + '_medikal_ölçüm_' + str(
        medicalmes.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'mdcls': medicalmes,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Personal Medical Model Pdf Makers
def personal_measurements_postural_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    postural = get_object_or_404(PosturInputs, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/measurements/measurements_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = postural.personal.user.first_name + '_' + postural.personal.user.last_name + '_postural_ölçüm_' + str(
        postural.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'posturals': postural,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



# Personal Prescriptions
# Personal Prescriptions Athletic development Model Pdf Makers
def personal_prescriptions_athletic_development_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    postural = get_object_or_404(PosturInputs, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/measurements/prescriptions_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = postural.personal.user.first_name + '_' + postural.personal.user.last_name + '_postural_ölçüm_' + str(
        postural.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'posturals': postural,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Personal Prescriptions Athletic development Model Pdf Makers
def personal_prescriptions_corrective_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    corr = get_object_or_404(corrective_exercise, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/prescriptions/prescriptions_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = corr.personal.user.first_name + '_' + corr.personal.user.last_name + '_düzeltici_egzersiz_' + str(
        corr.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'corrctives': corr,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


# Personal Prescriptions Athletic development Model Pdf Makers
def personal_prescriptions_exercise_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    exercise = get_object_or_404(exercise_prescription, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/prescriptions/prescriptions_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = exercise.personal.user.first_name + '_' + exercise.personal.user.last_name + '_egzersiz_reçetesi_' + str(
        exercise.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'exercises': exercise,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# Personal Medical Prescription Model Pdf Makers
def personal_prescriptions_medical_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    medical = get_object_or_404(medical_exercise1, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/prescriptions/prescriptions_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = medical.personal.user.first_name + '_' + medical.personal.user.last_name + '_medikal_reçetesi_' + str(
        medical.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'medicals': medical,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# Personal Metabolic Athletic development Model Pdf Makers
def personal_prescriptions_metabolic_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    metabolic = get_object_or_404(Metabolic, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/prescriptions/prescriptions_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = metabolic.personal.user.first_name + '_' + metabolic.personal.user.last_name + '_metabolik_reçetesi_' + str(
        metabolic.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'metabolics': metabolic,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# Personal Metabolic Athletic development Model Pdf Makers
def personal_prescriptions_personalTraining_pdf_view(request, id):
    # fitness = FitnessInputs.objects.filter(id=id).all()
    ptrain = get_object_or_404(personalTrainingInput1, id=id)
    template_path = personal_content_template_path + 'reporting_analysis/prescriptions/prescriptions_pdf.html'
    response = HttpResponse(content_type='application/pdf')
    fname = ptrain.personal.user.first_name + '_' + ptrain.personal.user.last_name + '_metabolik_reçetesi_' + str(
        ptrain.id)
    response["Content-Disposition"] = "filename={}".format(fname)
    template = get_template(template_path)
    context = {
        'id': id,
        'ptrains': ptrain,
        'fnames': fname,
    }
    html = template.render(context, request=request)
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

