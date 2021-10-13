from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
import medical_exercise
from medical_exercise.constant import MEDICAL_EXERCISE
from medical_exercise.forms import MedicalExerciseForm1, MedicalExerciseForm2, MedicalExerciseForm3, \
    MedicalExerciseForm4, MedicalExerciseForm5, MedicalExerciseForm6, MedicalExerciseForm7, MedicalExerciseForm8, \
    MedicalExerciseForm9, MedicalExerciseForm10, MedicalExerciseForm11, MedicalExerciseForm12, MedicalExerciseForm13
from medical_exercise.models import medical_exercise1, medical_exercise2, medical_exercise3, medical_exercise5, \
    medical_exercise6, medical_exercise7, medical_exercise4, medical_exercise8, medical_exercise9, medical_exercise10, \
    medical_exercise11, medical_exercise12, medical_exercise13
from registration.models import Personal
from registration.views import user_checking

corporate_content_template_path = 'modules/corporate_content/prescriptions/'
trainer_content_template_path = 'modules/trainer_content/prescriptions/'


def corporate_medical_exercise(request):
    user = request.user
    user_control_data = user_checking(user.id)
    template = corporate_content_template_path + 'medical_exercise/medical_exercise.html'
    context = {
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_medical_exercise(request):
    user = request.user
    user_control_data = user_checking(user.id)
    trainer_id = user_control_data['trainer_info'].id
    personal_data = Personal.objects.filter(trainer_id=trainer_id).all()
    template = trainer_content_template_path + 'medical_exercise/medical_exercise.html'
    context = {
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_medical_exercise_create_home(request):
    user = request.user
    md = MEDICAL_EXERCISE
    user_control_data = user_checking(user.id)
    trainer_id = user_control_data['trainer_info'].id
    personal_data = Personal.objects.filter(trainer_id=trainer_id).all()
    template = trainer_content_template_path + 'medical_exercise/medical_exercise_form.html'
    context = {
        'medical_exercise': md,
        'personals': personal_data,
        'user_control_data': user_control_data
    }
    return render(request=request, template_name=template, context=context)


def trainer_medical_exercise_create1(request):
    user = request.user
    user_control_data = user_checking(user.id)
    trainer_id = user_control_data['trainer_info'].id
    print('***********************************Giriş************************************************')
    if request.method == 'POST':
        print('***********************************Başarılı************************************************')
        md_form1 = MedicalExerciseForm1(request.POST)
        md_form2 = MedicalExerciseForm2(request.POST)
        md_form3 = MedicalExerciseForm3(request.POST)
        md_form4 = MedicalExerciseForm4(request.POST)
        md_form5 = MedicalExerciseForm5(request.POST)
        md_form6 = MedicalExerciseForm6(request.POST)
        md_form7 = MedicalExerciseForm7(request.POST)
        md_form8 = MedicalExerciseForm8(request.POST)
        md_form9 = MedicalExerciseForm9(request.POST)
        md_form10 = MedicalExerciseForm10(request.POST)
        md_form11 = MedicalExerciseForm11(request.POST)
        md_form12 = MedicalExerciseForm12(request.POST)
        md_form13 = MedicalExerciseForm13(request.POST)
        if md_form1.is_valid() and md_form2.is_valid() and md_form3.is_valid() and md_form4.is_valid() and md_form5.is_valid() and md_form6.is_valid() and md_form7.is_valid() and md_form8.is_valid() and md_form9.is_valid() and md_form10.is_valid() and md_form11.is_valid() and md_form12.is_valid() and md_form13.is_valid():
            medical1 = md_form1.save(commit=False)
            medical1.trainer_id = trainer_id
            medical2 = md_form2.save()
            medical1.medical2 = medical2
            medical3 = md_form3.save()
            medical1.medical3 = medical3
            medical4 = md_form4.save()
            medical1.medical4 = medical4
            medical5 = md_form5.save()
            medical1.medical5 = medical5
            medical6 = md_form6.save()
            medical1.medical6 = medical6
            medical7 = md_form7.save()
            medical1.medical7 = medical7
            medical8 = md_form8.save()
            medical1.medical8 = medical8
            medical9 = md_form9.save()
            medical1.medical9 = medical9
            medical10 = md_form10.save()
            medical1.medical10 = medical10
            medical11 = md_form11.save()
            medical1.medical11 = medical11
            medical12 = md_form12.save()
            medical1.medical12 = medical12
            medical13 = md_form13.save()
            medical1.medical13 = medical13
            medical1.save()
            messages.success(request, message='Kayıt Başaraılı')
            return redirect('trainer-medical-exercise-home')
        else:
            messages.warning(request, 'İşlem başarısız')
            print('********************************md_form1***************************************************')
            print(md_form1.errors)
            print('********************************md_form2***************************************************')
            print(md_form2.errors)
            print('********************************md_form3***************************************************')
            print(md_form3.errors)
            print('********************************md_form4***************************************************')
            print(md_form4.errors)
            print('********************************md_form5***************************************************')
            print(md_form5.errors)
            print('********************************md_form6***************************************************')
            print(md_form6.errors)
            print('********************************md_form7***************************************************')
            print(md_form7.errors)
            print('********************************md_form8***************************************************')
            print(md_form8.errors)
            print('********************************md_form9***************************************************')
            print(md_form9.errors)
            print('********************************md_form10***************************************************')
            print(md_form10.errors)
            print('********************************md_form11***************************************************')
            print(md_form11.errors)
            print('********************************md_form12***************************************************')
            print(md_form12.errors)
            print('********************************md_form13***************************************************')
            print(md_form13.errors)
    return redirect('trainer-medical-exercise-home')


def trainer_medical_exercise1_delete(request, id):
    medical = get_object_or_404(medical_exercise1, id=id)
    ps_id = medical.personal_id
    medical2 = medical_exercise2.objects.get(id=medical.medical2.id)
    medical2.delete()
    medical3 = medical_exercise3.objects.get(id=medical.medical3.id)
    medical3.delete()
    medical4 = medical_exercise4.objects.get(id=medical.medical4.id)
    medical4.delete()
    medical5 = medical_exercise5.objects.get(id=medical.medical5.id)
    medical5.delete()
    medical6 = medical_exercise6.objects.get(id=medical.medical6.id)
    medical6.delete()
    medical7 = medical_exercise7.objects.get(id=medical.medical7.id)
    medical7.delete()
    medical8 = medical_exercise8.objects.get(id=medical.medical8.id)
    medical8.delete()
    medical9 = medical_exercise9.objects.get(id=medical.medical9.id)
    medical9.delete()
    medical10 = medical_exercise10.objects.get(id=medical.medical10.id)
    medical10.delete()
    medical11 = medical_exercise11.objects.get(id=medical.medical11.id)
    medical11.delete()
    medical12 = medical_exercise12.objects.get(id=medical.medical12.id)
    medical12.delete()
    medical13 = medical_exercise13.objects.get(id=medical.medical13.id)
    medical13.delete()
    medical.delete()
    return redirect('trainer-prescriptions-medical-exercise-results', id=ps_id)


def corporate_medical_exercise1_delete(request, id):
    medical = get_object_or_404(medical_exercise1, id=id)
    crp_id = medical.personal_id
    medical2 = medical_exercise2.objects.get(id=medical.medical2.id)
    medical2.delete()
    medical3 = medical_exercise3.objects.get(id=medical.medical3.id)
    medical3.delete()
    medical4 = medical_exercise4.objects.get(id=medical.medical4.id)
    medical4.delete()
    medical5 = medical_exercise5.objects.get(id=medical.medical5.id)
    medical5.delete()
    medical6 = medical_exercise6.objects.get(id=medical.medical6.id)
    medical6.delete()
    medical7 = medical_exercise7.objects.get(id=medical.medical7.id)
    medical7.delete()
    medical8 = medical_exercise8.objects.get(id=medical.medical8.id)
    medical8.delete()
    medical9 = medical_exercise9.objects.get(id=medical.medical9.id)
    medical9.delete()
    medical10 = medical_exercise10.objects.get(id=medical.medical10.id)
    medical10.delete()
    medical11 = medical_exercise11.objects.get(id=medical.medical11.id)
    medical11.delete()
    medical12 = medical_exercise12.objects.get(id=medical.medical12.id)
    medical12.delete()
    medical13 = medical_exercise13.objects.get(id=medical.medical13.id)
    medical13.delete()
    medical.delete()
    return redirect('corporate-prescriptions-medical-exercise-results', id=crp_id)


def personal_medical_exercise1_delete(request, id):
    medical = get_object_or_404(medical_exercise1, id=id)
    medical2 = medical_exercise2.objects.get(id=medical.medical2.id)
    medical2.delete()
    medical3 = medical_exercise3.objects.get(id=medical.medical3.id)
    medical3.delete()
    medical4 = medical_exercise4.objects.get(id=medical.medical4.id)
    medical4.delete()
    medical5 = medical_exercise5.objects.get(id=medical.medical5.id)
    medical5.delete()
    medical6 = medical_exercise6.objects.get(id=medical.medical6.id)
    medical6.delete()
    medical7 = medical_exercise7.objects.get(id=medical.medical7.id)
    medical7.delete()
    medical8 = medical_exercise8.objects.get(id=medical.medical8.id)
    medical8.delete()
    medical9 = medical_exercise9.objects.get(id=medical.medical9.id)
    medical9.delete()
    medical10 = medical_exercise10.objects.get(id=medical.medical10.id)
    medical10.delete()
    medical11 = medical_exercise11.objects.get(id=medical.medical11.id)
    medical11.delete()
    medical12 = medical_exercise12.objects.get(id=medical.medical12.id)
    medical12.delete()
    medical13 = medical_exercise13.objects.get(id=medical.medical13.id)
    medical13.delete()
    medical.delete()
    return redirect('personal-prescriptions-medical-exercise-home')
