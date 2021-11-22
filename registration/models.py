import os
from tempfile import template

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils.safestring import mark_safe


class Corporate(models.Model):
    Gender = [('male', 'Erkek'), ('female', 'Kadın'), ]
    user = models.OneToOneField(to=User, verbose_name='Kullanıcı', on_delete=models.CASCADE, blank=True, null=True)
    corporate_name = models.CharField(max_length=150, verbose_name='Kurum Adı', blank=False, null=True)
    address = models.CharField(max_length=150, verbose_name='Adres', blank=True, null=True)
    phone = models.CharField(verbose_name='Cep Telefon No', max_length=20, null=True, blank=True)
    area = models.CharField(verbose_name="Kurum Alanı", max_length=50, null=True, blank=True)
    corporate_year = models.CharField(verbose_name="Kurum Çalışma Yılı", max_length=3, blank=True, null=True)
    corporate_clocks = models.CharField(verbose_name="Kurumsal Saatler", max_length=30, null=True, blank=True)
    logo = models.ImageField(upload_to='corporate', max_length=255, blank=True, verbose_name='Kurumsal Logo', null=True)
    contract = models.TextField(verbose_name="Sözleşme", blank=True, null=True)
    contract_start_date = models.DateField(verbose_name='Sözleşme Başlangıç tarihi', null=True, blank=True)
    contract_end_date = models.DateField(verbose_name='Sözleşme Başlangıç tarihi', null=True, blank=True)
    authorized_task = models.CharField(max_length=30, verbose_name='Yetkili Görevi', blank=True)
    authorized_age = models.CharField(verbose_name="Yetkilinin Yaşı", max_length=3, null=True, blank=True)
    authorized_gender = models.CharField(verbose_name="Cinsiyet", max_length=20, choices=Gender, blank=True, null=True)
    authorized_phone = models.CharField(verbose_name="Telefon Numarası", max_length=15, blank=True, null=True)
    authorized_image = models.ImageField(upload_to='corporate', max_length=255, blank=True, null=True,
                                         verbose_name='Yetkili Fotoğrafı')

    @property
    def corporate_logo_admin(self):
        if self.logo:
            return mark_safe(
                '<img src="{}" width="70" height="70" style=" border-radius: 50%;" />'.format(self.logo.url))
        return ""

    @property
    def authorized_image_admin(self):
        if self.authorized_image:
            return mark_safe(
                '<img src="{}" width="70" height="70" style=" border-radius: 50%;" />'.format(
                    self.authorized_image.url))
        return ""

    def corporate_avatar_path(instance, avatar):
        corporate_instance = Corporate.objects.get(pk=instance.pk)
        if corporate_instance.logo:
            logo = corporate_instance.logo
            if logo.file:
                if os.path.isfile(logo.path):
                    logo.file.close()
                    os.remove(logo.path)

    def authorized_image_path(instance, avatar):
        authorized_instance = Corporate.objects.get(pk=instance.pk)
        if authorized_instance.authorized_image:
            authorized_image = authorized_instance.authorized_image
            if authorized_image.file:
                if os.path.isfile(authorized_image.path):
                    authorized_image.file.close()
                    os.remove(authorized_image.path)

    @property
    def get_authorized_image_url(self):
        if self.authorized_image and hasattr(self.authorized_image, 'url'):
            return self.authorized_image.url
        else:
            return "/static/home_static/static_img/personal/user.png"

    @property
    def get_corp_logo_url(self):
        if self.logo and hasattr(self.logo, 'url'):
            return self.logo.url
        else:
            return "/static/home_static/static_img/logo/corplogo2.png"

    def __str__(self):  # Bu metodun anlamı burdaki adları arayuzde görebilmek
        return self.user.get_full_name() if self.user else ""

    def get_absolute_url(self):
        return reverse('corporate-detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('corporate-update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('corporate-delete', kwargs={'id': self.id})

    class Meta:
        verbose_name = "Kurumsal Kayıt"
        verbose_name_plural = 'Kurumsal Kayıtlar'


class Trainer(models.Model):
    Gender = [('male', 'Erkek'), ('female', 'Kadın'), ]
    user = models.OneToOneField(to=User, verbose_name='Kullanıcı', on_delete=models.CASCADE, blank=True, null=True)
    corporate = models.ForeignKey(to=Corporate, verbose_name="Kurum", on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=150, verbose_name='Adress', blank=True)
    phone = models.CharField(verbose_name='Cep Telefon No', max_length=20, null=True, blank=True)
    avatar = models.ImageField(upload_to='personal', max_length=255, blank=True, null=True,
                               verbose_name='Profil Fotoğrafı')
    trainer_gender = models.CharField(verbose_name="Cinsiyet", max_length=50, choices=Gender, blank=True, null=True)
    iban = models.CharField(verbose_name="IBAN Numarası", max_length=26, blank=True, null=True)
    age = models.CharField(verbose_name="Yaş", max_length=3, blank=True, null=True)
    school = models.CharField(verbose_name="Mezun Oluğu Okul", max_length=150, blank=True, null=True)
    graduation_year = models.DateField(verbose_name="Mezuniyet Yılı", null=True, blank=True)
    old_institution = models.CharField(verbose_name="Önceden Çalıştığı Kurum", max_length=150, null=True, blank=True)
    experience = models.CharField(verbose_name="Tecrübe", max_length=2, blank=True, null=True)
    contract = models.TextField(verbose_name="Sözleşme", blank=True, null=True)
    contract_start_date = models.DateField(verbose_name='Sözleşme Başlangıç tarihi', null=True, blank=True)
    contract_end_date = models.DateField(verbose_name='Sözleşme Başlangıç tarihi', null=True, blank=True)

    @property
    def get_trainer_avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return "/static/home_static/static_img/personal/user.png"

    def trainer_avatar_path(instance, avatar):
        trainer_instance = Trainer.objects.get(pk=instance.pk)
        if trainer_instance.avatar:
            avatar = trainer_instance.avatar
            if avatar.file:
                if os.path.isfile(avatar.path):
                    avatar.file.close()
                    os.remove(avatar.path)

    def __str__(self):  # Bu metodun anlamı burdaki adları arayuzde görebilmek
        return self.user.get_full_name() if self.user else ""

    def get_absolute_url(self):
        return reverse('trainer-detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('corporate-trainer-update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('corporate-trainer-delete', kwargs={'id': self.id})

    class Meta:
        verbose_name = "Antrenör Kayıt"
        verbose_name_plural = 'Antrenör Kayıtları'


class CV_upload(models.Model):
    trainer = models.ForeignKey(to=Trainer, verbose_name="Antrenör", on_delete=models.CASCADE, blank=True, null=True)
    cv_name = models.CharField(verbose_name='Cv Adı', max_length=100, blank=True, null=True)
    cv_path = models.FileField(upload_to='cv_pdf', verbose_name="Cv", max_length=255, blank=True, null=True)

    def trainer_avatar_path(instance):
        cv_instance = Trainer.objects.get(pk=instance.pk)
        if cv_instance.cv_path:
            cv_path = cv_instance.cv_path
            if cv_path.file:
                if os.path.isfile(cv_path.path):
                    cv_path.file.close()
                    os.remove(cv_path.path)

    def get_delete_url(self):
        return reverse('cv-delete', kwargs={'id': self.id})

    class Meta:
        verbose_name = "CV Yükleme"
        verbose_name_plural = 'CV Yükleme'


class TrainerDokumantations(models.Model):
    trainer = models.ForeignKey(to=Trainer, verbose_name="Antrenör", on_delete=models.CASCADE, blank=True, null=True)
    doc_name = models.CharField(verbose_name='Belge Adı', max_length=150, blank=True, null=True)
    trainer_document = models.FileField(upload_to='document_pdf', verbose_name="Antrenörlük Belgesi", max_length=255,
                                        blank=True, null=True)

    def trainer_avatar_path(instance, avatar):
        doc_instance = Trainer.objects.get(pk=instance.pk)
        if doc_instance.trainer_document:
            trainer_document = doc_instance.trainer_document
            if trainer_document.file:
                if os.path.isfile(trainer_document.path):
                    trainer_document.file.close()
                    os.remove(trainer_document.path)

    def get_delete_url(self):
        return reverse('doc-delete', kwargs={'id': self.id})

    class Meta:
        verbose_name = "Belge Yükleme"
        verbose_name_plural = 'Belge Yükleme'


# Start Medical inputs model
class Personal(models.Model):
    Gender = [('male', 'Erkek'), ('female', 'Kadın'), ]
    Marital_Status = [('married', 'Evli'), ('single', 'Bekar'), ]
    user = models.OneToOneField(to=User, verbose_name='Kullanıcı', on_delete=models.CASCADE, blank=True, null=True)
    trainer = models.ForeignKey(to=Trainer, verbose_name="Antrenör", on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=150, verbose_name='Adres', blank=True)
    phone = models.CharField(verbose_name='Cep Telefon No', max_length=20, null=True, blank=True)
    job = models.CharField(verbose_name="Meslek", max_length=150, null=True, blank=True)
    age = models.IntegerField(verbose_name="Yaş", blank=True, null=True)
    record_date = models.DateTimeField(verbose_name="Kayıt Tarihi", blank=True, null=True)
    lesson_count = models.IntegerField(verbose_name="Ders Sayısı", blank=True, null=True)
    price = models.DecimalField(verbose_name="Toplam Fiyat", max_digits=30, decimal_places=10, blank=True, null=True)
    gender = models.CharField(verbose_name="Cinsiyet", max_length=50, choices=Gender, blank=True, null=True)
    marital_status = models.CharField(verbose_name="Medeni Durum", max_length=50, choices=Marital_Status, blank=True,
                                      null=True)
    avatar = models.ImageField(upload_to='personal', max_length=255, blank=True, null=True,
                               verbose_name='Profil Fotoğrafı')
    contract = models.TextField(verbose_name="Sözleşme", blank=True, null=True)
    contract_start_date = models.DateField(verbose_name='Sözleşme Başlangıç tarihi', null=True, blank=True)
    contract_end_date = models.DateField(verbose_name='Sözleşme Başlangıç tarihi', null=True, blank=True)

    def personal_avatar_path(instance, avatar):
        personal_instance = Personal.objects.get(pk=instance.pk)
        if personal_instance.avatar:
            avatar = personal_instance.avatar
            if avatar.file:
                if os.path.isfile(avatar.path):
                    avatar.file.close()
                    os.remove(avatar.path)

    @property
    def personal_image_admin(self):
        if self.avatar:
            return mark_safe(
                '<img src="{}" width="70" height="70" style=" border-radius: 50%;" />'.format(self.avatar.url))
        return ""

    @property
    def get_personal_avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return "/static/home_static/static_img/personal/user.png"

    def __str__(self):  # Bu metodun anlamı burdaki adları arayuzde görebilmek
        return self.user.get_full_name() if self.user else ""

    def get_absolute_url(self):
        return reverse('personal-detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('trainer-personal-update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('trainer-personal-delete', kwargs={'id': self.id})

    def get_update_corporate_url(self):
        return reverse('corporate-personal-update', kwargs={'id': self.id})

    def get_delete_corporate_url(self):
        return reverse('corporate-personal-delete', kwargs={'id': self.id})

    def gender_value(self):
        tmp = self.gender
        if tmp == 'male':
            return 'Erkek'
        elif tmp == 'female':
            return 'Kadın'
        else:
            return ''

    class Meta:
        verbose_name = "Bireysel Kayıt"
        verbose_name_plural = 'Danışan Kayıtları'
