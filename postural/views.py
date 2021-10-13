from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from postural.constant import POSTURAL
from postural.forrms import PosturalForm
from postural.models import PosturInputs
from registration.forms import CustomUserRegistrationForm
from registration.models import Corporate, Trainer, Personal
from registration.views import user_checking

trainer_content_template_path = 'modules/trainer_content/measurements/'
corporate_content_template_path = 'modules/corporate_content/measurements/'


# Corporate Views
def corporate_postural_home(request):
    user = request.user
    template = corporate_content_template_path + 'postural/postural.html'

    user_control = user_checking(user.id)
    context = {

        'user_control_data': user_control,
    }
    return render(request=request, template_name=template, context=context)


def corporate_postural_create(request):
    user = request.user
    user_control_data = user_checking(user.id)

    template = corporate_content_template_path + 'postural/postural_form.html'

    context = {

        'user_control_data': user_control_data,

    }
    return render(request=request, template_name=template, context=context)


# Trainer Views
def trainer_postural_home(request):
    user = request.user
    template = trainer_content_template_path + 'postural/postural.html'

    user_control = user_checking(user.id)
    context = {

        'user_control_data': user_control,
    }
    return render(request=request, template_name=template, context=context)


def trainer_postural_create(request):
    user = request.user
    postural = POSTURAL
    user_control_data = user_checking(user.id)
    trainer_id = user_control_data['trainer_info'].id
    personal_data = Personal.objects.filter(trainer_id=trainer_id).all()
    template = trainer_content_template_path + 'postural/postural_form.html'
    if request.method == 'POST':
        postural_form = PosturalForm(request.POST, request.FILES)
        if postural_form.is_valid():
            postural = postural_form.save(commit=False)
            postural.trainer_id = trainer_id
            postural.save()
            messages.success(request, message='Kayıt Başaraılı')
            return redirect('trainer-postural-create')
        else:
            messages.success(request, message="İşlem Başarısız")
            print("------------------------------------------------")
            print(postural_form.errors)
            print("------------------------------------------------")
    else:
        postural_form = PosturalForm()

    context = {
        'action': 'create',
        'posturals': postural,
        'postural_form': postural_form,
        'user_control_data': user_control_data,
        'personals': personal_data,
    }
    return render(request=request, template_name=template, context=context)



def trainer_postural_delete(request, id):
    postural = get_object_or_404(PosturInputs, id=id)
    ps_id = postural.personal_id
    postural.delete()
    return redirect('trainer-measurements-postural-results-home', id=ps_id)


def corporate_postural_delete(request, id):
    postural = get_object_or_404(PosturInputs, id=id)
    crp_id = postural.personal_id
    postural.delete()
    return redirect('corporate-measurements-postural-results-home', id=crp_id)


def personal_postural_delete(request, id):
    postural = get_object_or_404(PosturInputs, id=id)
    postural.delete()
    return redirect('personal-measurements-postural-home')