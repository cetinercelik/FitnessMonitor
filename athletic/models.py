from django.urls import reverse

from django.db import models

# Create your models here.
from registration.models import Trainer, Personal
from datetime import datetime


class AthleticInpt(models.Model):
    trainer = models.ForeignKey(to=Trainer, verbose_name="Antrenör", on_delete=models.CASCADE, blank=True, null=True)
    personal = models.ForeignKey(to=Personal, verbose_name="Danışan", on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(("Date"), default=datetime.now(), blank=True)
    shoulder = models.CharField(max_length=5, verbose_name='Omuz', blank=True, null=True)
    chest = models.CharField(max_length=5, verbose_name='Göğüs', blank=True, null=True)
    biseps = models.CharField(max_length=5, verbose_name='Biseps', blank=True, null=True)
    wrist = models.CharField(max_length=5, verbose_name='El Bileği', blank=True, null=True)
    waist = models.CharField(max_length=5, verbose_name='Bel Çevresi', blank=True, null=True)
    hip = models.CharField(max_length=5, verbose_name='Kalça Çevresi', blank=True, null=True)
    knee = models.CharField(max_length=5, verbose_name='Diz Çevresi', blank=True, null=True)
    upper_leg = models.CharField(max_length=5, verbose_name='Üst Bacak', blank=True, null=True)
    gastrocnemius = models.CharField(max_length=5, verbose_name='Gastrocnemius', blank=True, null=True)
    ankle = models.CharField(max_length=5, verbose_name='Ayak Bileği', blank=True, null=True)

    man3ch = models.CharField(verbose_name='Chest', max_length=5, blank=True, null=True)  # BODYCOMPOSITION/BODYOIL
    man3tri = models.CharField(verbose_name='Triceps', max_length=5, blank=True, null=True)
    man3sub = models.CharField(verbose_name='Subscapula', max_length=5, blank=True, null=True)
    woman3tri = models.CharField(verbose_name='Triceps', max_length=5, blank=True, null=True)
    woman3abd = models.CharField(verbose_name='Abdomen', max_length=5, blank=True, null=True)
    woman3sub = models.CharField(verbose_name='Suprailiac', max_length=5, blank=True, null=True)
    man7ch = models.CharField(verbose_name='Chest', max_length=5, blank=True, null=True)
    man7tr = models.CharField(verbose_name='Triceps', max_length=5, blank=True, null=True)
    man7sub = models.CharField(verbose_name='Subscapula', max_length=5, blank=True, null=True)
    man7sic = models.CharField(verbose_name='Suprailiac', max_length=5, blank=True, null=True)
    man7mid = models.CharField(verbose_name='Midaxillary', max_length=5, blank=True, null=True)
    man7abd = models.CharField(verbose_name='Abdomen', max_length=5, blank=True, null=True)
    man7th = models.CharField(verbose_name='Thigh', max_length=5, blank=True, null=True)
    woman7ch = models.CharField(verbose_name='Chest', max_length=5, blank=True, null=True)
    woman7tri = models.CharField(verbose_name='Triceps', max_length=5, blank=True, null=True)
    woman7sub = models.CharField(verbose_name='Subscapula', max_length=5, blank=True, null=True)
    woman7sic = models.CharField(verbose_name='Suprailiac', max_length=5, blank=True, null=True)
    woman7mid = models.CharField(verbose_name='Midaxillary', max_length=5, blank=True, null=True)
    woman7abd = models.CharField(verbose_name='Abdomen', max_length=5, blank=True, null=True)
    woman7th = models.CharField(verbose_name='Thigh', max_length=5, blank=True, null=True)

    humerus = models.CharField(max_length=5, verbose_name='Humerus Bikondil', blank=True, null=True)
    femur = models.CharField(max_length=5, verbose_name='Femur Bikondil', blank=True, null=True)
    corrected_biseps = models.CharField(max_length=5, verbose_name='Düzeltilmiş Biseps Çevre', blank=True, null=True)
    corrected_gastrocnemius = models.CharField(max_length=5, verbose_name='Düzeltilmiş Gastrocnemius Çevre',
                                               blank=True, null=True)
    heart_rate = models.CharField(max_length=5, verbose_name='Dinlenim Kalp Atım Hızı', blank=True, null=True)
    ir1_test = models.CharField(max_length=5, verbose_name='Yo Yo IR-1 Testi (m)', blank=True, null=True)
    ir2_test = models.CharField(max_length=5, verbose_name='Yo Yo IR-2 Testi (m)', blank=True, null=True)
    ift_test = models.CharField(max_length=5, verbose_name='30-15 IFT Testi', blank=True, null=True)
    rast_test_dist = models.CharField(max_length=5, verbose_name='RAST Test (Mesafe)', blank=True, null=True)
    rast_test_time = models.CharField(max_length=5, verbose_name='RAST Test (Zaman)', blank=True, null=True)
    bruce_protokol = models.CharField(max_length=5, verbose_name='Bruce Protokolü (dk)', blank=True, null=True)
    cooper = models.CharField(max_length=5, verbose_name='Cooper (12 dk) Testi (m)', blank=True, null=True)
    shuttle_test = models.CharField(max_length=5, verbose_name='20 m Mekik Testi (seviye)', blank=True, null=True)
    step_test = models.CharField(max_length=5, verbose_name='Basamak Testi (atım/dk)', blank=True, null=True)
    bla = models.CharField(max_length=5, verbose_name='BLa', blank=True, null=True)
    laktat_heart_rate = models.CharField(max_length=5, verbose_name='Kalp Atım Hızı', blank=True, null=True)
    vo2maks = models.CharField(max_length=5, verbose_name='VO2maks', blank=True, null=True)
    maximal_power = models.CharField(max_length=5, verbose_name='Maksimal Güç (watt)', blank=True,
                                     null=True)  # Anaerobik Güç
    average_power = models.CharField(max_length=5, verbose_name='Ortalama Güç (watt)', blank=True, null=True)
    tiredness = models.CharField(max_length=5, verbose_name='Yorgunluk İndeksi (%)', blank=True, null=True)
    vertical_leap1 = models.CharField(max_length=5, verbose_name='Dikey Sıçrama(cm) 1:', blank=True, null=True)
    vertical_leap2 = models.CharField(max_length=5, verbose_name='Dikey Sıçrama(cm) 2:', blank=True, null=True)
    vertical_leap3 = models.CharField(max_length=5, verbose_name='Dikey Sıçrama(cm) 3:', blank=True, null=True)
    horizantal_leap1 = models.CharField(max_length=5, verbose_name='Yatay Sıçrama (cm) 1:', blank=True, null=True)
    horizantal_leap2 = models.CharField(max_length=5, verbose_name='Yatay Sıçrama (cm) 2:', blank=True, null=True)
    horizantal_leap3 = models.CharField(max_length=5, verbose_name='Yatay Sıçrama (cm) 3:', blank=True, null=True)
    distance1 = models.CharField(max_length=5, verbose_name='Mesafe1-(cm)', blank=True,
                                 null=True)  # Sağlık topu fırlatma
    distance2 = models.CharField(max_length=5, verbose_name='Mesafe2-(cm)', blank=True, null=True)
    distance3 = models.CharField(max_length=5, verbose_name='Mesafe2-(cm)', blank=True, null=True)
    five1 = models.CharField(max_length=5, verbose_name='1-5m', blank=True, null=True)  # Doğrusal Hız Testleri
    five2 = models.CharField(max_length=5, verbose_name='2-5m', blank=True, null=True)
    five3 = models.CharField(max_length=5, verbose_name='2-5m', blank=True, null=True)
    ten1 = models.CharField(max_length=5, verbose_name='1-10m', blank=True, null=True)
    ten2 = models.CharField(max_length=5, verbose_name='2-10m', blank=True, null=True)
    ten3 = models.CharField(max_length=5, verbose_name='3-10m', blank=True, null=True)
    twenty1 = models.CharField(max_length=5, verbose_name='1-20m', blank=True, null=True)
    twenty2 = models.CharField(max_length=5, verbose_name='1-20m', blank=True, null=True)
    twenty3 = models.CharField(max_length=5, verbose_name='1-20m', blank=True, null=True)
    thirty1 = models.CharField(max_length=5, verbose_name='1-30m', blank=True, null=True)
    thirty2 = models.CharField(max_length=5, verbose_name='1-30m', blank=True, null=True)
    thirty3 = models.CharField(max_length=5, verbose_name='1-30m', blank=True, null=True)
    fourty1 = models.CharField(max_length=5, verbose_name='1-40m', blank=True, null=True)
    fourty2 = models.CharField(max_length=5, verbose_name='1-40m', blank=True, null=True)
    fourty3 = models.CharField(max_length=5, verbose_name='1-40m', blank=True, null=True)
    illinois1 = models.CharField(max_length=5, verbose_name='İllinois Çeviklik Testi', blank=True,
                                 null=True)  # Çeviklik
    illinois2 = models.CharField(max_length=5, verbose_name='İllinois Çeviklik Testi', blank=True, null=True)
    illinois3 = models.CharField(max_length=5, verbose_name='İllinois Çeviklik Testi', blank=True, null=True)
    tLine1 = models.CharField(max_length=5, verbose_name='1-T Line Testi ', blank=True, null=True)
    tLine2 = models.CharField(max_length=5, verbose_name='2-T Line Testi ', blank=True, null=True)
    tLine3 = models.CharField(max_length=5, verbose_name='3-T Line Testi ', blank=True, null=True)
    koni_test1 = models.CharField(max_length=5, verbose_name='3 Koni Testi', blank=True, null=True)
    koni_test2 = models.CharField(max_length=5, verbose_name='3 Koni Testi', blank=True, null=True)
    koni_test3 = models.CharField(max_length=5, verbose_name='3 Koni Testi', blank=True, null=True)
    edgren1 = models.CharField(max_length=5, verbose_name='Edgren Side Testi ', blank=True, null=True)
    edgren2 = models.CharField(max_length=5, verbose_name='Edgren Side Testi ', blank=True, null=True)
    edgren3 = models.CharField(max_length=5, verbose_name='Edgren Side Testi ', blank=True, null=True)
    agility1 = models.CharField(max_length=5, verbose_name='505 Agility Testi', blank=True, null=True)
    agility2 = models.CharField(max_length=5, verbose_name='505 Agility Testi', blank=True, null=True)
    agility3 = models.CharField(max_length=5, verbose_name='505 Agility Testi', blank=True, null=True)
    pro_agility1 = models.CharField(max_length=5, verbose_name='Pro-Agility Test (5-10-5)', blank=True, null=True)
    pro_agility2 = models.CharField(max_length=5, verbose_name='Pro-Agility Test (5-10-5)', blank=True, null=True)
    pro_agility3 = models.CharField(max_length=5, verbose_name='Pro-Agility Test (5-10-5)', blank=True, null=True)
    heksogen1 = models.CharField(max_length=5, verbose_name='Heksogen Testi ', blank=True, null=True)
    heksogen2 = models.CharField(max_length=5, verbose_name='Heksogen Testi ', blank=True, null=True)
    heksogen3 = models.CharField(max_length=5, verbose_name='Heksogen Testi ', blank=True, null=True)
    right1 = models.CharField(max_length=5, verbose_name='1-Sağ(kg)',
                              blank=True, null=True)  # Kas Kuvveti Dayanıklılığı/El Kavrama Kuvveti (kg)
    right2 = models.CharField(max_length=5, verbose_name='2-Sağ(kg)', blank=True, null=True)
    right3 = models.CharField(max_length=5, verbose_name='3-Sağ(kg)', blank=True, null=True)
    left1 = models.CharField(max_length=5, verbose_name='1-Sol(kg)', blank=True, null=True)
    left2 = models.CharField(max_length=5, verbose_name='2-Sol(kg)', blank=True, null=True)
    left3 = models.CharField(max_length=5, verbose_name='3-Sol(kg)', blank=True, null=True)
    pushup = models.CharField(max_length=5, verbose_name='Push-up(tekrar)', blank=True,
                              null=True)  # Lokal Kas Dayanıklılığı
    curlup = models.CharField(max_length=5, verbose_name='Curl-up (tekrar)', blank=True, null=True)
    bench_press = models.CharField(max_length=5, verbose_name='Bench Press (tekrar)', blank=True, null=True)
    pullup = models.CharField(max_length=5, verbose_name='Pull-up (tekrar)', blank=True, null=True)
    modified_pullup = models.CharField(max_length=5, verbose_name='Modified Pull-up (tekrar)', blank=True, null=True)
    flexed = models.CharField(max_length=5, verbose_name='Flexed Arm Hang (süre)', blank=True, null=True)
    squat_mt = models.CharField(max_length=5, verbose_name='6 MT (Squat - kg)', blank=True, null=True)  # Squat
    lifting_squat = models.CharField(max_length=5, verbose_name='Kaldırma Hızı (Squat - sn)', blank=True, null=True)
    bench_mt = models.CharField(max_length=5, verbose_name=' 6 MT (Bench press - kg)', blank=True,
                                null=True)  # Bench Press
    lifting_bench = models.CharField(max_length=5, verbose_name='Kaldırma Hızı (Bench press - sn)', blank=True,
                                     null=True)
    kuadriseps60 = models.CharField(max_length=5, verbose_name='Kuadriseps (60°)', blank=True,
                                    null=True)  # İsokinetik /60o
    hamstring60 = models.CharField(max_length=5, verbose_name='Hamstring (60°)', blank=True, null=True)
    kuadriseps180 = models.CharField(max_length=5, verbose_name='Kuadriseps (180°)', blank=True, null=True)  # 180
    hamstring180 = models.CharField(max_length=5, verbose_name='Hamstring (180°)', blank=True, null=True)
    kuadriseps300 = models.CharField(max_length=5, verbose_name='Kuadriseps (300°)', blank=True, null=True)  # 300
    hamstring300 = models.CharField(max_length=5, verbose_name='Hamstring (300°)', blank=True, null=True)
    normal_overhead = models.CharField(max_length=40, verbose_name='Normal', blank=True,
                                       null=True)  # Hareket Kalitesi, Esneklik ve Denge/Overhead
    glenohumeral_overhead = models.CharField(max_length=40, verbose_name='Glenohumeral İmmobilite', blank=True,
                                             null=True)
    torakal_overhead = models.CharField(max_length=40, verbose_name='Torakal İmmobilite', blank=True, null=True)
    dinamic_overhead = models.CharField(max_length=40, verbose_name='Tüm Vücut Dinamik İmmobilite Varlığı', blank=True,
                                        null=True)
    leg_overhead = models.CharField(max_length=40, verbose_name='Ayak Bileği İmmobilitesi', blank=True, null=True)
    knee_overhead = models.CharField(max_length=40, verbose_name='Diz İnstabilitesi', blank=True, null=True)
    hip_overhead = models.CharField(max_length=40, verbose_name='Kalça İmmobilitesi', blank=True, null=True)
    balance_overhead = models.CharField(max_length=40, verbose_name='Denge Kayıpları (zayıf motor kontrol)', blank=True,
                                        null=True)
    ache_overhead = models.CharField(max_length=40, verbose_name='Ağrı Varlığı', blank=True, null=True)
    other_overhead = models.CharField(max_length=50, verbose_name='Diğer Bulgular ve Yorumlar (varsa)', blank=True,
                                      null=True)
    normal_squat = models.CharField(max_length=40, verbose_name='Normal', blank=True,
                                    null=True)  # Tek Bacak Squat Testi (Sağ-Sol Taraf İçin)
    torakal_squat = models.CharField(max_length=40, verbose_name='Torakal İmmobilite', blank=True, null=True)
    dinamic_squat = models.CharField(max_length=40, verbose_name='Tüm Vücut Dinamik İmmobilite Varlığı', blank=True,
                                     null=True)
    leg_squat = models.CharField(max_length=40, verbose_name='Ayak Bileği İmmobilitesi', blank=True, null=True)
    knee_squat = models.CharField(max_length=40, verbose_name='Diz İnstabilitesi', blank=True, null=True)
    hip_squat = models.CharField(max_length=40, verbose_name='Kalça İmmobilitesi', blank=True, null=True)
    balance_squat = models.CharField(max_length=40, verbose_name='Denge Kayıpları (zayıf motor kontrol)', blank=True,
                                     null=True)
    ache_squat = models.CharField(max_length=40, verbose_name=' Ağrı Varlığı', blank=True, null=True)
    other_squat = models.CharField(max_length=50, verbose_name='Diğer Bulgular ve Yorumlar (varsa)', blank=True,
                                   null=True)
    normal_bridge = models.CharField(max_length=40, verbose_name='Normal', blank=True, null=True)
    hip_bridge = models.CharField(max_length=40, verbose_name='Kalça Fleksiyon Artışı', blank=True, null=True)
    balance_bridge = models.CharField(max_length=40, verbose_name='Denge Kayıpları (zayıf motor kontrol)', blank=True,
                                      null=True)
    dinamic_bridge = models.CharField(max_length=40, verbose_name='Tüm Vücut Dinamik İmmobilite Varlığı', blank=True,
                                      null=True)
    knee_bridge = models.CharField(max_length=40, verbose_name='Diz İnstabilitesi', blank=True, null=True)
    hip_immobilit = models.CharField(max_length=40, verbose_name='Kalça İmmobilitesi', blank=True, null=True)
    hamstring_bridge = models.CharField(max_length=40, verbose_name='Hamstring Gerginliği', blank=True, null=True)
    kuadriseps_bridge = models.CharField(max_length=40, verbose_name='Kuadriseps Gerginliği', blank=True, null=True)
    ache_bridge = models.CharField(max_length=40, verbose_name='Ağrı Varlığı', blank=True, null=True)
    other_bridge = models.CharField(max_length=50, verbose_name='Diğer Bulgular ve Yorumlar (varsa)', blank=True,
                                    null=True)
    normal_lunge = models.CharField(max_length=40, verbose_name='Normal', blank=True,
                                    null=True)  # Lunge Testi (Sağ-Sol Taraf İçin)
    patello_lunge = models.CharField(max_length=40, verbose_name='Patello-Femoral Kayma', blank=True, null=True)
    over_lunge = models.CharField(max_length=40, verbose_name='Over-pronasyon', blank=True, null=True)
    fleksiyon_lunge = models.CharField(max_length=40, verbose_name='Gövde Fleksiyon Artışı', blank=True, null=True)
    balance_lunge = models.CharField(max_length=40, verbose_name='Denge Kayıpları (zayıf motor kontrol)', blank=True,
                                     null=True)
    dinamic_lunge = models.CharField(max_length=40, verbose_name='Tüm Vücut Dinamik İmmobilite Varlığı', blank=True,
                                     null=True)
    leg_lunge = models.CharField(max_length=40, verbose_name='Ayak Bileği İmmobilitesi', blank=True, null=True)
    knee_lunge = models.CharField(max_length=40, verbose_name='Diz İnstabilitesi', blank=True, null=True)
    hip_lunge = models.CharField(max_length=40, verbose_name='Kalça İmmobilitesi', blank=True, null=True)
    ache_lunge = models.CharField(max_length=40, verbose_name='Ağrı Varlığı', blank=True, null=True)
    other_lunge = models.CharField(max_length=50, verbose_name='Diğer Bulgular ve Yorumlar (varsa)', blank=True,
                                   null=True)
    normal_trunk = models.CharField(max_length=40, verbose_name='Normal', blank=True,
                                    null=True)  # Trunk Stability (Push-up)
    core_trunk = models.CharField(max_length=40, verbose_name='Core Stabilizasyon Kaybı', blank=True, null=True)
    skapula_trunk = models.CharField(max_length=40, verbose_name=' Skapula İnstabilizasyon', blank=True, null=True)
    hip_trunk = models.CharField(max_length=40, verbose_name='Kalça İmmobilitesi', blank=True, null=True)
    lomber_trunk = models.CharField(max_length=40, verbose_name='Lomber Lordoz Artışı', blank=True, null=True)
    balance_trunk = models.CharField(max_length=40, verbose_name=' Denge Kayıpları (zayıf motor kontrol)', blank=True,
                                     null=True)
    ache_trunk = models.CharField(max_length=40, verbose_name='Ağrı Varlığı', blank=True, null=True)
    other_trunk = models.CharField(max_length=50, verbose_name='Diğer Bulgular ve Yorumlar (varsa)', blank=True,
                                   null=True)
    normal_shoulder = models.CharField(max_length=40, verbose_name='Normal', blank=True,
                                       null=True)  # Shoulder Mobility (Sağ-Sol Taraf İçin)
    core_shoulder = models.CharField(max_length=40, verbose_name='Core Stabilizasyon Kaybı', blank=True, null=True)
    skapula_shoulder = models.CharField(max_length=40, verbose_name='Skapulo-Torasik İnstabilite - İmmobilite',
                                        blank=True, null=True)
    gleno_shoulder = models.CharField(max_length=40, verbose_name=' Gleno-Humeral Disfonksiyon', blank=True, null=True)
    balance_shoulder = models.CharField(max_length=40, verbose_name='Denge Kayıpları (zayıf motor kontrol)', blank=True,
                                        null=True)
    ache_shoulder = models.CharField(max_length=40, verbose_name='Ağrı Varlığı', blank=True, null=True)
    other_shoulder = models.CharField(max_length=50, verbose_name='Diğer Bulgular ve Yorumlar (varsa)', blank=True,
                                      null=True)
    normal_active = models.CharField(max_length=40, verbose_name='Normal', blank=True,
                                     null=True)  # Active Straight Leg Raise Test (Sağ-Sol Taraf İçin)
    pelvik_aktive = models.CharField(max_length=40, verbose_name='Pelvik Kontrol Kaybı', blank=True, null=True)
    hip_active = models.CharField(max_length=40, verbose_name='Kalça İmmobilitesi (Karşı taraf)', blank=True, null=True)
    hip_ekstansiyon_active = models.CharField(max_length=40, verbose_name='Kalça Ekstansiyon Disfonksiyonu', blank=True,
                                              null=True)
    hamstring_active = models.CharField(max_length=40, verbose_name=' Hamstring Gerginliği', blank=True, null=True)
    lomber_active = models.CharField(max_length=40, verbose_name='Lomber Lordoz Artışı', blank=True, null=True)
    rotasyon_active = models.CharField(max_length=50, verbose_name='Artmış Gövde Rotasyon (kaldırılan bacak yönüne)',
                                       blank=True, null=True)
    ache_active = models.CharField(max_length=40, verbose_name='Ağrı Varlığı (Sakro-iliak eklem)', blank=True,
                                   null=True)
    other_active = models.CharField(max_length=50, verbose_name='Diğer Bulgular ve Yorumlar (varsa)', blank=True,
                                    null=True)
    normal_rotary = models.CharField(max_length=40, verbose_name='Normal', blank=True,
                                     null=True)  # Rotary Stability (Sağ-Sol Taraf İçin)
    core_rotary = models.CharField(max_length=40, verbose_name='Core İnstabilitesi', blank=True, null=True)
    body_rotary = models.CharField(max_length=40, verbose_name='Gövde İnstabilitesi', blank=True, null=True)
    hip_rotary = models.CharField(max_length=40, verbose_name='Kalça-Diz-Omuz İmmobilitesi', blank=True, null=True)
    balance_rotary = models.CharField(max_length=40, verbose_name=' Denge Kayıpları (zayıf motor kontrol)', blank=True,
                                      null=True)
    ache_rotary = models.CharField(max_length=40, verbose_name='Ağrı Varlığı', blank=True, null=True)
    other_rotary = models.CharField(max_length=50, verbose_name='Diğer Bulgular ve Yorumlar (varsa)', blank=True,
                                    null=True)
    normal_front = models.CharField(max_length=40, verbose_name='Normal', blank=True,
                                    null=True)  # Front Plank Dayanıklılık Testi
    pelvisin_front = models.CharField(max_length=40, verbose_name='Pelvisin Aşağı Çökmesi', blank=True, null=True)
    core_front = models.CharField(max_length=40, verbose_name='Core İnstabilitesi', blank=True, null=True)
    body_front = models.CharField(max_length=40, verbose_name='Gövde Hizalama Sorunları', blank=True, null=True)
    arm_front = models.CharField(max_length=40, verbose_name='Kol-Omuz İnstabilitesi', blank=True, null=True)
    ache_front = models.CharField(max_length=40, verbose_name='Ağrı Varlığı (Lomber Omurga)', blank=True, null=True)
    other_front = models.CharField(max_length=50, verbose_name='Diğer Bulgular ve Yorumlar (varsa)', blank=True,
                                   null=True)
    normal_side = models.CharField(max_length=40, verbose_name='Normal', blank=True,
                                   null=True)  # Side Plank Dayanıklılık Testi
    pelvisin_side = models.CharField(max_length=40, verbose_name='Pelvisin Aşağı Çökmesi', blank=True, null=True)
    core_side = models.CharField(max_length=40, verbose_name='Core İnstabilitesi', blank=True, null=True)
    body_side = models.CharField(max_length=40, verbose_name='Gövde Hizalama Sorunları', blank=True, null=True)
    leg_side = models.CharField(max_length=40, verbose_name=' Ayak İnstabilitesi', blank=True, null=True)
    arm_side = models.CharField(max_length=40, verbose_name='Kol-Omuz İnstabilitesi', blank=True, null=True)
    ache_side = models.CharField(max_length=40, verbose_name=' Ağrı Varlığı (Lomber Omurga)', blank=True, null=True)
    other_side = models.CharField(max_length=50, verbose_name='Diğer Bulgular ve Yorumlar (varsa)', blank=True,
                                  null=True)
    normal_fleksor = models.CharField(max_length=40, verbose_name='Normal', blank=True,
                                      null=True)  # Gövde Fleksör Dayanıklılık Testi
    body_fleksor = models.CharField(max_length=40, verbose_name='Gövdenin Geriye Kayması', blank=True, null=True)
    core_fleksor = models.CharField(max_length=40, verbose_name='Core İnstabilitesi', blank=True, null=True)
    body_line_fleksor = models.CharField(max_length=40, verbose_name='Gövde Hizalama Sorunları', blank=True, null=True)
    hamstring_fleksor = models.CharField(max_length=40, verbose_name='Hamstring Gerginliği', blank=True, null=True)
    kuadriseps_fleksor = models.CharField(max_length=40, verbose_name='Kuadriseps Gerginliği', blank=True, null=True)
    leg_fleksor = models.CharField(max_length=40, verbose_name='Ayak İnstabilitesi', blank=True, null=True)
    ache_fleksor = models.CharField(max_length=40, verbose_name='Ağrı Varlığı (Lomber Omurga)', blank=True, null=True)
    other_fleksor = models.CharField(max_length=50, verbose_name='Diğer Bulgular ve Yorumlar (varsa)', blank=True,
                                     null=True)
    normal_extansor = models.CharField(max_length=40, verbose_name='Normal', blank=True,
                                       null=True)  # Gövde Ekstansör Dayanıklılık Testi
    body_extansor = models.CharField(max_length=40, verbose_name='Gövdenin Öne Kayması', blank=True, null=True)
    core_extansor = models.CharField(max_length=40, verbose_name='Core İnstabilitesi', blank=True, null=True)
    body_line_extansor = models.CharField(max_length=40, verbose_name=' Gövde Hizalama Sorunları', blank=True,
                                          null=True)
    lomber_extansor = models.CharField(max_length=40, verbose_name='Lomber Lordoz Artışı', blank=True, null=True)
    hamstring_extansor = models.CharField(max_length=40, verbose_name='Hamstring Gerginliği', blank=True, null=True)
    kuadriseps_extansor = models.CharField(max_length=40, verbose_name='Kuadriseps Gerginliği', blank=True, null=True)
    ache_extansor = models.CharField(max_length=40, verbose_name='Ağrı Varlığı (Lomber Omurga)', blank=True, null=True)
    other_extansor = models.CharField(max_length=50, verbose_name='Diğer Bulgular ve Yorumlar (varsa)', blank=True,
                                      null=True)
    open1 = models.CharField(max_length=5, verbose_name='Süre 1', blank=True,
                             null=True)  # Tek Bacak Denge Testi/Gözler Açık
    open2 = models.CharField(max_length=5, verbose_name='Süre 2', blank=True, null=True)
    open3 = models.CharField(max_length=5, verbose_name='Süre 3', blank=True, null=True)
    close1 = models.CharField(max_length=5, verbose_name='Süre 1', blank=True, null=True)
    close2 = models.CharField(max_length=5, verbose_name='Süre 2', blank=True, null=True)
    close3 = models.CharField(max_length=5, verbose_name='Süre 3', blank=True, null=True)
    star_test = models.CharField(max_length=5, verbose_name='Bacak Uzunluğu', blank=True,
                                 null=True)  # Yıldız Denge Testi/3 yön
    anterior = models.CharField(max_length=5, verbose_name='Anterior', blank=True, null=True)
    postero = models.CharField(max_length=5, verbose_name='Postero-medial', blank=True, null=True)
    postero_lateral = models.CharField(max_length=5, verbose_name='Postero-lateral', blank=True, null=True)

    all_anterior = models.CharField(max_length=5, verbose_name='Anterior', blank=True, null=True)
    lateral = models.CharField(max_length=5, verbose_name='Antero-lateral', blank=True, null=True)
    medial = models.CharField(max_length=5, verbose_name='Antero-medial', blank=True, null=True)
    all_lateral = models.CharField(max_length=5, verbose_name='Lateral', blank=True, null=True)
    all_medial = models.CharField(max_length=5, verbose_name='Medial', blank=True, null=True)
    posterior = models.CharField(max_length=5, verbose_name='Posterior', blank=True, null=True)
    postero_medial = models.CharField(max_length=5, verbose_name='Postero-medial', blank=True, null=True)
    all_postero_lateral = models.CharField(max_length=5, verbose_name='Postero-lateral', blank=True, null=True)
    two_leg = models.CharField(max_length=5, verbose_name='Sabit Zemin Çift Ayak(Hata Sayısı)', null=True,
                               blank=True)  # Denge Hata sayısı/Sbt Çift
    non_dominant = models.CharField(max_length=5, verbose_name='Sabit Zemin Non-Dominant Bacak(Hata Sayısı)',
                                    null=True, blank=True)
    tandem = models.CharField(max_length=5, verbose_name='Sabit Zemin Tandem(Hata Sayısı)', null=True, blank=True)
    two_leg1 = models.CharField(max_length=5, verbose_name='Hareketli Zemin Çift Ayak(Hata Sayısı)', null=True,
                                blank=True)
    non_dominant1 = models.CharField(max_length=5, verbose_name='Hareketli Zemin Non-Dominant Bacak(Hata Sayısı)',
                                     null=True, blank=True)
    tandem1 = models.CharField(max_length=5, verbose_name='Hareketli Zemin Tandem(Hata Sayısı)', null=True, blank=True)
    skor1 = models.CharField(max_length=5, verbose_name='Skor 1', blank=True, null=True)  # Modified Bass Test
    skor2 = models.CharField(max_length=5, verbose_name='Skor 1', blank=True, null=True)
    skor3 = models.CharField(max_length=5, verbose_name='Skor 1', blank=True, null=True)
    blood_sugar = models.CharField(max_length=5, verbose_name='Açlık Kan Şekeri', blank=True,
                                   null=True)  # Metabolik Uygunluk/Kan Glikoz Profili
    insulin = models.CharField(max_length=5, verbose_name='Açlık Insülin', blank=True, null=True)
    hb1ac = models.CharField(max_length=5, verbose_name='HB1AC', blank=True, null=True)
    ldl = models.CharField(max_length=5, verbose_name='LDL', blank=True, null=True)  # Kan Lipid Profili
    hdl = models.CharField(max_length=5, verbose_name='HDL', blank=True, null=True)
    trigliserit = models.CharField(max_length=5, verbose_name='Trigliserit', blank=True, null=True)
    kolesterol = models.CharField(max_length=5, verbose_name='Total Kolesterol', blank=True, null=True)
    sistolik = models.CharField(max_length=5, verbose_name='Sistolik Kan Basıncı', blank=True, null=True)
    diastolik = models.CharField(max_length=5, verbose_name='Diastolik Kan Basıncı', blank=True, null=True)

    def get_trainer_athletic_delete_url(self):
        return reverse('trainer-athletic-delete', kwargs={'id': self.id})

    def get_corporate_athletic_delete_url(self):
        return reverse('corporate-athletic-delete', kwargs={'id': self.id})

    def get_personal_athletic_delete_url(self):
        return reverse('personal-athletic-delete', kwargs={'id': self.id})

    def get_absolute_url(self):
        return reverse('athletic-detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('athletic-update', kwargs={'id': self.id})

    class Meta:
        verbose_name = "Atletik Performans Modülü"
        verbose_name_plural = 'Atletik Performans Ölçüm'
