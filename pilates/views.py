from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from pilates.constant import PILATES
from pilates.forms import PersonalTrainingForm1, PersonalTrainingForm2, PersonalTrainingForm3, \
    PersonalTrainingForm4
from pilates.models import personalTrainingInput1, personalTrainingInput2, personalTrainingInput3, \
    personalTrainingInput4
from registration.forms import CustomUserRegistrationForm
from registration.models import Personal
from registration.views import user_checking

trainer_template_name = 'modules/trainer_content/prescriptions/'


def trainer_pilates_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    trainer_id = user_control_data['trainer_info'].id
    personal_data = Personal.objects.filter(trainer_id=trainer_id).all()
    template = trainer_template_name + 'pilates/pilates.html'
    context = {
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_pilates_create(request):
    user = request.user
    pilates = PILATES
    user_control = user_checking(user.id)
    template = trainer_template_name + 'pilates/pilates_form.html'
    trainer_id = user_control['trainer_info'].id
    personal_data = Personal.objects.filter(trainer_id=trainer_id).all()
    if request.method == 'POST':
        training_form1 = PersonalTrainingForm1(request.POST)
        training_form2 = PersonalTrainingForm2(request.POST)
        training_form3 = PersonalTrainingForm3(request.POST)
        training_form4 = PersonalTrainingForm4(request.POST)
        if training_form1.is_valid() and training_form2.is_valid() and training_form3.is_valid() and training_form4.is_valid():
            training1 = training_form1.save(commit=False)
            training1.trainer_id = trainer_id
            training2 = training_form2.save()
            training1.training2 = training2
            training3 = training_form3.save()
            training1.training3 = training3
            training4 = training_form4.save()
            training1.training4 = training4
            training1.save()
            messages.success(request, message='Kayıt Başaraılı')
            return redirect('trainer-pilates-home')
        else:
            messages.warning(request, 'İşlem başarısız')
            print('************************************training1_form1***********************************************')
            print(training_form1.errors)
            print('************************************training_form2***********************************************')
            print(training_form2.errors)
            print('************************************training_form3***********************************************')
            print(training_form3.errors)
            print('************************************training_form4***********************************************')
            print(training_form4.errors)
    else:
        user_form = CustomUserRegistrationForm()
        context = {
            'action': 'create',
            'pilates': pilates,
            'personals': personal_data,
            'user_form': user_form,
            'user_control_data': user_control,
        }
        return render(request=request, template_name=template, context=context)


def trainer_pilates_delete(request, id):
    personalTraining1 = get_object_or_404(personalTrainingInput1, id=id)
    ps_id = personalTraining1.personal_id
    personalTraining2 = personalTrainingInput2.objects.get(id=personalTraining1.training2.id)
    personalTraining3 = personalTrainingInput3.objects.get(id=personalTraining1.training3.id)
    personalTraining4 = personalTrainingInput4.objects.get(id=personalTraining1.training4.id)
    personalTraining2.delete()
    personalTraining3.delete()
    personalTraining4.delete()
    personalTraining1.delete()
    return redirect('trainer-prescriptions-pilates-prescription-results', id=ps_id)


def corporate_pilates_delete(request, id):
    personalTraining1 = get_object_or_404(personalTrainingInput1, id=id)
    crp_id = personalTraining1.personal_id
    personalTraining2 = personalTrainingInput2.objects.get(id=personalTraining1.training2.id)
    personalTraining3 = personalTrainingInput3.objects.get(id=personalTraining1.training3.id)
    personalTraining4 = personalTrainingInput4.objects.get(id=personalTraining1.training4.id)
    personalTraining2.delete()
    personalTraining3.delete()
    personalTraining4.delete()
    personalTraining1.delete()
    return redirect('corporate-prescriptions-pilates-prescription-results', id=crp_id)


def personal_pilates_delete(request, id):
    personalTraining1 = get_object_or_404(personalTrainingInput1, id=id)
    personalTraining2 = personalTrainingInput2.objects.get(id=personalTraining1.training2.id)
    personalTraining3 = personalTrainingInput3.objects.get(id=personalTraining1.training3.id)
    personalTraining4 = personalTrainingInput4.objects.get(id=personalTraining1.training4.id)
    personalTraining2.delete()
    personalTraining3.delete()
    personalTraining4.delete()
    personalTraining1.delete()
    personalTraining1.delete()
    return redirect('personal-prescriptions-pilates-prescription-results')
