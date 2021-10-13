from datetime import datetime

from django.db import models
from django.urls import reverse

# Create your models here.
from registration.models import Trainer, Personal


class PosturInputs(models.Model):
    trainer = models.ForeignKey(to=Trainer, verbose_name="Antrenör", on_delete=models.CASCADE, blank=True, null=True)
    personal = models.ForeignKey(to=Personal, verbose_name="Danışan", on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(("Date"), default=datetime.now(), blank=True)
    normal_leg = models.CharField(verbose_name='Normal', max_length=100, null=True, blank=True)  # Ayak Tabanı Gözlem ve Değerlendirme
    over = models.CharField(verbose_name='Over pronasyon (İçe Basma)', max_length=100, null=True, blank=True)
    dorsi_fleksiyon = models.CharField(verbose_name='Dorsi-fleksiyon Kaybı', max_length=100, null=True, blank=True)
    plantar = models.CharField(verbose_name='Plantar Fasya Ağrısı', max_length=100, null=True, blank=True)
    gastroknemius = models.CharField(verbose_name='Gastroknemius Hassasiyeti', max_length=100, null=True, blank=True)
    other_leg = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)

    normal_knees_legs = models.CharField(verbose_name='Normal', max_length=100, null=True, blank=True)  # Diz ve Bacaklar Gözlem ve Değerlendirme
    genu = models.CharField(verbose_name='Genu Valgus (X bacak)', max_length=100, null=True, blank=True)
    knee_pain = models.CharField(verbose_name='Diz Ağrısı', max_length=100, null=True, blank=True)
    kripitasyon = models.CharField(verbose_name='Kripitasyon (Çıtlama) Varlığı', max_length=100, null=True, blank=True)
    other_knees_legs = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)

    normal_lumbo1 = models.CharField(verbose_name='Normal', max_length=100, null=True, blank=True)  # Lumbo-Pelvik Kalça Gözlem ve Değerlendirme
    lomber = models.CharField(verbose_name='Lomber Lordoz Artışı', max_length=100, null=True, blank=True)
    anterior = models.CharField(verbose_name='Anterior Pelvik Tilt ', max_length=100, null=True, blank=True)
    posterior = models.CharField(verbose_name='Posterior Pelvik Tilt', max_length=100, null=True, blank=True)
    unleveling = models.CharField(verbose_name='Unleveling Pelvis Sendromu', max_length=100, null=True, blank=True)
    gluteal = models.CharField(verbose_name='Gluteal Amnezi (Ölü Popo) Sendromu', max_length=100, null=True, blank=True)
    hip_pain = models.CharField(verbose_name='Kalça Ağrısı', max_length=100, null=True, blank=True)
    lower_back = models.CharField(verbose_name='Alt Sırt Ağrısı', max_length=100, null=True, blank=True)
    siyatik = models.CharField(verbose_name=' Siyatik Sinir Hassasiyeti', max_length=100, null=True, blank=True)
    other_lumbo1 = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_Torakal = models.CharField(verbose_name='Normal', max_length=100, null=True, blank=True)  # Torakal Omurga Gözlem ve Değerlendirme
    torakal_kifoz = models.CharField(verbose_name='Torakal Kifoz Artışı ', max_length=100, null=True, blank=True)
    sway_back = models.CharField(verbose_name='Sway Back (Lordoz artışı)', max_length=100, null=True, blank=True)
    flat_back = models.CharField(verbose_name='Flat Back (Düz Sırt)', max_length=100, null=True, blank=True)
    upper_tread = models.CharField(verbose_name='Üst Sırt Bölgesinde Ağrı', max_length=100, null=True, blank=True)
    other_torakal = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    shoulder_normal = models.CharField(verbose_name='Normal', max_length=100, null=True, blank=True)  # Omuz/Skapula/Kol Gözlem ve Değerlendirme
    protracted = models.CharField(verbose_name='Protracted Skapula (Yukarı Öne Açılmış Skapula)', max_length=100, null=True, blank=True)
    internal = models.CharField(verbose_name='İnternal Rotasyon (Kol) Varlığı', max_length=100, null=True, blank=True)
    round_shoulder = models.CharField(verbose_name='Round Shoulder (Dönmüş Omuz)', max_length=100, null=True, blank=True)
    elevated = models.CharField(verbose_name='Elevated Shoulder Blade (Yükselmiş Skapula)', max_length=100, null=True, blank=True)
    shoulder_pain = models.CharField(verbose_name='Omuz Ağrısı', max_length=100, null=True, blank=True)
    shoulder_mobility = models.CharField(verbose_name='Omuz Hareketliliğinde Azalma', max_length=100, null=True, blank=True)
    other_shoulder = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_chief = models.CharField(verbose_name='Normal', max_length=100, null=True, blank=True)  # Baş Gözlem ve Değerlendirme
    forward = models.CharField(verbose_name='Forward Head (İleri Baş) Sendromu', max_length=100, null=True, blank=True)
    servikal = models.CharField(verbose_name='Servikal Lordoz Artışı', max_length=100, null=True, blank=True)
    head_neck_pain = models.CharField(verbose_name='Baş-Boyun Ağrısı', max_length=100, null=True, blank=True)
    head_neck_mobility = models.CharField(verbose_name='Baş-Boyun Hareket Kaybı', max_length=100, null=True, blank=True)
    other_chief = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_anke = models.CharField(verbose_name='Normal Konum', max_length=100, null=True, blank=True)  # Overhead Squat Testi #Ayak Bileği
    foot_flattening = models.CharField(verbose_name='Ayak düzleşmesi ', max_length=100, null=True, blank=True)
    over1 = models.CharField(verbose_name='Over pronasyon', max_length=100, null=True, blank=True)
    turning_outside = models.CharField(verbose_name='Dışa dönme', max_length=100, null=True, blank=True)
    heel_lift = models.CharField(verbose_name='Topuk kalkma', max_length=100, null=True, blank=True)
    other_anke = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_knee = models.CharField(verbose_name='Normal Hizalama', max_length=100, null=True, blank=True)  # Diz
    varum = models.CharField(verbose_name='Dışa dönme (Varum) ', max_length=100, null=True, blank=True)
    valgus = models.CharField(verbose_name='İçe Çökme (Valgus)', max_length=100, null=True, blank=True)
    slip_forward = models.CharField(verbose_name='Öne Kayma', max_length=100, null=True, blank=True)
    other_knee = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_lumbo2 = models.CharField(verbose_name='Normal Konum', max_length=100, null=True, blank=True)  # Lumbo Pelvik Kalça Kuşağı
    lordotik_plus = models.CharField(verbose_name='Artmış Lordotik Eğri', max_length=100, null=True, blank=True)
    lordotik = models.CharField(verbose_name='Azalmış Lordotik Eğri', max_length=100, null=True, blank=True)
    hip_asymmetry = models.CharField(verbose_name='Kalça Asimetrisi', max_length=100, null=True, blank=True)
    body_shifting = models.CharField(verbose_name='Gövdenin Öne Kayması', max_length=100, null=True, blank=True)
    other_lumbo2 = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    shoulder_crossed = models.CharField(verbose_name='Omuz – Kolların Öne Kayması', max_length=100, null=True, blank=True)  # Omuzlar
    falling_arms = models.CharField(verbose_name='Kolların Düşmes', max_length=100, null=True, blank=True)
    other_shoulder1 = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_head_neck = models.CharField(verbose_name='Normal Konum', max_length=100, null=True, blank=True)  # Baş-Boyun
    head_bowing = models.CharField(verbose_name='Başın Öne Kayması', max_length=100, null=True, blank=True)
    neck_curve = models.CharField(verbose_name='Boyun Eğrisinin Artması', max_length=100, null=True, blank=True)
    other_head_neck = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_knee1 = models.CharField(verbose_name='Normal Hizalama', max_length=100, null=True, blank=True)  # Single Leg Squat Testi  # Diz
    valgus1 = models.CharField(verbose_name='İçe Çökme (Valgus)', max_length=100, null=True, blank=True)
    slip_forward1 = models.CharField(verbose_name='Öne Kayma ', max_length=100, null=True, blank=True)
    other_knee1 = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_lumbo3 = models.CharField(verbose_name='Normal Hizalama', max_length=100, null=True, blank=True)  # Lumbo Pelvik Kalça Kuşağı
    hip_rise = models.CharField(verbose_name='Kalçanın Yükselmesi', max_length=100, null=True, blank=True)
    drop_hip = models.CharField(verbose_name='Kalçanın Düşmesi', max_length=100, null=True, blank=True)
    other_lumbo3 = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_upper_body = models.CharField(verbose_name='Normal Konum', max_length=100, null=True, blank=True)  # Üst Vücut
    front_into_body = models.CharField(verbose_name='Gövdenin Öne-İçeri Kayması', max_length=100, null=True, blank=True)
    back_out_body = models.CharField(verbose_name='Gövdenin Geriye-Dışarı Kayması', max_length=100, null=True, blank=True)
    other_upper_body = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_lumbo4 = models.CharField(verbose_name='Normal Hizalama', max_length=100, null=True, blank=True)  # Push-up Testi # Lumbo Pelvik Kalça Kuşağı
    lordotik_collapse = models.CharField(verbose_name='Lordotik Eğrinin Artması (Aşağı Çökme)', max_length=100, null=True, blank=True)
    lordotik_up = models.CharField(verbose_name='Lordotik Eğrinin Azalması (Yukarı Kalkma)', max_length=100, null=True, blank=True)
    other_lumbo4 = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_shoulder = models.CharField(verbose_name='Normal Hizalama', max_length=100, null=True, blank=True)  # Omuzlar
    shoulder_up = models.CharField(verbose_name='Omuzların Yükselmesi', max_length=100, null=True, blank=True)
    skap_shoulder = models.CharField(verbose_name='Skapulaların Kanatlaşması', max_length=100, null=True, blank=True)
    other_shoulder2 = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_head_neck1 = models.CharField(verbose_name='Normal Hizalama', max_length=100, null=True, blank=True)  # Baş-Boyun Omurları
    hiper_ekstansiyon = models.CharField(verbose_name='Hiper-ekstansiyon Artışı', max_length=100, null=True, blank=True)
    other_head_neck1 = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_lumbo5 = models.CharField(verbose_name='Normal Hizalama', max_length=100, null=True, blank=True)  # Standing Row Testi # Lumbo Pelvik Kalça Kuş
    lordotik_collapse1 = models.CharField(verbose_name='Lordotik Eğrinin Artması (Aşağı Çökme)', max_length=100, null=True, blank=True)
    other_lumbo5 = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_shoulder1 = models.CharField(verbose_name='Normal Hizalama', max_length=100, null=True, blank=True)  # Omuzlar
    shoulder_up1 = models.CharField(verbose_name='Omuzların Yükselmesi', max_length=100, null=True, blank=True)
    other_shoulder3 = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_head_neck2 = models.CharField(verbose_name='Normal Hizalama', max_length=100, null=True, blank=True)  # Baş-Boyun Omurları
    head_forward = models.CharField(verbose_name='Başın İleri Kayması', max_length=100, null=True, blank=True)
    other_head_neck2 = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_horizontal = models.CharField(verbose_name='Normal', max_length=100, null=True, blank=True)  # Üst Ekstremite Postürel Değerlendirmeler
    shoulder_up2 = models.CharField(verbose_name='Omuzların Yükselmesi', max_length=100, null=True, blank=True)  # Horizontal Abdüksiyon Testi
    shoulder_protraksiyon = models.CharField(verbose_name='Omuzların Protraksiyonu', max_length=100, null=True, blank=True)
    fleks = models.CharField(verbose_name='Dirseklerin Flekse Olması', max_length=100, null=True, blank=True)
    other_horizontal = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_rotasyon = models.CharField(verbose_name='Normal', max_length=100, null=True, blank=True)  # Rotasyon Testi
    shoulder_up3 = models.CharField(verbose_name='Omuzların Yükselmesi', max_length=100, null=True, blank=True)
    shoulder_protraksiyon1 = models.CharField(verbose_name='Omuzların Protraksiyonu', max_length=100, null=True, blank=True)
    internal_rotasyon = models.CharField(verbose_name='Ellerin Duvardan Uzaklaşması – İnternal Rotasyonda', max_length=100, null=True, blank=True)
    eksternal_rotasyon = models.CharField(verbose_name='Ellerin Duvardan Uzaklaşması – Eksternal Rotasyonda', max_length=100, null=True, blank=True)
    other_rotasyon = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_fleksiyon = models.CharField(verbose_name='Normal', max_length=100, null=True, blank=True)  # Omuz Fleksiyon Testi
    shoulder_up4 = models.CharField(verbose_name='Omuzların Yükselmesi', max_length=100, null=True, blank=True)
    lomber_lordoz = models.CharField(verbose_name='Lomber Lordoz Artışı', max_length=100, null=True, blank=True)
    fleks1 = models.CharField(verbose_name='Dirseklerin Fleksiyonu', max_length=100, null=True, blank=True)
    other_fleksiyon = models.CharField(max_length=200, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('postural-detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('postural-update', kwargs={'id': self.id})

    def get_trainer_postural_delete_url(self):
        return reverse('trainer-postural-delete', kwargs={'id': self.id})

    def get_corporate_postural_delete_url(self):
        return reverse('corporate-postural-delete', kwargs={'id': self.id})

    def get_personal_postural_delete_url(self):
        return reverse('personal-postural-delete', kwargs={'id': self.id})

    class Meta:
        verbose_name = "Postürel Ölçme ve Değerlendirme "
        verbose_name_plural = 'Postürel Ölçüm'
