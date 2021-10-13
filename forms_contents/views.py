from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
# Create your views here.
from forms_contents.constant import FORM
from forms_contents.forms import InterviewForm, ContractForm, MedikalInpt, VoluntaryForm, FamilyForm, \
    ExercisehistoryForm, ParqForm, MoodForm, SleepqualityForm, NutritionForm, EudaimoniaForm, \
    MedikalForm, CurriculumWalkingForm, CurriculumMorningForm, CurriculumNoonForm, CurriculumEveningForm, \
    CurriculumSnackForms
from forms_contents.models import NutritionInput, InterviewInput, ContractInput, VoluntaryInput, ParqInput, MoodInput, \
    ExercisehistoryInput, FamilyInput, SleepqualityInput, EudaimoniaInput, CurriculumMorning, CurriculumWalking1, \
    CurriculumNoon, CurriculumEvening, CurriculumSnack
from registration.forms import CustomUserRegistrationForm
from registration.models import Personal
from registration.views import user_checking

trainer_content_template_path = 'modules/trainer_content/'
corporate_content_template_path = 'modules/corporate_content/'
personal_content_template_path = 'modules/personel_content/'


def trainer_forms_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    trainer_id = user_control_data['trainer_info'].id
    personal_data = Personal.objects.filter(trainer_id=trainer_id).all()
    template = trainer_content_template_path + 'forms/forms.html'
    form = FORM
    context = {
        'personals': personal_data,
        'user_control_data': user_control_data,
        'form': form,
    }
    return render(request=request, template_name=template, context=context)


# Start Interview form CRUD
def trainer_interview_create(request):
    user = request.user
    user_control_data = user_checking(user.id)
    trainer = user_control_data['trainer_info']
    print('-------------------************Başlangıç*******--------------------------')
    if request.method == 'POST':
        interview_form = InterviewForm(request.POST)
        if interview_form.is_valid():
            interview = interview_form.save(commit=False)
            interview.trainer = trainer
            interview.save()
            messages.success(request, message='Kayıt Başarılı')
            print('--------------------************Başarılı*******--------------------------')
        else:
            messages.warning(request, 'İşlem Başarısız')
            print('--------------- ----************Başarısız*******--------------------------')
            print(interview_form.errors)

    return redirect('trainer-forms-home')


def trainer_interview_delete(request, id):
    interview = get_object_or_404(InterviewInput, id=id)
    ps_id = interview.personal_id
    interview.delete()
    return redirect('trainer-forms-analysis-results-home', id=ps_id)


def corporate_interview_delete(request, id):
    interview = get_object_or_404(InterviewInput, id=id)
    crp_id = interview.personal_id
    interview.delete()
    return redirect('corporate-forms-analysis-results-home', id=crp_id)


def personal_interview_delete(request, id):
    interview = get_object_or_404(InterviewInput, id=id)
    interview.delete()
    return redirect('corporate-forms-analysis-results-home')


# Finish Interview Form CRUD
# Start Contact Form CRUD
def trainer_contract_create(request):
    user = request.user
    user_control_data = user_checking(user.id)
    trainer = user_control_data['trainer_info']
    if request.method == 'POST':
        contract_form = ContractForm(request.POST)
        if contract_form.is_valid():
            contract = contract_form.save(commit=False)
            contract.trainer = trainer
            contract.save()
            messages.success(request, message='Kayıt Başarılı')
        else:
            messages.warning(request, 'İşlem Başarısız')

    return redirect('trainer-forms-home')


def trainer_contract_delete(request, id):
    contract = get_object_or_404(ContractInput, id=id)
    ps_id = contract.personal_id
    contract.delete()
    return redirect('trainer-forms-analysis-results-home', id=ps_id)


def corporate_contract_delete(request, id):
    contract = get_object_or_404(ContractInput, id=id)
    crp_id = contract.personal_id
    contract.delete()
    return redirect('corporate-forms-analysis-results-home', id=crp_id)


def personal_contract_delete(request, id):
    contract = get_object_or_404(ContractInput, id=id)
    contract.delete()
    return redirect('corporate-forms-analysis-results-home')


# Finish Contact Form CRUD
# Start Medical Form CRUD
def trainer_medicalForm_create(request):
    user = request.user
    user_control_data = user_checking(user.id)
    trainer = user_control_data['trainer_info']
    print('-------------------************Başlangıç*******--------------------------')
    if request.method == 'POST':
        medical_form = MedikalForm(request.POST)
        if medical_form.is_valid():
            medical = medical_form.save(commit=False)
            medical.trainer = trainer
            medical.save()
            messages.success(request, message='Kayıt Başarılı')
            print('--------------------************Başarılı*******--------------------------')
        else:
            messages.warning(request, 'İşlem Başarısız')
            print('--------------- ----************Başarısız*******--------------------------')
            print(medical_form.errors)

    return redirect('trainer-forms-home')


def trainer_medical_delete(request, id):
    medical = get_object_or_404(MedikalInpt, id=id)
    ps_id = medical.personal_id
    medical.delete()
    return redirect('trainer-forms-analysis-results-home', id=ps_id)


def corporate_medical_delete(request, id):
    medical = get_object_or_404(MedikalInpt, id=id)
    crp_id = medical.personal_id
    medical.delete()
    return redirect('corporate-forms-analysis-results-home', id=crp_id)


def personal_medical_delete(request, id):
    medical = get_object_or_404(MedikalInpt, id=id)
    medical.delete()
    return redirect('corporate-forms-analysis-results-home')


# Finish Medical Form CRUD

# Start Voluntary Form CRUD
def trainer_voluntary_create(request):
    user = request.user
    user_control_data = user_checking(user.id)
    trainer = user_control_data['trainer_info']
    if request.method == 'POST':
        voluntary_form = VoluntaryForm(request.POST)
        if voluntary_form.is_valid():
            voluntary = voluntary_form.save(commit=False)
            voluntary.trainer = trainer
            voluntary.save()
            print("----------------------Başarılı--------------------")
            messages.success(request, message='Kayıt Başarılı')
        else:
            messages.warning(request, 'İşlem Başarısız')
            print("-------------------------------------------")
            print(voluntary_form.errors)
            print("-------------------------------------------")

    return redirect('trainer-forms-home')


def trainer_voluntary_delete(request, id):
    voluntary = get_object_or_404(VoluntaryInput, id=id)
    ps_id = voluntary.personal_id
    voluntary.delete()
    return redirect('trainer-forms-analysis-results-home', id=ps_id)


def corporate_voluntary_delete(request, id):
    voluntary = get_object_or_404(VoluntaryInput, id=id)
    crp_id = voluntary.personal_id
    voluntary.delete()
    return redirect('corporate-forms-analysis-results-home', id=crp_id)


def personal_voluntary_delete(request, id):
    voluntary = get_object_or_404(VoluntaryInput, id=id)
    voluntary.delete()
    return redirect('corporate-forms-analysis-results-home')


# Finish Voluntary Form CRUD

# Start Parq Form CRUD
def trainer_parq_create(request):
    user = request.user
    user_control_data = user_checking(user.id)
    trainer = user_control_data['trainer_info']
    if request.method == 'POST':
        parq_form = ParqForm(request.POST)
        if parq_form.is_valid():
            parq = parq_form.save(commit=False)
            parq.trainer = trainer
            parq.save()
            messages.success(request, message='Kayıt Başarılı')
        else:
            messages.warning(request, 'İşlem Başarısız')

    return redirect('trainer-forms-home')


def trainer_parq_delete(request, id):
    parq = get_object_or_404(ParqInput, id=id)
    ps_id = parq.personal_id
    parq.delete()
    return redirect('trainer-forms-analysis-results-home', id=ps_id)


def corporate_parq_delete(request, id):
    parq = get_object_or_404(ParqInput, id=id)
    crp_id = parq.personal_id
    parq.delete()
    return redirect('corporate-forms-analysis-results-home', id=crp_id)


def personal_parq_delete(request, id):
    parq = get_object_or_404(ParqInput, id=id)
    parq.delete()
    return redirect('corporate-forms-analysis-results-home')


#  Finish Parq Form CRUD

def personal_forms_home(request):
    user = request.user
    form = FORM
    user_control_data = user_checking(user.id)
    template = personal_content_template_path + 'forms/forms.html'
    context = {
        'form': form,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


# Start Family Form CRUD
def personal_family_create(request):
    user = request.user
    user_control_data = user_checking(user.id)
    personal = user_control_data['personal_info']
    trainer = personal.trainer
    if request.method == 'POST':
        family_form = FamilyForm(request.POST)
        if family_form.is_valid():
            family = family_form.save(commit=False)
            family.personal = personal
            family.trainer = trainer
            family.save()
            messages.success(request, message='Kayıt Başarılı')
        else:
            messages.warning(request, 'İşlem Başarısız')

    return redirect('personal-forms-home')


def trainer_family_delete(request, id):
    family = get_object_or_404(FamilyInput, id=id)
    ps_id = family.personal_id
    family.delete()
    return redirect('trainer-forms-analysis-results-home', id=ps_id)


def corporate_family_delete(request, id):
    family = get_object_or_404(FamilyInput, id=id)
    crp_id = family.personal_id
    family.delete()
    return redirect('corporate-forms-analysis-results-home', id=crp_id)


def personal_family_delete(request, id):
    family = get_object_or_404(FamilyInput, id=id)
    family.delete()
    return redirect('personal-forms-analysis-home')


# Finish Family Form CRUD

# Start Exercise History Form CRUD
def personal_exercisehistory_create(request):
    user = request.user
    user_control_data = user_checking(user.id)
    personal = user_control_data['personal_info']
    trainer = personal.trainer
    if request.method == 'POST':
        exercisehistory_form = ExercisehistoryForm(request.POST)
        if exercisehistory_form.is_valid():
            exercisehistory = exercisehistory_form.save(commit=False)
            exercisehistory.personal = personal
            exercisehistory.trainer = trainer
            exercisehistory.save()
            messages.success(request, message='Kayıt Başarılı')
        else:
            messages.warning(request, 'İşlem Başarısız')

    return redirect('personal-forms-home')


def trainer_exercisehistory_delete(request, id):
    exh = get_object_or_404(ExercisehistoryInput, id=id)
    ps_id = exh.personal_id
    exh.delete()
    return redirect('trainer-forms-analysis-results-home', id=ps_id)


def corporate_exercisehistory_delete(request, id):
    exh = get_object_or_404(ExercisehistoryInput, id=id)
    crp_id = exh.personal_id
    exh.delete()
    return redirect('corporate-forms-analysis-results-home', id=crp_id)


def personal_exercisehistory_delete(request, id):
    exh = get_object_or_404(ExercisehistoryInput, id=id)
    exh.delete()
    return redirect('personal-forms-analysis-home')


# Finish Exercise History Form CRUD

# Start Mood History Form CRUD
def personal_mood_create(request):
    user = request.user
    user_control_data = user_checking(user.id)
    personal = user_control_data['personal_info']
    trainer = personal.trainer
    if request.method == 'POST':
        mood_form = MoodForm(request.POST)
        if mood_form.is_valid():
            mood = mood_form.save(commit=False)
            mood.personal = personal
            mood.trainer = trainer
            mood.save()
            messages.success(request, message='Kayıt Başarılı')
        else:
            messages.warning(request, 'İşlem Başarısız')

    return redirect('personal-forms-home')


def trainer_mood_delete(request, id):
    mood = get_object_or_404(MoodInput, id=id)
    ps_id = mood.personal_id
    mood.delete()
    return redirect('trainer-forms-analysis-results-home', id=ps_id)


def corporate_mood_delete(request, id):
    mood = get_object_or_404(MoodInput, id=id)
    crp_id = mood.personal_id
    mood.delete()
    return redirect('corporate-forms-analysis-results-home', id=crp_id)


def personal_mood_delete(request, id):
    mood = get_object_or_404(MoodInput, id=id)
    mood.delete()
    return redirect('personal-forms-analysis-home')


# Finish Mood Form CRUD

# Start Sleepquality Form CRUD
def personal_sleepquality_create(request):
    user = request.user
    user_control_data = user_checking(user.id)
    personal = user_control_data['personal_info']
    trainer = personal.trainer
    if request.method == 'POST':
        sleepquality_form = SleepqualityForm(request.POST)
        if sleepquality_form.is_valid():
            sleepquality = sleepquality_form.save(commit=False)
            sleepquality.personal = personal
            sleepquality.trainer = trainer
            sleepquality.save()
            messages.success(request, message='Kayıt Başarılı')
        else:
            messages.warning(request, 'İşlem Başarısız')

    return redirect('personal-forms-home')


def trainer_sleepquality_delete(request, id):
    slp = get_object_or_404(SleepqualityInput, id=id)
    ps_id = slp.personal_id
    slp.delete()
    return redirect('trainer-forms-analysis-results-home', id=ps_id)


def corporate_sleepquality_delete(request, id):
    slp = get_object_or_404(SleepqualityInput, id=id)
    crp_id = slp.personal_id
    slp.delete()
    return redirect('corporate-forms-analysis-results-home', id=crp_id)


def personal_sleepquality_delete(request, id):
    slp = get_object_or_404(SleepqualityInput, id=id)
    slp.delete()
    return redirect('personal-forms-analysis-home')


# Finish Sleepquality Form CRUD


# Start Nutrition Form CRUD
def personal_nutrition_create(request):
    user = request.user
    user_control_data = user_checking(user.id)
    personal = user_control_data['personal_info']
    trainer = personal.trainer
    if request.method == 'POST':
        nutrition_form = NutritionForm(request.POST)
        if nutrition_form.is_valid():
            nutrition = nutrition_form.save(commit=False)
            nutrition.personal = personal
            nutrition.trainer = trainer
            nutrition.save()
            print("-------------------Başarılı------------------------------------")
            messages.success(request, message='Kayıt Başarılı')
        else:
            messages.warning(request, 'İşlem Başarısız')
            print("-------------------------------------------")
            print(nutrition_form.errors)
            print("-------------------------------------------")

    return redirect('personal-forms-home')


def trainer_nutrition_delete(request, id):
    ntr = get_object_or_404(NutritionInput, id=id)
    ps_id = ntr.personal_id
    ntr.delete()
    return redirect('trainer-forms-analysis-results-home', id=ps_id)


def corporate_nutrition_delete(request, id):
    ntr = get_object_or_404(NutritionInput, id=id)
    crp_id = ntr.personal_id
    ntr.delete()
    return redirect('corporate-forms-analysis-results-home', id=crp_id)


def personal_nutrition_delete(request, id):
    ntr = get_object_or_404(NutritionInput, id=id)
    ntr.delete()
    return redirect('personal-forms-analysis-home')


# Finish Nutrition Form CRUD

# Start Eudaimonia Form CRUD
def personal_eudaimonia_create(request):
    user = request.user
    user_control_data = user_checking(user.id)
    personal = user_control_data['personal_info']
    trainer = personal.trainer
    if request.method == 'POST':
        eudaimonia_form = EudaimoniaForm(request.POST)
        if eudaimonia_form.is_valid():
            eudaimonia = eudaimonia_form.save(commit=False)
            eudaimonia.personal = personal
            eudaimonia.trainer = trainer
            eudaimonia.save()
            messages.success(request, message='Kayıt Başarılı')
        else:
            messages.warning(request, 'İşlem Başarısız')

    return redirect('personal-forms-home')


def trainer_eudaimonia_delete(request, id):
    edm = get_object_or_404(EudaimoniaInput, id=id)
    ps_id = edm.personal_id
    edm.delete()
    return redirect('trainer-forms-analysis-results-home', id=ps_id)


def corporate_eudaimonia_delete(request, id):
    edm = get_object_or_404(EudaimoniaInput, id=id)
    crp_id = edm.personal_id
    edm.delete()
    return redirect('corporate-forms-analysis-results-home', id=crp_id)


def personal_eudaimonia_delete(request, id):
    edm = get_object_or_404(EudaimoniaInput, id=id)
    edm.delete()
    return redirect('personal-forms-analysis-home')


# Finish Eudaimonia Form CRUD


# İzlence Formu başlangıcı

def personal_notification_home(request):
    user = request.user
    form = FORM
    user_control_data = user_checking(user.id)
    template = personal_content_template_path + 'analyzes/notification_panel/notification.html'
    context = {
        'form': form,
        'user_control_data': user_control_data
    }

    return render(request=request, template_name=template, context=context)


def personal_curriculum_walking_create(request):
    user = request.user
    user_control_data = user_checking(user.id)
    personal = user_control_data['personal_info']
    trainer = personal.trainer
    print('-------------------************Başlangıç*******--------------------------')
    if request.method == 'POST':
        walkingForm = CurriculumWalkingForm(request.POST)
        morningForm = CurriculumMorningForm(request.POST)
        noonForm = CurriculumNoonForm(request.POST)
        evenForm = CurriculumEveningForm(request.POST)
        snackForm = CurriculumSnackForms(request.POST)
        if walkingForm.is_valid() and morningForm.is_valid() and noonForm.is_valid() and evenForm.is_valid() and snackForm.is_valid():
            walking = walkingForm.save(commit=False)
            walking.personal = personal
            walking.trainer = trainer
            morning = morningForm.save()
            noon = noonForm.save()
            even = evenForm.save()
            snack = snackForm.save()
            walking.morning = morning
            walking.noon = noon
            walking.even = even
            walking.snack = snack
            walking.save()
            messages.success(request, message='Kayıt Başarılı')
            print('--------------------************Başarılı*******--------------------------')
        else:
            messages.warning(request, 'İşlem Başarısız')
            print('--------------- ----************walkingForm*******--------------------------')
            print(walkingForm.errors)
            print('--------------- ----************morningForm*******--------------------------')
            print(morningForm.errors)
            print('--------------- ----************noonForm*******--------------------------')
            print(noonForm.errors)
            print('--------------- ----************evenForm*******--------------------------')
            print(evenForm.errors)
            print('--------------- ----************snackForm*******--------------------------')
            print(snackForm.errors)

    return redirect('personal-notifications-home')


def trainer_curriculum_delete(request, id):
    crclm = get_object_or_404(CurriculumWalking1, id=id)
    ps_id = crclm.personal_id
    crclmmorning = CurriculumMorning.objects.get(id=crclm.morning.id)
    crclmmorning.delete()
    crclmnoon = CurriculumNoon.objects.get(id=crclm.noon.id)
    crclmnoon.delete()
    crclmevening = CurriculumEvening.objects.get(id=crclm.even.id)
    crclmevening.delete()
    crclmsnack = CurriculumSnack.objects.get(id=crclm.snack.id)
    crclmsnack.delete()
    crclm.delete()
    return redirect('trainer-forms-analysis-results-home', id=ps_id)


def corporate_curriculum_delete(request, id):
    crclm = get_object_or_404(CurriculumWalking1, id=id)
    crp_id = crclm.personal_id
    crclmmorning = CurriculumMorning.objects.get(id=crclm.morning.id)
    crclmmorning.delete()
    crclmnoon = CurriculumNoon.objects.get(id=crclm.noon.id)
    crclmnoon.delete()
    crclmevening = CurriculumEvening.objects.get(id=crclm.even.id)
    crclmevening.delete()
    crclmsnack = CurriculumSnack.objects.get(id=crclm.snack.id)
    crclmsnack.delete()
    crclm.delete()
    return redirect('corporate-forms-analysis-results-home', id=crp_id)


def personal_curriculum_delete(request, id):
    crclm = get_object_or_404(CurriculumWalking1, id=id)
    crclmmorning = CurriculumMorning.objects.get(id=crclm.morning.id)
    crclmmorning.delete()
    crclmnoon = CurriculumNoon.objects.get(id=crclm.noon.id)
    crclmnoon.delete()
    crclmevening = CurriculumEvening.objects.get(id=crclm.even.id)
    crclmevening.delete()
    crclmsnack = CurriculumSnack.objects.get(id=crclm.snack.id)
    crclmsnack.delete()
    crclm.delete()
    return redirect('personal-forms-analysis-home')
# İzlance Formu bitişi
