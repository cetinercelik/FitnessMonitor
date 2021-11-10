import os
from logging import disable

from ckeditor.fields import RichTextField
from django.core.validators import FileExtensionValidator
from django.db import models
from stdimage import StdImageField, JPEGField
from datetime import datetime


# Create your models here.


class homemodel(models.Model):
    corporate_logo = StdImageField(upload_to='home_page/upload_image/logo', max_length=255, blank=True,
                                   verbose_name='Logo Resimleri',
                                   null=True, variations={
        }, delete_orphans=True)
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

    @property
    def get_logo_url(self):
        if self.corporate_logo and hasattr(self.corporate_logo, 'url'):
            return self.corporate_logo.url
        else:
            return "/static/home_static/static_img/logo/homelogo.png"

    def corporate_logo_path(instance, corporate_logo):
        corporate_instance = homemodel.objects.get(pk=instance.pk)
        if corporate_instance.corporate_logo:
            corp_logo = corporate_instance.corporate_logo
            if corp_logo.file:
                if os.path.isfile(corp_logo.path):
                    corp_logo.file.close()
                    os.remove(corp_logo.path)

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

    @property
    def get_slider_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/home_static/static_img/sliders/Three-Swans.jpg"

    def slider_image_path(instance, image):
        image_instance = homemodel.objects.get(pk=instance.pk)
        if image_instance.image:
            image_obj = image_instance.image
            if image_obj.file:
                if os.path.isfile(image_obj.path):
                    image_obj.file.close()
                    os.remove(image_obj.path)

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
    image = StdImageField(upload_to='home_page/upload_image/team_image', max_length=255, blank=True,
                          verbose_name='Slider Resimleri',
                          null=True, variations={
            'thumbnail': (525, 350, True),
        }, delete_orphans=True)

    @property
    def get_team_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/home_static/static_img/personal/user.png"

    def team_image_path(instance, image):
        image_instance = homemodel.objects.get(pk=instance.pk)
        if image_instance.image:
            image_obj = image_instance.image
            if image_obj.file:
                if os.path.isfile(image_obj.path):
                    image_obj.file.close()
                    os.remove(image_obj.path)

    class Meta:
        verbose_name = "Ekip Adaylarını Ekle"
        verbose_name_plural = "Ekip Adaylarını Ekle"


class Blog(models.Model):
    blog_title = models.CharField(verbose_name='Blog Haber Başlığı', max_length=250, blank=True, null=True)
    blog_descriptions = models.TextField(verbose_name='Blog Haber Kısa Açıklaması', max_length=250, blank=True,
                                         null=True)
    blog_link = models.CharField(verbose_name="Blok Link", null=True, blank=True, max_length=200)
    blog_date = models.DateField(default=datetime.now())
    blog_image = StdImageField(upload_to='home_page/upload_image/blog_image', max_length=255, blank=True,
                               verbose_name='Slider Resimleri',
                               null=True, variations={
            'thumbnail': (525, 350, True),
        }, delete_orphans=True)

    @property
    def get_blog_image_url(self):
        if self.blog_image and hasattr(self.blog_image, 'url'):
            return self.blog_image.url
        else:
            return "/static/home_static/static_img/blog/blog.jpg"

    def blog_image_path(instance, image):
        blog_instance = homemodel.objects.get(pk=instance.pk)
        if blog_instance.blog_image:
            blog_image_obj = blog_instance.blog_image
            if blog_image_obj.file:
                if os.path.isfile(blog_image_obj.path):
                    blog_image_obj.file.close()
                    os.remove(blog_image_obj.path)

    class Meta:
        verbose_name = 'Blog Haberleri Ekle'
        verbose_name_plural = 'Blog Haberleri Ekle'


class About(models.Model):
    title = models.CharField(verbose_name='Başlık', max_length=150, blank=True, null=True)
    description = RichTextField(verbose_name='Hakkımızda Açıklama')
    image = StdImageField(upload_to='home_page/upload_image/about_image', max_length=255, blank=True,
                          verbose_name='Hakkımızda Resim',
                          null=True, variations={
            'thumbnail': (1920, 1280, True),
        }, delete_orphans=True)

    @property
    def get_about_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/home_static/static_img/about/about.jpg"

    def about_image_path(instance, image):
        image_instance = homemodel.objects.get(pk=instance.pk)
        if image_instance.image:
            image_obj = image_instance.image
            if image_obj.file:
                if os.path.isfile(image_obj.path):
                    image_obj.file.close()
                    os.remove(image_obj.path)

    class Meta:
        verbose_name = 'Hakkımzda Alanı Bilgileri'
        verbose_name_plural = 'Hakkımızda Alanı Bilgileri'


class FitnessMonitor(models.Model):
    title = models.CharField(verbose_name='Yazılım Başlığı', max_length=150, blank=True, null=True)
    description = RichTextField(verbose_name='Yazılım Açıklaması', blank=True, null=True)
    image = StdImageField(upload_to='home_page/upload_image/fitnessmonitor_image', max_length=255, blank=True,
                          verbose_name='Kurumsal Resimler',
                          null=True, variations={
            'thumbnail': (1920, 1280, True),
        }, delete_orphans=True)

    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/home_static/static_img/fitnessmonitor/fitnessmonitor.jpg"

    def fitness_image_path(instance, image):
        image_instance = homemodel.objects.get(pk=instance.pk)
        if image_instance.image:
            image_obj = image_instance.image
            if image_obj.file:
                if os.path.isfile(image_obj.path):
                    image_obj.file.close()
                    os.remove(image_obj.path)

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
    image = StdImageField(upload_to='home_page/upload_image/founder_image', max_length=255, blank=True,
                          verbose_name='Kurucu Fotoğraf',
                          null=True, variations={
            'thumbnail': (1920, 1280, True),
        }, delete_orphans=True)

    @property
    def get_founder_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/home_static/static_img/founder/founder.jpg"

    def founder_image_path(instance, image):
        image_instance = homemodel.objects.get(pk=instance.pk)
        if image_instance.image:
            image_obj = image_instance.image
            if image_obj.file:
                if os.path.isfile(image_obj.path):
                    image_obj.file.close()
                    os.remove(image_obj.path)

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
    corp_video = models.FileField(upload_to='home_page/upload_video/', verbose_name="Video Yükle", blank=True,
                                  null=True, validators=[
            FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    image_2 = StdImageField(upload_to='home_page/upload_image/corporate_image', max_length=255, blank=True,
                            verbose_name='Resim 2',
                            null=True, variations={
            'thumbnail': (1920, 1280, True),
        }, delete_orphans=True)
    image_3 = StdImageField(upload_to='home_page/upload_image/corporate_image', max_length=255, blank=True,
                            verbose_name='Resim 3',
                            null=True, variations={
            'thumbnail': (1920, 1280, True),
        }, delete_orphans=True)

    @property
    def get_vido1_url(self):
        if self.corp_video and hasattr(self.corp_video, 'url'):
            return self.corp_video.url
        else:
            return "/static/home_static/static_video/r13 png_1.mp4"

    @property
    def get_image2_url(self):
        if self.image_2 and hasattr(self.image_2, 'url'):
            return self.image_2.url
        else:
            return "/static/home_static/static_img/corpsolve/corpsolve.png"

    @property
    def get_image3_url(self):
        if self.image_3 and hasattr(self.image_3, 'url'):
            return self.image_3.url
        else:
            return "/static/home_static/static_img/corpsolve/corpsolve.png"

    def corporate_solve_path(instance, image):
        image_instance1 = Corporate_solve.objects.get(pk=instance.pk)
        image_instance2 = Corporate_solve.objects.get(pk=instance.pk)
        image_instance3 = Corporate_solve.objects.get(pk=instance.pk)
        if image_instance1.image_1 or image_instance2.image_1 or image_instance3.image_3:
            image_obj1 = image_instance1.image_1
            image_obj2 = image_instance2.image_2
            image_obj3 = image_instance3.image_3
            if image_obj1.file or image_obj2.file or image_obj3.file:
                if os.path.isfile(image_obj1.path) or os.path.isfile(image_obj2.path) or os.path.isfile(
                        image_obj3.path):
                    image_obj1.file.close()
                    image_obj2.file.close()
                    image_obj3.file.close()
                    os.remove(image_obj1.path)
                    os.remove(image_obj2.path)
                    os.remove(image_obj3.path)

    class Meta:
        verbose_name = 'Kurumsal Çözümleme Alanı Bilgileri'
        verbose_name_plural = 'Kurumsal Çözümleme Alanı Bilgileri'


class Philosophy(models.Model):
    title = models.CharField(verbose_name='Başlık', max_length=150, blank=True, null=True)
    first_description = RichTextField(verbose_name='İlk Açıklama', blank=True, null=True)
    phl_video = models.FileField(upload_to='home_page/upload_video/', verbose_name="Video Yükle", blank=True, null=True,
                                 validators=[
                                     FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    last_description = RichTextField(verbose_name='Son Açıklama', blank=True, null=True)

    @property
    def get_philosophy_video_url(self):
        if self.phl_video and hasattr(self.phl_video, 'url'):
            return self.phl_video.url
        else:
            return "/static/home_static/static_video/r3.mp4"

    def philosophy_video_path(instance, image):
        video_instance = Philosophy.objects.get(pk=instance.pk)
        if video_instance.image:
            video_obj = video_instance.phl_video
            if video_obj.file:
                if os.path.isfile(video_obj.path):
                    video_obj.file.close()
                    os.remove(video_obj.path)

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
    image = StdImageField(upload_to='home_page/upload_image/philosophy_image', max_length=255, blank=True,
                          verbose_name='Adım Fotoğraf',
                          null=True, variations={
            'thumbnail': (1920, 1280, True),
        }, delete_orphans=True)

    @property
    def get_sub_philosopy_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "/static/home_static/static_img/philosophy/philosophy.png"

    def philosophy_image_path(instance, image):
        image_instance = homemodel.objects.get(pk=instance.pk)
        if image_instance.image:
            image_obj = image_instance.image
            if image_obj.file:
                if os.path.isfile(image_obj.path):
                    image_obj.file.close()
                    os.remove(image_obj.path)

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
