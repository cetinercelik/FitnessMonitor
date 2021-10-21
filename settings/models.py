from logging import disable

from ckeditor.fields import RichTextField
from django.db import models
from stdimage import StdImageField, JPEGField
from datetime import datetime


# Create your models here.


class homemodel(models.Model):
    corporate_logo = models.ImageField(upload_to='home_page', verbose_name='Şirket logosu', max_length=255, blank=True,
                                       null=True)
    corporate_main_title = models.TextField(verbose_name='Kurumsal Ana Başlık Açıklama', max_length=500,
                                            blank=True, null=True)
    software_main_title = models.TextField(verbose_name='FitnessMonitor Keşfet Üst Ana açıklama', max_length=500,
                                           blank=True,
                                           null=True)
    blog_main_title = models.TextField(verbose_name='Blog Üst Ana açıklama', max_length=500, blank=True,
                                       null=True)
    team_main_title = models.TextField(verbose_name='Ekibimiz Üst Ana açıklama', max_length=500, blank=True,
                                       null=True)
    central_address = models.TextField(verbose_name="Merkez Ofis Adres", blank=True, null=True)
    central_phone = models.CharField(verbose_name='Merekez Ofis Telefon', max_length=20, blank=True, null=True)
    central_local_link = models.TextField(verbose_name='Merkez Ofis Konum Linki', null=True, blank=True)
    branch_adress = models.TextField(verbose_name='Şube Ofis Adresi', blank=True, null=True)
    branch_phone = models.CharField(verbose_name='Şube Ofis Telefon', max_length=20, blank=True, null=True)
    branch_local_link = models.TextField(verbose_name='Şube Ofis Konum Linki', null=True, blank=True)
    instagram = models.CharField(verbose_name='Kurum Instagram Link', max_length=100, blank=True, null=True)
    twitter = models.CharField(verbose_name='Kurum Twitter Link', max_length=100, blank=True, null=True)
    facebook = models.CharField(verbose_name='Kurum Facebook Link', max_length=100, blank=True, null=True)
    mail = models.CharField(verbose_name='Kurum Mail Address', max_length=100, blank=True, null=True)

    def delete(self, using=None, keep_parents=False):
        self.corporate_logo.storage.delete(self.corporate_logo.name)
        super().delete()

    class Meta:
        verbose_name = "Anasayfa Bilgileri"
        verbose_name_plural = 'Anasayfa Bilgileri'


class ImagePost(models.Model):
    main_title = models.CharField(verbose_name='Slider Ana Başlık', max_length=100, blank=True,
                                  null=True)
    sub_title = models.CharField(verbose_name='Slider Alt Başlık', max_length=600, blank=True, null=True)
    image = StdImageField(upload_to='home_page/upload_image/slider_image', max_length=255, blank=True,
                          verbose_name='Slider Resimleri',
                          null=True, variations={
            'thumbnail': (1920, 1280, True),
        }, delete_orphans=True)

    class Meta:
        verbose_name = "Slider Resim Ekle"
        verbose_name_plural = 'Slider Resim Ekle'


class Team(models.Model):
    name_surname = models.CharField(verbose_name='Ad ve Soyad', max_length=100, blank=True, null=True)
    job = models.CharField(verbose_name='Uğraş Alanı', max_length=100, blank=True, null=True)
    personal_descriptions = models.TextField(verbose_name='Kişi hakkında kısa açıklama', max_length=150, blank=True,
                                             null=True)
    instagram = models.CharField(verbose_name='Instagram Link', max_length=100, blank=True, null=True)
    twitter = models.CharField(verbose_name='Twitter Link', max_length=100, blank=True, null=True)
    facebook = models.CharField(verbose_name='Facebook Link', max_length=100, blank=True, null=True)
    mail = models.CharField(verbose_name='Mail Address', max_length=100, blank=True, null=True)
    image = StdImageField(upload_to='home_page/upload_image/team_image', max_length=255,blank=True,
                          verbose_name='Slider Resimleri',
                          null=True, variations={
            'thumbnail': (525, 350, True),
        }, delete_orphans=True)

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    class Meta:
        verbose_name = "Ekip Adaylarını Ekle"
        verbose_name_plural = "Ekip Adaylarını Ekle"


class Blog(models.Model):
    blog_title = models.CharField(verbose_name='Blog Haber Başlığı', max_length=250, blank=True, null=True)
    blog_descriptions = models.TextField(verbose_name='Blog Haber Kısa Açıklaması', max_length=250, blank=True,
                                         null=True)
    blog_date = models.DateField(default=datetime.now())
    blog_image = StdImageField(upload_to='home_page/upload_image/blog_image', max_length=255,blank=True,
                               verbose_name='Slider Resimleri',
                               null=True, variations={
            'thumbnail': (525, 350, True),
        }, delete_orphans=True)

    def delete(self, using=None, keep_parents=False):
        self.blog_image.storage.delete(self.blog_image.name)
        super().delete()

    class Meta:
        verbose_name = 'Blog Haberleri Ekle'
        verbose_name_plural = 'Blog Haberleri Ekle'


class About(models.Model):
    title = models.CharField(verbose_name='Başlık', max_length=150, blank=True, null=True)
    description = RichTextField(verbose_name='Hakkımızda Açıklama')
    image = StdImageField(upload_to='home_page/upload_image/about_image', max_length=255,blank=True,
                          verbose_name='Hakkımızda Resim',
                          null=True, variations={
            'thumbnail': (1920, 1280, True),
        }, delete_orphans=True)

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    class Meta:
        verbose_name = 'Hakkımzda Alanı Bilgileri'
        verbose_name_plural = 'Hakkımızda Alanı Bilgileri'


class FitnessMonitor(models.Model):
    title = models.CharField(verbose_name='Yazılım Başlığı', max_length=150, blank=True, null=True)
    description = RichTextField(verbose_name='Yazılım Açıklaması', blank=True, null=True)
    image = StdImageField(upload_to='home_page/upload_image/fitnessmonitor_image', max_length=255,blank=True,
                          verbose_name='Kurumsal Resimler',
                          null=True, variations={
            'thumbnail': (1920, 1280, True),
        }, delete_orphans=True)

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    class Meta:
        verbose_name = 'FitnessMonitor Keşfet Alanı Bilgileri'
        verbose_name_plural = 'FitnessMonitor Keşfet Alanı Bilgileri'


class Founder(models.Model):
    founder_name_surname = models.CharField(verbose_name='Kurucu Adı ve Soyadı', max_length=100, null=True, blank=True)
    founder_descriptions = RichTextField(verbose_name='Kurucu Açıklama', null=True, blank=True)
    founder_link = models.CharField(verbose_name='Kurucu Websitesi link alanı', max_length=150, blank=True, null=True)
    founder_link_name = models.CharField(verbose_name='Kurucu Websiitesi link Açıklaması', max_length=150, blank=True,
                                         null=True)
    instagram = models.CharField(verbose_name='Instagram Link', max_length=100, blank=True, null=True)
    twitter = models.CharField(verbose_name='Twitter Link', max_length=100, blank=True, null=True)
    facebook = models.CharField(verbose_name='Facebook Link', max_length=100, blank=True, null=True)
    mail = models.CharField(verbose_name='Mail Address', max_length=100, blank=True, null=True)
    image = StdImageField(upload_to='home_page/upload_image/founder_image', max_length=255,blank=True,
                          verbose_name='Kurucu Fotoğraf',
                          null=True, variations={
            'thumbnail': (1920, 1280, True),
        }, delete_orphans=True)

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    class Meta:
        verbose_name = 'Kurucu Alanı Bilgileri'
        verbose_name_plural = 'Kurucu Alanı Bilgileri'


class Corporate_solve(models.Model):
    main_title = models.CharField(verbose_name='Ana Başlık', max_length=100, blank=True, null=True)
    description = RichTextField(verbose_name='Açıklama', blank=True, null=True)
    sub_title1 = models.CharField(verbose_name='Birinci Alt Başlık', max_length=150, blank=True, null=True)
    sub_description1 = RichTextField(verbose_name='Birinci Alt Açıklama', blank=True, null=True)
    sub_title2 = models.CharField(verbose_name='İkinci Alt Başlık', max_length=150, blank=True, null=True)
    sub_description = RichTextField(verbose_name='İkinci Alt Açıklama', blank=True, null=True)
    image_1 = StdImageField(upload_to='home_page/upload_image/corporate_image', max_length=255,blank=True,
                            verbose_name='Resim 1',
                            null=True, variations={
            'thumbnail': (1920, 1280, True),
        }, delete_orphans=True)
    image_2 = StdImageField(upload_to='home_page/upload_image/corporate_image', max_length=255,blank=True,
                            verbose_name='Resim 2',
                            null=True, variations={
            'thumbnail': (1920, 1280, True),
        }, delete_orphans=True)
    image_3 = StdImageField(upload_to='home_page/upload_image/corporate_image', max_length=255,blank=True,
                            verbose_name='Resim 3',
                            null=True, variations={
            'thumbnail': (1920, 1280, True),
        }, delete_orphans=True)

    def delete(self, using=None, keep_parents=False):
        self.image_1.storage.delete(self.image_1.name)
        self.image_2.storage.delete(self.image_2.name)
        self.image_3.storage.delete(self.image_3.name)
        super().delete()

    class Meta:
        verbose_name = 'Kurumsal Çözümleme Alanı Bilgileri'
        verbose_name_plural = 'Kurumsal Çözümleme Alanı Bilgileri'


class Philosophy(models.Model):
    title = models.CharField(verbose_name='Başlık', max_length=150, blank=True, null=True)
    first_description = RichTextField(verbose_name='İlk Açıklama', blank=True, null=True)
    image = StdImageField(upload_to='home_page/upload_image/philosophy_image', max_length=255,blank=True,
                          verbose_name='Felsefe Fotoğraf',
                          null=True, variations={
            'thumbnail': (1920, 1280, True),
        }, delete_orphans=True)
    last_description = RichTextField(verbose_name='Son Açıklama', blank=True, null=True)

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    class Meta:
        verbose_name = 'FitnessMonitor Felsefesi Alanı Bilgileri'
        verbose_name_plural = 'FitnessMonitor Felsefesi Alanı Bilgileri'


class SocialMedia(models.Model):
    founder = models.ForeignKey(to=Founder, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    # home_model = models.ForeignKey(to=homemodel, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    team_model = models.ForeignKey(to=Team, on_delete=models.CASCADE, blank=True, null=True, editable=False)
    instagram = models.CharField(verbose_name='Instagram Link', max_length=100, blank=True, null=True)
    twitter = models.CharField(verbose_name='Twitter Link', max_length=100, blank=True, null=True)
    facebook = models.CharField(verbose_name='Facebook Link', max_length=100, blank=True, null=True)
    mail = models.CharField(verbose_name='Mail Address', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Sosyal Medya Alanı'
        verbose_name_plural = 'Sosyal Medya Alanı'


class Sub_Philosophy(models.Model):
    philosopy = models.ForeignKey(to=Philosophy, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(verbose_name='Adım Başlık', max_length=150, blank=True, null=True)
    description = RichTextField(verbose_name='Adım Açıklama', blank=True, null=True)
    image = StdImageField(upload_to='home_page/upload_image/philosophy_image', max_length=255,blank=True,
                          verbose_name='Adım Fotoğraf',
                          null=True, variations={
            'thumbnail': (1920, 1280, True),
        }, delete_orphans=True)

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()

    class Meta:
        verbose_name = 'Felsefe Adım Ekleme Alanı'
        verbose_name_plural = 'Felsefe Adım Ekleme Alanı'


class Pricing(models.Model):
    title = models.CharField(verbose_name='Paket ve Danışan sayısı', max_length=150, blank=True, null=True)
    sub_title = models.CharField(verbose_name='danışan ve süre', max_length=150, blank=True, null=True)
    price = models.CharField(verbose_name='Fiyat Belirle', max_length=100, blank=True, null=True)
    trainer_panel = models.CharField(verbose_name='Antrenör paneli kullanıcı sayısı', max_length=100, blank=True,
                                     null=True)
    personal_panel = models.CharField(verbose_name='Personel Paneli kullnıcı sayısı', max_length=100, blank=True,
                                      null=True)
    fitnessmonitor = models.CharField(verbose_name='FitnessMonitor Başlık', max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'FitnessMonitor Fiyatlandırma Ana Bilgileri'
        verbose_name_plural = 'FitnessMonitor Fiyatlandırma Ana Bilgileri'


class Sub_Pricing(models.Model):
    title = models.CharField(verbose_name='Alt Başlık Ekle', max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = 'FitnessMonitor Fiyatlandırma Paneli Altbaşlıklar'
        verbose_name_plural = 'FitnessMonitor Fiyatlandırma Paneli Altbaşlıklar'


class sendMessage(models.Model):
    name_surname = models.CharField(verbose_name='Ad Soyad', max_length=150, null=True, blank=True)
    mail = models.EmailField(verbose_name='mail', max_length=150, null=True, blank=True)
    subject = models.CharField(verbose_name='Konu', max_length=150, null=True, blank=True)
    message = models.TextField(verbose_name='Mesaj', max_length=500, blank=True, null=True)

    class Meta:
        verbose_name = 'Kullnıcı Mesajları'
        verbose_name_plural = 'Kullnıcı Mesajları'