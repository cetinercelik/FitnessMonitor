from datetime import datetime

from django.db import models

# Create your models here.
from django.urls import reverse

from registration.models import Trainer, Personal





class MedicalInputModel2(models.Model):
    dorsi1 = models.CharField(max_length=10, verbose_name='Dorsi-Fleksiyon', null=True,
                              blank=True)  # Goniometrik Eklem/Ayak ve Ayak
    plantar1 = models.CharField(max_length=10, verbose_name=' Plantar-Fleksiyon', null=True, blank=True)
    inversiyon = models.CharField(max_length=10, verbose_name='Inversiyon', null=True, blank=True)
    eversiyon = models.CharField(max_length=10, verbose_name='Eversiyon', null=True, blank=True)
    ekstansiyon = models.CharField(max_length=10, verbose_name='Ekstansiyon (Kalça Bükülü)', null=True,
                                   blank=True)  # Diz Eklemi
    fleksiyon1 = models.CharField(max_length=10, verbose_name='Fleksiyon', null=True, blank=True)
    fleksiyon2 = models.CharField(max_length=10, verbose_name='Fleksiyon (Diz Bükülü)', null=True,
                                  blank=True)  # Kalça Kompleksi
    abduksiyon = models.CharField(max_length=10, verbose_name='Abdüksiyon', null=True, blank=True)
    internal1 = models.CharField(max_length=10, verbose_name='İnternal Rotasyon', null=True, blank=True)
    eksternal1 = models.CharField(max_length=10, verbose_name='Eksternal Rotasyon', null=True, blank=True)
    ekstansiyon1 = models.CharField(max_length=10, verbose_name='Ekstansiyon', null=True, blank=True)
    fleksiyon3 = models.CharField(max_length=10, verbose_name='Fleksiyon', null=True, blank=True)  # Omuz Kompleksi
    ekstansiyon2 = models.CharField(max_length=10, verbose_name='Ekstansiyon', null=True, blank=True)
    abduksiyon1 = models.CharField(max_length=10, verbose_name='Abdüksiyon', null=True, blank=True)
    internal2 = models.CharField(max_length=10, verbose_name='İnternal Rotasyon', null=True, blank=True)
    eksternal2 = models.CharField(max_length=10, verbose_name='Eksternal Rotasyon', null=True, blank=True)
    fleksiyon4 = models.CharField(max_length=10, verbose_name='Fleksiyon', null=True, blank=True)  # Dirsek Eklemi
    ekstansiyon3 = models.CharField(max_length=10, verbose_name='Ekstansiyon', null=True, blank=True)
    fleksiyon5 = models.CharField(max_length=10, verbose_name='Fleksiyon', null=True, blank=True)  # Bilek Eklemi
    ekstansiyon4 = models.CharField(max_length=10, verbose_name='Ekstansiyon', null=True, blank=True)
    radial = models.CharField(max_length=10, verbose_name=' Radial Deviasyon', null=True, blank=True)
    ulnar = models.CharField(max_length=10, verbose_name='Ulnar Deviasyon', null=True, blank=True)
    a_suger = models.CharField(max_length=10, verbose_name='Açlık Kan Şekeri ', null=True,
                               blank=True)  # Metabolik Uygunluk/Kan Glikoz
    t_suger = models.CharField(max_length=10, verbose_name='Tokluk Kan Şekeri ', null=True, blank=True)
    insulin = models.CharField(max_length=10, verbose_name=' Açlık Insülin ', null=True, blank=True)
    hb1ac = models.CharField(max_length=10, verbose_name='HB1AC ', null=True, blank=True)
    fruktozamin = models.CharField(max_length=10, verbose_name='Fruktozamin', null=True, blank=True)

    hs_crp = models.CharField(max_length=10, verbose_name='Hs-CRP', null=True, blank=True)  # /Bağışıklık Profili
    sedimantasyon = models.CharField(max_length=10, verbose_name='Sedimantasyon (ESR)', null=True, blank=True)
    ldl = models.CharField(max_length=10, verbose_name='LDL ', null=True, blank=True)  # /Kan Lipid Profili
    hdl = models.CharField(max_length=10, verbose_name='HDL', null=True, blank=True)
    trigliserit = models.CharField(max_length=10, verbose_name='Trigliserit', null=True, blank=True)
    total_kolesterol = models.CharField(max_length=10, verbose_name='Total Kolesterol ', null=True, blank=True)
    sistolik = models.CharField(max_length=10, verbose_name='Sistolik Kan Basıncı', null=True,
                                blank=True)  # /Kan Basıncı Profili
    diastolik = models.CharField(max_length=10, verbose_name='Diastolik Kan Basıncı', null=True, blank=True)
    hemoglobin = models.CharField(max_length=10, verbose_name='Hemoglobin', null=True, blank=True)  # /Kan Fonksiyonları
    hemotokrit = models.CharField(max_length=10, verbose_name='Hemotokrit', null=True, blank=True)
    ast = models.CharField(max_length=10, verbose_name='AST', null=True, blank=True)
    alt = models.CharField(max_length=10, verbose_name='ALT', null=True, blank=True)
    ggt = models.CharField(max_length=10, verbose_name='GGT', null=True, blank=True)
    leptin = models.CharField(max_length=10, verbose_name='Leptin', null=True, blank=True)  # /Hormon Profili
    ghrelin = models.CharField(max_length=10, verbose_name='Ghrelin', null=True, blank=True)
    insulin1 = models.CharField(max_length=10, verbose_name='İnsülin', null=True, blank=True)
    kortizol = models.CharField(max_length=10, verbose_name='Kortizol', null=True, blank=True)
    testosteron = models.CharField(max_length=10, verbose_name='Testosteron', null=True, blank=True)
    ostrojen = models.CharField(max_length=10, verbose_name='Östrojen', null=True, blank=True)
    growth_hormone = models.CharField(max_length=10, verbose_name='Büyüme Hormonu', null=True, blank=True)
    tsh = models.CharField(max_length=10, verbose_name='TSH (Tiroit Stimule Edici Horrmon)', null=True, blank=True)
    triiyodotrinin = models.CharField(max_length=10, verbose_name='Triiyodotrinin (T3)', null=True, blank=True)
    total_tiroksin = models.CharField(max_length=10, verbose_name='Total Tiroksin (T4)', null=True, blank=True)
    c_vit = models.CharField(max_length=10, verbose_name='C Vitamini', null=True, blank=True)  # /Vitamin Profili
    e_vit = models.CharField(max_length=10, verbose_name='E Vitamini', null=True, blank=True)
    a_vit = models.CharField(max_length=10, verbose_name='A Vitamini', null=True, blank=True)
    folik = models.CharField(max_length=10, verbose_name='Folik Asit', null=True, blank=True)
    b6 = models.CharField(max_length=10, verbose_name='B6', null=True, blank=True)
    b12 = models.CharField(max_length=10, verbose_name='B12', null=True, blank=True)
    d3_vit = models.CharField(max_length=10, verbose_name='Vitamin D3', null=True, blank=True)
    kalsiyum = models.CharField(max_length=10, verbose_name='Kalsiyum', null=True, blank=True)  # /Mineral Profili
    demir = models.CharField(max_length=10, verbose_name='Demir', null=True, blank=True)
    magnezyum = models.CharField(max_length=10, verbose_name='Magnezyum', null=True, blank=True)
    bakir = models.CharField(max_length=10, verbose_name='Bakır', null=True, blank=True)
    cinko = models.CharField(max_length=10, verbose_name='Çinko', null=True, blank=True)
    selenyum = models.CharField(max_length=10, verbose_name='Selenyum', null=True, blank=True)
    potasyum = models.CharField(max_length=10, verbose_name='Potasyum', null=True, blank=True)
    koenzim = models.CharField(max_length=10, verbose_name='Koenzim Q10', null=True, blank=True)
    lizin = models.CharField(max_length=10, verbose_name='Lizin', null=True, blank=True)  # Aminoasit Profili
    metiyonin = models.CharField(max_length=10, verbose_name='Metiyonin', null=True, blank=True)
    triptofan = models.CharField(max_length=10, verbose_name='Triptofan', null=True, blank=True)
    losin = models.CharField(max_length=10, verbose_name='Lösin', null=True, blank=True)
    izolosin = models.CharField(max_length=10, verbose_name='Izolösin', null=True, blank=True)
    valin = models.CharField(max_length=10, verbose_name='Valin', null=True, blank=True)
    treonin = models.CharField(max_length=10, verbose_name='Treonin', null=True, blank=True)
    fenilalanin = models.CharField(max_length=10, verbose_name='Fenilalanin', null=True, blank=True)
    histidin = models.CharField(max_length=10, verbose_name='Histidin', null=True, blank=True)
    arjinin = models.CharField(max_length=50, verbose_name='Arjinin', null=True, blank=True)
    glutamin = models.CharField(max_length=10, verbose_name='Glutamin', null=True, blank=True)
    serin = models.CharField(max_length=10, verbose_name='Serin', null=True, blank=True)
    tirozin = models.CharField(max_length=10, verbose_name='Tirozin', null=True, blank=True)
    prolin = models.CharField(max_length=10, verbose_name='Prolin', null=True, blank=True)
    sistein = models.CharField(max_length=10, verbose_name='Sistein', null=True, blank=True)
    alanin = models.CharField(max_length=10, verbose_name='Alanin', null=True, blank=True)
    aspartik = models.CharField(max_length=10, verbose_name='Aspartik Asit', null=True, blank=True)
    glutamik = models.CharField(max_length=10, verbose_name='Glutamik Asit', null=True, blank=True)
    asparajin = models.CharField(max_length=10, verbose_name='Asparajin', null=True, blank=True)
    z_Skoru = models.CharField(max_length=10, verbose_name='Z-Skoru', null=True, blank=True)  # /Kemik Mineral Yoğunluğu
    t_Skoru = models.CharField(max_length=10, verbose_name='T-Skoru', null=True, blank=True)
    overhead_normal = models.CharField(verbose_name='Normal', max_length=40, null=True,
                                       blank=True)  # Hareket Kalitesi/Overhead Squat Testi
    overhead_glenohumeral = models.CharField(verbose_name='Glenohumeral İmmobilite', max_length=40, null=True,
                                             blank=True)
    overhead_torakal = models.CharField(verbose_name='Torakal İmmobilite', max_length=40, null=True, blank=True)
    overhead_body = models.CharField(verbose_name='Tüm Vücut Dinamik İmmobilite Varlığı', max_length=40, null=True,
                                     blank=True)
    overhead_foot = models.CharField(verbose_name='Ayak Bileği İmmobilitesi', max_length=40, null=True, blank=True)
    overhead_knee = models.CharField(verbose_name='Diz İnstabilitesi', max_length=40, null=True, blank=True)
    overhead_hip = models.CharField(verbose_name='Kalça İmmobilitesi', max_length=40, null=True, blank=True)
    overhead_balance = models.CharField(verbose_name='Denge Kayıpları (zayıf motor kontrol)', max_length=40, null=True,
                                        blank=True)
    overhead_pain = models.CharField(verbose_name='Ağrı Varlığı', max_length=40, null=True, blank=True)
    overhead_other = models.CharField(max_length=100, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    squat_normal = models.CharField(verbose_name='Normal', max_length=40, null=True,
                                    blank=True)  # /Tek Bacak Squat Testi (Sağ-Sol Taraf İçin)
    squat_torakal = models.CharField(verbose_name='Torakal İmmobilite', max_length=40, null=True, blank=True)
    squat_body = models.CharField(verbose_name='Tüm Vücut Dinamik İmmobilite Varlığı', max_length=40, null=True,
                                  blank=True)
    squat_foot = models.CharField(verbose_name='Ayak Bileği İmmobilitesi', max_length=40, null=True, blank=True)
    squat_knee = models.CharField(verbose_name='Diz İnstabilitesi', max_length=40, null=True, blank=True)
    squat_hip = models.CharField(verbose_name='Kalça İmmobilitesi', max_length=40, null=True, blank=True)
    squat_balance = models.CharField(verbose_name='Denge Kayıpları (zayıf motor kontrol)', max_length=40, null=True,
                                     blank=True)
    squat_pain = models.CharField(verbose_name=' Ağrı Varlığı', max_length=40, null=True, blank=True)
    squat_other = models.CharField(max_length=100, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    bridge_normal = models.CharField(verbose_name='Normal', max_length=40, null=True,
                                     blank=True)  # /Tek Bacak Köprü Testi (Sağ-Sol Taraf İçin)
    bridge_hip_fleksiyon = models.CharField(verbose_name='Kalça Fleksiyon Artışı', max_length=40, null=True, blank=True)
    bridge_balance = models.CharField(verbose_name='Denge Kayıpları (zayıf motor kontrol)', max_length=40, null=True,
                                      blank=True)
    bridge_body = models.CharField(verbose_name='Tüm Vücut Dinamik İmmobilite Varlığı', max_length=40, null=True,
                                   blank=True)
    bridge_knee = models.CharField(verbose_name='Diz İnstabilitesi', max_length=40, null=True, blank=True)
    bridge_hip_imo = models.CharField(verbose_name='Kalça İmmobilitesi', max_length=40, null=True, blank=True)
    bridge_hamstring = models.CharField(verbose_name='Hamstring Gerginliği', max_length=40, null=True, blank=True)
    bridge_Kuadriseps = models.CharField(verbose_name='Kuadriseps Gerginliği', max_length=40, null=True, blank=True)
    bridge_pain = models.CharField(verbose_name='Ağrı Varlığı', max_length=40, null=True, blank=True)
    bridge_other = models.CharField(max_length=100, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    lunge_normal = models.CharField(verbose_name='Normal', max_length=40, null=True,
                                    blank=True)  # /Lunge Testi (Sağ-Sol Taraf İçin)
    lunge_patello = models.CharField(verbose_name='Patello-Femoral Kayma', max_length=40, null=True, blank=True)
    lunge_over = models.CharField(verbose_name='Over-pronasyon', max_length=40, null=True, blank=True)
    lunge_body_fleksiyon = models.CharField(verbose_name='Gövde Fleksiyon Artışı', max_length=40, null=True, blank=True)
    lunge_balance = models.CharField(verbose_name='Denge Kayıpları (zayıf motor kontrol)', max_length=40, null=True,
                                     blank=True)
    lunge_body = models.CharField(verbose_name='Tüm Vücut Dinamik İmmobilite Varlığı', max_length=40, null=True,
                                  blank=True)
    lunge_foot = models.CharField(verbose_name='Ayak Bileği İmmobilitesi', max_length=40, null=True, blank=True)
    lunge_knee = models.CharField(verbose_name='Diz İnstabilitesi', max_length=40, null=True, blank=True)
    lunge_hip = models.CharField(verbose_name=' Kalça İmmobilitesi', max_length=40, null=True, blank=True)
    lunge_pain = models.CharField(verbose_name='Ağrı Varlığı', max_length=40, null=True, blank=True)
    lunge_other = models.CharField(max_length=100, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    trunk_normal = models.CharField(verbose_name='Normal', max_length=40, null=True,
                                    blank=True)  # /Trunk Stability (Push-up)
    trunk_core = models.CharField(verbose_name='Core Stabilizasyon Kaybı', max_length=40, null=True, blank=True)
    trunk_skapula = models.CharField(verbose_name='Skapula İnstabilizasyon', max_length=40, null=True, blank=True)
    trunk_hip = models.CharField(verbose_name='Kalça İmmobilitesi', max_length=40, null=True, blank=True)
    trunk_lomber = models.CharField(verbose_name='Lomber Lordoz Artışı', max_length=40, null=True, blank=True)
    trunk_balance = models.CharField(verbose_name='Denge Kayıpları (zayıf motor kontrol)', max_length=40, null=True,
                                     blank=True)
    trunk_pain = models.CharField(verbose_name='Ağrı Varlığı', max_length=40, null=True, blank=True)
    trunk_other = models.CharField(max_length=100, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    shoulder_normal = models.CharField(verbose_name='Normal', max_length=40, null=True,
                                       blank=True)  # /Shoulder Mobility (Sağ-Sol Taraf İçin)
    shoulder_core = models.CharField(verbose_name='Core Stabilizasyon Kaybı', max_length=40, null=True, blank=True)
    shoulder_skapula = models.CharField(verbose_name='Skapulo-Torasik İnstabilite - İmmobilite', max_length=40,
                                        null=True,
                                        blank=True)
    shoulder_gleno = models.CharField(verbose_name='Gleno-Humeral Disfonksiyon', max_length=40, null=True, blank=True)
    shoulder_balance = models.CharField(verbose_name='Denge Kayıpları (zayıf motor kontrol)', max_length=40, null=True,
                                        blank=True)
    shoulder_pain = models.CharField(verbose_name='Ağrı Varlığı', max_length=40, null=True, blank=True)
    shoulder_other = models.CharField(max_length=100, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    active_normal = models.CharField(verbose_name='Normal', max_length=40, null=True, blank=True)
    active_pelvik = models.CharField(verbose_name='Pelvik Kontrol Kaybı', max_length=40, null=True, blank=True)
    active_hip = models.CharField(verbose_name='Kalça İmmobilitesi (Karşı taraf)', max_length=40, null=True, blank=True)
    active_ekstansiyon = models.CharField(verbose_name='Kalça Ekstansiyon Disfonksiyonu', max_length=40, null=True,
                                          blank=True)
    active_hamstring = models.CharField(verbose_name='Hamstring Gerginliği', max_length=40, null=True, blank=True)
    active_lomber = models.CharField(verbose_name='Lomber Lordoz Artışı', max_length=40, null=True, blank=True)
    active_rotasyon = models.CharField(verbose_name='Artmış Gövde Rotasyon (kaldırılan bacak yönüne)', max_length=50,
                                       null=True,
                                       blank=True)
    active_pain = models.CharField(verbose_name='Ağrı Varlığı (Sakro-iliak eklem)', max_length=40, null=True,
                                   blank=True)
    active_other = models.CharField(max_length=100, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    rotary_normal = models.CharField(verbose_name='Normal', max_length=40, null=True,
                                     blank=True)  # /Rotary Stability (Sağ-Sol Taraf İçin)
    rotary_core = models.CharField(verbose_name='Core İnstabilitesi', max_length=40, null=True, blank=True)
    rotary_body = models.CharField(verbose_name='Gövde İnstabilitesi', max_length=40, null=True, blank=True)
    rotary_hip = models.CharField(verbose_name=' Kalça-Diz-Omuz İmmobilitesi', max_length=40, null=True, blank=True)
    rotary_balance = models.CharField(verbose_name='Denge Kayıpları (zayıf motor kontrol)', max_length=40, null=True,
                                      blank=True)
    rotary_pain = models.CharField(verbose_name='Ağrı Varlığı', max_length=40, null=True, blank=True)
    rotary_other = models.CharField(max_length=100, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    front_normal = models.CharField(verbose_name='Normal', max_length=40, null=True,
                                    blank=True)  # /Front Plank Dayanıklılık Testi
    front_pelvisin = models.CharField(verbose_name=' Pelvisin Aşağı Çökmesi', max_length=40, null=True, blank=True)
    front_core = models.CharField(verbose_name='Core İnstabilitesi', max_length=40, null=True, blank=True)
    front_body = models.CharField(verbose_name='Gövde Hizalama Sorunları', max_length=40, null=True, blank=True)
    front_arm = models.CharField(verbose_name='Kol-Omuz İnstabilitesi', max_length=40, null=True, blank=True)
    front_pain = models.CharField(verbose_name='Ağrı Varlığı (Lomber Omurga)', max_length=40, null=True, blank=True)
    front_other = models.CharField(max_length=100, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    side_normal = models.CharField(verbose_name='Normal', max_length=40, null=True,
                                   blank=True)  # /Side Plank Dayanıklılık Testi
    side_pelvisin = models.CharField(verbose_name=' Pelvisin Aşağı Çökmesi', max_length=40, null=True, blank=True)
    side_core = models.CharField(verbose_name='Core İnstabilitesi', max_length=40, null=True, blank=True)
    side_body = models.CharField(verbose_name='Gövde Hizalama Sorunları', max_length=40, null=True, blank=True)
    side_foot = models.CharField(verbose_name='Ayak İnstabilitesi', max_length=40, null=True, blank=True)
    side_arm = models.CharField(verbose_name='Kol-Omuz İnstabilitesi', max_length=40, null=True, blank=True)
    side_pain = models.CharField(verbose_name='Ağrı Varlığı (Lomber Omurga)', max_length=40, null=True, blank=True)
    side_other = models.CharField(max_length=100, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    fleksor_normal = models.CharField(verbose_name='Normal', max_length=40, null=True,
                                      blank=True)  # /Gövde Fleksör Dayanıklılık Testi
    fleksor_body = models.CharField(verbose_name='Gövdenin Geriye Kayması', max_length=40, null=True, blank=True)
    fleksor_core = models.CharField(verbose_name='Core İnstabilitesi', max_length=40, null=True, blank=True)
    fleksor_problem = models.CharField(verbose_name='Gövde Hizalama Sorunları', max_length=40, null=True, blank=True)
    fleksor_hamstring = models.CharField(verbose_name='Hamstring Gerginliği', max_length=40, null=True, blank=True)
    fleksor_kuadriseps = models.CharField(verbose_name='Kuadriseps Gerginliği', max_length=40, null=True, blank=True)
    fleksor_foot = models.CharField(verbose_name='Ayak İnstabilitesi', max_length=40, null=True, blank=True)
    fleksor_pain = models.CharField(verbose_name='Ağrı Varlığı (Lomber Omurga)', max_length=40, null=True, blank=True)
    fleksor_other = models.CharField(max_length=100, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    extansor_normal = models.CharField(verbose_name='Normal', max_length=40, null=True, blank=True)
    extansor_body_shift = models.CharField(verbose_name='Gövdenin Öne Kayması', max_length=40, null=True, blank=True)
    extansor_core = models.CharField(verbose_name=' Core İnstabilitesi', max_length=40, null=True, blank=True)
    extansor_problems = models.CharField(verbose_name='Gövde Hizalama Sorunları', max_length=40, null=True, blank=True)
    extansor_lomber = models.CharField(verbose_name='Lomber Lordoz Artışı', max_length=40, null=True, blank=True)
    extansor_hamstring = models.CharField(verbose_name='Hamstring Gerginliği', max_length=40, null=True, blank=True)
    extansor_kuadriseps = models.CharField(verbose_name='Kuadriseps Gerginliği', max_length=40, null=True, blank=True)
    extansor_pain = models.CharField(verbose_name='Ağrı Varlığı (Lomber Omurga)', max_length=40, null=True, blank=True)
    extansor_other = models.CharField(max_length=100, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    open_time1 = models.CharField(max_length=10, verbose_name='Süre 1', null=True, blank=True)  # Tek bacak/Gözler açık
    open_time2 = models.CharField(max_length=10, verbose_name='Süre 2', null=True, blank=True)
    open_time3 = models.CharField(max_length=10, verbose_name='Süre 3', null=True, blank=True)
    close_time1 = models.CharField(max_length=10, verbose_name='Süre 1', null=True, blank=True)  # /Gözler kapalı
    close_time2 = models.CharField(max_length=10, verbose_name='Süre 2', null=True, blank=True)
    close_time3 = models.CharField(max_length=10, verbose_name='Süre 3', null=True, blank=True)
    star_test = models.CharField(max_length=10, verbose_name='Bacak Uzunluğu', null=True,
                                 blank=True)  # Yıldız denge/3 Yön
    treedirect_anterior = models.CharField(max_length=10, verbose_name='Anterior', null=True, blank=True)
    treedirect_medial = models.CharField(max_length=10, verbose_name='Postero-medial', null=True, blank=True)
    treedirect_lateral = models.CharField(max_length=10, verbose_name='Postero-lateral', null=True, blank=True)
    all_anterior = models.CharField(max_length=10, verbose_name='Anterior', null=True, blank=True)
    all_antero_lateral = models.CharField(max_length=10, verbose_name='Antero-lateral', null=True, blank=True)
    all_antero_media = models.CharField(max_length=10, verbose_name='Antero-media', null=True, blank=True)
    all_lateral = models.CharField(max_length=10, verbose_name='Lateral', null=True, blank=True)
    all_medial = models.CharField(max_length=10, verbose_name='Medial', null=True, blank=True)
    all_posterior = models.CharField(max_length=10, verbose_name='Posterior', null=True, blank=True)
    all_postero_medial = models.CharField(max_length=10, verbose_name='Postero-medial', null=True, blank=True)
    all_postero_lateral = models.CharField(max_length=10, verbose_name='Postero-lateral', null=True, blank=True)
    two_leg = models.CharField(max_length=10, verbose_name='Sabit Zemin Çift Ayak(Hata Sayısı)', null=True,
                               blank=True)  # Denge Hata sayısı/Sbt Çift
    non_dominant = models.CharField(max_length=10, verbose_name='Sabit Zemin Non-Dominant Bacak(Hata Sayısı)',
                                    null=True, blank=True)
    tandem = models.CharField(max_length=10, verbose_name='Sabit Zemin Tandem(Hata Sayısı)', null=True, blank=True)
    two_leg1 = models.CharField(max_length=10, verbose_name='Hareketli Zemin Çift Ayak(Hata Sayısı)', null=True,
                                blank=True)
    non_dominant1 = models.CharField(max_length=10, verbose_name='Hareketli Zemin Non-Dominant Bacak(Hata Sayısı)',
                                     null=True, blank=True)
    tandem1 = models.CharField(max_length=10, verbose_name='Hareketli Zemin Tandem(Hata Sayısı)', null=True, blank=True)
    skor1 = models.CharField(max_length=10, verbose_name='Skor 1', null=True, blank=True)
    skor2 = models.CharField(max_length=10, verbose_name='Skor 2', null=True, blank=True)
    skor3 = models.CharField(max_length=10, verbose_name='Skor 3', null=True, blank=True)


    class Meta:
        verbose_name = "Medikal Ölçme ve Değerlendirme "
        verbose_name_plural = 'Medikal Ölçme Paneli 2'



class MedicalInputModel1(models.Model):
    trainer = models.ForeignKey(to=Trainer, verbose_name="Antrenör", on_delete=models.CASCADE, blank=True, null=True)
    personal = models.ForeignKey(to=Personal, verbose_name="Danışan", on_delete=models.CASCADE, blank=True, null=True)
    medical2 = models.ForeignKey(to=MedicalInputModel2, verbose_name="Medical", on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(("Date"), default=datetime.now(), blank=True)
    sole1 = models.CharField(verbose_name="Normal", max_length=20, null=True,
                             blank=True)  # Ayak Tabanı Gözlem ve Değerlendirme
    Pes_Planus = models.CharField(verbose_name='Pes-Planus/Over-pronasyon (İçe basma)', max_length=50, null=True,
                                  blank=True)
    Pes_Cavus = models.CharField(verbose_name='Pes-Cavus/Over-supinasyon (Dışa basma)', max_length=50, null=True,
                                 blank=True)
    flat_feet = models.CharField(verbose_name='Flat Feet (Düz taban)', max_length=50, null=True, blank=True)
    dorsi_fleksiyon = models.CharField(verbose_name='Dorsi-fleksiyon Kaybı', max_length=50, null=True, blank=True)
    plantar = models.CharField(verbose_name='Plantar Fasya Ağrısı', max_length=50, null=True, blank=True)
    gastrocnemius_sensitive = models.CharField(verbose_name='Gastrocnemius Hassasiyeti', max_length=50, null=True,
                                               blank=True)
    ankle_sprain = models.CharField(verbose_name='Ayak Bileği Burkulması', max_length=50, null=True, blank=True)
    achilles_tendonopathy = models.CharField(verbose_name='Aşil Tendonopati', max_length=50, null=True, blank=True)
    achilles_tendonopathy_tear = models.CharField(verbose_name='Aşil Tendonu Yırtığı', max_length=50, null=True,
                                                  blank=True)
    plantar_fasiitis = models.CharField(verbose_name='Plantar Fasiitis', max_length=50, null=True, blank=True)
    other_leg_sole = models.CharField(max_length=100, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_leg_knee = models.CharField(verbose_name='Normal', max_length=50, null=True,
                                       blank=True)  # Diz ve Bacaklar Gözlem ve Değerlendirme
    genu_recurvatum = models.CharField(verbose_name=' Genu Recurvatum (Hiperekstensiyonda diz)', max_length=50,
                                       null=True,
                                       blank=True)
    flexed_knee = models.CharField(verbose_name='Flexed Knee (Bükülü diz)', max_length=50, null=True, blank=True)
    genu = models.CharField(verbose_name=' Genu Varum (Parantez bacak)', max_length=50, null=True, blank=True)
    genu_valgus = models.CharField(verbose_name='Genu Valgus (X bacak)', max_length=50, null=True, blank=True)
    knee_pain = models.CharField(verbose_name='Diz Ağrısı', max_length=50, null=True, blank=True)
    kripitasyon = models.CharField(verbose_name='Kripitasyon (Çıtlama) Varlığı', max_length=50, null=True, blank=True)
    acl_tear = models.CharField(verbose_name='ACL Yırtığı', max_length=50, null=True, blank=True)
    pcl_tear = models.CharField(verbose_name='PCL Yırtığı', max_length=50, null=True, blank=True)
    medial_tear = models.CharField(verbose_name='Medial Menisküs Yırtığı', max_length=50, null=True, blank=True)
    lateral_tear = models.CharField(verbose_name='Lateral Menisküs Yırtığı', max_length=50, null=True, blank=True)
    patello_sendrom = models.CharField(verbose_name='Patello-Femoral Sendrom', max_length=50, null=True, blank=True)
    it_sendrom = models.CharField(verbose_name='IT Band Sendrom', max_length=50, null=True, blank=True)
    kuadriseps = models.CharField(verbose_name='Kuadriseps Gerginliği', max_length=50, null=True, blank=True)
    hamstring_g = models.CharField(verbose_name='Hamstring Gerginliği', max_length=50, null=True, blank=True)
    hamstring_tear = models.CharField(verbose_name='Hamstring Yırtığı', max_length=50, null=True, blank=True)
    groin_tear = models.CharField(verbose_name='Kasık Yırtığı', max_length=50, null=True, blank=True)
    shin = models.CharField(verbose_name='Shin Splints (Medial Tibia Stres Kırığı) Sendromu', max_length=50, null=True,
                            blank=True)
    kneecap_pains = models.CharField(verbose_name='Diz Kapağı Ağrıları', max_length=50, null=True, blank=True)
    patellar_dislokasiyon = models.CharField(verbose_name='Patellar Dislokasyon', max_length=50, null=True, blank=True)
    other_leg_knee = models.CharField(max_length=100, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_lumbo_hip = models.CharField(verbose_name='Normal', max_length=50, null=True,
                                        blank=True)  # Lumbo-Pelvik Kalça Gözlem ve Değerlendirme
    lomber = models.CharField(verbose_name='Lomber Lordoz Artışı', max_length=50, null=True, blank=True)
    anterior = models.CharField(verbose_name='Anterior Pelvik Tilt', max_length=50, null=True, blank=True)
    posterior = models.CharField(verbose_name='Posterior Pelvic Tilt', max_length=50, null=True, blank=True)
    unleveling = models.CharField(verbose_name='Unleveling Pelvis Sendromu', max_length=50, null=True, blank=True)
    gluteal_amnezi = models.CharField(verbose_name='Gluteal Amnezi (Ölü Popo) Sendromu', max_length=50, null=True,
                                      blank=True)
    hip_pain = models.CharField(verbose_name='Kalça Ağrısı', max_length=50, null=True, blank=True)
    lower_back_pain = models.CharField(verbose_name='Alt Sırt Ağrısı', max_length=50, null=True, blank=True)
    siyatik = models.CharField(verbose_name='Siyatik Sinir Hassasiyeti', max_length=50, null=True, blank=True)
    piriformis = models.CharField(verbose_name='Piriformis Sendromu', max_length=50, null=True, blank=True)
    medial_meniskus_tear = models.CharField(verbose_name='Medial Menisküs Yırtığı', max_length=50, null=True,
                                            blank=True)
    hip_surgeon = models.CharField(verbose_name='Kalça Cerrahisi', max_length=50, null=True, blank=True)
    hip_labrum = models.CharField(verbose_name='Kalça Labrum Sendromu', max_length=50, null=True, blank=True)
    spinal_fuzyon = models.CharField(verbose_name='Spinal Füzyon', max_length=50, null=True, blank=True)
    waist = models.CharField(verbose_name='Bel Fıtığı', max_length=50, null=True, blank=True)
    waist_surgeon = models.CharField(verbose_name='Bel Fıtığı Cerrahisi', max_length=50, null=True, blank=True)
    ankilozan = models.CharField(verbose_name='Ankilozan Spondilit', max_length=50, null=True, blank=True)
    spondoliztesiz = models.CharField(verbose_name='Spondoliztesiz', max_length=50, null=True, blank=True)
    waist_artrit = models.CharField(verbose_name='Kalça Artriti – Bursiti', max_length=50, null=True, blank=True)
    sakro = models.CharField(verbose_name='Sakro-İliak Eklem Ağrısı', max_length=50, null=True, blank=True)
    disk_hernia = models.CharField(verbose_name='Disk Hernia - Bulge', max_length=50, null=True, blank=True)
    spinal_pain = models.CharField(verbose_name='Omurilik Ağrıları', max_length=50, null=True, blank=True)
    other_lumbo_hip = models.CharField(max_length=100, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_torakal = models.CharField(verbose_name='Normal', max_length=50, null=True,
                                      blank=True)  # Torakal Omurga Gözlem ve Değerlendirme
    torakal_kifoz = models.CharField(verbose_name='Torakal Kifoz Artışı ', max_length=50, null=True, blank=True)
    sway_back = models.CharField(verbose_name='Sway Back (Düz Sırt)', max_length=50, null=True, blank=True)
    fonksiyonel_skolyoz = models.CharField(verbose_name='Fonksiyonel Skolyoz', max_length=50, null=True, blank=True)
    wing_skapula = models.CharField(verbose_name='Wing Skapula', max_length=50, null=True, blank=True)
    torasik = models.CharField(verbose_name='Torasik Outlet Sendromu', max_length=50, null=True, blank=True)
    torakal_g = models.CharField(verbose_name='Torakal Gerginlik ve Ağrı', max_length=50, null=True, blank=True)
    other_torakal = models.CharField(max_length=100, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_skapula = models.CharField(verbose_name='Normal', max_length=50, null=True,
                                      blank=True)  # Omuz/Skapula/Kol Gözlem ve Değerlendirme
    protracted_skapula = models.CharField(verbose_name='Protracted Skapula (Yukarı Öne Açılmış Skapula)', max_length=50,
                                          null=True, blank=True)
    scapula_control = models.CharField(verbose_name='Skapular Kontrol Problemleri', max_length=50, null=True,
                                       blank=True)
    shoulder_instabilty = models.CharField(verbose_name=' Omuz İnstabiltesi', max_length=50, null=True, blank=True)
    internal_rotasyon = models.CharField(verbose_name='İnternal Rotasyon (Kol) Varlığı', max_length=50, null=True,
                                         blank=True)
    round_shoulder = models.CharField(verbose_name='Round Shoulder (Dönmüş Omuz)', max_length=50, null=True, blank=True)
    elevated_shoulder = models.CharField(verbose_name='Elevated Shoulder Blade (Yükselmiş Skapula)', max_length=50,
                                         null=True,
                                         blank=True)
    shoulder_disloksiyon = models.CharField(verbose_name='Omuz Eklemi Dislokasyonu', max_length=50, null=True,
                                            blank=True)
    kapsul_sendrom = models.CharField(verbose_name='Yapışkan Kapsül Sendromu', max_length=50, null=True, blank=True)
    rotator_cuff = models.CharField(verbose_name='Rotatof (Manşet) Sendromur Cuf', max_length=50, null=True, blank=True)
    shoulder_impingment = models.CharField(verbose_name='Omuz Impingment (Sıkışma) Sendromu', max_length=50, null=True,
                                           blank=True)
    frozen_shoulder = models.CharField(verbose_name='Frozen (Donuk) Shoulder', max_length=50, null=True, blank=True)
    tenis = models.CharField(verbose_name='Tenisçi Dirseği', max_length=50, null=True, blank=True)
    golf = models.CharField(verbose_name='Golfçü Dirseği', max_length=50, null=True, blank=True)
    kubitel = models.CharField(verbose_name='Kübitel Tünel Sendromu', max_length=50, null=True, blank=True)
    karpal = models.CharField(verbose_name='Karpal Tünel Sendromu', max_length=50, null=True, blank=True)
    wrist_pain = models.CharField(verbose_name='El Bileği Ağrıları', max_length=50, null=True, blank=True)
    brakial = models.CharField(verbose_name='Brakial Pleksus Gerginliği', max_length=50, null=True, blank=True)
    other_skapula = models.CharField(max_length=100, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    normal_head = models.CharField(verbose_name='Normal', max_length=50, null=True,
                                   blank=True)  # Baş Gözlem ve Değerlendirme
    forward_head = models.CharField(verbose_name=' Forward Head (İleri Baş) Sendromu', max_length=50, null=True,
                                    blank=True)
    servikal = models.CharField(verbose_name='Servikal Lordoz Artışı', max_length=50, null=True, blank=True)
    neck_straightening = models.CharField(verbose_name='Boyun Düzleşmesi', max_length=50, null=True, blank=True)
    neck_hernia = models.CharField(verbose_name='Boyun Fıtığı', max_length=50, null=True, blank=True)
    neck_surgeon = models.CharField(verbose_name='Boyun Omurları Cerrahisi', max_length=50, null=True, blank=True)
    temporo_mandibular = models.CharField(verbose_name='Temporo-mandibular Eklem Ağrıları', max_length=50, null=True,
                                          blank=True)
    head_pain = models.CharField(verbose_name='Baş Ağrısı', max_length=50, null=True, blank=True)
    other_head = models.CharField(max_length=100, verbose_name='Diğer Bulgular (varsa)', null=True, blank=True)
    anterior_tibialis = models.CharField(max_length=50, blank=True, null=True)  # Manuel Kas Ölçümleri/Ayak ve Ayak bil
    posterior_tibialis = models.CharField(max_length=50, blank=True,
                                          null=True)  # Manuel Kas Ölçümleri/Posterior Tibialis
    medial = models.CharField(max_length=40, blank=True, null=True)  # Diz Kasları/Medial Hamstring
    biseps = models.CharField(max_length=40, blank=True, null=True)  # Diz Kasları/Biseps Femoris
    ilio = models.CharField(max_length=40, blank=True, null=True)  # Lumbo-Pelvik / İlio-Psoas
    adduktor = models.CharField(max_length=40, blank=True, null=True)  # Lumbo-Pelvik /Adduktör Kompleks
    gluteus = models.CharField(max_length=40, blank=True, null=True)  # Lumbo-Pelvik / Gluteus Maksimus
    medius = models.CharField(max_length=40, blank=True, null=True)  # Lumbo-Pelvik / Gluteus Medius
    hip = models.CharField(max_length=40, blank=True, null=True)  # Lumbo-Pelvik /  Kalça Dış Rotatörleri
    rektus = models.CharField(max_length=40, blank=True, null=True)  # Gövde Kasları / Rektus Abdominis
    abdominal = models.CharField(max_length=40, blank=True, null=True)  # Gövde Kasları  /  Abdominal Oblikler
    latissimus = models.CharField(max_length=40, blank=True, null=True)  # Gövde Kasları  / Latissimus Dorsi
    eksternal = models.CharField(max_length=40, blank=True, null=True)  # Omuz-Skapula Kasları/ Omuz Eksternal
    internal = models.CharField(max_length=40, blank=True, null=True)  # Omuz-Skapula Kasları /Omuz İnternal Rotatörleri
    rhomboidler = models.CharField(max_length=40, blank=True, null=True)  # Omuz-Skapula Kasları/ Rhomboidler
    trapezius = models.CharField(max_length=40, blank=True, null=True)  # Omuz-Skapula Kasları /Alt Trapezius
    serratus = models.CharField(max_length=40, blank=True, null=True)  # Omuz-Skapula Kasları/ Serratus Anterior
    neck_front = models.CharField(max_length=40, blank=True, null=True)  # Baş-Boyun Kasları/ Boyun Fleksörleri (Ön)
    neck_side = models.CharField(max_length=40, blank=True, null=True)  # Baş-Boyun Kasları/ Boyun Fleksörleri (Yan)
    neck_ex = models.CharField(max_length=40, blank=True, null=True)  # Baş-Boyun Kasları/  Boyun Ekstansörleri

    def get_absolute_url(self):
        return reverse('medical-detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('medical-update', kwargs={'id': self.id})

    def get_trainer_measurement_medical_delete_url(self):
        return reverse('trainer-measurement_medical-delete', kwargs={'id': self.id})

    def get_corporate_measurement_medical_delete_url(self):
        return reverse('corporate-measurement_medical-delete', kwargs={'id': self.id})

    def get_personal_measurement_medical_delete_url(self):
        return reverse('personal-measurement_medical-delete', kwargs={'id': self.id})

    class Meta:
        verbose_name = "Medikal Ölçme ve Değerlendirme "
        verbose_name_plural = 'Medikal Ölçme Paneli'