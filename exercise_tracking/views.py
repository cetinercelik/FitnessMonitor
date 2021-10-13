from django.shortcuts import render

# Create your views here.
from registration.views import user_checking

corporate_content_template_path = 'modules/corporate_content/prescriptions/'
trainer_content_template_path = 'modules/trainer_content/prescriptions/'


def corporate_exercise_tracking_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    template = corporate_content_template_path + 'exercise_tracking/exercise_tracking.html'
    context = {
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)

def trainer_exercise_tracking_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    template = trainer_content_template_path + 'exercise_tracking/exercise_tracking.html'
    context = {
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)
