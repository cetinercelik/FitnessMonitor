from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from corrective_exercise.constant import CORRECTIVE
from corrective_exercise.forms import Corrective_exercise, Corrective_exercise2, Corrective_exercise3, \
    Corrective_exercise4
from corrective_exercise.models import corrective_exercise, corrective_exercise2, corrective_exercise3, \
    corrective_exercise4
from registration.models import Personal
from registration.views import user_checking

corporate_cor_exercise_path = 'modules/corporate_content/prescriptions/'
trainer_cor_exercise_path = 'modules/trainer_content/prescriptions/'


def cororate_cor_exercise_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    template = corporate_cor_exercise_path + 'corrective_exercise/corrective_exercise.html'

    context = {
        'user_control_data': user_control_data
    }
    return render(request=request, template_name=template, context=context)


def corporate_cor_exercise_create(request):
    user = request.user
    user_control_data = user_checking(user.id)
    template = corporate_cor_exercise_path + 'corrective_exercise/corrective_exercise_form.html'

    context = {
        'user_control_data': user_control_data
    }
    return render(request=request, template_name=template, context=context)


def trainer_cor_exercise_home(request):
    user = request.user
    template = trainer_cor_exercise_path + 'corrective_exercise/corrective_exercise.html'
    user_control_data = user_checking(user.id)
    context = {
        'user_control_data': user_control_data
    }
    return render(request=request, template_name=template, context=context)


def trainer_cor_exercise_create(request):
    user = request.user
    corrective_constant = CORRECTIVE
    user_control_data = user_checking(user.id)
    trainer_id = user_control_data['trainer_info'].id
    personal_data = Personal.objects.filter(trainer_id=trainer_id)
    template = trainer_cor_exercise_path + 'corrective_exercise/corrective_exercise_form.html'
    if request.method == 'POST':
        corrective_form = Corrective_exercise(request.POST)
        corrective_form2 = Corrective_exercise2(request.POST)
        corrective_form3 = Corrective_exercise3(request.POST)
        corrective_form4 = Corrective_exercise4(request.POST)
        if corrective_form.is_valid() and corrective_form2.is_valid() and corrective_form3.is_valid() and corrective_form4.is_valid():
            corrective1 = corrective_form.save(commit=False)
            corrective1.trainer_id = trainer_id
            corrective2 = corrective_form2.save()
            corrective1.corrective2 = corrective2
            corrective3 = corrective_form3.save()
            corrective1.corrective3 = corrective3
            corrective4 = corrective_form4.save()
            corrective1.corrective4 = corrective4
            corrective1.save()
            messages.success(request, message='Kayıt Başarılı')
            return redirect('trainer-corrective_exercise-home')
        else:
            messages.warning(request, 'İşlem başarısız.')
            print('****************************Form*****************************')
            print(corrective_form.errors)
            print('****************************Form2*****************************')
            print(corrective_form2.errors)
            print('****************************Form3*****************************')
            print(corrective_form3.errors)
            print('****************************Form4*****************************')
            print(corrective_form4.errors)
    else:
        corrective_form = Corrective_exercise()
    context = {
        'action': 'create',
        'corrective': corrective_constant,
        'corrective_form': corrective_form,
        'user_control_data': user_control_data,
        'personals': personal_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_corrective_exercise_delete(request, id):
    corrective = get_object_or_404(corrective_exercise, id=id)
    ps_id = corrective.personal_id
    corrective2 = corrective_exercise2.objects.get(id=corrective.corrective2.id)
    corrective3 = corrective_exercise3.objects.get(id=corrective.corrective3.id)
    corrective4 = corrective_exercise4.objects.get(id=corrective.corrective4.id)
    corrective2.delete()
    corrective3.delete()
    corrective4.delete()
    corrective.delete()
    return redirect('trainer-prescriptions-corrective-exercise-results', id=ps_id)


def corporate_corrective_exercise_delete(request, id):
    corrective = get_object_or_404(corrective_exercise, id=id)
    crp_id = corrective.personal_id
    corrective2 = corrective_exercise2.objects.get(id=corrective.corrective2.id)
    corrective3 = corrective_exercise3.objects.get(id=corrective.corrective3.id)
    corrective4 = corrective_exercise4.objects.get(id=corrective.corrective4.id)
    corrective2.delete()
    corrective3.delete()
    corrective4.delete()
    corrective.delete()
    return redirect('corporate-prescriptions-corrective-exercise-results-home', id=crp_id)


def personal_corrective_exercise_delete(request, id):
    corrective = get_object_or_404(corrective_exercise, id=id)
    corrective2 = corrective_exercise2.objects.get(id=corrective.corrective2.id)
    corrective3 = corrective_exercise3.objects.get(id=corrective.corrective3.id)
    corrective4 = corrective_exercise4.objects.get(id=corrective.corrective4.id)
    corrective2.delete()
    corrective3.delete()
    corrective4.delete()
    corrective.delete()
    return redirect('personal-prescriptions-corrective-exercise-home')
