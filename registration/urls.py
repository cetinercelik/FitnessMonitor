from django.urls import path
from django.contrib.auth import views as auth_views
from registration import views
from registration.views import PasswordChange

urlpatterns = [
    # Personal CRUD operations
    path('personal/index', views.personal_home, name='personal-home'),
    path('personal/register', views.personal_create_register, name='personal-register'),

    # Corporate CRUD operations
    path('corporate/index', views.corporate_home, name='corporate-home'),
    path('corporate/corporateregister', views.corporate_create_register, name='corporate-register'),

    # Corporate Trainer Crud
    path('corporate/trainer/index', views.corporate_trainer_home, name='corporate-trainer-home'),
    path('corporate/trainer/create', views.corporate_tariner_create, name='corporate-trainer-create'),
    path('corporate/trainer/update/<int:id>', views.corporate_trainer_update, name='corporate-trainer-update'),
    path('corporate/delete/<int:id>', views.corporate_trainer_delete, name='corporate-trainer-delete'),

    # Corporate Personal CRUD
    path('corporate/personal/index', views.corporate_personal_home, name='corporate-personal-home'),
    path('corporate/personal/create', views.corporate_personal_create, name='corporate-personal-create'),
    path('corporate/personal/update/<int:id>', views.corporate_personal_update, name='corporate-personal-update'),
    path('corporate/personal/delete/<int:id>', views.corporate_personal_delete, name='corporate-personal-delete'),

    # Trainer CRUD operations
    path('trainer/index', views.trainer_home, name='trainer-home'),
    path('trainer/register', views.trainer_create_register, name='trainer-register'),

    # Trainer personal CRUD
    path('trainer/personal/index', views.trainer_personal_home, name='trainer-personal-home'),
    path('trainer/personal/create', views.trainer_personal_create, name='trainer-personal-create'),
    path('trainer/personal/update/<int:id>', views.trainer_personal_update, name='trainer-personal-update'),
    path('trainer/personal/delete/<int:id>', views.trainer_personal_delete, name='trainer-personal-delete'),

    # Settings CRUD operations
    # Personal Settings
    path('personal/personal_settings/<int:id>', views.personal_settings, name='personal-settings'),

    # Corporate Settings
    path('settings/corporate_settings/<int:id>', views.corporate_settings, name='corporate-settings'),

    # Trainer Settings
    path('trainers/trainer_settings/<int:id>', views.trainer_settings, name='trainer-settings'),
    # CV Uploader
    path('trainers/cv_ıpload/<int:id>', views.cv_uplaod_view, name='cv-upload-view'),
    path('trainers/documantation/<int:id>', views.documantations_upload_view, name='documantation-upload-view'),

    # CV and Trainer Documantions delete
    path('trainer/cv/delete/<int:id>', views.cv_delete, name='cv-delete'),
    path('trainer/doc/delete/<int:id>', views.doc_delete, name='doc-delete'),

    # password reset operations
    path('reset_password/',
         auth_views.PasswordResetView.as_view(template_name="password/password_reset_email.html"),
         name="reset_password"),

    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(template_name="password/password_reset_sent.html"),
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_form.html"),
         name="password_reset_confirm"),

    path('reset_password_complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name="password/password_reset_done.html"),
         name="password_reset_complete"),
    # End Password Reset

    # Start Password Change
    path('password/change_password/',
         PasswordChange.as_view(template_name="registration/settings/password_change_settings/change-password.html"),
         name="change-password"),
    path('password/change_password_done/', auth_views.PasswordChangeDoneView.as_view(
        template_name="registration/settings/password_change_settings/change_password_done.html"),
         name="change-password-done"),
    # End Password Change

]
