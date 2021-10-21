from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


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

    def delete(self, using=None, keep_parents=False):
        self.authorized_image.storage.delete(self.authorized_image.name)
        self.logo.storage.delete(self.logo.name)
        super().delete()

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
    cv = models.FileField(upload_to='cv_pdf', verbose_name="Cv", max_length=255, blank=True, null=True)
    trainer_document = models.FileField(upload_to='document_pdf', verbose_name="Antrenörlük Belgesi", max_length=255,
                                        blank=True, null=True)
    certificate = models.FileField(upload_to='certificate_pdf', verbose_name="Sertifika", max_length=255, blank=True,
                                   null=True)
    contract = models.TextField(verbose_name="Sözleşme", blank=True, null=True)
    contract_start_date = models.DateField(verbose_name='Sözleşme Başlangıç tarihi', null=True, blank=True)
    contract_end_date = models.DateField(verbose_name='Sözleşme Başlangıç tarihi', null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.avatar.storage.delete(self.avatar.name)
        self.cv.storage.delete(self.cv.name)
        self.trainer_document.storage.delete(self.trainer_document.name)
        self.certificate.storage.delete(self.certificate.name)
        super().delete()

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
    avatar = models.ImageField(upload_to='personal', max_length=255, blank=True,null=True, verbose_name='Profil Fotoğrafı')
    contract = models.TextField(verbose_name="Sözleşme", blank=True, null=True)
    contract_start_date = models.DateField(verbose_name='Sözleşme Başlangıç tarihi', null=True, blank=True)
    contract_end_date = models.DateField(verbose_name='Sözleşme Başlangıç tarihi', null=True, blank=True)

    def delete(self, using=None, keep_parents=False):
        self.avatar.storage.delete(self.avatar.name)
        super().delete()

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
        else:
            return 'Kadın'

    class Meta:
        verbose_name = "Bireysel Kayıt"
        verbose_name_plural = 'Danışan Kayıtları'
