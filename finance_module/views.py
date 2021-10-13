from django.shortcuts import render

# Create your views here.
from registration.models import Trainer, Personal
from registration.views import user_checking

corporate_content_template_path = 'modules/corporate_content/analyzes/'
trainer_content_template_path = 'modules/trainer_content/analyzes/'
personal_content_template_path = 'modules/personel_content/analyzes/'


def corporate_finance_module_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    corporate_id = user_control_data['corporate_info'].id
    trainers_data = Trainer.objects.filter(corporate_id=corporate_id)
    trainer_ids = [trainers.id for trainers in trainers_data]
    personal_data = Personal.objects.filter(trainer_id__in=trainer_ids).all()
    template = corporate_content_template_path + 'finance_module/finance_module.html'

    context = {
        'personals': personal_data,
        'trainers': trainers_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_finance_module_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    trainers_data = Trainer.objects.filter().all()
    trainer_ids = [trainers.id for trainers in trainers_data]
    personal_data = Personal.objects.filter(trainer_id__in=trainer_ids).all()
    template = trainer_content_template_path + 'finance_module/finance_module.html'

    context = {
        'personals': personal_data,
        'trainers': trainers_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def personal_finance_module_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    personal_data = Personal.objects.filter().all()
    template = personal_content_template_path + 'finance_module/finance_module.html'

    context = {
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)
