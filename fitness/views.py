from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from fitness.constant import FITNESS
from fitness.forms import FitnessForm
from fitness.models import FitnessInputs
from registration.forms import CustomUserRegistrationForm
from registration.models import Corporate, Trainer, Personal
from registration.views import user_checking

trainer_content_template_path = 'modules/trainer_content/measurements/'
corporate_content_template_path = 'modules/corporate_content/measurements/'


# Corporate Views
def corporate_fitness_home(request):
    user = request.user
    template = corporate_content_template_path + 'fitness/fitness.html'
    user_control = user_checking(user.id)
    context = {

        'user_control_data': user_control,
    }

    return render(request=request, template_name=template, context=context)


def corporate_fitness_create(request):
    user = request.user
    user_control_data = user_checking(user.id)
    template = corporate_content_template_path + 'fitness/fitness_form.html'
    context = {

        'user_control_data': user_control_data,
    }

    return render(request=request, template_name=template, context=context)


# Trainer Views
def trainer_fitness_home(request):
    user = request.user
    template = trainer_content_template_path + 'fitness/fitness.html'
    user_control_data = user_checking(user.id)
    context = {
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_fitness_create(request):
    user = request.user
    fitness = FITNESS
    user_control_data = user_checking(user.id)
    trainer_id = user_control_data['trainer_info'].id
    personal_data = Personal.objects.filter(trainer_id=trainer_id).all()
    template = trainer_content_template_path + 'fitness/fitness_form.html'
    if request.method == 'POST':
        fitnes_form = FitnessForm(request.POST, request.FILES)
        if fitnes_form.is_valid():
            fitness = fitnes_form.save(commit=False)
            fitness.trainer_id = trainer_id
            fitness.save()
            messages.success(request, message='Kayıt Başaraılı')
            return redirect('trainer-fitness-create')
        else:
            messages.warning(request, 'İşlem başarısız')
            print('***********************************************************************************')
            print(fitnes_form.errors)
            print('**********************************************************************************')
    else:
        fitnes_form = FitnessForm()
        user_form = CustomUserRegistrationForm()
        context = {
            'action': 'create',
            'fitness': fitness,
            'fitness_form': fitnes_form,
            'user_form': user_form,
            'user_control_data': user_control_data,
            'personals': personal_data,

        }
        return render(request=request, template_name=template, context=context)


def trainer_fitness_delete(request, id):
    fitness = get_object_or_404(FitnessInputs, id=id)
    ps_id = fitness.personal_id
    fitness.delete()
    return redirect('trainer-measurements-fitness-results-home', id=ps_id)


def corporate_fitness_delete(request, id):
    fitness = get_object_or_404(FitnessInputs, id=id)
    crp_id = fitness.personal_id
    fitness.delete()
    return redirect('corporate-measurements-fitness-results-home', id=crp_id)


def personal_fitness_delete(request, id):
    fitness = get_object_or_404(FitnessInputs, id=id)
    fitness.delete()
    return redirect('personal-measurements-fitness-home')
