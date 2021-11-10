from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.urls import reverse_lazy

from registration.forms import PersonalForm, CorporateForm, CustomUserRegistrationForm, CustomUserChangeForm, \
    TrainerForm
from registration.models import Personal, Corporate, Trainer

personal_template_path = 'registration/personal/'
corporate_template_path = 'registration/corporate/'
trainer_template_path = 'registration/trainer/'


# Kullanıcı kontrol alanı
def user_checking(user_id):
    corporate = Corporate.objects.filter(user_id=user_id).first()
    trainer = Trainer.objects.filter(user_id=user_id).first()
    personal = Personal.objects.filter(user_id=user_id).first()
    check_data = {
        'corporate_info': corporate,
        'trainer_info': trainer,
        'personal_info': personal,
        'corporate_c': False,
        'trainer_c': False,
        'personal_c': False,
    }

    if corporate:
        check_data['corporate_c'] = True
    elif trainer:
        check_data['trainer_c'] = True
    elif personal:
        check_data['personal_c'] = True
    return check_data


# Kişisel kayıt alnı Başlangıç
def personal_home(request):
    user = request.user
    template = personal_template_path + 'personal.html'
    personal_data = Personal.objects.all()
    user_control_data = user_checking(user.id)
    context = {
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


# Kişisel kayıt alanı bitiş


# Antrenör kayıt işlemleri başlangıç
def trainer_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    template = trainer_template_path + 'trainer.html'
    id = user_control_data['trainer_info'].id
    trainer_data = Trainer.objects.all()
    context = {
        'trainers': trainer_data,
        'user_control_data': user_control_data
    }
    return render(request=request, template_name=template, context=context)


# Trainer personal Home
def trainer_personal_home(request):
    user = request.user
    template = trainer_template_path + 'trainer-personal/trainer_personal.html'
    user_control_data = user_checking(user.id)
    trainer_id = user_control_data['trainer_info'].id
    personal_data = Personal.objects.filter(trainer_id=trainer_id).all()
    context = {
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


# Trainer personal creat
def trainer_personal_create(request):
    user = request.user
    user_control_data = user_checking(user.id)
    trainer_id = user_control_data['trainer_info'].id
    template = trainer_template_path + 'trainer-personal/trainer_personal_create.html'
    if request.method == 'POST':
        trainer_personal_form = PersonalForm(request.POST, request.FILES)
        user_registration_form = CustomUserRegistrationForm(request.POST)
        if trainer_personal_form.is_valid() and user_registration_form.is_valid():
            user = user_registration_form.save()
            personal = trainer_personal_form.save(commit=False)
            personal.trainer_id = trainer_id
            personal.user = user
            personal.save()
            messages.success(request, message='Kayıt Başarılı')
            return redirect('trainer-personal-home')
        else:
            messages.warning(request, message='İşlem başarısız')
    else:
        trainer_personal_form = PersonalForm()
        user_registration_form = CustomUserRegistrationForm()
    context = {
        'action': 'create',
        'form_personal': trainer_personal_form,
        'form2': user_registration_form,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


def trainer_personal_update(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    trainer_id = user_control_data['trainer_info'].id
    template = trainer_template_path + 'trainer-personal/trainer_personal_create.html'
    personal = get_object_or_404(Personal, id=id)
    if request.method == 'POST':
        if personal.avatar:
            personal.avatar.delete()
        trainer_personal_form = PersonalForm(request.POST, request.FILES, instance=personal)
        user_change_form = CustomUserChangeForm(request.POST, instance=personal.user)
        if trainer_personal_form.is_valid() and user_change_form.is_valid():
            user = user_change_form.save()
            trainer_personal = trainer_personal_form.save(commit=False)
            trainer_personal.trainer_id = trainer_id
            trainer_personal.user = user
            trainer_personal.save()
            messages.success(request, message='Güncelleme İşlemi Başarılı')
            return redirect('trainer-personal-home')
        else:
            messages.warning(request, message='Güncelleme İşlemi Başarısız')
    else:
        trainer_personal_form = PersonalForm(instance=personal)
        user_change_form = CustomUserChangeForm(instance=personal.user)
    context = {
        'model_id': id,
        'action': 'update',
        'form_personal': trainer_personal_form,
        'form2': user_change_form,
        'user_control_data': user_control_data,

    }
    return render(request=request, template_name=template, context=context)


def trainer_personal_delete(request, id):
    personal = get_object_or_404(Personal, id=id)
    if personal.avatar:
        personal.avatar.delete()
    personal.delete()
    personal.user.delete()
    return redirect('trainer-personal-home')


# Antrenör kayıt işlemaleri bitiş

# Kurumsal kayıt alanı
def corporate_home(request):
    user = request.user
    template = corporate_template_path + 'corporate.html'
    corporate_data = Corporate.objects.all()
    user_control_data = user_checking(user.id)
    corporate_id = user_control_data['corporate_info'].id
    trainer_data = Trainer.objects.filter(corporate_id=corporate_id)
    trainer_ids = [trainer.id for trainer in trainer_data]
    personal_data = Personal.objects.filter(trainer_id__in=trainer_ids).all()
    context = {
        'corporates': corporate_data,
        'trainers': trainer_data,
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


# Kurumsalın altındaki antrenörlerin ekleme alanı
def corporate_trainer_home(request):
    user = request.user
    user_control_data = user_checking(user.id)
    corporate_id = user_control_data['corporate_info'].id
    trainer_data = Trainer.objects.filter(corporate_id=corporate_id).all()
    template = corporate_template_path + 'corporate-trainer/corporate_trainer.html'
    context = {
        'trainers': trainer_data,
        'user_control_data': user_control_data,
    }

    return render(request=request, template_name=template, context=context)


def corporate_tariner_create(request):
    template = corporate_template_path + 'corporate-trainer/corporate_trainer_create.html'
    user = request.user
    user_control_data = user_checking(user.id)
    corporate_id = user_control_data['corporate_info'].id
    corporate_data = Corporate.objects.all()
    trainer_data = Trainer.objects.all()
    personal_data = Personal.objects.all()
    if request.method == 'POST':
        corporate_trainer_form = TrainerForm(request.POST, request.FILES)
        user_creation_form = CustomUserRegistrationForm(request.POST)
        if corporate_trainer_form.is_valid() and user_creation_form.is_valid():
            user = user_creation_form.save()
            trainer = corporate_trainer_form.save(commit=False)
            trainer.corporate_id = corporate_id
            trainer.user = user
            trainer.save()
            messages.success(request, message='Kayıt Başarılı')
            return redirect('corporate-trainer-home')
        else:
            messages.warning(request, message='İşlem başarısız')
    else:
        corporate_trainer_form = TrainerForm()
        user_creation_form = CustomUserRegistrationForm()
    context = {
        'action': 'create',
        'form_trainer': corporate_trainer_form,
        'form2': user_creation_form,
        'corporates': corporate_data,
        'trainers': trainer_data,
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


# Kurumsalın altındaki antrenörlerin güncelleme alanı
def corporate_trainer_update(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    template = corporate_template_path + 'corporate-trainer/corporate_trainer_create.html'
    trainer = get_object_or_404(Trainer, id=id)
    if request.method == 'POST':
        if trainer.avatar or trainer.cv or trainer.trainer_document or trainer.certificate:  # Antrenör profil resmi ve belgelerinin silindiği yer
            trainer.avatar.delete()
            trainer.cv.delete()
            trainer.trainer_document.delete()
            trainer.certificate.delete()
        corporate_trainer_form = TrainerForm(request.POST, request.FILES, instance=trainer)
        corporate_change_form = CustomUserChangeForm(request.POST, instance=trainer.user)
        if corporate_trainer_form.is_valid() and corporate_change_form.is_valid():
            corporate_change_form.save()
            corporate_trainer_form.save()
            messages.success(request, message='Güncelleme İşlemi Başarılı')
            return redirect('corporate-trainer-home')
        else:
            messages.warning(request, message='Güncelleme İşlemi Başarısız')
    else:
        corporate_trainer_form = TrainerForm(instance=trainer)
        corporate_change_form = CustomUserChangeForm(instance=trainer.user)
    context = {
        'model_id': id,
        'action': 'update',
        'form_trainer': corporate_trainer_form,
        'form2': corporate_change_form,
        'user_control_data': user_control_data
    }
    return render(request=request, template_name=template, context=context)


def corporate_trainer_delete(request, id):
    trainer = get_object_or_404(Trainer, id=id)
    if trainer.avatar or trainer.cv or trainer.trainer_document or trainer.certificate:
        trainer.avatar.delete()
        trainer.cv.delete()
        trainer.trainer_document.delete()
        trainer.certificate.delete()
    trainer.delete()
    return redirect('corporate-trainer-home')


# Kurumsalın altındaki Danışanları görüntüleme,guncelleme ve  ekleme alanı
def corporate_personal_home(request):
    user = request.user
    template = corporate_template_path + 'corporate-personal/corporate_personal.html'
    user_conterol_data = user_checking(user.id)
    corporate_id = user_conterol_data['corporate_info'].id
    trainers_data = Trainer.objects.filter(corporate_id=corporate_id)
    trainer_ids = [trainers.id for trainers in trainers_data]
    personal_data = Personal.objects.filter(trainer_id__in=trainer_ids).all()
    context = {
        'trainers': trainers_data,
        'personals': personal_data,
        'user_control_data': user_conterol_data,
    }
    return render(request=request, template_name=template, context=context)


def corporate_personal_create(request):
    user = request.user
    user_control_data = user_checking(user.id)
    template = corporate_template_path + 'corporate-personal/corporate_personal_create.html'
    corporate_id = user_control_data['corporate_info'].id
    trainer_data = Trainer.objects.filter(corporate_id=corporate_id).all()
    trainer_ids = [trainer.id for trainer in trainer_data]
    personal_data = Personal.objects.filter(trainer_id__in=trainer_ids).all()
    user_control_data = user_checking(user.id)
    if request.method == 'POST':
        corporate_personal_form = PersonalForm(request.POST, request.FILES)
        user_creation_form = CustomUserRegistrationForm(request.POST)
        if corporate_personal_form.is_valid() and user_creation_form.is_valid():
            user = user_creation_form.save()
            personal = corporate_personal_form.save(commit=False)
            personal.user = user
            personal.save()
            messages.success(request, message='Kayıt Başarılı')
            return redirect('corporate-personal-home')
        else:
            messages.warning(request, message='İşlem başarısız')
    else:
        corporate_personal_form = PersonalForm()
        user_creation_form = CustomUserRegistrationForm()
    context = {
        'action': 'create',
        'form': corporate_personal_form,
        'form2': user_creation_form,
        'trainers': trainer_data,
        'personals': personal_data,
        'user_control_data': user_control_data,
    }
    return render(request=request, template_name=template, context=context)


# Kurumsalın altındaki antrenörlerin güncelleme alanı
def corporate_personal_update(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    corporate_id = user_control_data['corporate_info'].id
    template = corporate_template_path + 'corporate-personal/corporate_personal_create.html'
    trainer_data = Trainer.objects.filter(corporate_id=corporate_id).all()
    personal_data = Personal.objects.all()
    personal = get_object_or_404(Personal, id=id)
    if request.method == 'POST':
        corporate_personal_form = PersonalForm(request.POST, request.FILES, instance=personal)
        corporate_change_form = CustomUserChangeForm(request.POST, instance=personal.user)
        if corporate_personal_form.is_valid() and corporate_change_form.is_valid():
            corporate_change_form.save()
            corporate_personal_form.save()
            messages.success(request, message='Güncelleme İşlemi Başarılı')
            return redirect('corporate-personal-home')
        else:
            messages.warning(request, message='Güncelleme İşlemi Başarısız')
    else:
        corporate_personal_form = PersonalForm(instance=personal)
        corporate_change_form = CustomUserChangeForm(instance=personal.user)
    context = {
        'model_id': id,
        'action': 'update',
        'form': corporate_personal_form,
        'form2': corporate_change_form,
        'trainers': trainer_data,
        'personals': personal_data,
        'personal_info': get_object_or_404(Personal, id=id),
        'user_control_data': user_control_data
    }
    return render(request=request, template_name=template, context=context)


def corporate_personal_delete(request, id):
    personal = get_object_or_404(Personal, id=id)
    if personal.avatar:
        personal.avatar.delete()
    personal.delete()
    return redirect('corporate-personal-home')


# Kurumsal alanlarının bitişi


# Bireysel ve kurumsal yeni kayıt alanları
def personal_create_register(request):
    template = 'pages/personal_register.html'
    if request.method == 'POST':
        personal_form = PersonalForm(request.POST, request.FILES)
        user_creation_form = CustomUserRegistrationForm(request.POST)
        if personal_form.is_valid() and user_creation_form.is_valid():
            user = user_creation_form.save()
            personal = personal_form.save(commit=False)
            personal.user = user
            personal.save()
            messages.success(request, message='Kayıt Başarılı')
            return redirect('login')
        else:
            messages.warning(request, message='İşlem başarısız')
    else:
        personal_form = PersonalForm()
        user_creation_form = CustomUserRegistrationForm()
    context = {
        'action': 'create',
        'form': personal_form,
        'form2': user_creation_form,
    }
    return render(request=request, template_name=template, context=context)


# Antrenör yeni kayıt alanı
def trainer_create_register(request):
    template = 'pages/personal_register.html'
    if request.method == 'POST':
        trainer_form = TrainerForm(request.POST, request.FILES)
        user_creation_form = CustomUserRegistrationForm(request.POST)
        if trainer_form.is_valid() and user_creation_form.is_valid():
            user = user_creation_form.save()
            trainer = trainer_form.save(commit=False)
            trainer.user = user
            trainer.save()
            messages.success(request, message='Kayıt Başarılı')
            return redirect('login')
        else:
            messages.warning(request, message='İşlem başarısız')
    else:
        trainer_form = TrainerForm()
        user_creation_form = CustomUserRegistrationForm()
    context = {
        'action': 'create',
        'trainer_form': trainer_form,
        'trainer_user_form': user_creation_form,
    }
    return render(request=request, template_name=template, context=context)


def corporate_create_register(request):
    template = 'pages/personal_register.html'
    if request.method == 'POST':
        corporate_form = CorporateForm(request.POST, request.FILES)
        user_creation_form = CustomUserRegistrationForm(request.POST)
        if corporate_form.is_valid() and user_creation_form.is_valid():
            user = user_creation_form.save()
            corporate = corporate_form.save(commit=False)
            corporate.user = user
            corporate.save()
            messages.success(request, message='Kayıt Başarılı')
            return redirect('home-dashboard')
        else:
            messages.warning(request, message='İşlem başarısız')
    else:
        corporate_form = CorporateForm()
        user_creation_form = CustomUserRegistrationForm()
    context = {
        'action': 'create',
        'corporate_form': corporate_form,
        'corporate_user_form': user_creation_form,
    }
    return render(request=request, template_name=template, context=context)


def personal_settings(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    trainer_id = user_control_data['personal_info'].trainer_id
    template = 'registration/settings/personel_settings/personal_settings.html'
    personel_profil = get_object_or_404(Personal, user_id=id)
    if request.method == 'POST':
        personal_profil_form = PersonalForm(request.POST, request.FILES, instance=personel_profil)
        user_profil_form = CustomUserChangeForm(request.POST, instance=personel_profil.user)
        if personal_profil_form.is_valid() and user_profil_form.is_valid():
            user = user_profil_form.save()
            personal_settings = personal_profil_form.save(commit=False)
            personal_settings.trainer_id = trainer_id
            personal_settings.user = user
            personal_settings.save()
            messages.success(request, message='Güncelleme İşlemi Başarılı')
            return redirect('personal-home')
        else:
            messages.warning(request, message='Güncelleme İşlemi Başarısız')
    else:
        personal_profil_form = PersonalForm(instance=personel_profil)
        user_profil_form = CustomUserChangeForm(instance=personel_profil.user)
    context = {
        'model_id': id,
        'action': 'update',
        'form': personal_profil_form,
        'form2': user_profil_form,
        'user_control_data': user_control_data
    }
    return render(request=request, template_name=template, context=context)


def trainer_settings(request, id):
    user = request.user
    user_control_data = user_checking(user.id)
    template = 'registration/settings/trainer_settings/trainer_setting.html'
    trainer_id = user_control_data['trainer_info'].id
    trainer_data = Trainer.objects.filter(id=id)
    trainer_setting = get_object_or_404(Trainer, user_id=id)
    if request.method == 'POST':
        trainer_setting_form = TrainerForm(request.POST, request.FILES, instance=trainer_setting)
        user_profil_form = CustomUserChangeForm(request.POST, instance=trainer_setting.user)
        if trainer_setting_form.is_valid() and user_profil_form.is_valid():
            user_profil_form.save()
            trainer_setting_form.save()
            messages.success(request, message='Güncelleme İşlemi Başarılı')
            return redirect('trainer-home')
        else:
            messages.warning(request, message='Güncelleme İşlemi Başarısız')
    else:
        trainer_setting_form = TrainerForm(instance=trainer_setting)
        user_profil_form = CustomUserChangeForm(instance=trainer_setting.user)
    context = {
        'model_id': id,
        'action': 'update',
        'trainers': trainer_data,
        'form_tr_setting': trainer_setting_form,
        'form2': user_profil_form,
        'user_control_data': user_control_data,
        'trainer_id': trainer_id,
    }
    return render(request=request, template_name=template, context=context)


def corporate_settings(request, id):
    user = request.user
    template = 'registration/settings/corporate_settings/corp_settings.html'
    corporate_profil = get_object_or_404(Corporate, user_id=id)
    user_control = user_checking(user.id)
    if request.method == 'POST':
        corporate_profil_form = CorporateForm(request.POST, request.FILES, instance=corporate_profil)
        user_profil_form = CustomUserChangeForm(request.POST, instance=corporate_profil.user)
        if corporate_profil_form.is_valid() and user_profil_form.is_valid():
            user_profil_form.save()
            corporate_profil_form.save()
            messages.success(request, message='Güncelleme İşlemi Başarılı')
            return redirect('corporate-home')
        else:
            messages.warning(request, message='Güncelleme İşlemi Başarısız')
    else:
        corporate_profil_form = CorporateForm(instance=corporate_profil)
        user_profil_form = CustomUserChangeForm(instance=corporate_profil.user)
    context = {
        'model_id': id,
        'action': 'update',
        'form': corporate_profil_form,
        'form2': user_profil_form,
        'user_control_data': user_control,
    }
    return render(request=request, template_name=template, context=context)


# Change Password
class PasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('change-password-done')
# End Change Password
