from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView

from registration.models import Personal, Corporate, Trainer


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


class CorporateForm(forms.ModelForm):
    class Meta:
        model = Corporate
        fields = [
            'corporate_name',
            'authorized_task',
            'address',
            'phone',
            'logo',
            'area',
            'corporate_year',
            'corporate_clocks',
            'corporate_year',
            'authorized_task',
            'authorized_age',
            'authorized_gender',
            'authorized_phone',
            'authorized_image',
        ]


class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = [
            'address',
            'phone',
            'avatar',
            'trainer_gender',
            'iban',
            'age',
            'school',
            'graduation_year',
            'old_institution',
            'experience',
            'cv',
            'trainer_document',
            'certificate',
        ]


class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = [
            'trainer',
            'phone',
            'avatar',
            'address',
            'job',
            'age',
            'record_date',
            'gender',
            'marital_status',
            'lesson_count',
            'price',
            'contract',
        ]

