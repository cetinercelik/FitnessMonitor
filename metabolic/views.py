from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from metabolic.constant import METABOLIC
from metabolic.forms import MetabolicForms, MetabolicForms2
from metabolic.models import Metabolic, Metabolic2
from registration.models import Personal
from registration.views import user_checking

trainer_content_template_path = 'modules/trainer_content/prescriptions/'


def trainer_metabolic_exercise_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    trainer_id = user_control_data['trainer_info'].id
    personal_data = Personal.objects.filter(trainer_id=trainer_id).all()
    template = trainer_content_template_path + 'metabolic/metabolic.html'
    context = {
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_metabolic_exercise_create(request):
    user = request.user
    metabolic = METABOLIC
    user_control_data = user_checking(user.id)
    trainer_id = user_control_data['trainer_info'].id
    personal_data = Personal.objects.filter(trainer_id=trainer_id).all()
    template = trainer_content_template_path + 'metabolic/metabolic_form.html'
    if request.method == 'POST':
        metabolic_form = MetabolicForms(request.POST)
        metabolic_form2 = MetabolicForms2(request.POST)
        if metabolic_form.is_valid() and metabolic_form2.is_valid():
            metabolic = metabolic_form.save(commit=False)
            metabolic.trainer_id = trainer_id
            metabolic2 = metabolic_form2.save()
            metabolic.metabolic2 = metabolic2
            metabolic.save()
            messages.success(request, message='Kayıt Başaraılı')
            return redirect('trainer-metabolic-exercise-home')
        else:
            messages.warning(request, 'İşlem başarısız')
            print('*****************************Metabolic******************************************************')
            print(metabolic_form.errors)
            print('*****************************Metabolic 2******************************************************')
            print(metabolic_form2.errors)
    context = {
        'action': 'create',
        'metabolic': metabolic,
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_metabolic_exercise_delete(request, id):
    metabolic = get_object_or_404(Metabolic, id=id)
    ps_id = metabolic.personal_id
    metabolic2 = Metabolic2.objects.get(id=metabolic.metabolic2.id)
    metabolic2.delete()
    metabolic.delete()
    return redirect('trainer-metabolic-exercise-results', id=ps_id)


def corporate_metabolic_exercise_delete(request, id):
    metabolic = get_object_or_404(Metabolic, id=id)
    crp_id = metabolic.personal_id
    metabolic2 = Metabolic2.objects.get(id=metabolic.metabolic2.id)
    metabolic2.delete()
    metabolic.delete()
    return redirect('corporate-metabolic-exercise-results', id=crp_id)


def personal_metbolic_exercise_delete(request, id):
    metabolic = get_object_or_404(Metabolic, id=id)
    metabolic2 = Metabolic2.objects.get(id=metabolic.metabolic2.id)
    metabolic2.delete()
    metabolic.delete()
    return redirect('personal-metabolic-exercise-results')
