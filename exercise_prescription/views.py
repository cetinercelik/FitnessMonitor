from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from exercise_prescription.constant import EXERCISE
from exercise_prescription.forms import Exercise_prescriptionForm, exercise_prescription_levelForm, \
    exercise_prescripion_chestForm, exercise_prescription_shoulderForm, exercise_prescription_backForm, \
    exercise_prescription_bisepsForm, exercise_prescription_trisepsForm, exercise_prescription_glutealForm, \
    exercise_prescription_kuadrisepsForm, exercise_prescription_hamstringForm, exercise_prescription_gastrocnemiusForm, \
    exercise_prescription_coreForm
from exercise_prescription.models import exercise_prescription, exercise_prescription_level, exercise_prescripion_chest, \
    exercise_prescription_shoulder, exercise_prescription_back, exercise_prescription_biseps, \
    exercise_prescription_triseps, exercise_prescription_gluteal, exercise_prescription_kuadriseps, \
    exercise_prescription_hamstring, exercise_prescription_gastrocnemius
from registration.models import Personal
from registration.views import user_checking

corp_template_name = 'modules/corporate_content/prescriptions/'
trainer_template_name = 'modules/trainer_content/prescriptions/'


def corporate_exercise_prescription_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    template = corp_template_name + 'exercise_prescription/exercise_prescription.html'
    context = {
        'user_control_data': user_control_data,
    }

    return render(request=request, template_name=template, context=context)


def corporate_exercise_prescription_create(request):
    user = request.user
    user_control_data = user_checking(user.id)
    template = corp_template_name + 'exercise_prescription/exercise_prescription_form.html'

    context = {

        'user_control_data': user_control_data,
    }

    return render(request=request, template_name=template, context=context)


def trainer_exercise_prescription_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    template = trainer_template_name + 'exercise_prescription/exercise_prescription.html'
    context = {
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_exercise_prescription_create(request):
    user = request.user
    exercise_constant = EXERCISE
    user_control_data = user_checking(user.id)
    trainer_id = user_control_data['trainer_info'].id
    personal_data = Personal.objects.filter(trainer_id=trainer_id)
    template = trainer_template_name + 'exercise_prescription/exercise_prescription_form.html'
    if request.method == 'POST':
        exercise_form = Exercise_prescriptionForm(request.POST)
        levelForm = exercise_prescription_levelForm(request.POST)
        chestForm = exercise_prescripion_chestForm(request.POST)
        shoulderForm = exercise_prescription_shoulderForm(request.POST)
        backForm = exercise_prescription_backForm(request.POST)
        bisepsForm = exercise_prescription_bisepsForm(request.POST)
        trisepsForm = exercise_prescription_trisepsForm(request.POST)
        glutealForm = exercise_prescription_glutealForm(request.POST)
        kuadrisepsForm = exercise_prescription_kuadrisepsForm(request.POST)
        hamstringForm = exercise_prescription_hamstringForm(request.POST)
        gastrocnemiusForm = exercise_prescription_gastrocnemiusForm(request.POST)
        coreForm = exercise_prescription_coreForm(request.POST)
        if exercise_form.is_valid() and levelForm.is_valid() and chestForm.is_valid() and shoulderForm.is_valid() and backForm.is_valid() and bisepsForm.is_valid() and trisepsForm.is_valid() and glutealForm.is_valid() and kuadrisepsForm.is_valid() and hamstringForm.is_valid() and gastrocnemiusForm.is_valid() and coreForm.is_valid():
            exercise = exercise_form.save(commit=False)
            exercise.trainer_id = trainer_id
            level = levelForm.save()
            exercise.level = level
            chest = chestForm.save()
            exercise.chest = chest
            shoulder = shoulderForm.save()
            exercise.shoulder = shoulder
            back = backForm.save()
            exercise.back = back
            biseps = bisepsForm.save()
            exercise.biseps = biseps
            triseps = trisepsForm.save()
            exercise.triseps = triseps
            gluteal = glutealForm.save()
            exercise.gluteal = gluteal
            kuadriseps = kuadrisepsForm.save()
            exercise.kuadriseps = kuadriseps
            hamstring = hamstringForm.save()
            exercise.hamstring = hamstring
            gastrocnemius = gastrocnemiusForm.save()
            exercise.gastrocnemius = gastrocnemius
            core = coreForm.save()
            exercise.core = core
            exercise.save()
            messages.success(request, message='Kayıt Başaraılı')
            return redirect('trainer-exercise_prescription-home')
        else:
            messages.warning(request, 'İşlem başarısız.')
            print('**********************************exercise_form*************************************************')
            print(exercise_form.errors)
            print('*****************************levelForm*****************************************************')
            print(levelForm.errors)
            print('*****************************chestForm*****************************************************')
            print(chestForm.errors)
            print('*****************************shoulderForm*****************************************************')
            print(shoulderForm.errors)
            print('*****************************backForm*****************************************************')
            print(backForm.errors)
            print('*****************************bisepsForm*****************************************************')
            print(bisepsForm.errors)
            print('*****************************trisepsForm*****************************************************')
            print(trisepsForm.errors)
            print('*****************************glutealForm*****************************************************')
            print(glutealForm.errors)
            print('*****************************kuadrisepsForm*****************************************************')
            print(kuadrisepsForm.errors)
            print('*****************************hamstringForm*****************************************************')
            print(hamstringForm.errors)
            print('*****************************gastrocnemiusForm*****************************************************')
            print(gastrocnemiusForm.errors)
            print('*****************************coreForm*****************************************************')
            print(coreForm.errors)
    else:
        exercise_form = Exercise_prescriptionForm()
    context = {
        'action': 'create',
        'exercise': exercise_constant,
        'exercise_form': exercise_form,
        'user_control_data': user_control_data,
        'personals': personal_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_exercise_prescription_delete(request, id):
    exercise = get_object_or_404(exercise_prescription, id=id)
    ps_id = exercise.personal_id
    level = exercise_prescription_level.objects.get(id=id)
    chest = exercise_prescripion_chest.objects.get(id=id)
    shoulder = exercise_prescription_shoulder.objects.get(id=id)
    back = exercise_prescription_back.objects.get(id=id)
    biseps = exercise_prescription_biseps.objects.get(id=id)
    triseps = exercise_prescription_triseps.objects.get(id=id)
    gluteal = exercise_prescription_gluteal.objects.get(id=id)
    kuadriseps = exercise_prescription_kuadriseps.objects.get(id=id)
    hamstring = exercise_prescription_hamstring.objects.get(id=id)
    gastrocnemius = exercise_prescription_gastrocnemius.objects.get(id=id)
    level.delete()
    chest.delete()
    shoulder.delete()
    back.delete()
    biseps.delete()
    triseps.delete()
    gluteal.delete()
    kuadriseps.delete()
    hamstring.delete()
    gastrocnemius.delete()
    exercise.delete()
    return redirect('trainer-prescriptions-exercise-prescription-results', id=ps_id)


def corporate_exercise_prescription_delete(request, id):
    exercise = get_object_or_404(exercise_prescription, id=id)
    crp_id = exercise.personal_id
    level = exercise_prescription_level.objects.get(id=id)
    chest = exercise_prescripion_chest.objects.get(id=id)
    shoulder = exercise_prescription_shoulder.objects.get(id=id)
    back = exercise_prescription_back.objects.get(id=id)
    biseps = exercise_prescription_biseps.objects.get(id=id)
    triseps = exercise_prescription_triseps.objects.get(id=id)
    gluteal = exercise_prescription_gluteal.objects.get(id=id)
    kuadriseps = exercise_prescription_kuadriseps.objects.get(id=id)
    hamstring = exercise_prescription_hamstring.objects.get(id=id)
    gastrocnemius = exercise_prescription_gastrocnemius.objects.get(id=id)
    level.delete()
    chest.delete()
    shoulder.delete()
    back.delete()
    biseps.delete()
    triseps.delete()
    gluteal.delete()
    kuadriseps.delete()
    hamstring.delete()
    gastrocnemius.delete()
    exercise.delete()
    return redirect('corporate-exercise-prescription-results-home', id=crp_id)


def personal_exercise_prescription_delete(request, id):
    exercise = get_object_or_404(exercise_prescription, id=id)
    level = exercise_prescription_level.objects.get(id=exercise.level.id)
    chest = exercise_prescripion_chest.objects.get(id=exercise.chest.id)
    shoulder = exercise_prescription_shoulder.objects.get(id=exercise.shoulder.id)
    back = exercise_prescription_back.objects.get(id=exercise.back)
    biseps = exercise_prescription_biseps.objects.get(id=exercise.biseps.id)
    triseps = exercise_prescription_triseps.objects.get(id=exercise.triseps.id)
    gluteal = exercise_prescription_gluteal.objects.get(id=exercise.gluteal.id)
    kuadriseps = exercise_prescription_kuadriseps.objects.get(id=exercise.kuadriseps.id)
    hamstring = exercise_prescription_hamstring.objects.get(id=exercise.hamstring.id)
    gastrocnemius = exercise_prescription_gastrocnemius.objects.get(id=exercise.gastrocnemius.id)
    level.delete()
    chest.delete()
    shoulder.delete()
    back.delete()
    biseps.delete()
    triseps.delete()
    gluteal.delete()
    kuadriseps.delete()
    hamstring.delete()
    gastrocnemius.delete()
    exercise.delete()
    return redirect('personal-prescriptions-exercise-prescription-home')
