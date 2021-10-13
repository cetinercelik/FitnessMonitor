from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

# Start Fıness inputs model
from registration.models import Corporate, Trainer, Personal


class FitnessInputs(models.Model):
    trainer = models.ForeignKey(to=Trainer, verbose_name="Antrenör", on_delete=models.CASCADE, blank=True, null=True)
    personal = models.ForeignKey(to=Personal, verbose_name="Danışan", on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(("Date"), default=datetime.now(), blank=True)
    age = models.CharField(max_length=10, verbose_name='Yaş', null=True, blank=True)  # DEMOGRAFI
    height = models.CharField(max_length=10, verbose_name='Boy', null=True, blank=True)
    weight = models.CharField(max_length=10, verbose_name='Vucut Ağırlığı', null=True, blank=True)
    bki = models.CharField(max_length=10, verbose_name='BKİ', null=True, blank=True)  # BODYCOMPOSITION/BODYCOMPOSITION1
    fat_mass = models.CharField(max_length=10, verbose_name='Görece Yağ Kütle İndeksi', null=True, blank=True)
    lean_body = models.CharField(max_length=10, verbose_name='Yağsız Vücut Ağırlığı', null=True, blank=True)
    shoulder = models.CharField(max_length=10, verbose_name='Omuz', null=True,
                                blank=True)  # BODYCOMPOSITION/ENVIRONMENT
    chest = models.CharField(max_length=10, verbose_name='Göğüs', null=True, blank=True)
    biseps = models.CharField(max_length=10, verbose_name='Biseps', null=True, blank=True)
    wrist = models.CharField(max_length=10, verbose_name='El Bileği', null=True, blank=True)
    waist = models.CharField(max_length=10, verbose_name='Bel Çevresi', null=True, blank=True)
    hip = models.CharField(max_length=10, verbose_name='Kalça Çevresi', null=True, blank=True)
    knee = models.CharField(max_length=10, verbose_name='Diz Çevresi', null=True, blank=True)
    upper_leg = models.CharField(max_length=10, verbose_name='Üst Bacak', null=True, blank=True)
    gastrocnemius = models.CharField(max_length=10, verbose_name='Gastrocnemius', null=True, blank=True)
    ankle = models.CharField(max_length=10, verbose_name='Ayak Bileği', null=True, blank=True)
    waist_Hip = models.CharField(max_length=10, verbose_name='Bel/Kalça Oranı', null=True, blank=True)
    man3ch = models.CharField(verbose_name='Chest', max_length=20, blank=True, null=True)  # BODYCOMPOSITION/BODYOIL
    man3tri = models.CharField(verbose_name='Triceps', max_length=20, blank=True, null=True)
    man3sub = models.CharField(verbose_name='Subscapula', max_length=20, blank=True, null=True)
    woman3tri = models.CharField(verbose_name='Triceps', max_length=20, blank=True, null=True)
    woman3abd = models.CharField(verbose_name='Abdomen', max_length=20, blank=True, null=True)
    woman3sub = models.CharField(verbose_name='Suprailiac', max_length=20, blank=True, null=True)
    man7ch = models.CharField(verbose_name='Chest', max_length=20, blank=True, null=True)
    man7tr = models.CharField(verbose_name='Triceps', max_length=20, blank=True, null=True)
    man7sub = models.CharField(verbose_name='Subscapula', max_length=20, blank=True, null=True)
    man7sic = models.CharField(verbose_name='Suprailiac', max_length=20, blank=True, null=True)
    man7mid = models.CharField(verbose_name='Midaxillary', max_length=20, blank=True, null=True)
    man7abd = models.CharField(verbose_name='Abdomen', max_length=20, blank=True, null=True)
    man7th = models.CharField(verbose_name='Thigh', max_length=20, blank=True, null=True)
    woman7ch = models.CharField(verbose_name='Chest', max_length=20, blank=True, null=True)
    woman7tri = models.CharField(verbose_name='Triceps', max_length=20, blank=True, null=True)
    woman7sub = models.CharField(verbose_name='Subscapula', max_length=20, blank=True, null=True)
    woman7sic = models.CharField(verbose_name='Suprailiac', max_length=20, blank=True, null=True)
    woman7mid = models.CharField(verbose_name='Midaxillary', max_length=20, blank=True, null=True)
    woman7abd = models.CharField(verbose_name='Abdomen', max_length=20, blank=True, null=True)
    woman7th = models.CharField(verbose_name='Thigh', max_length=20, blank=True, null=True)
    humerus_bikondil = models.CharField(max_length=10, verbose_name='Humerus Bikondil ', null=True, blank=True)
    femur_bikondil = models.CharField(max_length=10, verbose_name='Femur Bikondil', null=True, blank=True)
    adjusted_biseps = models.CharField(max_length=10, verbose_name='Düzeltilmiş Biseps Çevre', null=True, blank=True)
    adjusted_gastrocnemius = models.CharField(max_length=10, verbose_name='Düzeltilmiş Gastrocnemius Çevre', null=True,
                                              blank=True)
    rest_heart = models.CharField(max_length=10, verbose_name='Dinlenim Kalp Atım Hızı', null=True,
                                  blank=True)  # HEARTBREATHING/HEARTBEAT
    max_heart = models.CharField(max_length=10, verbose_name='Maksimum Kalp Atım Hızı', null=True, blank=True)
    direct_method = models.CharField(max_length=10, verbose_name='Direkt Yöntem', null=True,
                                     blank=True)  # HEARTBREATHING/VO2MAKS
    step_test = models.CharField(max_length=10, verbose_name='Basamak Testi', null=True, blank=True)
    rockport = models.CharField(max_length=10, verbose_name='Rockport 1-mil koş yürü', null=True, blank=True)
    rockporttime = models.CharField(max_length=10, null=True, blank=True)
    hand_grip = models.CharField(max_length=10, verbose_name='El Kavrama Kuvveti', null=True, blank=True)
    push_up = models.CharField(max_length=10, verbose_name='Push-up', null=True, blank=True)  # EYEBROW/LOKAL
    curl_up = models.CharField(max_length=10, verbose_name='Curl-up', null=True, blank=True)
    squat = models.CharField(max_length=10, verbose_name='Squad', null=True, blank=True)  # EYEBROW/1MT
    squat_1mt = models.CharField(max_length=10, verbose_name='1 MT', null=True, blank=True)
    squat_relatif = models.CharField(max_length=10, verbose_name='Relatif Kuvvet', null=True, blank=True)
    bench_1mt = models.CharField(max_length=10, verbose_name='1 MT', null=True, blank=True)
    bench_press = models.CharField(max_length=10, verbose_name="Bench Press", null=True, blank=True)
    bench_relatif = models.CharField(max_length=10, verbose_name='Relatif Kuvvet', null=True, blank=True)
    otur_uzan = models.CharField(max_length=10, verbose_name='Otur-Uzan', null=True, blank=True)  # FLEXIBILITY
    one_leg = models.CharField(max_length=10, verbose_name='Tek Bacak Denge', null=True, blank=True)
    blood_sugar = models.CharField(max_length=10, verbose_name='Açlık Kan Şekeri', null=True,
                                   blank=True)  # BLOOD/GLUCOSE
    insulin = models.CharField(max_length=10, verbose_name='Açlık Insülin', null=True, blank=True)
    hb1ac = models.CharField(max_length=10, verbose_name='HB1AC', null=True, blank=True)
    homosistein = models.CharField(max_length=10, verbose_name='Homosistein (umol/l)', null=True, blank=True)
    ldl = models.CharField(max_length=10, verbose_name='LDL', null=True, blank=True)
    hdl = models.CharField(max_length=10, verbose_name='HDL', null=True, blank=True)
    vdl = models.CharField(max_length=10, verbose_name='VDL  (mg/dl)', null=True, blank=True)
    trigliserit = models.CharField(max_length=10, verbose_name='Trigliserit', null=True, blank=True)
    kolesterol = models.CharField(max_length=10, verbose_name='Kolesterol', null=True, blank=True)
    kolesterol_hdl = models.CharField(max_length=10, verbose_name='Total Kolesterol/HDL Oranı', null=True, blank=True)
    sistolik = models.CharField(max_length=10, verbose_name='Sistolik Kan Basıncı', null=True, blank=True)
    diastolik = models.CharField(max_length=10, verbose_name='Diastolik Kan Basıncı', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('fitness-detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('fitness-update', kwargs={'id': self.id})

    def get_trainer_fitness_delete_url(self):
        return reverse('trainer-fitness-delete', kwargs={'id': self.id})

    def get_corporate_fitness_delete_url(self):
        return reverse('corporate-fitness-delete', kwargs={'id': self.id})

    def get_personal_fitness_delete_url(self):
        return reverse('personal-fitness-delete', kwargs={'id': self.id})

    class Meta:
        verbose_name = "Fitnes Ölçme ve Değerlendirme "
        verbose_name_plural = 'Fitnes Ölçüm '
