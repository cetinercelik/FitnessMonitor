from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from athletic.constant import ATHLETIC
from athletic.forms import AthleticForm
from athletic.models import AthleticInpt
from registration.forms import CustomUserRegistrationForm
from registration.models import Corporate, Trainer, Personal
from registration.views import user_checking

trainer_content_template_path = 'modules/trainer_content/measurements/'
corporate_content_template_path = 'modules/corporate_content/measurements/'


# Corporate View
def corporate_athletic_home(request):
    user = request.user
    template = corporate_content_template_path + 'athletic_performance/athletic_performance.html'
    user_control_data = user_checking(user.id)
    context = {

        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


# Trainer Wiews
def trainer_athletic_home(request):
    user = request.user
    template = trainer_content_template_path + 'athletic_performance/athletic_performance.html'
    corporate_data = Corporate.objects.all()
    trainer_data = Trainer.objects.all()
    personal_data = Personal.objects.all()
    user_control_data = user_checking(user.id)
    context = {
        'corporates': corporate_data,
        'trainers': trainer_data,
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_athletic_create_home(request):
    user = request.user
    athletic_constant = ATHLETIC
    user_control_data = user_checking(user.id)
    trainer_id = user_control_data['trainer_info'].id
    personal_data = Personal.objects.filter(trainer_id=trainer_id).all()
    template = trainer_content_template_path + 'athletic_performance/athletic_performance_form.html'
    context = {
        'athletic': athletic_constant,
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_athletic_create(request):
    user = request.user
    user_control_data = user_checking(user.id)
    trainer_id = user_control_data['trainer_info'].id
    if request.method == 'POST':
        athletic_form = AthleticForm(request.POST, request.FILES)
        if athletic_form.is_valid():
            athletic = athletic_form.save(commit=False)
            athletic.trainer_id = trainer_id
            athletic.save()
            messages.success(request, message='Kayıt Başaraılı')
            return redirect('trainer-athletic-create')
        else:
            messages.warning(request, 'İşlem başarısız')
            print('***********************************************************************************')
            print(athletic_form.errors)
            print('**********************************************************************************')

    return redirect('trainer-athletic-create-home')


def trainer_athletic_delete(request, id):
    athletic = get_object_or_404(AthleticInpt, id=id)
    ps_id = athletic.personal_id
    athletic.delete()
    return redirect('trainer-measurements-athletic-result-home', id=ps_id)


def corporate_athletic_delete(request, id):
    athletic = get_object_or_404(AthleticInpt, id=id)
    crp_id = athletic.personal_id
    athletic.delete()
    return redirect('corporate-measurements-athletic-results-home', id=crp_id)


def personal_athletic_delete(request, id):
    athletic = get_object_or_404(AthleticInpt, id=id)
    athletic.delete()
    return redirect('personal-measurements-athletic-home')
