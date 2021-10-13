from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.shortcuts import render
from django.contrib import messages

from medical.constant import MEDICAL
from medical.forms import MedicalForm, MedicalForm2
from medical.models import MedicalInputModel1, MedicalInputModel2
from registration.forms import CustomUserRegistrationForm
from registration.models import Corporate, Trainer, Personal
from registration.views import user_checking

trainer_content_template_path = 'modules/trainer_content/measurements/'
corporate_content_template_path = 'modules/corporate_content/measurements/'


# Corporate Views
def corporate_medical_home(request):
    user = request.user
    template = corporate_content_template_path + 'medical/medical.html'

    user_control = user_checking(user.id)
    context = {

        'user_control_data': user_control,
    }
    return render(request=request, template_name=template, context=context)


def corporate_medical_create(request):
    user = request.user
    user_control = user_checking(user.id)
    template = corporate_content_template_path + 'medical/medical_form.html'
    if request.method == "POST":
        medical_form = MedicalForm(request.POST, request.FILES)
        user_form = CustomUserRegistrationForm(request.POST)
        if medical_form.is_valid():
            medical_form.save()
            messages.success(request, message='Kayıt Başarılı')
            return redirect('corporate-medical-home')
        else:
            messages.warning(request, 'İşlem Başarısız')
    else:
        medical_form = MedicalForm()
        user_form = CustomUserRegistrationForm()
    context = {
        'action': 'create',
        'medical_form': medical_form,
        'user_control_data': user_control,
    }
    return render(request=request, template_name=template, context=context)


# Trainer Views
def trainer_medical_home(request):
    user = request.user
    template = trainer_content_template_path + 'medical/medical.html'
    corporate_data = Corporate.objects.all()
    trainer_data = Trainer.objects.all()
    personal_data = Personal.objects.all()
    user_control = user_checking(user.id)
    context = {
        'corporates': corporate_data,
        'trainers': trainer_data,
        'personals': personal_data,
        'user_control_data': user_control,
    }
    return render(request=request, template_name=template, context=context)


def trainer_medical_create(request):
    user = request.user
    medical_constant = MEDICAL
    user_control = user_checking(user.id)
    trainer_id = user_control['trainer_info'].id
    personal_data = Personal.objects.filter(trainer_id=trainer_id).all()
    template = trainer_content_template_path + 'medical/medical_form.html'
    if request.method == "POST":
        medical_form = MedicalForm(request.POST)
        medical_form2 = MedicalForm2(request.POST)
        if medical_form.is_valid() and medical_form2.is_valid():
            medical = medical_form.save(commit=False)
            medical.trainer_id = trainer_id
            medical2 = medical_form2.save()
            medical.medical2 = medical2
            medical.save()
            messages.success(request, message='Kayıt Başarılı')
            return redirect('trainer-medical-create')
        else:
            messages.warning(request, 'İşlem Başarısız')
            print("-----------------------Medical Form1----------------------------------------")
            print(medical_form.errors)
            print("-----------------------------------Medical Form2------------------------------")
            print(medical_form2.errors)
    else:
        medical_form = MedicalForm()
    context = {
        'action': 'create',
        'medical': medical_constant,
        'medical_form': medical_form,
        'user_control_data': user_control,
        'personals': personal_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_medical_delete(request, id):
    medical = get_object_or_404(MedicalInputModel1, id=id)
    ps_id = medical.personal_id
    medical2=MedicalInputModel2.objects.get(id=medical.medical2.id)
    medical2.delete()
    medical.delete()
    return redirect('trainer-measurements-medical-results-home', id=ps_id)


def corporate_medical_delete(request, id):
    medical = get_object_or_404(MedicalInputModel1, id=id)
    crp_id = medical.personal_id
    medical.delete()
    return redirect('corporate-measurements-medical-results-home', id=crp_id)


def personal_medical_delete(request, id):
    medical = get_object_or_404(MedicalInputModel1, id=id)
    medical.delete()
    return redirect('personal-measurements-medical-home')
