from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from athletic_development.forms import AthleticDevForm
from athletic_development.models import athDev_mainTitle, athleticDev_subTitle, athletticDev_inputs, ath_property
from registration.forms import CustomUserRegistrationForm
from registration.models import Personal
from registration.views import user_checking

corp_template_name = 'modules/corporate_content/prescriptions/'
trainer_template_name = 'modules/trainer_content/prescriptions/'


def corporate_athletic_development_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    template = corp_template_name + 'athletic_development/athletic_development.html'

    context = {
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_athletic_development_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    trainer_id = user_control_data['trainer_info'].id
    personal_data = Personal.objects.filter(trainer_id=trainer_id).all()
    template = trainer_template_name + 'athletic_development/athletic_development.html'

    context = {
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_athltc_dvlpmnt_create_home(request):
    user = request.user
    user_control = user_checking(user.id)
    template = trainer_template_name + 'athletic_development/athletic_development_form.html'
    trainer_id = user_control['trainer_info'].id
    personal_data = Personal.objects.filter(trainer_id=trainer_id).all()
    athMainTitle = athDev_mainTitle.objects.all()
    athSubTitle = athleticDev_subTitle.objects.all()
    athInput = ath_property.objects.all()

    context = {
        'action': 'create',
        'maintitles': athMainTitle,
        'subtitles': athSubTitle,
        'athinputs': athInput,
        'personals': personal_data,
        'user_control_data': user_control,
    }
    return render(request=request, template_name=template, context=context)


def trainer_athletic_development_create(request):
    user = request.user
    user_control = user_checking(user.id)
    trainer_id = user_control['trainer_info'].id
    if request.method == 'POST':
        athleticDev_form = AthleticDevForm(request.POST)
        if athleticDev_form.is_valid():
            inputsname = request.POST['inputsname']
            sub_id = request.POST['sub_id']
            personal_id = request.POST['personal_id']
            new_forms = athleticDev_form.save(commit=False)
            new_forms.inputs_name = inputsname
            new_forms.trainer_id = trainer_id
            new_forms.personal_id = personal_id
            new_forms.subtitle_id = sub_id
            new_forms.save()
            messages.success(request, message='Kayıt Başarılı')
            print('--------------------************Başarılı*******--------------------------')
        else:
            messages.warning(request, 'İşlem Başarısız')
            print('--------------- ----************Başarısız*******--------------------------')
            print(athleticDev_form.errors)

        return redirect('trainer-athletic-development-home-create')
