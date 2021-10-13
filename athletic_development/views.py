from django.shortcuts import render

# Create your views here.
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
    template = trainer_template_name + 'athletic_development/athletic_development.html'

    context = {
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)



