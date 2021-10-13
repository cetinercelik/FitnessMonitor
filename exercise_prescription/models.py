from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

from registration.models import Trainer, Personal




class exercise_prescription_level(models.Model):
    person_level1 = models.CharField(max_length=150, verbose_name='Kişinin Düzeyini Belirle', blank=True, null=True)
    # Amaç Belirle
    health1 = models.CharField(max_length=30, verbose_name='Genel Sağlık Gelişimi', blank=True, null=True)
    force = models.CharField(max_length=30, verbose_name='Genel Kuvvet Gelişimi', blank=True, null=True)
    muscular_endurance = models.CharField(max_length=30, verbose_name='Kas Dayanıklılığı', blank=True, null=True)
    muscle_mass = models.CharField(max_length=30, verbose_name='Kas Kütlesi Artışı', blank=True, null=True)
    optimal = models.CharField(max_length=30, verbose_name=' Optimal Hipertrofi', blank=True, null=True)
    fonksiyonel = models.CharField(max_length=30, verbose_name='Fonksiyonel Hipertrofi', blank=True, null=True)
    explosive_force = models.CharField(max_length=30, verbose_name='Patlayıcı Kuvvet ', blank=True, null=True)
    # Direnç Programı/ Gün sayısı
    monday1 = models.CharField(max_length=10, verbose_name='Pazartesi', blank=True, null=True)
    tuesday1 = models.CharField(max_length=10, verbose_name='Salı', blank=True, null=True)
    wednesday1 = models.CharField(max_length=10, verbose_name='Çarşamba', blank=True, null=True)
    thursday1 = models.CharField(max_length=10, verbose_name='Perşembe', blank=True, null=True)
    friday1 = models.CharField(max_length=10, verbose_name='Cuma', blank=True, null=True)
    saturday1 = models.CharField(max_length=10, verbose_name='Cumartesi', blank=True, null=True)
    sunday1 = models.CharField(max_length=10, verbose_name='Pazar', blank=True, null=True)
    train_time1 = models.CharField(max_length=20, verbose_name="Antrenman Süresi Belirle",
                                   blank=True,
                                   null=True)  # Antrenman Süresi Belirle
    train_type = models.CharField(max_length=100, verbose_name="Antrenman Türü", blank=True,
                                  null=True)

    class Meta:
        verbose_name = "Egzersiz Reçetesi"
        verbose_name_plural = 'Kişinin Düzeyini Belirleme'


class exercise_prescripion_chest(models.Model):
    chest_set_number = models.CharField(max_length=5, verbose_name="Set Sayısı", blank=True, null=True)
    chest_over_number = models.CharField(max_length=5, verbose_name="Tekrar Sayısı", blank=True, null=True)
    chest_tempo = models.CharField(max_length=10, verbose_name="Tempo (TUT)", blank=True, null=True)
    # Setler arası dinlenme
    chest_sets_between = models.CharField(max_length=10, verbose_name="Setler Arası Dinlenme", blank=True, null=True)
    chest_move_between = models.CharField(max_length=10, verbose_name="Hareketler Arası Dinlenme", blank=True,
                                          null=True)
    chest_kl_level1_knee = models.CharField(max_length=30, verbose_name='Knee Push-Up', blank=True, null=True)
    chest_kl_level1_hand = models.CharField(max_length=30, verbose_name='Hand Elevated Push-Up', blank=True, null=True)
    chest_kl_level1_reverse = models.CharField(max_length=30, verbose_name='Reverse Push-Up', blank=True, null=True)
    chest_kl_level1_hip = models.CharField(max_length=30, verbose_name='Push-Up and Hip Abduction', blank=True, null=True)
    chest_kl_level1_svend = models.CharField(max_length=30, verbose_name='Svend Press w/Med Ball', blank=True, null=True)
    chest_kl_level1_decline = models.CharField(max_length=30, verbose_name='Decline Push-Up/Feet Elevated',
                                               blank=True, null=True)
    chest_kl_level1_chest = models.CharField(max_length=30, verbose_name='Chest Pass w/Med Ball', blank=True, null=True)
    chest_kl_level2_pushup = models.CharField(max_length=30, verbose_name='Push-up', blank=True, null=True)
    chest_kl_level2_archer = models.CharField(max_length=30, verbose_name='Archer Push-Up', blank=True, null=True)
    chest_kl_level2_reverse = models.CharField(max_length=30, verbose_name='Reverse Push-Up', blank=True, null=True)
    chest_kl_level2_hip = models.CharField(max_length=30, verbose_name='Push-Up and Hip Abduction', blank=True, null=True)
    chest_kl_level2_depthdrop = models.CharField(max_length=30, verbose_name='Depth-drop Push-up', blank=True, null=True)
    chest_kl_level2_diver = models.CharField(max_length=30, verbose_name='Diver Bomb Push-Up', blank=True, null=True)
    chest_kl_level2_decline = models.CharField(max_length=30, verbose_name='Decline Push-Up/Feet Elevated',
                                               blank=True, null=True)
    chest_kl_level2_rolling = models.CharField(max_length=30, verbose_name='Push-Up Rolling w/Med Ball', blank=True, null=True)
    chest_kl_level2_cross = models.CharField(max_length=30, verbose_name='Cross Over Push-Up', blank=True, null=True)
    chest_kl_level2_chest = models.CharField(max_length=30, verbose_name='Chest Pass w/Med Ball', blank=True, null=True)
    chest_kl_level3_jumping = models.CharField(max_length=30, verbose_name='Jumping Push-Up', blank=True, null=True)
    chest_kl_level3_diamond = models.CharField(max_length=30, verbose_name='Diamond Push-Up', blank=True, null=True)
    chest_kl_level3_archer = models.CharField(max_length=30, verbose_name='Archer Push-Up', blank=True, null=True)
    chest_kl_level3_tpushup = models.CharField(max_length=30, verbose_name='T-Push-Up', blank=True, null=True)
    chest_kl_level3_depthdrop = models.CharField(max_length=30, verbose_name='Depth-drop Push', blank=True, null=True)
    chest_kl_level3_diver = models.CharField(max_length=30, verbose_name='Diver Bomb Push-up', blank=True, null=True)
    chest_kl_level3_dips = models.CharField(max_length=30, verbose_name='Paralel Dips', blank=True, null=True)
    chest_kl_level3_rotational = models.CharField(max_length=30, verbose_name='Rotational Throw w/Med Bal',
                                                  blank=True, null=True)
    chest_kl_level3_rolling = models.CharField(max_length=30, verbose_name='Push-Up Rolling w/Med Ball', blank=True, null=True)
    chest_wg_level1_barbell = models.CharField(max_length=40, verbose_name='Flat Bench Chest Press w/Barbell',
                                               blank=True, null=True)
    chest_wg_level1_dumbbell = models.CharField(max_length=40, verbose_name='Flat Bench Chest Press w/Dumbbell',
                                                blank=True, null=True)
    chest_wg_level1_bilateral = models.CharField(max_length=50,
                                                 verbose_name='Flat Bench Bilateral Chest Press w/Dumbbell',
                                                 blank=True, null=True)
    chest_wg_level1_inc = models.CharField(max_length=50, verbose_name='Incline Bench Bilateral Chest Press',
                                           blank=True, null=True)
    chest_wg_level1_decline = models.CharField(max_length=50, verbose_name='Decline Bench Chest Press w/Dumbbell',
                                               blank=True, null=True)
    chest_wg_level1_decline_bil = models.CharField(max_length=50,
                                                   verbose_name='Decline Bench Bilateral Chest Press w/Dumbbell',
                                                   blank=True, null=True)
    chest_wg_level1_flat_fly = models.CharField(max_length=50, verbose_name='Flat Bench Chest Fly w/Dumbbell & KB',
                                                blank=True, null=True)
    chest_wg_level1_inc_fly = models.CharField(max_length=50, verbose_name='Incline Bench Chest Fly w/Dumbbell',
                                               blank=True, null=True)
    chest_wg_level1_dc_fly = models.CharField(max_length=50, verbose_name='Decline Bench Chest Fly w/Dumbbell',
                                              blank=True, null=True)
    chest_wg_level1_flr_ch = models.CharField(max_length=50, verbose_name='Floor Chest Press w/Dumbbell & Kettlebell',
                                              blank=True, null=True)
    chest_wg_level1_flr_fly = models.CharField(max_length=50, verbose_name='Floor Fly w/Kettlebell & Dumbbell',
                                               blank=True, null=True)

    chest_wg_level2_barbell = models.CharField(max_length=50, verbose_name='Flat Bench Chest Press w/Barbell',
                                               blank=True, null=True)
    chest_wg_level2_dambbell = models.CharField(max_length=50,
                                                verbose_name='Flat Bench Bilateral Chest Press w/Dumbbell',
                                                blank=True, null=True)
    chest_wg_level2_unilateral = models.CharField(max_length=50,
                                                  verbose_name='Flat Bench Unilateral Chest Press w/Dumbbell',
                                                  blank=True, null=True)
    chest_wg_level2_incline = models.CharField(max_length=50, verbose_name='Incline Bench Chest Press w/Dumbbell',
                                               blank=True, null=True)
    chest_wg_level2_inc_bil = models.CharField(max_length=50, verbose_name='Incline Bench Bilateral Chest Press',
                                               blank=True, null=True)
    chest_wg_level2_inc_cntr = models.CharField(max_length=50, verbose_name='Incline Bench Contralateral Chest Press',
                                                blank=True, null=True)
    chest_wg_level2_decline = models.CharField(max_length=50, verbose_name='Decline Bench Chest Press w/Barbell',
                                               blank=True, null=True)
    chest_wg_level2_dc_bil = models.CharField(max_length=50,
                                              verbose_name='Decline Bench Bilateral Chest Press w/Dumbbell',
                                              blank=True, null=True)
    chest_wg_level2_dc_cntr = models.CharField(max_length=50,
                                               verbose_name='Decline Bench Contralateral Chest Press w/Dumbbell',
                                               blank=True, null=True)
    chest_wg_level2_inc_fly = models.CharField(max_length=50, verbose_name='Incline Bench Chest Fly w/Dumbbell',
                                               blank=True, null=True)
    chest_wg_level2_flt_svnd = models.CharField(max_length=50, verbose_name='Flat Bench Svend Press w/Plate',
                                                blank=True, null=True)
    chest_wg_level2_flr = models.CharField(max_length=50, verbose_name='Floor Chest Press w/Dumbbell & Kettlebell',
                                           blank=True, null=True)
    chest_wg_level2_single = models.CharField(max_length=50, verbose_name='Single- Arm Floor Press w/Kettlebell',
                                              blank=True, null=True)
    chest_wg_level2_oblq = models.CharField(max_length=60,
                                            verbose_name='Oblique Sling Chest Press w/Deadbug Dumell & Kettlebell',
                                            blank=True, null=True)

    chest_wg_level3_unilateral = models.CharField(max_length=50,
                                                  verbose_name='Flat Bench Unilateral Chest Press w/Dumbell',
                                                  blank=True, null=True)
    chest_wg_level3_barbell = models.CharField(max_length=50, verbose_name='Incline Bench Chest Press w/Barbell',
                                               blank=True, null=True)
    chest_wg_level3_dumbbell = models.CharField(max_length=50, verbose_name='Incline Bench Chest Press w/Dumbbell',
                                                blank=True, null=True)
    chest_wg_level3_contr = models.CharField(max_length=50, verbose_name='Incline Bench Contralateral Chest Press',
                                             blank=True, null=True)
    chest_wg_level3_oblique = models.CharField(max_length=60,
                                               verbose_name='Oblique Sling Chest Press w/Deadbug Dumell&Kettlebell',
                                               blank=True, null=True)
    chest_wg_level3_hangig = models.CharField(max_length=50, verbose_name='Hangig Kettlebell Bench Press',
                                              blank=True, null=True)
    chest_wg_level3_throw = models.CharField(max_length=50, verbose_name='Flat Bench Press Throw w/Barbell',
                                             blank=True, null=True)
    chest_wg_level3_inc_landmine = models.CharField(max_length=50, verbose_name='Incline Landmine Press', blank=True, null=True)
    chest_wg_level3_crossover = models.CharField(max_length=50, verbose_name='Landmine Crossover', blank=True, null=True)
    chest_wg_level3_crush = models.CharField(max_length=50, verbose_name='Crush Grip Push Up', blank=True, null=True)

    chest_mc_level1_seated = models.CharField(max_length=50, verbose_name='Seated Machine Chest Press', blank=True, null=True)
    chest_mc_level1_st_fly = models.CharField(max_length=50, verbose_name='Seated Machine Chest Fly (Butterfly)',
                                              blank=True, null=True)
    chest_mc_level1_flat = models.CharField(max_length=50, verbose_name='Flat Bench Smith Machine Chest Press',
                                            blank=True, null=True)
    chest_mc_level1_decline = models.CharField(max_length=50, verbose_name='Decline Bench Smith Machine Chest Press',
                                               blank=True, null=True)
    chest_mc_level1_incline = models.CharField(max_length=50, verbose_name='Incline Bench Smith Machine Chest Press',
                                               blank=True, null=True)

    chest_mc_level2_flat = models.CharField(max_length=50, verbose_name='Flat Bench Smith Machine Chest Press',
                                            blank=True, null=True)
    chest_mc_level2_dc_smith = models.CharField(max_length=50, verbose_name='Decline Bench Smith Machine Chest Press',
                                                blank=True, null=True)
    chest_mc_level2_inc_smith = models.CharField(max_length=50, verbose_name='Incline Bench Smith Machine Chest Press',
                                                 blank=True, null=True)
    chest_mc_level2_flt_single = models.CharField(max_length=50,
                                                  verbose_name='Flat Bench Single-Arm Chest Press w/Cable',
                                                  blank=True, null=True)
    chest_mc_level2_standing = models.CharField(max_length=50, verbose_name='Standing Stability Chest Press w/Cable',
                                                blank=True, null=True)
    chest_mc_level2_incline = models.CharField(max_length=50, verbose_name='Incline Bench Chest Press w/Cable',
                                               blank=True, null=True)
    chest_mc_level2_decline = models.CharField(max_length=50, verbose_name='Decline Bench Chest Press w/Cable',
                                               blank=True, null=True)
    chest_mc_level2_high = models.CharField(max_length=50, verbose_name='High Cable Chest Fly (Cable Crossover)',
                                            blank=True, null=True)
    chest_mc_level2_low = models.CharField(max_length=50, verbose_name='Low Cable Chest Fly', blank=True, null=True)
    chest_mc_level2_middle = models.CharField(max_length=50, verbose_name='Middle Cable Chest Fly', blank=True, null=True)
    chest_mc_level2_inc_fly = models.CharField(max_length=50, verbose_name='Incline Bench Chest Fly w/Cable',
                                               blank=True, null=True)
    chest_mc_level2_dc_fly = models.CharField(max_length=50, verbose_name='Decline Bench Chest Fly w/Cable',
                                              blank=True, null=True)

    chest_mc_level3_machine = models.CharField(max_length=50, verbose_name='Flat Bench Smith Machine Chest Throw',
                                               blank=True, null=True)
    chest_mc_level3_incline = models.CharField(max_length=50, verbose_name='Incline Bench Chest Press w/Cable',
                                               blank=True, null=True)
    chest_mc_level3_decline = models.CharField(max_length=50, verbose_name='Decline Bench Chest Press w/Cable',
                                               blank=True, null=True)
    chest_mc_level3_push = models.CharField(max_length=50, verbose_name='Push Position Cable Chest Fly  w/Cable',
                                            blank=True, null=True)
    chest_mc_level3_single = models.CharField(max_length=50, verbose_name='Single Leg Chest Fly  w/Cable',
                                              blank=True, null=True)
    chest_mc_level3_bird = models.CharField(max_length=50, verbose_name='Bird Dog Chest Fly  w/Cable', blank=True, null=True)
    chest_mc_level3_dead = models.CharField(max_length=50, verbose_name='Dead Bug Chest Fly  w/Cable', blank=True, null=True)
    chest_mc_level3_inc_fly = models.CharField(max_length=50, verbose_name='Incline Bench Chest Fly  w/Cable',
                                               blank=True, null=True)
    chest_mc_level3_dc_fly = models.CharField(max_length=50, verbose_name='Decline Full Range Fly  w/Cable',
                                              blank=True, null=True)
    chest_mc_level3_dc_chop = models.CharField(max_length=50, verbose_name='Decline Chop, Tall Kneeling', blank=True, null=True)
    chest_mc_level3_cable = models.CharField(max_length=50,
                                             verbose_name='Cable Tall Kneeling Single Arm Chest Fly w/Cable',
                                             blank=True, null=True)

    chest_rc_level1_pushup = models.CharField(max_length=50, verbose_name='Push-Up w/RB', blank=True, null=True)
    chest_rc_level1_dynamic = models.CharField(max_length=50, verbose_name='Dynamic Hug w/RB', blank=True, null=True)
    chest_rc_level1_serratus = models.CharField(max_length=50, verbose_name='Serratus Punch w/RB', blank=True, null=True)
    chest_rc_level1_diagonal = models.CharField(max_length=50, verbose_name='Diagonal Cross w/RB', blank=True, null=True)
    chest_rc_level1_chest = models.CharField(max_length=50, verbose_name='Chest Fly', blank=True, null=True)
    chest_rc_level1_psh_plus = models.CharField(max_length=50, verbose_name='Push-Up Plus w/Strap', blank=True, null=True)
    chest_rc_level1_single = models.CharField(max_length=50, verbose_name='Single Arm Chest Press w/Straps',
                                              blank=True, null=True)
    chest_rc_level1_ch_fly = models.CharField(max_length=50, verbose_name='Chest Fly  Offset Stance w/Straps',
                                              blank=True, null=True)

    chest_rc_level2_pushup = models.CharField(max_length=40, verbose_name='Push-Up w/RB', blank=True, null=True)
    chest_rc_level2_flat = models.CharField(max_length=40, verbose_name='Flat Bench Press w/RB', blank=True, null=True)
    chest_rc_level2_wrap = models.CharField(max_length=40, verbose_name='Wrap Around Press w/RB', blank=True, null=True)
    chest_rc_level2_incline = models.CharField(max_length=40, verbose_name='Incline Chest Press w/RB', blank=True, null=True)
    chest_rc_level2_decline = models.CharField(max_length=40, verbose_name='Decline Chest Press w/RB', blank=True, null=True)
    chest_rc_level2_dc_fly = models.CharField(max_length=40, verbose_name='Decline Standing Chest Fly w/RB',
                                              blank=True, null=True)
    chest_rc_level2_prone = models.CharField(max_length=40, verbose_name='Prone Punchouts w/RB', blank=True, null=True)
    chest_rc_level2_rotational = models.CharField(max_length=50,
                                                  verbose_name='Rotational Lunge with one-arm Chest Press w/RB',
                                                  blank=True, null=True)
    chest_rc_level2_chest = models.CharField(max_length=40, verbose_name='Chest Fly', blank=True, null=True)
    chest_rc_level2_sngl_leg = models.CharField(max_length=40, verbose_name='Single Leg Flexed  Chest Fly w/Straps',
                                                blank=True, null=True)
    chest_rc_level2_sndl_arm = models.CharField(max_length=40, verbose_name='Single Arm Chest Press w/Straps',
                                                blank=True, null=True)
    chest_rc_level2_drop = models.CharField(max_length=40, verbose_name='Drop Push-Up w/Strap', blank=True, null=True)
    chest_rc_level2_ch_press = models.CharField(max_length=40, verbose_name='Chest Press, Inside Grip w/Strap',
                                                blank=True, null=True)

    chest_rc_level3_pushup = models.CharField(max_length=40, verbose_name='Push Up and  Chest Fly w/RB', blank=True, null=True)
    chest_rc_level3_wrap = models.CharField(max_length=40, verbose_name='Wrap Around Press w/RB', blank=True, null=True)
    chest_rc_level3_incline = models.CharField(max_length=40, verbose_name='Incline Chest Press w/RB', blank=True, null=True)
    chest_rc_level3_decline = models.CharField(max_length=40, verbose_name='Decline Chest Press w/RB', blank=True, null=True)
    chest_rc_level3_st_standing = models.CharField(max_length=40, verbose_name='Decline Standing Chest  Fly w/RB',
                                                   blank=True, null=True)
    chest_rc_level3_plank = models.CharField(max_length=40, verbose_name='Plank & Push Punchouts w/RB', blank=True, null=True)
    chest_rc_level3_sngl_fly = models.CharField(max_length=40, verbose_name='Single-Arm Chest Fly w/Strap',
                                                blank=True, null=True)
    chest_rc_level3_sngl_ex = models.CharField(max_length=40, verbose_name='Single Leg Extended Chest Press w/Straps',
                                               blank=True, null=True)
    chest_rc_level3_sngl_arm = models.CharField(max_length=40, verbose_name='Single Leg Chest Press Single Arm w/RB',
                                                blank=True, null=True)
    chest_rc_level3_inc_pushup = models.CharField(max_length=40, verbose_name='Incline Push-Up w/Strap', blank=True, null=True)
    chest_rc_level3_suspended = models.CharField(max_length=40, verbose_name='Suspended Push-Up w/Strap', blank=True, null=True)
    chest_rc_level3_prone = models.CharField(max_length=40, verbose_name='Prone Iron Cross  w/Strap', blank=True, null=True)
    chest_rc_level3_crunch = models.CharField(max_length=40, verbose_name='Push-Up w/Reverse Crunch ', blank=True, null=True)
    chest_rc_level3_oblique = models.CharField(max_length=50, verbose_name='Suspended Oblique Atomic  Push Up w/Strap',
                                               blank=True, null=True)
    chest_rc_level3_drop = models.CharField(max_length=50, verbose_name='Drop Push-Up w/Strap', blank=True, null=True)
    chest_rc_level3_explosive = models.CharField(max_length=50, verbose_name='Explosive Push-Up', blank=True, null=True)

    class Meta:
        verbose_name = "Egzersiz Reçetesi"
        verbose_name_plural = 'Göğüs'


class exercise_prescription_shoulder(models.Model):
    # Akut Değişkeni/Omuz
    shld_set_number = models.CharField(max_length=5, verbose_name="Set Sayısı", blank=True, null=True)
    shld_over_number = models.CharField(max_length=5, verbose_name="Tekrar Sayısı", blank=True, null=True)
    shld_tempo = models.CharField(max_length=10, verbose_name="Tempo (TUT)", blank=True, null=True)
    # Setler arası dinlenme
    shld_sets_between = models.CharField(max_length=10, verbose_name="Setler Arası Dinlenme", blank=True, null=True)
    shld_move_between = models.CharField(max_length=10, verbose_name="Hareketler Arası Dinlenme", blank=True, null=True)

    shld_kl_level1_rotator = models.CharField(max_length=50, verbose_name='Shoulder Rotator Cuff Rotation 90 Degree',
                                              blank=True, null=True)
    shld_kl_level1_shoulder = models.CharField(max_length=50, verbose_name='Shoulder W at Wall', blank=True, null=True)
    shld_kl_level1_sphinx = models.CharField(max_length=50, verbose_name='Sphinx Pose with Shoulder Forward Reach',
                                             blank=True, null=True)
    shld_kl_level1_pushup = models.CharField(max_length=50, verbose_name='Push-Up Squat to Press w/Medicine Ball',
                                             blank=True, null=True)
    shld_kl_level1_overhead = models.CharField(max_length=50, verbose_name='Overhead Reach w/Medicine Ball',
                                               blank=True, null=True)
    shld_kl_level1_ys = models.CharField(max_length=50, verbose_name='Dumbbell Shoulder Y’s', blank=True, null=True)
    shld_kl_level1_as = models.CharField(max_length=50, verbose_name='Dumbbell Shoulder A’s', blank=True, null=True)
    shld_kl_level1_ts = models.CharField(max_length=50, verbose_name='Dumbbell Shoulder T’s', blank=True, null=True)

    shld_kl_level2_inverted = models.CharField(max_length=50, verbose_name='Inverted Shoulder Press', blank=True, null=True)
    shld_kl_level2_wall = models.CharField(max_length=50, verbose_name='Wall Ball w/Medicine Ball', blank=True, null=True)
    shld_kl_level2_pushup = models.CharField(max_length=50, verbose_name='Push-Up Squat to Press w/Medicine Ball',
                                             blank=True, null=True)
    shld_kl_level2_diagonal = models.CharField(max_length=50, verbose_name='Diagonal Chop and Lift w/Medicine Ball',
                                               blank=True, null=True)
    shld_kl_level2_reverse = models.CharField(max_length=50, verbose_name='Reverse Scoop Throw w/Medicine Ball',
                                              blank=True, null=True)

    shld_kl_level3_wall = models.CharField(max_length=50, verbose_name='Wall Walk', blank=True, null=True)
    shld_kl_level3_handstand = models.CharField(max_length=50, verbose_name='Handstand Push-Up', blank=True, null=True)
    shld_kl_level3_reverse = models.CharField(max_length=50, verbose_name='Reverse Scoop Throw w/Medicine Ball',
                                              blank=True, null=True)

    shld_wg_level1_std_dumbbell = models.CharField(max_length=50, verbose_name='Seated Dumbbell Shoulder Press',
                                                   blank=True, null=True)
    shld_wg_level1_sd_shoulder = models.CharField(max_length=50,
                                                  verbose_name='Standing Dumbbell Shoulder Press w/Dumbbell &KB',
                                                  blank=True, null=True)
    shld_wg_level1_tl_dumbbell = models.CharField(max_length=60,
                                                  verbose_name='Tall Kneeling Dumbbell Shoulder Press w/Dumbell & KB ',
                                                  blank=True, null=True)
    shld_wg_level1_barbell = models.CharField(max_length=50, verbose_name='Barbell Overhead Push Press', blank=True, null=True)
    shld_wg_level1_lseated = models.CharField(max_length=50, verbose_name='Dumbbell L-Seated Shoulder Z Press',
                                              blank=True, null=True)
    shld_wg_level1_alternating = models.CharField(max_length=50, verbose_name='Alternating Shoulder Press w/Dumbbell',
                                                  blank=True, null=True)
    shld_wg_level1_onearm = models.CharField(max_length=50, verbose_name='One-Arm Shoulder Press  w/Dumbbell',
                                             blank=True, null=True)
    shld_wg_level1_side = models.CharField(max_length=50, verbose_name='Dumbbell Side Lying Lateral Raise',
                                           blank=True, null=True)
    shld_wg_level1_sd_lateral = models.CharField(max_length=50, verbose_name='Standing Dumbbell Lateral Raise',
                                                 blank=True, null=True)
    shld_wg_level1_std_lateral = models.CharField(max_length=50, verbose_name='Seated Dumbell Lateral Raise',
                                                  blank=True, null=True)
    shld_wg_level1_shl_bench = models.CharField(max_length=50, verbose_name='Shoulder Reverse on Bench Fly  w/Dumbbell',
                                                blank=True, null=True)
    shld_wg_level1_shl_front = models.CharField(max_length=50, verbose_name='Shoulder Front Raise w/Dumbbell',
                                                blank=True, null=True)
    shld_wg_level1_shl_raise = models.CharField(max_length=50, verbose_name='Shoulder Front Raise w/Plate',
                                                blank=True, null=True)
    shld_wg_level1_tl_knee = models.CharField(max_length=60,
                                              verbose_name='Tall Kneeling Shoulder Front Raise w/Dumbell & Plate',
                                              blank=True, null=True)
    shld_wg_level1_up_dumbbell = models.CharField(max_length=50, verbose_name='Upright Row w/Dumbbell', blank=True, null=True)
    shld_wg_level1_up_barbell = models.CharField(max_length=50, verbose_name='Upright Row w/BarBell', blank=True, null=True)
    shld_wg_level1_wide_arm = models.CharField(max_length=50, verbose_name='Dumbbell Wide-Arm Upright Row',
                                               blank=True, null=True)
    shld_wg_level1_power = models.CharField(max_length=50, verbose_name='Power Jerk w/Dumbbell', blank=True, null=True)

    shld_wg_level2_flat = models.CharField(max_length=50, verbose_name='Flat Barbell Standing Shoulder Press',
                                           blank=True, null=True)
    shld_wg_level2_barbell = models.CharField(max_length=50, verbose_name='Barbell Overhead Push Press', blank=True, null=True)
    shld_wg_level2_shl_bottom = models.CharField(max_length=50, verbose_name='Shoulder Bottom-Up w/KB', blank=True, null=True)
    shld_wg_level2_seated = models.CharField(max_length=50, verbose_name='Seated Barbell Shoulder Press', blank=True, null=True)
    shld_wg_level2_lseated = models.CharField(max_length=50, verbose_name='Dumbbell L-Seated Shoulder Z Press',
                                              blank=True, null=True)
    shld_wg_level2_kettlebell = models.CharField(max_length=50, verbose_name='One Arm Kettlebell Push Press',
                                                 blank=True, null=True)
    shld_wg_level2_alternating = models.CharField(max_length=50, verbose_name='Alternating Shoulder Press w/Dumbbell',
                                                  blank=True, null=True)
    shld_wg_level2_onearm = models.CharField(max_length=50, verbose_name='One-Arm Shoulder Press w/Dumbbell',
                                             blank=True, null=True)
    shld_wg_level2_side = models.CharField(max_length=50, verbose_name='Dumbbell Side Lying Lateral Raise',
                                           blank=True, null=True)
    shld_wg_level2_reverse = models.CharField(max_length=50, verbose_name='Shoulder Reverse on Bench Fly w/Dumbbell',
                                              blank=True, null=True)
    shld_wg_level2_bent = models.CharField(max_length=50, verbose_name='Bent Over Dumbell Reverse Fly wDumbell / KB',
                                           blank=True, null=True)
    shld_wg_level2_overhead = models.CharField(max_length=50, verbose_name='Kettlebell Overhead Swing', blank=True, null=True)
    shld_wg_level2_front = models.CharField(max_length=50, verbose_name='Shoulder Front Raise w/Plate', blank=True, null=True)
    shld_wg_level2_bentover = models.CharField(max_length=50, verbose_name='Bent-Over Dumbbell Shoulder Fly',
                                               blank=True, null=True)
    shld_wg_level2_up_dumbbell = models.CharField(max_length=50, verbose_name='Upright Row w/Dumbbell', blank=True, null=True)
    shld_wg_level2_up_barbell = models.CharField(max_length=50, verbose_name='Upright Row w/BarBell', blank=True, null=True)
    shld_wg_level2_widearm = models.CharField(max_length=50, verbose_name='Dumbbell Wide-Arm Upright Row',
                                              blank=True, null=True)
    shld_wg_level2_thruster = models.CharField(max_length=50, verbose_name='Dumbbell Thruster', blank=True, null=True)
    shld_wg_level2_lunge = models.CharField(max_length=50, verbose_name='Front Lunge with Lateral Raise w/Dumbbell',
                                            blank=True, null=True)
    shld_wg_level2_pw_dumbbell = models.CharField(max_length=50, verbose_name='Power Jerk w/Dumbbell', blank=True, null=True)
    shld_wg_level2_pw_barbell = models.CharField(max_length=50, verbose_name='Power Jerk w/Barbell', blank=True, null=True)
    shld_wg_level2_alt_power = models.CharField(max_length=50, verbose_name='Alternating Power Jerk w/Dumbbell',
                                                blank=True, null=True)
    shld_wg_level2_sp_jerk = models.CharField(max_length=50, verbose_name='Split Alternating-Feet Jerk', blank=True, null=True)
    shld_wg_level2_sp_feet = models.CharField(max_length=50, verbose_name='Split Alternating-Feet Alternating-Arm Jerk',
                                              blank=True, null=True)

    shld_wg_level3_shoulder = models.CharField(max_length=50, verbose_name='Shoulder Bottom-Up Pres w/KB',
                                               blank=True, null=True)
    shld_wg_level3_std_barbell = models.CharField(max_length=50, verbose_name='Seated Barbell  Shoulder Press',
                                                  blank=True, null=True)
    shld_wg_level3_rotational = models.CharField(max_length=50, verbose_name='One-Arm Dumbbell Rotational Push Press',
                                                 blank=True, null=True)
    shld_wg_level3_unilateral = models.CharField(max_length=50, verbose_name='Standing Unilateral  Dumbell Press',
                                                 blank=True, null=True)
    shld_wg_level3_angled = models.CharField(max_length=50, verbose_name='Angled Barbell  Press (Landmine)',
                                             blank=True, null=True)
    shld_wg_level3_side = models.CharField(max_length=50, verbose_name='Side Bridge and Lateral Raise w/Dumbbell',
                                           blank=True, null=True)
    shld_wg_level3_snatch = models.CharField(max_length=50, verbose_name='Dumbbell Snatch', blank=True, null=True)
    shld_wg_level3_ropes = models.CharField(max_length=50, verbose_name='Battle Ropes, Double Wave', blank=True, null=True)
    shld_wg_level3_kettlebell = models.CharField(max_length=50, verbose_name='Kettlebell Overhead Swing', blank=True, null=True)
    shld_wg_level3_upright = models.CharField(max_length=50, verbose_name='Upright Row with Triple Extension Barbell',
                                              blank=True, null=True)
    shld_wg_level3_brb_thruster = models.CharField(max_length=50, verbose_name='Barbell Thruster', blank=True, null=True)
    shld_wg_level3_dmb_thruster = models.CharField(max_length=50, verbose_name='Dumbbell Thruster', blank=True, null=True)
    shld_wg_level3_push = models.CharField(max_length=50, verbose_name='Push Ups  with Shoulder Abduction w/Dumbbell',
                                           blank=True, null=True)
    shld_wg_level3_onearm_ket = models.CharField(max_length=50, verbose_name='One Arm Kettlebell Push and Jerk',
                                                 blank=True, null=True)
    shld_wg_level3_lunge = models.CharField(max_length=50, verbose_name='Front Lunge with Lateral Raise w/Dumbbell',
                                            blank=True, null=True)
    shld_wg_level3_pw_jerk = models.CharField(max_length=50, verbose_name='Power Jerk w/Barbell', blank=True, null=True)
    shld_wg_level3_split = models.CharField(max_length=50, verbose_name='Split Alternating-Feet Alternating-Arm Jerk',
                                            blank=True, null=True)

    shld_mc_level1_cb_onearm = models.CharField(max_length=50, verbose_name='Cable One-Arm Shoulder Press',
                                                blank=True, null=True)
    shld_mc_level1_rear = models.CharField(max_length=50, verbose_name='Rear Deltoid High Row (Machine)', blank=True, null=True)
    shld_mc_level1_shl_reverse = models.CharField(max_length=50, verbose_name='Shoulder Reverse Fly (Cable)',
                                                  blank=True, null=True)
    shld_mc_level1_upright = models.CharField(max_length=50, verbose_name='Upright Rows (Low Pulley) w/cable',
                                              blank=True, null=True)
    shld_mc_level1_onearm_lateral = models.CharField(max_length=50, verbose_name='One-arm Cable Lateral Raise',
                                                     blank=True, null=True)
    shld_mc_level1_onearm_front = models.CharField(max_length=50, verbose_name='One-arm Cable Front Raise',
                                                   blank=True, null=True)
    shld_mc_level1_shl_front = models.CharField(max_length=50, verbose_name='Shoulder Front Raise w/Cable',
                                                blank=True, null=True)
    shld_mc_level1_cb_reverse = models.CharField(max_length=50, verbose_name='Cable Reverse Shoulder Fly',
                                                 blank=True, null=True)

    shld_mc_level2_behind = models.CharField(max_length=60,
                                             verbose_name='Behind The Neck Press (Flat Barbell or Smith Machine)',
                                             blank=True, null=True)
    shld_mc_level2_cb_onearm = models.CharField(max_length=50, verbose_name='Cable One-Arm Shoulder Press',
                                                blank=True, null=True)
    shld_mc_level2_stability = models.CharField(max_length=50,
                                                verbose_name='Stability Cable Shoulder Press Progression',
                                                blank=True, null=True)
    shld_mc_level2_reverse = models.CharField(max_length=50, verbose_name='Reverse Stepping Chop (Rip Trainer)',
                                              blank=True, null=True)
    shld_mc_level2_rear = models.CharField(max_length=50, verbose_name='Rear Deltoid High Row (Machine)', blank=True, null=True)
    shld_mc_level2_bentavor = models.CharField(max_length=50, verbose_name='Bentover Reverse Fly (Cable)',
                                               blank=True, null=True)
    shld_mc_level2_onearm = models.CharField(max_length=50, verbose_name='One-arm Cable Lateral Raise', blank=True, null=True)
    shld_mc_level2_shoulder = models.CharField(max_length=50, verbose_name='Shoulder Front Raise w/Cable',
                                               blank=True, null=True)
    shld_mc_level2_rope = models.CharField(max_length=50, verbose_name='Rope Face Pull', blank=True, null=True)
    shld_mc_level2_cb_reverse = models.CharField(max_length=50, verbose_name='Cable Reverse Shoulder Fly',
                                                 blank=True, null=True)

    shld_mc_level3_shoulder = models.CharField(max_length=50, verbose_name='Shoulder Barbell Throw w Smite Machine',
                                               blank=True, null=True)
    shld_mc_level3_stability = models.CharField(max_length=50,
                                                verbose_name='Stability Cable Shoulder Press Progression',
                                                blank=True, null=True)
    shld_mc_level3_reverse = models.CharField(max_length=50, verbose_name='Reverse Stepping Chop (Rip Trainer)',
                                              blank=True, null=True)
    shld_mc_level3_rope = models.CharField(max_length=50, verbose_name='Rope Face Pull', blank=True, null=True)

    shld_rc_level1_Ideltoid = models.CharField(max_length=50, verbose_name='I Deltoid Fly w/Straps', blank=True, null=True)
    shld_rc_level1_Ydeltoid = models.CharField(max_length=50, verbose_name='Y Deltoid Fly w/Straps', blank=True, null=True)
    shld_rc_level1_dualarm = models.CharField(max_length=50, verbose_name='Dual-Arm External Rotation w/Straps',
                                              blank=True, null=True)
    shld_rc_level1_field = models.CharField(max_length=50, verbose_name='Field Goal w/Strap', blank=True, null=True)
    shld_rc_level1_press = models.CharField(max_length=50, verbose_name='Shoulder Press w/Resistance Band',
                                            blank=True, null=True)
    shld_rc_level1_front = models.CharField(max_length=50, verbose_name='Shoulder Front Raise w/RB', blank=True, null=True)
    shld_rc_level1_rear = models.CharField(max_length=50, verbose_name='Rear Deltoid Row w/RB', blank=True, null=True)
    shld_rc_level1_upright = models.CharField(max_length=50, verbose_name='Upright Row w/RB', blank=True, null=True)
    shld_rc_level1_kneeling = models.CharField(max_length=50, verbose_name='Kneeling Front Raise wRB', blank=True, null=True)

    shld_rc_level2_high = models.CharField(max_length=50, verbose_name='High Back Row w/Straps', blank=True, null=True)
    shld_rc_level2_Ideltoid = models.CharField(max_length=50, verbose_name='I Deltoid Fly w/Straps', blank=True, null=True)
    shld_rc_level2_Ydeltoid = models.CharField(max_length=50, verbose_name='Y Deltoid Fly w/Straps', blank=True, null=True)
    shld_rc_level2_dualarm = models.CharField(max_length=50, verbose_name='Dual-Arm ExternalRotation w/Strap',
                                              blank=True, null=True)
    shld_rc_level2_field = models.CharField(max_length=50, verbose_name='Field Goal w/Straps', blank=True, null=True)
    shld_rc_level2_shl_internal = models.CharField(max_length=50,
                                                   verbose_name='Shoulder Internal Rotation at 0 degrees w/RB',
                                                   blank=True, null=True)
    shld_rc_level2_shl_external = models.CharField(max_length=50,
                                                   verbose_name='Shoulder External Rotation at 0 degrees w/RB',
                                                   blank=True, null=True)
    shld_rc_level2_shl_press = models.CharField(max_length=50, verbose_name='Shoulder Press w/Resistance Band',
                                                blank=True, null=True)
    shld_rc_level2_bridhe = models.CharField(max_length=50, verbose_name='Bridge with Lateral Raise w/Resistance Band',
                                             blank=True, null=True)
    shld_rc_level2_shl_front = models.CharField(max_length=50, verbose_name='Shoulder Front Raise w/RB', blank=True, null=True)
    shld_rc_level2_diagonal = models.CharField(max_length=50, verbose_name='Diagonal Flexion w/RB', blank=True, null=True)
    shld_rc_level2_rear = models.CharField(max_length=50, verbose_name='Rear Deltoid Row w/RB', blank=True, null=True)
    shld_rc_level2_upright = models.CharField(max_length=50, verbose_name='Upright Row w/RB', blank=True, null=True)
    shld_rc_level2_kneeling = models.CharField(max_length=50, verbose_name='Kneeling Front Raise w/RB', blank=True, null=True)

    shld_rc_level3_high = models.CharField(max_length=50, verbose_name='High Back Row w/Straps', blank=True, null=True)
    shld_rc_level3_clock = models.CharField(max_length=50, verbose_name='Clock Press w/Strap', blank=True, null=True)
    shld_rc_level3_shl_internal = models.CharField(max_length=50,
                                                   verbose_name='Shoulder Internal Rotation at 0 degrees w/RB',
                                                   blank=True, null=True)
    shld_rc_level3_shl_external = models.CharField(max_length=50,
                                                   verbose_name='Shoulder External Rotation at 0 degrees w/RB',
                                                   blank=True, null=True)
    shld_rc_level3_bridge = models.CharField(max_length=50, verbose_name='Bridge with Lateral Raise w/Resistance Band',
                                             blank=True, null=True)

    class Meta:
        verbose_name = "Egzersiz Reçetesi"
        verbose_name_plural = 'Omuz'


class exercise_prescription_back(models.Model):
    # trainer = models.ForeignKey(to=Trainer, verbose_name="Antrenör", on_delete=models.CASCADE, blank=True, null=True)
    # personal = models.ForeignKey(to=Personal, verbose_name="Danışan", on_delete=models.CASCADE, blank=True, null=True)
    # date = models.DateField(("Date"), default=datetime.now(), blank=True)
    back_set_number = models.CharField(max_length=5, verbose_name="Set Sayısı", blank=True, null=True)
    back_over_number = models.CharField(max_length=5, verbose_name="Tekrar Sayısı", blank=True, null=True)
    back_tempo = models.CharField(max_length=10, verbose_name="Tempo (TUT)", blank=True, null=True)
    # Setler arası dinlenme
    back_sets_between = models.CharField(max_length=10, verbose_name="Setler Arası Dinlenme", blank=True, null=True)
    back_move_between = models.CharField(max_length=10, verbose_name="Hareketler Arası Dinlenme", blank=True, null=True)

    back_kl_level1_chinup = models.CharField(max_length=50, verbose_name='Chin-Up', blank=True, null=True)
    back_kl_level1_assisted = models.CharField(max_length=50, verbose_name='Assisted Pull-Up (Bodyweight)',
                                               blank=True, null=True)
    back_kl_level1_scapular = models.CharField(max_length=50, verbose_name='Scapular Pull-Up', blank=True, null=True)
    back_kl_level1_inverted = models.CharField(max_length=50, verbose_name='Inverted Row with Bar', blank=True, null=True)
    back_kl_level1_cobra = models.CharField(max_length=50, verbose_name='Cobra', blank=True, null=True)
    back_kl_level1_superman = models.CharField(max_length=50, verbose_name='Superman', blank=True, null=True)
    back_kl_level1_pulldown = models.CharField(max_length=50, verbose_name='Alternating Scapular Pull-Down',
                                               blank=True, null=True)
    back_kl_level1_plank = models.CharField(max_length=50, verbose_name='Alternating Plank Row (Renegade)',
                                            blank=True, null=True)

    back_kl_level2_pullup = models.CharField(max_length=50, verbose_name='Pull-Up (Bodyweight)', blank=True, null=True)
    back_kl_level2_chinup = models.CharField(max_length=50, verbose_name='Chin-Up', blank=True, null=True)
    back_kl_level2_with = models.CharField(max_length=50, verbose_name='Pull-Up with Legs Help', blank=True, null=True)
    back_kl_level2_assisted = models.CharField(max_length=50, verbose_name='Assisted Pull-Up (Bodyweight)',
                                               blank=True, null=True)
    back_kl_level2_scapular = models.CharField(max_length=50, verbose_name='Scapular Pull-Up ', blank=True, null=True)
    back_kl_level2_inverted = models.CharField(max_length=50, verbose_name='Inverted Row with Bar with Bar',
                                               blank=True, null=True)
    back_kl_level2_lsit = models.CharField(max_length=50, verbose_name='L-Sit Pull-Up (Bodyweight)', blank=True, null=True)
    back_kl_level2_asymmetric = models.CharField(max_length=50, verbose_name='Asymmetric Pull-Up (Bodyweight)',
                                                 blank=True, null=True)
    back_kl_level2_pulldown = models.CharField(max_length=50, verbose_name='Alternating Scapular Pull-Down',
                                               blank=True, null=True)
    back_kl_level2_plank = models.CharField(max_length=50, verbose_name='Alternating Plank Row (Renegade)',
                                            blank=True, null=True)

    back_kl_level3_pullup = models.CharField(max_length=50, verbose_name='Pull-Up (Bodyweight)', blank=True, null=True)
    back_kl_level3_jumping = models.CharField(max_length=50, verbose_name='Jumping Pull-Up', blank=True, null=True)
    back_kl_level3_resisted = models.CharField(max_length=50, verbose_name='Resisted Pull Up', blank=True, null=True)
    back_kl_level3_scapular = models.CharField(max_length=50, verbose_name='Scapular Pull-Up', blank=True, null=True)
    back_kl_level3_muscle = models.CharField(max_length=50, verbose_name='Muscle-Up', blank=True, null=True)
    back_kl_level3_lsit = models.CharField(max_length=50, verbose_name='L-Sit Pull-Up (Bodyweight)', blank=True, null=True)
    back_kl_level3_asymmetric = models.CharField(max_length=50, verbose_name='Asymmetric Pull-Up (Bodyweight)',
                                                 blank=True, null=True)
    back_kl_level3_alternating = models.CharField(max_length=50, verbose_name='Alternating Plank Row (Renegade)',
                                                  blank=True, null=True)

    back_wg_level1_bent = models.CharField(max_length=50, verbose_name='Bent Over Row w/Dumbbell', blank=True, null=True)
    back_wg_level1_amrbent = models.CharField(max_length=50, verbose_name='Single Arm Bent Over Row w/Dumbbell',
                                              blank=True, null=True)
    back_wg_level1_pullover = models.CharField(max_length=50, verbose_name='Pullover w/Dumbbell', blank=True, null=True)
    back_wg_level1_bag = models.CharField(max_length=50, verbose_name='Single-Arm Bag Row on Bench w/Dumbbell',
                                          blank=True, null=True)
    back_wg_level1_bench = models.CharField(max_length=50, verbose_name='Bench Lying Row w/Barbell & Dumbbell',
                                            blank=True, null=True)
    back_wg_level1_onearm = models.CharField(max_length=50, verbose_name='One-Arm Free Standing Row w/Dumbbell & KB',
                                             blank=True, null=True)

    back_wg_level2_barbell = models.CharField(max_length=50, verbose_name='Bent Over Row w/Barbell & Kettlebell',
                                              blank=True, null=True)
    back_wg_level2_dumbbell = models.CharField(max_length=50, verbose_name='Bent Over Row w/Dumbbell', blank=True, null=True)
    back_wg_level2_pullover = models.CharField(max_length=50, verbose_name='Pullover w/Dumbbell', blank=True, null=True)
    back_wg_level2_single = models.CharField(max_length=50, verbose_name='Single-Arm Bag Row on Bench w/Dumbbell',
                                             blank=True, null=True)
    back_wg_level2_bench = models.CharField(max_length=50, verbose_name='Bench Lying Row w/Barbell & Dumbbell',
                                            blank=True, null=True)
    back_wg_level2_tbar = models.CharField(max_length=50, verbose_name='T-Bar Row', blank=True, null=True)
    back_wg_level2_renegade = models.CharField(max_length=50, verbose_name='Renegade Row w/Dumbbell & KB',
                                               blank=True, null=True)
    back_wg_level2_one_sty_up = models.CharField(max_length=50, verbose_name='One-Stays-Up Row w/KB', blank=True, null=True)
    back_wg_level2_landmine = models.CharField(max_length=50, verbose_name='One-Arm Landmine Row', blank=True, null=True)
    back_wg_level2_free = models.CharField(max_length=50, verbose_name='One-Arm Free Standing Row w/Dumbbell & KB',
                                           blank=True, null=True)

    back_wg_level3_bent = models.CharField(max_length=50, verbose_name='Bent Over Row w/Barbell & Kettlebell',
                                           blank=True, null=True)
    back_wg_level3_single = models.CharField(max_length=50, verbose_name='Single Leg Bent Over Barbell Row',
                                             blank=True, null=True)
    back_wg_level3_tbar = models.CharField(max_length=50, verbose_name='T-Bar Row', blank=True, null=True)
    back_wg_level3_renegade = models.CharField(max_length=50, verbose_name='Renegade Row w/Dumbbell & KB',
                                               blank=True, null=True)
    back_wg_level3_landmine = models.CharField(max_length=50, verbose_name='One-Arm Landmine Row', blank=True, null=True)
    back_wg_level3_sinle = models.CharField(max_length=50, verbose_name='Single Leg One-Arm Landmine Row',
                                            blank=True, null=True)
    back_wg_level3_bench = models.CharField(max_length=50, verbose_name='One-Arm One-Leg Bench Row w/Dumbbell & KB',
                                            blank=True, null=True)

    back_mc_level1_std_wide = models.CharField(max_length=50, verbose_name='Seated Wide Grip Row w/Cable',
                                               blank=True, null=True)
    back_mc_level1_lat = models.CharField(max_length=50, verbose_name='Lat. Pull-Down w/Machine', blank=True, null=True)
    back_mc_level1_close = models.CharField(max_length=50, verbose_name='Close Grip Lat. Pull Down w/Cable',
                                            blank=True, null=True)
    back_mc_level1_reverse = models.CharField(max_length=50, verbose_name='Reverse Grip Lat. Pull-Down', blank=True, null=True)
    back_mc_level1_mc_pullover = models.CharField(max_length=50, verbose_name='Machine Pullover', blank=True, null=True)
    back_mc_level1_st_onearm = models.CharField(max_length=50, verbose_name='Standing One-Arm Row w/Cable',
                                                blank=True, null=True)
    back_mc_level1_mc_row = models.CharField(max_length=50, verbose_name='Machine Row', blank=True, null=True)

    back_mc_level2_std_wide = models.CharField(max_length=50, verbose_name='Seated Wide Grip Row w/Cable',
                                               blank=True, null=True)
    back_mc_level2_lat = models.CharField(max_length=50, verbose_name='Lat. Pull Down w/Cable', blank=True, null=True)
    back_mc_level2_leaning = models.CharField(max_length=50, verbose_name='Leaning Lat Pull-Down', blank=True, null=True)
    back_mc_level2_close = models.CharField(max_length=50, verbose_name='Close Grip Lat. Pull Down w/Cable',
                                            blank=True, null=True)
    back_mc_level2_reverse = models.CharField(max_length=50, verbose_name='Reverse Grip Lat. Pull-Down', blank=True, null=True)
    back_mc_level2_straight = models.CharField(max_length=50, verbose_name='Straight-Arm Lat. Pull-Down w/Cable',
                                               blank=True, null=True)
    back_mc_level2_standing = models.CharField(max_length=50, verbose_name='Standing One-Arm Row w/Cable',
                                               blank=True, null=True)
    back_mc_level2_onearm = models.CharField(max_length=50, verbose_name='One-Arm Cable Row With Hip Rotation',
                                             blank=True, null=True)
    back_mc_level2_bent = models.CharField(max_length=50, verbose_name='Bent-Over One-Arm Cable Row', blank=True, null=True)
    back_mc_level2_cable = models.CharField(max_length=50, verbose_name='Cable-Rope Tug-of-War Row', blank=True, null=True)

    back_mc_level3_leaning = models.CharField(max_length=50, verbose_name='Leaning Lat Pull-Down', blank=True, null=True)
    back_mc_level3_fighter = models.CharField(max_length=50, verbose_name='Fighter’s Cable Lat Pull-Down',
                                              blank=True, null=True)
    back_mc_level3_Straight = models.CharField(max_length=50, verbose_name='Straight-Arm Lat. Pull-Down w/Cable',
                                               blank=True, null=True)
    back_mc_level3_Lunge = models.CharField(max_length=50, verbose_name='Lunge Position One-Arm Row w/Cable',
                                            blank=True, null=True)
    back_mc_level3_Cb_Row = models.CharField(max_length=50, verbose_name='One-Arm Cable Row With Hip Rotation',
                                             blank=True, null=True)
    back_mc_level3_Bent = models.CharField(max_length=50, verbose_name='Bent-Over One-Arm Cable Row', blank=True, null=True)
    back_mc_level3_Cb_Rope = models.CharField(max_length=50, verbose_name='Cable-Rope Tug-of-War Row', blank=True, null=True)

    back_rc_level1_Row = models.CharField(max_length=50, verbose_name='Seated Row w/RB', blank=True, null=True)
    back_rc_level1_Linton = models.CharField(max_length=50, verbose_name='Linton External Rotation w/RB', blank=True, null=True)
    back_rc_level1_Bilateral = models.CharField(max_length=50, verbose_name='Bilateral Extension With Retraction w/RB',
                                                blank=True, null=True)
    back_rc_level1_Upright = models.CharField(max_length=50, verbose_name='Upright Row w/RB', blank=True, null=True)
    back_rc_level1_Supine = models.CharField(max_length=50, verbose_name='Supine Pullover w/RB', blank=True, null=True)
    back_rc_level1_Shrug = models.CharField(max_length=50, verbose_name='Shrug w/RB', blank=True, null=True)
    back_rc_level1_Lying = models.CharField(max_length=50,
                                            verbose_name='Lying Close-Grip Lat Pulldown w/Resistance Band',
                                            blank=True, null=True)
    back_rc_level1_Single = models.CharField(max_length=50, verbose_name='Single Arm Row, on Bench w/Resistance Band',
                                             blank=True, null=True)
    back_rc_level1_Resistance = models.CharField(max_length=50, verbose_name='Seated Row /Resistance Band',
                                                 blank=True, null=True)
    back_rc_level1_Back = models.CharField(max_length=50, verbose_name='Back Row w/Resistance Band & Straps',
                                           blank=True, null=True)
    back_rc_level1_Low = models.CharField(max_length=50, verbose_name='Low Row w/Strap', blank=True, null=True)
    back_rc_level1_Split = models.CharField(max_length=50, verbose_name='Split Fly w/Strap', blank=True, null=True)

    back_rc_level2_Pullup = models.CharField(max_length=50, verbose_name='Pull-Up w/Band', blank=True, null=True)
    back_rc_level2_Row = models.CharField(max_length=50, verbose_name='Seated Row w/RB', blank=True, null=True)
    back_rc_level2_Bent = models.CharField(max_length=50, verbose_name='Bent-Over Row w/RB', blank=True, null=True)
    back_rc_level2_Linton = models.CharField(max_length=50, verbose_name='Linton External Rotation w/RB', blank=True, null=True)
    back_rc_level2_Bilateral = models.CharField(max_length=50, verbose_name='Bilateral Extension With Retraction w/RB',
                                                blank=True, null=True)
    back_rc_level2_Upright = models.CharField(max_length=50, verbose_name='Upright Row w/RB', blank=True, null=True)
    back_rc_level2_Supine = models.CharField(max_length=50, verbose_name='Supine Pullover w/RB', blank=True, null=True)
    back_rc_level2_Standing = models.CharField(max_length=50, verbose_name='Standing Reverse Fly w/RB', blank=True, null=True)
    back_rc_level2_Close = models.CharField(max_length=50,
                                            verbose_name='Lying Close-Grip Lat Pulldown w/Resistance Band',
                                            blank=True, null=True)
    back_rc_level2_Wide = models.CharField(max_length=50, verbose_name='Wide-Grip Lat Pulldown w/Resistance Band',
                                           blank=True, null=True)
    back_rc_level2_Pullover = models.CharField(max_length=50, verbose_name='Lying Pullover w/Resistance Band',
                                               blank=True, null=True)
    back_rc_level2_Sng_Row = models.CharField(max_length=50, verbose_name='Single Arm Row, on Bench', blank=True, null=True)
    back_rc_level2_Resistance = models.CharField(max_length=50, verbose_name='Seated Row /Resistance Band',
                                                 blank=True, null=True)
    back_rc_level2_Back = models.CharField(max_length=50, verbose_name='Back Row w/Resistance Band & Straps',
                                           blank=True, null=True)
    back_rc_level2_Single = models.CharField(max_length=50,
                                             verbose_name='Single Arm, Back Row w/Resistance Band & Straps',
                                             blank=True, null=True)
    back_rc_level2_Inverted = models.CharField(max_length=50, verbose_name='Inverted Row w/Ring ', blank=True, null=True)
    back_rc_level2_Battle = models.CharField(max_length=50, verbose_name='Battle Ropes, Double Wave', blank=True, null=True)
    back_rc_level2_Low = models.CharField(max_length=50, verbose_name='Low Row w/Strap', blank=True, null=True)
    back_rc_level2_Split = models.CharField(max_length=50, verbose_name='Split Fly w/Strap', blank=True, null=True)

    back_rc_level3_Pullup = models.CharField(max_length=50, verbose_name='Pull-Up w/Band', blank=True, null=True)
    back_rc_level3_Bent = models.CharField(max_length=50, verbose_name='Bent-Over Row w/RB', blank=True, null=True)
    back_rc_level3_Standing = models.CharField(max_length=50, verbose_name='Standing Reverse Fly w/RB', blank=True, null=True)
    back_rc_level3_Wide = models.CharField(max_length=50, verbose_name='Wide-Grip Lat Pulldown w/Resistance Band',
                                           blank=True, null=True)
    back_rc_level3_Lying = models.CharField(max_length=50, verbose_name='Lying Pullover w/Resistance Band',
                                            blank=True, null=True)
    back_rc_level3_Single = models.CharField(max_length=50,
                                             verbose_name='Single Arm, Back Row w/Resistance Band & Straps',
                                             blank=True, null=True)
    back_rc_level3_Inverted = models.CharField(max_length=50, verbose_name='Inverted Row w/Ring ', blank=True, null=True)
    back_rc_level3_Battle = models.CharField(max_length=50, verbose_name='Battle Ropes, Double Wave', blank=True, null=True)

    class Meta:
        verbose_name = "Egzersiz Reçetesi"
        verbose_name_plural = 'Sırt'


class exercise_prescription_biseps(models.Model):
    # Akut Değişkeni/Kol (Biseps)
    biseps_set_number = models.CharField(max_length=5, verbose_name="Set Sayısı", blank=True, null=True)
    biseps_over_number = models.CharField(max_length=5, verbose_name="Tekrar Sayısı", blank=True, null=True)
    biseps_tempo = models.CharField(max_length=10, verbose_name="Tempo (TUT)", blank=True, null=True)
    # Setler arası dinlenme
    biseps_sets_between = models.CharField(max_length=10, verbose_name="Setler Arası Dinlenme", blank=True, null=True)
    biseps_move_between = models.CharField(max_length=10, verbose_name="Hareketler Arası Dinlenme", blank=True,
                                           null=True)
    biseps_kl_level1_Curls = models.CharField(max_length=50, verbose_name='Biceps Curls (Bodyweight, Chin)',
                                              blank=True, null=True)
    biseps_kl_level1_With = models.CharField(max_length=50, verbose_name='Bridge with Biceps Curls Stability Ball',
                                             blank=True, null=True)
    biseps_kl_level2_Curls = models.CharField(max_length=50, verbose_name='Biceps Curls (Bodyweight, Chin)',
                                              blank=True, null=True)
    biseps_kl_level2_With = models.CharField(max_length=50, verbose_name='Bridge with Biceps Curls Stability Ball',
                                             blank=True, null=True)
    biseps_kl_level3_Curls = models.CharField(max_length=50, verbose_name='Biceps Curls (Bodyweight, Chin)',
                                              blank=True, null=True)
    biseps_kl_level3_With = models.CharField(max_length=50, verbose_name='Bridge with Biceps Curls Stability Ball',
                                             blank=True, null=True)

    biseps_wg_level1_Preacher = models.CharField(max_length=50, verbose_name='Preacher Curl w/Dumbbell', blank=True, null=True)
    biseps_wg_level1_Dumbbells = models.CharField(max_length=50, verbose_name='Dumbbells Concentration Curls',
                                                  blank=True, null=True)
    biseps_wg_level1_Standing = models.CharField(max_length=50, verbose_name='Standing Dumbbell Biceps Curl',
                                                 blank=True, null=True)
    biseps_wg_level1_Seated = models.CharField(max_length=50, verbose_name='Seated Dumbbell Biceps Curl', blank=True, null=True)
    biseps_wg_level1_Hammer = models.CharField(max_length=50, verbose_name='Hammer Curls (Dumbbells)', blank=True, null=True)
    biseps_wg_level1_Reverse = models.CharField(max_length=50, verbose_name='Reverse Curl w/Dumbbell', blank=True, null=True)

    biseps_wg_level2_Preacher = models.CharField(max_length=50, verbose_name='Preacher Curl w/Dumbbell', blank=True, null=True)
    biseps_wg_level2_Barbell = models.CharField(max_length=50, verbose_name='Barbell Wide Grip Biceps Curl',
                                                blank=True, null=True)
    biseps_wg_level2_Dumbbells = models.CharField(max_length=50, verbose_name='Dumbbells Concentration Curls',
                                                  blank=True, null=True)
    biseps_wg_level2_Seated = models.CharField(max_length=50, verbose_name='Seated Dumbbell Biceps Curl', blank=True, null=True)
    biseps_wg_level2_Incline = models.CharField(max_length=50, verbose_name='Incline Bench Biceps Curl w/Dumbells',
                                                blank=True, null=True)
    biseps_wg_level2_Hammer = models.CharField(max_length=50, verbose_name='Hammer Curls (Dumbbells)', blank=True, null=True)
    biseps_wg_level2_Wide = models.CharField(max_length=50,
                                             verbose_name='Wide Grip Biceps  Curls w/Flat Barbell & Z Barbell',
                                             blank=True, null=True)
    biseps_wg_level2_Reverse = models.CharField(max_length=50, verbose_name='Reverse Curl w/Dumbbell', blank=True, null=True)
    biseps_wg_level2_Biceps = models.CharField(max_length=50, verbose_name='Biceps Curl w/KB', blank=True, null=True)
    biseps_wg_level2_Close = models.CharField(max_length=50, verbose_name='Close Grip Biceps Curl w/Barbell',
                                              blank=True, null=True)

    biseps_wg_level3_Barbell = models.CharField(max_length=50, verbose_name='Barbell Wide Grip Biceps Curl',
                                                blank=True, null=True)
    biseps_wg_level3_Incline = models.CharField(max_length=50, verbose_name='Incline Bench Biceps Curl w/Dumbells',
                                                blank=True, null=True)
    biseps_wg_level3_Hammer = models.CharField(max_length=50, verbose_name='Hammer Curls (Dumbbells)', blank=True, null=True)
    biseps_wg_level3_Wide = models.CharField(max_length=50,
                                             verbose_name='Wide Grip Biceps Curls w/Flat Barbell & Z Barbell',
                                             blank=True, null=True)
    biseps_wg_level3_Reverse = models.CharField(max_length=50, verbose_name='Reverse Curl w/Dumbbell', blank=True, null=True)
    biseps_wg_level3_Biceps = models.CharField(max_length=50, verbose_name='Biceps Curl w/KB', blank=True, null=True)
    biseps_wg_level3_Close = models.CharField(max_length=50, verbose_name='Close Grip Biceps Curl w/Barbell',
                                              blank=True, null=True)

    biseps_mc_level1_Preacher = models.CharField(max_length=50, verbose_name='Preacher Biceps Curls (Machine)',
                                                 blank=True, null=True)
    biseps_mc_level1_Low = models.CharField(max_length=50, verbose_name='Low Pulley Biceps Curl', blank=True, null=True)
    biseps_mc_level1_Onearm = models.CharField(max_length=50, verbose_name='One-Arm Biceps  Curl w/Cable',
                                               blank=True, null=True)
    biseps_mc_level1_Biceps = models.CharField(max_length=50, verbose_name='Biceps Curls(Machine)', blank=True, null=True)

    biseps_mc_level2_Low = models.CharField(max_length=50, verbose_name='Low Pulley Biceps Curl', blank=True, null=True)
    biseps_mc_level2_Lying = models.CharField(max_length=50, verbose_name='Lying Biceps Curl w/Cable', blank=True, null=True)
    biseps_mc_level2_Hercules = models.CharField(max_length=50, verbose_name='Hercules Biceps Curl w/Cable',
                                                 blank=True, null=True)
    biseps_mc_level2_Onearm = models.CharField(max_length=50, verbose_name='One-Arm Biceps Curl w/Cable', blank=True, null=True)

    biseps_mc_level3_Lying = models.CharField(max_length=50, verbose_name='Lying Biceps Curl w/Cable', blank=True, null=True)
    biseps_mc_level3_Hercules = models.CharField(max_length=50, verbose_name='Hercules Biceps Curl w/Cable',
                                                 blank=True, null=True)
    biseps_mc_level3_Cable = models.CharField(max_length=50, verbose_name='Cable Biceps Curl w/Rope', blank=True, null=True)

    biseps_rc_level1_Standing = models.CharField(max_length=50, verbose_name='Standing Biceps Curl w/Resistance Band',
                                                 blank=True, null=True)
    biseps_rc_level1_High = models.CharField(max_length=50, verbose_name='Biceps Curl, High w/Resistance Band',
                                             blank=True, null=True)
    biseps_rc_level1_Lunge = models.CharField(max_length=50, verbose_name='Biceps Curl, Lunge Stance w/Resistance Band',
                                              blank=True, null=True)
    biseps_rc_level1_Biceps = models.CharField(max_length=50, verbose_name='Biceps Curls w/Straps', blank=True, null=True)

    biseps_rc_level2_Standing = models.CharField(max_length=50, verbose_name='Standing Biceps Curl w/Resistance Band',
                                                 blank=True, null=True)
    biseps_rc_level2_High = models.CharField(max_length=50, verbose_name='Biceps Curl, High w/Resistance Band',
                                             blank=True, null=True)
    biseps_rc_level2_Concentration = models.CharField(max_length=50,
                                                      verbose_name='Concentration Curl w/Resistance Band',
                                                      blank=True, null=True)
    biseps_rc_level2_Lunge = models.CharField(max_length=50, verbose_name='Biceps Curl, Lunge Stance w/Resistance Band',
                                              blank=True, null=True)
    biseps_rc_level2_Biceps = models.CharField(max_length=50, verbose_name='Biceps Curls w/Straps', blank=True, null=True)
    biseps_rc_level2_Onearm = models.CharField(max_length=50, verbose_name='One-Arm Biceps Curl w/Straps',
                                               blank=True, null=True)

    biseps_rc_level3_Biceps = models.CharField(max_length=50, verbose_name='Biceps Curl, High w/Resistance Band',
                                               blank=True, null=True)
    biseps_rc_level3_Concentration = models.CharField(max_length=50,
                                                      verbose_name='Concentration Curl w/Resistance Band',
                                                      blank=True, null=True)
    biseps_rc_level3_Onearm = models.CharField(max_length=50, verbose_name='One-Arm Biceps Curl w/Straps',
                                               blank=True, null=True)
    biseps_rc_level3_Plank = models.CharField(max_length=50, verbose_name='Plank & Push Position Biceps Curl w/RB',
                                              blank=True, null=True)


    class Meta:
        verbose_name = "Egzersiz Reçetesi"
        verbose_name_plural = 'Kol Biseps'


class exercise_prescription_triseps(models.Model):
    # Akut Değişkeni/ Kol (Triseps)
    triseps_set_number = models.CharField(max_length=5, verbose_name="Set Sayısı", blank=True, null=True)
    triseps_over_number = models.CharField(max_length=5, verbose_name="Tekrar Sayısı", blank=True, null=True)
    triseps_tempo = models.CharField(max_length=10, verbose_name="Tempo (TUT)", blank=True, null=True)
    # Setler arası dinlenme
    triseps_sets_between = models.CharField(max_length=10, verbose_name="Setler Arası Dinlenme", blank=True, null=True)
    triseps_move_between = models.CharField(max_length=10, verbose_name="Hareketler Arası Dinlenme", blank=True,
                                            null=True)

    triseps_kl_level1_Triceps = models.CharField(max_length=50, verbose_name='Triceps Dips (Bodyweight)', blank=True, null=True)

    triseps_kl_level2_Kneeling = models.CharField(max_length=60,
                                                  verbose_name='Kneeling Preacher Triceps Extension w/Stability Ball',
                                                  blank=True, null=True)
    triseps_kl_level2_Dips = models.CharField(max_length=50, verbose_name='Triceps Dips (Bodyweight)', blank=True, null=True)
    triseps_kl_level2_Extension = models.CharField(max_length=50, verbose_name='Triceps Extension (Bodyweight)',
                                                   blank=True, null=True)
    triseps_kl_level2_Diamond = models.CharField(max_length=50, verbose_name='Diamond Push Up', blank=True, null=True)

    triseps_kl_level3_Kneeling = models.CharField(max_length=60,
                                                  verbose_name='Kneeling Preacher Triceps Extension w/Stability Ball',
                                                  blank=True, null=True)
    triseps_kl_level3_Extension = models.CharField(max_length=50, verbose_name='Triceps Extension (Bodyweight)',
                                                   blank=True, null=True)
    triseps_kl_level3_Diamond = models.CharField(max_length=50, verbose_name='Diamond Push Up', blank=True, null=True)
    triseps_kl_level3_Triceps = models.CharField(max_length=50, verbose_name='Triceps Extension Push Up', blank=True, null=True)

    triseps_wg_level1_Dumbbell = models.CharField(max_length=50, verbose_name='Dumbbell Triceps Kickback',
                                                  blank=True, null=True)
    triseps_wg_level1_Onearm = models.CharField(max_length=50, verbose_name='One-Arm Skull Crusher w/Dumbbell',
                                                blank=True, null=True)
    triseps_wg_level1_Overhead = models.CharField(max_length=40, verbose_name='Overhead Triceps Extension w/Dumbbell',
                                                  blank=True, null=True)

    triseps_wg_level2_Dumbbell = models.CharField(max_length=40, verbose_name='Dumbbell Triceps Kickback',
                                                  blank=True, null=True)
    triseps_wg_level2_ly_Dumbbell = models.CharField(max_length=40, verbose_name='Lying Triceps Extension w/Dumbbell',
                                                     blank=True, null=True)
    triseps_wg_level2_ly_Barbell = models.CharField(max_length=40, verbose_name='Lying Triceps Extension w/Barbell',
                                                    blank=True, null=True)
    triseps_wg_level2_Skull = models.CharField(max_length=40, verbose_name='Skull Crusher w/Zbar', blank=True, null=True)
    triseps_wg_level2_Onearm = models.CharField(max_length=40, verbose_name='One-Arm Skull Crusher w/Dumbbell',
                                                blank=True, null=True)
    triseps_wg_level2_Overhead = models.CharField(max_length=40, verbose_name='Overhead Triceps Extension w/Dumbbell',
                                                  blank=True, null=True)
    triseps_wg_level2_Barbell = models.CharField(max_length=40, verbose_name='Barbell Close Grip Bench Press',
                                                 blank=True, null=True)

    triseps_wg_level3_ly_Dumbbell = models.CharField(max_length=40, verbose_name='Lying Triceps Extension  w/Dumbbell',
                                                     blank=True, null=True)
    triseps_wg_level3_ly_Barbell = models.CharField(max_length=40, verbose_name='Lying Triceps Extension  w/Barbell',
                                                    blank=True, null=True)
    triseps_wg_level3_Skull = models.CharField(max_length=40, verbose_name='Skull Crusher w/Zbar', blank=True, null=True)
    triseps_wg_level3_Barbell = models.CharField(max_length=40, verbose_name='Barbell Close Grip Bench Press',
                                                 blank=True, null=True)
    triseps_wg_level3_Bent = models.CharField(max_length=40, verbose_name='Bent Over Triceps w/Dumbell', blank=True, null=True)

    triseps_mc_level1_Pushdowns = models.CharField(max_length=40, verbose_name='Triceps Pushdowns w/Cable',
                                                   blank=True, null=True)
    triseps_mc_level1_Triceps = models.CharField(max_length=40, verbose_name='Triceps Push-Down w/Rope', blank=True, null=True)
    triseps_mc_level1_Reverse = models.CharField(max_length=40, verbose_name='Reverse Grip Triceps Push Down w/Cable',
                                                 blank=True, null=True)
    triseps_mc_level1_Onearm = models.CharField(max_length=40, verbose_name='One-Arm Triceps Push-Down w/Cable',
                                                blank=True, null=True)
    triseps_mc_level1_Cable = models.CharField(max_length=40, verbose_name='Cable Triceps Kickback', blank=True, null=True)
    triseps_mc_level1_Machine = models.CharField(max_length=40, verbose_name='Triceps Pushdowns w/Machine',
                                                 blank=True, null=True)
    triseps_mc_level1_Press = models.CharField(max_length=40, verbose_name='Triceps Press w/Machine', blank=True, null=True)

    triseps_mc_level2_Pushdowns = models.CharField(max_length=40, verbose_name='Triceps Push-downs w/Cable',
                                                   blank=True, null=True)
    triseps_mc_level2_Triceps = models.CharField(max_length=40, verbose_name='Triceps Push-Down w/Rope', blank=True, null=True)
    triseps_mc_level2_Reverse = models.CharField(max_length=40, verbose_name='Reverse Grip Triceps Push Down w/Cable',
                                                 blank=True, null=True)
    triseps_mc_level2_Overhead = models.CharField(max_length=40, verbose_name='Overhead Triceps Push-Down  w/Rope',
                                                  blank=True, null=True)
    triseps_mc_level2_Onearm = models.CharField(max_length=40, verbose_name='One-Arm Triceps Push w/Cable',
                                                blank=True, null=True)
    triseps_mc_level2_Grip = models.CharField(max_length=50,
                                              verbose_name='Reverse Grip One-Arm Triceps Push-Down w/Cable',
                                              blank=True, null=True)
    triseps_mc_level2_Cable = models.CharField(max_length=40, verbose_name='Cable Triceps Kickback', blank=True, null=True)
    triseps_mc_level2_Dips = models.CharField(max_length=40, verbose_name='Dips Triceps w/Machine', blank=True, null=True)
    triseps_mc_level2_tr_Pushdowns = models.CharField(max_length=40, verbose_name='Triceps Push-Downs w/Machine',
                                                      blank=True, null=True)
    triseps_mc_level2_tr_Press = models.CharField(max_length=40, verbose_name='Triceps Press w/Machine', blank=True, null=True)

    triseps_mc_level3_Overhead = models.CharField(max_length=40, verbose_name='Overhead Triceps Push-Down W/Rope',
                                                  blank=True, null=True)
    triseps_mc_level3_Reverse = models.CharField(max_length=50,
                                                 verbose_name='Reverse Grip One-Arm  Triceps Push-Down w/Cable',
                                                 blank=True, null=True)
    triseps_mc_level3_Dips = models.CharField(max_length=50, verbose_name='Dips Triceps w/Machine', blank=True, null=True)

    triseps_rc_level1_ex_Overhead = models.CharField(max_length=50,
                                                     verbose_name='Triceps Extension-Overhead w/Resistance Band',
                                                     blank=True, null=True)
    triseps_rc_level1_Lying = models.CharField(max_length=50, verbose_name='Lying Triceps Extension w/Resistance Band',
                                               blank=True, null=True)
    triseps_rc_level1_ex = models.CharField(max_length=50, verbose_name='Triceps Extension w/Resistance Band',
                                            blank=True, null=True)
    triseps_rc_level1_Standing = models.CharField(max_length=50, verbose_name='Standing Skull Crusher w/Strap',
                                                  blank=True, null=True)
    triseps_rc_level2_ex_Overhead = models.CharField(max_length=50,
                                                     verbose_name='Triceps Extension-Overhead w/Resistance Band',
                                                     blank=True, null=True)
    triseps_rc_level2_Lying = models.CharField(max_length=50, verbose_name='Lying Triceps Extension w/Resistance Band',
                                               blank=True, null=True)
    triseps_rc_level2_ex = models.CharField(max_length=50, verbose_name='Triceps Extension w/Resistance Band',
                                            blank=True, null=True)
    triseps_rc_level2_Kickback = models.CharField(max_length=50, verbose_name='Triceps Kickback w/Resistance Band',
                                                  blank=True, null=True)
    triseps_rc_level2_sd_Overhead = models.CharField(max_length=50, verbose_name='Standing Overhead Triceps Extension',
                                                     blank=True, null=True)
    triseps_rc_level2_sd_Skull = models.CharField(max_length=50, verbose_name='Standing Skull Crusher w/Strap',
                                                  blank=True, null=True)
    triseps_rc_level2_kn_Skull = models.CharField(max_length=50, verbose_name='Kneeling Skull Crusher w/Strap',
                                                  blank=True, null=True)
    triseps_rc_level2_kn_Overhead = models.CharField(max_length=50,
                                                     verbose_name='Kneeling Overhead Triceps Extension w/Strap',
                                                     blank=True, null=True)
    triseps_rc_level2_Dips = models.CharField(max_length=30, verbose_name='Dips w/RB', blank=True, null=True)
    triseps_rc_level3_Kickback = models.CharField(max_length=40, verbose_name='Triceps Kickback w/Resistance Band',
                                                  blank=True, null=True)
    triseps_rc_level3_sd_Overhead = models.CharField(max_length=40, verbose_name='Standing Overhead Triceps Extension',
                                                     blank=True, null=True)
    triseps_rc_level3_kn_Skull = models.CharField(max_length=40, verbose_name='Kneeling Skull Crusher w/Strap',
                                                  blank=True, null=True)
    triseps_rc_level3_kn_Overhead = models.CharField(max_length=50,
                                                     verbose_name='Kneeling Overhead Triceps Extension w/Strap',
                                                     blank=True, null=True)
    triseps_rc_level3_Dips = models.CharField(max_length=40, verbose_name='Dips w/RB', blank=True, null=True)


    class Meta:
        verbose_name = "Egzersiz Reçetesi"
        verbose_name_plural = 'Kol Triseps'


class exercise_prescription_gluteal(models.Model):
    # Akut Değişkeni/Gluteal
    gluteal_set_number = models.CharField(max_length=5, verbose_name="Set Sayısı", blank=True, null=True)
    gluteal_over_number = models.CharField(max_length=5, verbose_name="Tekrar Sayısı", blank=True, null=True)
    gluteal_tempo = models.CharField(max_length=10, verbose_name="Tempo (TUT)", blank=True, null=True)
    # Setler arası dinlenme
    gluteal_sets_between = models.CharField(max_length=10, verbose_name="Setler Arası Dinlenme", blank=True, null=True)
    gluteal_move_between = models.CharField(max_length=10, verbose_name="Hareketler Arası Dinlenme", blank=True,
                                            null=True)

    gluteal_kl_level1_Side = models.CharField(max_length=40, verbose_name='Side Lunge', blank=True, null=True)
    gluteal_kl_level1_Hip = models.CharField(max_length=40, verbose_name='Hip Thrust w/Bosu Ball', blank=True, null=True)
    gluteal_kl_level1_Roman = models.CharField(max_length=40, verbose_name='Roman Chair Hip Extension', blank=True, null=True)
    gluteal_kl_level1_Glute = models.CharField(max_length=40, verbose_name='Glute Bridge', blank=True, null=True)

    gluteal_kl_level2_Full = models.CharField(max_length=40, verbose_name='Full Squat w/Bodyweight', blank=True, null=True)
    gluteal_kl_level2_Side = models.CharField(max_length=40, verbose_name='Side Lunge', blank=True, null=True)
    gluteal_kl_level2_Hip = models.CharField(max_length=40, verbose_name='Hip Thrust w/Bosu Ball', blank=True, null=True)
    gluteal_kl_level2_sngl_Hip = models.CharField(max_length=40, verbose_name='Single Leg Hip Thrust', blank=True, null=True)
    gluteal_kl_level2_Split = models.CharField(max_length=40, verbose_name='Split Squat', blank=True, null=True)
    gluteal_kl_level2_Bulgarian = models.CharField(max_length=40, verbose_name='Bulgarian Squat', blank=True, null=True)
    gluteal_kl_level2_Hack = models.CharField(max_length=40, verbose_name='Hack Squat', blank=True, null=True)
    gluteal_kl_level2_Roman = models.CharField(max_length=40, verbose_name='Roman Chair Hip Extension', blank=True, null=True)
    gluteal_kl_level2_sngl_Leg = models.CharField(max_length=40, verbose_name='Single Leg Glute Bridge', blank=True, null=True)

    gluteal_kl_level3_Single = models.CharField(max_length=40, verbose_name='Single Leg Hip Thrust', blank=True, null=True)
    gluteal_kl_level3_Split = models.CharField(max_length=40, verbose_name='Split Squat', blank=True, null=True)
    gluteal_kl_level3_Bulgarian = models.CharField(max_length=40, verbose_name='Bulgarian Squat', blank=True, null=True)
    gluteal_kl_level3_Hack = models.CharField(max_length=40, verbose_name='Hack Squat', blank=True, null=True)

    gluteal_wg_level1_Hip = models.CharField(max_length=40, verbose_name='Hip Thrust on Bench w/Barbell', blank=True, null=True)
    gluteal_wg_level1_Glute = models.CharField(max_length=40, verbose_name='Glute Bridge w/Barbell', blank=True, null=True)
    gluteal_wg_level1_db_Squat = models.CharField(max_length=40, verbose_name='Dumbbell Squat', blank=True, null=True)
    gluteal_wg_level1_Goblet = models.CharField(max_length=40, verbose_name='Goblet Squat w/Dumbbell & KB',
                                                blank=True, null=True)
    gluteal_wg_level1_Narrow = models.CharField(max_length=40, verbose_name='Narrow Squat w/Dumbbell', blank=True, null=True)
    gluteal_wg_level1_db_Single = models.CharField(max_length=40, verbose_name='Dumbbell Single Arm Overhead Squat',
                                                   blank=True, null=True)
    gluteal_wg_level1_Wide = models.CharField(max_length=40, verbose_name='Wide Squat (Smith Machine)', blank=True, null=True)
    gluteal_wg_level1_Sumo = models.CharField(max_length=40, verbose_name='Sumo Squat (Dumbbell & Barbell)',
                                              blank=True, null=True)

    gluteal_wg_level2_Hip = models.CharField(max_length=40, verbose_name='Hip Thrust on Bench w/Barbell', blank=True, null=True)
    gluteal_wg_level2_Glute = models.CharField(max_length=40, verbose_name='Glute Bridge w/Barbell', blank=True, null=True)
    gluteal_wg_level2_Squat = models.CharField(max_length=40, verbose_name='Squat-Side, Split w/Barbell', blank=True, null=True)
    gluteal_wg_level2_db_Squat = models.CharField(max_length=40, verbose_name='Dumbbell Squat', blank=True, null=True)
    gluteal_wg_level2_Full = models.CharField(max_length=40, verbose_name='Full Squat w/Barbell', blank=True, null=True)
    gluteal_wg_level2_Front = models.CharField(max_length=40, verbose_name='Front Squat w/Barbell', blank=True, null=True)
    gluteal_wg_level2_Goblet = models.CharField(max_length=40, verbose_name='Goblet Squat w/Dumbbell & KB',
                                                blank=True, null=True)
    gluteal_wg_level2_Narrow = models.CharField(max_length=40, verbose_name='Narrow Squat w/Dumbbell', blank=True, null=True)
    gluteal_wg_level2_br_Squat = models.CharField(max_length=40, verbose_name='Barbell Squat Jump', blank=True, null=True)
    gluteal_wg_level2_br_Overhead = models.CharField(max_length=40, verbose_name='Barbell Overhead Squat',
                                                     blank=True, null=True)
    gluteal_wg_level2_br_Single = models.CharField(max_length=40, verbose_name='Dumbbell Single Arm Overhead Squat',
                                                   blank=True, null=True)
    gluteal_wg_level2_Wide = models.CharField(max_length=40, verbose_name='Wide Squat (Smith Machine)', blank=True, null=True)
    gluteal_wg_level2_on_Squat = models.CharField(max_length=40, verbose_name='One-Leg Squat (Bulgarian) w/Dumbbell',
                                                  blank=True, null=True)
    gluteal_wg_level2_on_Jump = models.CharField(max_length=40, verbose_name='One-Leg Jump Squat (Dumbbell)',
                                                 blank=True, null=True)
    gluteal_wg_level2_Close = models.CharField(max_length=40, verbose_name='Close Squat w/Barbell & Dumbbell',
                                               blank=True, null=True)
    gluteal_wg_level2_Sumo = models.CharField(max_length=40, verbose_name='Sumo Squat (Dumbbell & Barbell)',
                                              blank=True, null=True)
    gluteal_wg_level2_Barbell = models.CharField(max_length=40, verbose_name='Barbell Jump Lunge', blank=True, null=True)

    gluteal_wg_level3_Squat = models.CharField(max_length=40, verbose_name='Squat-Side, Split w/Barbell', blank=True, null=True)
    gluteal_wg_level3_Full = models.CharField(max_length=40, verbose_name='Full Squat w/Barbell', blank=True, null=True)
    gluteal_wg_level3_Front = models.CharField(max_length=40, verbose_name='Front Squat w/Barbell', blank=True, null=True)
    gluteal_wg_level3_br_Squat = models.CharField(max_length=40, verbose_name='Barbell Squat Jump', blank=True, null=True)
    gluteal_wg_level3_br_Overhead = models.CharField(max_length=40, verbose_name='Barbell Overhead Squat',
                                                     blank=True, null=True)
    gluteal_wg_level3_Jump = models.CharField(max_length=40, verbose_name='One-Leg Jump Squat (Dumbbell)',
                                              blank=True, null=True)
    gluteal_wg_level3_Close = models.CharField(max_length=40, verbose_name='Close Squat w/Barbell & Dumbbell',
                                               blank=True, null=True)
    gluteal_wg_level3_Barbell = models.CharField(max_length=40, verbose_name='Barbell Jump Lunge', blank=True, null=True)

    gluteal_mc_level1_Machine = models.CharField(max_length=40, verbose_name='Machine Hip Extension', blank=True, null=True)
    gluteal_mc_level1_Squat = models.CharField(max_length=40, verbose_name='Squat w/Smith Machine', blank=True, null=True)

    gluteal_mc_level2_Machine = models.CharField(max_length=40, verbose_name='Machine Hip Extension', blank=True, null=True)
    gluteal_mc_level2_Squat = models.CharField(max_length=40, verbose_name='Squat w/Smith Machine', blank=True, null=True)

    gluteal_mc_level3_Machine = models.CharField(max_length=40, verbose_name='Machine Hip Extension', blank=True, null=True)
    gluteal_mc_level3_Squat = models.CharField(max_length=40, verbose_name='Squat w/Smith Machine', blank=True, null=True)

    gluteal_rc_level1_Internal = models.CharField(max_length=40, verbose_name='Hip Internal Rotation w/RB',
                                                  blank=True, null=True)
    gluteal_rc_level1_External = models.CharField(max_length=30, verbose_name='Hip External Rotation w/RB',
                                                  blank=True, null=True)
    gluteal_rc_level1_Fleksiyon = models.CharField(max_length=30, verbose_name='Hip Fleksiyon w/RB', blank=True, null=True)
    gluteal_rc_level1_Ekstension = models.CharField(max_length=30, verbose_name='Hip Ekstension w/RB', blank=True, null=True)
    gluteal_rc_level1_Abduction = models.CharField(max_length=30, verbose_name='Hip Abduction w/RB', blank=True, null=True)
    gluteal_rc_level1_Adduction = models.CharField(max_length=30, verbose_name='Hip Adduction w/RB', blank=True, null=True)
    gluteal_rc_level1_Half = models.CharField(max_length=30, verbose_name='Half Squat w/RB', blank=True, null=True)
    gluteal_rc_level1_Bridge = models.CharField(max_length=30, verbose_name='Bridge w/RB', blank=True, null=True)
    gluteal_rc_level1_Barbell = models.CharField(max_length=30, verbose_name='Barbell Squat w/RB', blank=True, null=True)
    gluteal_rc_level1_Monster = models.CharField(max_length=30, verbose_name='Monster Walk w/RB', blank=True, null=True)

    gluteal_rc_level2_Half = models.CharField(max_length=30, verbose_name='Half Squat w/RB', blank=True, null=True)
    gluteal_rc_level2_Side = models.CharField(max_length=30, verbose_name='Side-Lying Hip Lift w/RB', blank=True, null=True)
    gluteal_rc_level2_Bridge = models.CharField(max_length=30, verbose_name='Bridge w/RB', blank=True, null=True)
    gluteal_rc_level2_Hip = models.CharField(max_length=40, verbose_name='Hip Extension (Donkey Kick) w/RB',
                                             blank=True, null=True)
    gluteal_rc_level2_gd_Morning = models.CharField(max_length=30, verbose_name='Good Morning w/RB', blank=True, null=True)
    gluteal_rc_level2_Supine = models.CharField(max_length=40, verbose_name='Supine Hip-Bridge March With Mini Band',
                                                blank=True, null=True)
    gluteal_rc_level2_Lunge = models.CharField(max_length=30, verbose_name='Lunge w/RB', blank=True, null=True)
    gluteal_rc_level2_lt_Lunge = models.CharField(max_length=30, verbose_name='Lateral Lunge w/RB', blank=True, null=True)
    gluteal_rc_level2_Barbell = models.CharField(max_length=30, verbose_name='Barbell Squat w/RB', blank=True, null=True)
    gluteal_rc_level2_Monster = models.CharField(max_length=30, verbose_name='Monster Walk w/RB', blank=True, null=True)
    gluteal_rc_level2_lt_Squat = models.CharField(max_length=30, verbose_name='Lateral Squat w/Strap', blank=True, null=True)
    gluteal_rc_level2_Bulgarian = models.CharField(max_length=30, verbose_name='Bulgarian Squat w/Strap', blank=True, null=True)
    gluteal_rc_level2_Triangle = models.CharField(max_length=30, verbose_name='Triangle Squat w/Strap', blank=True, null=True)
    gluteal_rc_level2_Full = models.CharField(max_length=30, verbose_name='Full Squat w/Strap', blank=True, null=True)
    gluteal_rc_level2_Overhead = models.CharField(max_length=30, verbose_name='Overhead Squat w/Strap', blank=True, null=True)

    gluteal_rc_level3_gd_Morning = models.CharField(max_length=30, verbose_name='Good Morning w/RB', blank=True, null=True)
    gluteal_rc_level3_Supine = models.CharField(max_length=40, verbose_name='Supine Hip-Bridge March With Mini Band',
                                                blank=True, null=True)
    gluteal_rc_level3_lt_Lunge = models.CharField(max_length=40, verbose_name='Lateral Lunge w/RB', blank=True, null=True)
    gluteal_rc_level3_lt_Squat = models.CharField(max_length=40, verbose_name='Lateral Squat w/Strap', blank=True, null=True)
    gluteal_rc_level3_Barbell = models.CharField(max_length=40, verbose_name='Barbell Squat w/RB', blank=True, null=True)
    gluteal_rc_level3_Bulgarian = models.CharField(max_length=40, verbose_name='Bulgarian Squat w/Strap', blank=True, null=True)
    gluteal_rc_level3_Triangle = models.CharField(max_length=40, verbose_name='Triangle Squat w/Strap', blank=True, null=True)
    gluteal_rc_level3_Figure = models.CharField(max_length=40, verbose_name='Figure Four Squat w/', blank=True, null=True)
    gluteal_rc_level3_Squat = models.CharField(max_length=40, verbose_name='Squat Jump w/Strap', blank=True, null=True)
    gluteal_rc_level3_Full = models.CharField(max_length=40, verbose_name='Full Squat w/Strap', blank=True, null=True)
    gluteal_rc_level3_Overhead = models.CharField(max_length=40, verbose_name='Overhead Squat w/Strap', blank=True, null=True)

    class Meta:
        verbose_name = "Egzersiz Reçetesi"
        verbose_name_plural = 'Gluteal'


class exercise_prescription_kuadriseps(models.Model):
    # Akut Değişkeni/Kuadriseps
    kdrsps_set_number = models.CharField(max_length=5, verbose_name="Set Sayısı", blank=True, null=True)
    kdrsps_over_number = models.CharField(max_length=5, verbose_name="Tekrar Sayısı", blank=True, null=True)
    kdrsps_tempo = models.CharField(max_length=10, verbose_name="Tempo (TUT)", blank=True, null=True)
    # Setler arası dinlenme
    kdrsps_sets_between = models.CharField(max_length=10, verbose_name="Setler Arası Dinlenme", blank=True, null=True)
    kdrsps_move_between = models.CharField(max_length=10, verbose_name="Hareketler Arası Dinlenme", blank=True,
                                           null=True)

    kdrsps_kl_level1_Sissy = models.CharField(max_length=40, verbose_name='Sissy Squat', blank=True, null=True)
    kdrsps_kl_level1_Hell = models.CharField(max_length=40, verbose_name='Hell Elevated Squat', blank=True, null=True)
    kdrsps_kl_level1_Narrow = models.CharField(max_length=40, verbose_name='Narrow Squat', blank=True, null=True)
    kdrsps_kl_level2_Elevated = models.CharField(max_length=40, verbose_name='Elevated Front Foot Split Squat',
                                                 blank=True, null=True)
    kdrsps_kl_level2_Sissy = models.CharField(max_length=40, verbose_name='Sissy Squat', blank=True, null=True)
    kdrsps_kl_level2_Hell = models.CharField(max_length=40, verbose_name='Hell Elevated Squat', blank=True, null=True)
    kdrsps_kl_level2_Narrow = models.CharField(max_length=40, verbose_name='Narrow Squat', blank=True, null=True)
    kdrsps_kl_level3_Pistol = models.CharField(max_length=40, verbose_name='Pistol Squat', blank=True, null=True)
    kdrsps_kl_level3_Elevated = models.CharField(max_length=40, verbose_name='Elevated Front Foot Split Squat',
                                                 blank=True, null=True)

    kdrsps_wg_level1_Goblet = models.CharField(max_length=40, verbose_name='Goblet Squat w/Dumbbell & KB',
                                               blank=True, null=True)
    kdrsps_wg_level1_Stand = models.CharField(max_length=40, verbose_name='Stand-Up (From Knees)', blank=True, null=True)
    kdrsps_wg_level1_Squat = models.CharField(max_length=40, verbose_name='Squat Plie w/Dumbbell', blank=True, null=True)
    kdrsps_wg_level1_Narrow = models.CharField(max_length=40, verbose_name='Narrow Squat w/Barbell & Dumbbell',
                                               blank=True, null=True)
    kdrsps_wg_level1_Front = models.CharField(max_length=40, verbose_name='Front Lunge w/Barbell & Dumbbell',
                                              blank=True, null=True)
    kdrsps_wg_level1_Hell = models.CharField(max_length=40, verbose_name='Hell Elevated Squat w/Dumbbell',
                                             blank=True, null=True)

    kdrsps_wg_level2_stp_Dumbbell = models.CharField(max_length=40, verbose_name='Step-Up w/Dumbbell', blank=True, null=True)
    kdrsps_wg_level2_frnt_Squat = models.CharField(max_length=40, verbose_name='Front Squat w/Barbell', blank=True, null=True)
    kdrsps_wg_level2_Goblet = models.CharField(max_length=40, verbose_name='Goblet Squat w/Dumbbell & KB',
                                               blank=True, null=True)
    kdrsps_wg_level2_stp_Barbell = models.CharField(max_length=40, verbose_name='Step-up w/Barbell', blank=True, null=True)
    kdrsps_wg_level2_Stand = models.CharField(max_length=40, verbose_name='Stand-Up (From Knees)', blank=True, null=True)
    kdrsps_wg_level2_Squat = models.CharField(max_length=40, verbose_name='Squat Plie w/Dumbbell', blank=True, null=True)
    kdrsps_wg_level2_Double = models.CharField(max_length=40, verbose_name='Double Squat w/Dumbbell', blank=True, null=True)
    kdrsps_wg_level2_Narrow = models.CharField(max_length=40, verbose_name='Narrow Squat w/Barbell & Dumbbell',
                                               blank=True, null=True)
    kdrsps_wg_level2_frnt_Lunge = models.CharField(max_length=50, verbose_name='Front Lunge w/Barbell & Dumbbell',
                                                   blank=True, null=True)
    kdrsps_wg_level2_Hell = models.CharField(max_length=50, verbose_name='Hell Elevated Squat w', blank=True, null=True)
    kdrsps_wg_level2_Elevated = models.CharField(max_length=50,
                                                 verbose_name='Elevated Front Foot Split  Squat w/Dumbbell',
                                                 blank=True, null=True)

    kdrsps_wg_level3_stp_Dumbbell = models.CharField(max_length=50, verbose_name='Step-Up w/Dumbbell', blank=True, null=True)
    kdrsps_wg_level3_Front = models.CharField(max_length=50, verbose_name='Front Squat w/Barbell', blank=True, null=True)
    kdrsps_wg_level3_stp_Barbell = models.CharField(max_length=50, verbose_name='Step-up w/Barbell', blank=True, null=True)
    kdrsps_wg_level3_Sissy = models.CharField(max_length=50, verbose_name='Sissy Squat w/Plate', blank=True, null=True)
    kdrsps_wg_level3_Double = models.CharField(max_length=50, verbose_name='Double Squat w/Dumbbell', blank=True, null=True)
    kdrsps_wg_level3_Narrow = models.CharField(max_length=50, verbose_name='Narrow Squat w/Barbell & Dumbbell',
                                               blank=True, null=True)
    kdrsps_wg_level3_Elevated = models.CharField(max_length=50,
                                                 verbose_name='Elevated Front Foot Split Squat w/Dumbbell',
                                                 blank=True, null=True)

    kdrsps_mc_level1_Extension = models.CharField(max_length=50, verbose_name='Leg Extension w/Machine', blank=True, null=True)
    kdrsps_mc_level1_Press = models.CharField(max_length=50, verbose_name='Leg Press w/Machine', blank=True, null=True)
    kdrsps_mc_level1_Smith = models.CharField(max_length=50, verbose_name='Smith Machine Duck Stance', blank=True, null=True)

    kdrsps_mc_level2_Leg = models.CharField(max_length=50, verbose_name='Leg Extension w/Machine', blank=True, null=True)
    kdrsps_mc_level2_onlg_Extension = models.CharField(max_length=50, verbose_name='One-Leg Extension w/Machine',
                                                       blank=True, null=True)
    kdrsps_mc_level2_Press = models.CharField(max_length=50, verbose_name='Leg Press w/Machine', blank=True, null=True)
    kdrsps_mc_level2_onlg_Press = models.CharField(max_length=50, verbose_name='One-Leg Press w/Machine', blank=True, null=True)
    kdrsps_mc_level2_Smith = models.CharField(max_length=50, verbose_name='Smith Machine Duck Stance', blank=True, null=True)

    kdrsps_mc_level3_onlg_Extension = models.CharField(max_length=50, verbose_name='One-Leg Extension w/Machine',
                                                       blank=True, null=True)
    kdrsps_mc_level3_onlg_Press = models.CharField(max_length=50, verbose_name='One-Leg Press w/Machine', blank=True, null=True)

    kdrsps_rc_level1_Strap = models.CharField(max_length=50, verbose_name='Knee Extension w/Strap', blank=True, null=True)
    kdrsps_rc_level1_RB = models.CharField(max_length=50, verbose_name='Knee Extension w/RB', blank=True, null=True)
    kdrsps_rc_level1_Leg = models.CharField(max_length=50, verbose_name='Leg Press w/RB', blank=True, null=True)

    kdrsps_rc_level2_Pistol = models.CharField(max_length=50, verbose_name='Pistol Squat w/Strap', blank=True, null=True)
    kdrsps_rc_level2_Hack = models.CharField(max_length=50, verbose_name='Hack Squat w/RB', blank=True, null=True)
    kdrsps_rc_level2_Strap = models.CharField(max_length=50, verbose_name='Knee Extension w/Strap', blank=True, null=True)
    kdrsps_rc_level2_Single = models.CharField(max_length=50,
                                               verbose_name='Single-Leg Suspended Knee Extension w/Strap',
                                               blank=True, null=True)
    kdrsps_rc_level2_RB = models.CharField(max_length=50, verbose_name='Knee Extension w/RB', blank=True, null=True)
    kdrsps_rc_level2_Leg = models.CharField(max_length=50, verbose_name='Leg Press w/RB', blank=True, null=True)

    kdrsps_rc_level3_Pistol = models.CharField(max_length=50, verbose_name='Pistol Squat w/Strap', blank=True, null=True)
    kdrsps_rc_level3_Single = models.CharField(max_length=50,
                                               verbose_name='Single-Leg Suspended Knee Extension w/Strap',
                                               blank=True, null=True)
    kdrsps_rc_level3_Leg = models.CharField(max_length=50, verbose_name='Leg Press w/RB', blank=True, null=True)

    class Meta:
        verbose_name = "Egzersiz Reçetesi"
        verbose_name_plural = 'Kuadriseps'


class exercise_prescription_hamstring(models.Model):
    # Akut Değişkeni/Hamstring
    hmstrng_set_number = models.CharField(max_length=5, verbose_name="Set Sayısı", blank=True, null=True)
    hmstrng_over_number = models.CharField(max_length=5, verbose_name="Tekrar Sayısı", blank=True, null=True)
    hmstrng_tempo = models.CharField(max_length=10, verbose_name="Tempo (TUT)", blank=True, null=True)
    # Setler arası dinlenme
    hmstrng_sets_between = models.CharField(max_length=10, verbose_name="Setler Arası Dinlenme", blank=True, null=True)
    hmstrng_move_between = models.CharField(max_length=10, verbose_name="Hareketler Arası Dinlenme", blank=True,
                                            null=True)

    hmstrng_kl_level1_Hinge = models.CharField(max_length=50, verbose_name='Hip-Hinge', blank=True, null=True)
    hmstrng_kl_level1_Thrust = models.CharField(max_length=50, verbose_name='Hip Thrust on Heel w/Bosu-Ball',
                                                blank=True, null=True)
    hmstrng_kl_level1_Stability = models.CharField(max_length=50, verbose_name='Stability-Ball Leg Curl', blank=True, null=True)
    hmstrng_kl_level1_Glute = models.CharField(max_length=50, verbose_name='Glute-Ham Roller Leg Curl', blank=True, null=True)

    hmstrng_kl_level2_Single = models.CharField(max_length=50, verbose_name='Single Leg Deadlift', blank=True, null=True)
    hmstrng_kl_level2_Hip = models.CharField(max_length=50, verbose_name='Hip Thrust on Heel w/Bosu-Ball',
                                             blank=True, null=True)
    hmstrng_kl_level2_Nordic = models.CharField(max_length=50, verbose_name='Nordic Hamstring Curl', blank=True, null=True)
    hmstrng_kl_level2_Stability = models.CharField(max_length=50, verbose_name='Stability-Ball Leg Curl', blank=True, null=True)
    hmstrng_kl_level2_Oneleg = models.CharField(max_length=50, verbose_name='One-Leg Stability-Ball Leg Curl',
                                                blank=True, null=True)
    hmstrng_kl_level2_Glute = models.CharField(max_length=50, verbose_name='Glute-Ham Roller Leg Curl', blank=True, null=True)

    hmstrng_kl_level3_Single = models.CharField(max_length=50, verbose_name='Single Leg Deadlift', blank=True, null=True)
    hmstrng_kl_level3_Nordic = models.CharField(max_length=50, verbose_name='Nordic Hamstring Curl', blank=True, null=True)
    hmstrng_kl_level3_Stability = models.CharField(max_length=50, verbose_name='Stability-Ball Leg Curl', blank=True, null=True)
    hmstrng_kl_level3_Oneleg = models.CharField(max_length=50, verbose_name='One-Leg Stability-Ball Leg Curl',
                                                blank=True, null=True)
    hmstrng_kl_level3_Glute = models.CharField(max_length=50, verbose_name='Glute-Ham Roller Leg Curl', blank=True, null=True)

    hmstrng_wg_level1_Rear = models.CharField(max_length=50, verbose_name='Rear Lunge w/Dumbbell & KB', blank=True, null=True)
    hmstrng_wg_level1_Hip = models.CharField(max_length=50, verbose_name='Hip Thrust on Heel w/Dumbbell & KB',
                                             blank=True, null=True)
    hmstrng_wg_level1_Dumbbell = models.CharField(max_length=50, verbose_name='Dumbbell Rotational Lunge',
                                                  blank=True, null=True)
    hmstrng_wg_level1_Side = models.CharField(max_length=50, verbose_name='Side Lunge w/Dumbbell', blank=True, null=True)
    hmstrng_wg_level1_Pivot = models.CharField(max_length=50, verbose_name='Pivot Lunge w/Dumbbell', blank=True, null=True)

    hmstrng_wg_level2_Rear = models.CharField(max_length=50, verbose_name='Rear Lunge w/Dumbbell & KB', blank=True, null=True)
    hmstrng_wg_level2_Hip = models.CharField(max_length=50, verbose_name='Hip Thrust on Heel w/Dumbbell & KB',
                                             blank=True, null=True)
    hmstrng_wg_level2_Good = models.CharField(max_length=50, verbose_name='Good Morning, Bent Legs w/Barbell',
                                              blank=True, null=True)
    hmstrng_wg_level2_Romanian = models.CharField(max_length=50, verbose_name='Romanian Deadlift w/Barbell',
                                                  blank=True, null=True)
    hmstrng_wg_level2_Deadlift = models.CharField(max_length=50, verbose_name='Deadlift w/Barbell & Dumbbell',
                                                  blank=True, null=True)
    hmstrng_wg_level2_Single = models.CharField(max_length=50, verbose_name='Single Leg Deadlift w/KB', blank=True, null=True)
    hmstrng_wg_level2_Dumbbell = models.CharField(max_length=50, verbose_name='Dumbbell Rotational Lunge',
                                                  blank=True, null=True)
    hmstrng_wg_level2_Arc = models.CharField(max_length=50, verbose_name='Arc Lunge w/Dumbbell', blank=True, null=True)
    hmstrng_wg_level2_sd_Dumbbell = models.CharField(max_length=50, verbose_name='Side Lunge w/Dumbbell', blank=True, null=True)
    hmstrng_wg_level2_sd_Barbell = models.CharField(max_length=50, verbose_name='Side Lunge w/Barbell', blank=True, null=True)
    hmstrng_wg_level2_Pivot = models.CharField(max_length=50, verbose_name='Pivot Lunge w/Dumbbell', blank=True, null=True)
    hmstrng_wg_level2_Straight = models.CharField(max_length=50, verbose_name='Straight-Leg Deadlift w/Dumbbell',
                                                  blank=True, null=True)
    hmstrng_wg_level2_Oneleg = models.CharField(max_length=50,
                                                verbose_name='One-Leg One-Arm Angled Barbell Romanian Deadlift',
                                                blank=True, null=True)
    hmstrng_wg_level2_Angled = models.CharField(max_length=50,
                                                verbose_name='Angled Barbell Cross-Shoulder  Reverse Lunge',
                                                blank=True, null=True)

    hmstrng_wg_level3_Good = models.CharField(max_length=50, verbose_name='Good Morning, Bent Legs ', blank=True, null=True)
    hmstrng_wg_level3_Romanian = models.CharField(max_length=50, verbose_name='Romanian Deadlift w/Barbell',
                                                  blank=True, null=True)
    hmstrng_wg_level3_Deadlift = models.CharField(max_length=50, verbose_name='Deadlift w/Barbell & Dumbbell',
                                                  blank=True, null=True)
    hmstrng_wg_level3_Single = models.CharField(max_length=50, verbose_name='Single Leg Deadlift w/KB', blank=True, null=True)
    hmstrng_wg_level3_Arc = models.CharField(max_length=50, verbose_name='Arc Lunge w/Dumbbell', blank=True, null=True)
    hmstrng_wg_level3_Side = models.CharField(max_length=50, verbose_name='Side Lunge w/Barbell', blank=True, null=True)
    hmstrng_wg_level3_Straight = models.CharField(max_length=50, verbose_name='Straight-Leg Deadlift w/Dumbbell',
                                                  blank=True, null=True)
    hmstrng_wg_level3_Oneleg = models.CharField(max_length=50,
                                                verbose_name='One-Leg One-Arm Angled Barbell Romanian Deadlift',
                                                blank=True, null=True)
    hmstrng_wg_level3_Angled = models.CharField(max_length=50,
                                                verbose_name='Angled Barbell Cross-Shoulder Reverse Lunge',
                                                blank=True, null=True)

    hmstrng_mc_level1_Leg = models.CharField(max_length=50, verbose_name='Leg Curl w/Machine', blank=True, null=True)

    hmstrng_mc_level2_Reverse = models.CharField(max_length=50, verbose_name='Reverse Lunge w/Smith Machine',
                                                 blank=True, null=True)
    hmstrng_mc_level2_Leg = models.CharField(max_length=50, verbose_name='Leg Curl w/Machine', blank=True, null=True)

    hmstrng_mc_level3_Reverse = models.CharField(max_length=50, verbose_name='Reverse Lunge w/Smith Machine',
                                                 blank=True, null=True)

    hmstrng_rc_level1_Hip = models.CharField(max_length=50, verbose_name='Hip Thrust on Heel w/RB', blank=True, null=True)
    hmstrng_rc_level1_Reverse = models.CharField(max_length=50, verbose_name='Reverse Lunge w/Strap', blank=True, null=True)
    hmstrng_rc_level1_Lying = models.CharField(max_length=50, verbose_name='Lying Leg Curl w/Strap', blank=True, null=True)
    hmstrng_rc_level1_Knee = models.CharField(max_length=50, verbose_name='Knee Flexion w/RB', blank=True, null=True)
    hmstrng_rc_level1_Bird = models.CharField(max_length=50, verbose_name='Bird Dog Leg Curl w/RB', blank=True, null=True)

    hmstrng_rc_level2_hp_Strap = models.CharField(max_length=50, verbose_name='Hip Thrust on Heel w/Strap',
                                                  blank=True, null=True)
    hmstrng_rc_level2_hp_RB = models.CharField(max_length=50, verbose_name='Hip Thrust on Heel w/RB', blank=True, null=True)
    hmstrng_rc_level2_sngl_Reaching = models.CharField(max_length=50,
                                                       verbose_name='Single-Leg Reaching Romanian Deadlift w/Strap',
                                                       blank=True, null=True)
    hmstrng_rc_level2_Reverse = models.CharField(max_length=50, verbose_name='Reverse Lunge With Knee Drive w/Strap',
                                                 blank=True, null=True)
    hmstrng_rc_level2_Lying = models.CharField(max_length=50, verbose_name='Lying Leg Curl w/Strap', blank=True, null=True)
    hmstrng_rc_level2_sngl_Lying = models.CharField(max_length=50, verbose_name='Single-Leg Lying Leg Curl w/Strap',
                                                    blank=True, null=True)
    hmstrng_rc_level2_Knee = models.CharField(max_length=50, verbose_name='Knee Flexion w/RB', blank=True, null=True)
    hmstrng_rc_level2_Bird = models.CharField(max_length=50, verbose_name='Bird Dog Leg Curl w/Strap', blank=True, null=True)

    hmstrng_rc_level3_Hip = models.CharField(max_length=50, verbose_name='Hip Thrust on Heel w/RB', blank=True, null=True)
    hmstrng_rc_level3_sngl_Reaching = models.CharField(max_length=50,
                                                       verbose_name='Single-Leg Reaching Romanian Deadlift w/Strap',
                                                       blank=True, null=True)
    hmstrng_rc_level3_Reverse = models.CharField(max_length=50, verbose_name='Reverse Lunge With Knee Drive w/Strap',
                                                 blank=True, null=True)
    hmstrng_rc_level3_sngl_Lying = models.CharField(max_length=50, verbose_name='Single-Leg Lying Leg Curl w/Strap',
                                                    blank=True, null=True)
    hmstrng_rc_level3_Push = models.CharField(max_length=50, verbose_name='Push Position Leg Curl w/Strap',
                                              blank=True, null=True)

    class Meta:
        verbose_name = "Egzersiz Reçetesi"
        verbose_name_plural = 'Hamstring'


class exercise_prescription_gastrocnemius(models.Model):
    # Akut Değişkeni/Gastrocnemius
    gstr_set_number = models.CharField(max_length=5, verbose_name="Set Sayısı", blank=True, null=True)
    gstr_over_number = models.CharField(max_length=5, verbose_name="Tekrar Sayısı", blank=True, null=True)
    gstr_tempo = models.CharField(max_length=10, verbose_name="Tempo (TUT)", blank=True, null=True)
    # Setler arası dinlenme
    gstr_sets_between = models.CharField(max_length=10, verbose_name="Setler Arası Dinlenme", blank=True, null=True)
    gstr_move_between = models.CharField(max_length=10, verbose_name="Hareketler Arası Dinlenme", blank=True, null=True)

    gstr_kl_level1_Seated = models.CharField(max_length=50, verbose_name='Seated Calf Raise', blank=True, null=True)
    gstr_kl_level1_Standing = models.CharField(max_length=50, verbose_name='Standing Calf Raise', blank=True, null=True)

    gstr_kl_level2_Seated = models.CharField(max_length=50, verbose_name='Seated Calf Raise', blank=True, null=True)
    gstr_kl_level2_Standing = models.CharField(max_length=50, verbose_name='Standing Calf Raise', blank=True, null=True)
    gstr_kl_level2_Donkey = models.CharField(max_length=50, verbose_name='Donkey Raise', blank=True, null=True)

    gstr_kl_level3_Seated = models.CharField(max_length=50, verbose_name='Seated Calf Raise', blank=True, null=True)
    gstr_kl_level3_Standing = models.CharField(max_length=50, verbose_name='Standing Calf Raise', blank=True, null=True)
    gstr_kl_level3_Donkey = models.CharField(max_length=50, verbose_name='Donkey Raise', blank=True, null=True)

    gstr_wg_level1_Seated = models.CharField(max_length=50, verbose_name='Seated Calf Raise w/Dumbbell & KB',
                                             blank=True, null=True)
    gstr_wg_level1_Toe = models.CharField(max_length=50, verbose_name='Toe Raise w/Dumbbell', blank=True, null=True)
    gstr_wg_level1_Dumbbell = models.CharField(max_length=50, verbose_name='Dumbbell Heel Raise w/Dumbbell',
                                               blank=True, null=True)

    gstr_wg_level2_Barbell = models.CharField(max_length=50, verbose_name='Barbell Calf Raise', blank=True, null=True)
    gstr_wg_level2_Toe = models.CharField(max_length=50, verbose_name='Toe Raise w/Dumbbell', blank=True, null=True)
    gstr_wg_level2_Dumbbell = models.CharField(max_length=50, verbose_name='Dumbbell Heel Raise w/Dumbbell',
                                               blank=True, null=True)

    gstr_wg_level3_Barbell = models.CharField(max_length=50, verbose_name='Barbell Calf Raise', blank=True, null=True)
    gstr_wg_level3_Toe = models.CharField(max_length=50, verbose_name='Toe Raise w/Dumbbell', blank=True, null=True)
    gstr_wg_level3_Dumbbell = models.CharField(max_length=50, verbose_name='Dumbbell Heel Raise w/Dumbbell',
                                               blank=True, null=True)

    gstr_mc_level1_Calf = models.CharField(max_length=50, verbose_name='Calf Raise (Machine)', blank=True, null=True)

    gstr_mc_level2_Standing = models.CharField(max_length=50, verbose_name='Standing Calf Raise (Smith Machine)',
                                               blank=True, null=True)

    gstr_mc_level3_Standing = models.CharField(max_length=50, verbose_name='Standing Calf Raise (Smith Machine)',
                                               blank=True, null=True)

    gstr_rc_level1_Standing = models.CharField(max_length=50, verbose_name='Standing Calf Raise w/Strap', blank=True, null=True)
    gstr_rc_level1_Dorsiflexion = models.CharField(max_length=50, verbose_name='Seated Dorsiflexion w/RB',
                                                   blank=True, null=True)
    gstr_rc_level1_Plantar = models.CharField(max_length=50, verbose_name='Seated Plantar Flexion w/RB', blank=True, null=True)
    gstr_rc_level1_Inversion = models.CharField(max_length=50, verbose_name='Ankle Inversion w/RB', blank=True, null=True)
    gstr_rc_level1_Eversion = models.CharField(max_length=50, verbose_name='Ankle Eversion w/RB', blank=True, null=True)

    gstr_rc_level2_Single = models.CharField(max_length=50, verbose_name='Single Leg Calf Raise w/Strap', blank=True, null=True)
    gstr_rc_level2_Dorsiflexion = models.CharField(max_length=50, verbose_name='Seated Dorsiflexion w/RB',
                                                   blank=True, null=True)
    gstr_rc_level2_Plantar = models.CharField(max_length=50, verbose_name='Seated Plantar Flexion w/RB', blank=True, null=True)
    gstr_rc_level2_Inversion = models.CharField(max_length=50, verbose_name='Ankle Inversion w/RB', blank=True, null=True)
    gstr_rc_level2_Eversion = models.CharField(max_length=50, verbose_name='Ankle Eversion w/RB', blank=True, null=True)

    gstr_rc_level3_Dorsiflexion = models.CharField(max_length=50, verbose_name='Seated Dorsiflexion w/RB',
                                                   blank=True, null=True)
    gstr_rc_level3_Plantar = models.CharField(max_length=50, verbose_name='Seated Plantar Flexion w/RB', blank=True, null=True)
    gstr_rc_level3_Inversion = models.CharField(max_length=50, verbose_name='Ankle Inversion w/RB', blank=True, null=True)
    gstr_rc_level3_Single = models.CharField(max_length=50, verbose_name='Single Leg Calf Raise w/RB', blank=True, null=True)
    gstr_rc_level3_Eversion = models.CharField(max_length=50, verbose_name='Ankle Eversion w/RB', blank=True, null=True)

    class Meta:
        verbose_name = "Egzersiz Reçetesi"
        verbose_name_plural = 'Gastrocnemius'


class exercise_prescription_core(models.Model):
    # Akut Değişkeni/Merkezi Sütun (Core)
    core_set_number = models.CharField(max_length=5, verbose_name="Set Sayısı", blank=True, null=True)
    core_over_number = models.CharField(max_length=5, verbose_name="Tekrar Sayısı", blank=True, null=True)
    core_tempo = models.CharField(max_length=10, verbose_name="Tempo (TUT)", blank=True, null=True)
    # Setler arası dinlenme
    core_sets_between = models.CharField(max_length=10, verbose_name="Setler Arası Dinlenme", blank=True, null=True)
    core_move_between = models.CharField(max_length=10, verbose_name="Hareketler Arası Dinlenme", blank=True, null=True)

    core_kl_level1_Reverse = models.CharField(max_length=50, verbose_name='Reverse Crunch', blank=True, null=True)
    core_kl_level1_Bird = models.CharField(max_length=50, verbose_name='Bird Dog', blank=True, null=True)
    core_kl_level1_Stability = models.CharField(max_length=50, verbose_name='Stability Ball Crunch', blank=True, null=True)
    core_kl_level1_Russian = models.CharField(max_length=50, verbose_name='Russian Twist', blank=True, null=True)
    core_kl_level1_Dumbbell = models.CharField(max_length=50, verbose_name='Dumbbell Side Bend', blank=True, null=True)
    core_kl_level1_Swimmer = models.CharField(max_length=50, verbose_name='Swimmer', blank=True, null=True)
    core_kl_level1_Superman = models.CharField(max_length=50, verbose_name='Superman', blank=True, null=True)
    core_kl_level1_Leg = models.CharField(max_length=50, verbose_name='Leg Lower', blank=True, null=True)
    core_kl_level1_Dead = models.CharField(max_length=50, verbose_name='Dead Bug', blank=True, null=True)
    core_kl_level1_Back = models.CharField(max_length=50, verbose_name='Back Extension/Hyperextension', blank=True, null=True)
    core_kl_level1_Sit = models.CharField(max_length=50, verbose_name='Sit-Up', blank=True, null=True)
    core_kl_level1_Bully = models.CharField(max_length=50, verbose_name='Bully w/Medicine Ball', blank=True, null=True)
    core_kl_level1_Flutter = models.CharField(max_length=50, verbose_name='Flutter Kick', blank=True, null=True)
    core_kl_level1_Scissor = models.CharField(max_length=50, verbose_name='Scissor Flutter Kick', blank=True, null=True)
    core_kl_level1_Medicine = models.CharField(max_length=50, verbose_name='Medicine Ball Seated Twist', blank=True, null=True)
    core_kl_level1_Kneeling = models.CharField(max_length=50, verbose_name='Cable Kneeling Rope Crunch', blank=True, null=True)
    core_kl_level1_Side = models.CharField(max_length=50, verbose_name='Cable Side Bend', blank=True, null=True)
    core_kl_level1_Torso = models.CharField(max_length=50, verbose_name='Cable Torso Rotation', blank=True, null=True)
    core_kl_level1_Diagonal = models.CharField(max_length=50, verbose_name='Diagonal Plate Chop', blank=True, null=True)
    core_kl_level1_Plate = models.CharField(max_length=50, verbose_name='Plate V-Up', blank=True, null=True)

    core_kl_level2_Bicycle = models.CharField(max_length=50, verbose_name='Bicycle Crunch', blank=True, null=True)
    core_kl_level2_Crunch = models.CharField(max_length=50, verbose_name='Reverse Crunch ', blank=True, null=True)
    core_kl_level2_Pendulum = models.CharField(max_length=50, verbose_name='Reverse Pendulum ', blank=True, null=True)
    core_kl_level2_Plank = models.CharField(max_length=50, verbose_name='Prone Plank', blank=True, null=True)
    core_kl_level2_Prone = models.CharField(max_length=50, verbose_name='Prone Plank With Hip Extension', blank=True, null=True)
    core_kl_level2_Hyperextension = models.CharField(max_length=50, verbose_name='Stability Ball Hyperextension',
                                                     blank=True, null=True)
    core_kl_level2_std_Ball = models.CharField(max_length=50, verbose_name='Stability Ball ', blank=True, null=True)
    core_kl_level2_Side = models.CharField(max_length=50, verbose_name='Stability Ball ', blank=True, null=True)
    core_kl_level2_Rotating = models.CharField(max_length=50, verbose_name='Stability Ball ', blank=True, null=True)
    core_kl_level2_Supine = models.CharField(max_length=50, verbose_name='Stability Ball ', blank=True, null=True)
    core_kl_level2_sd_Double = models.CharField(max_length=50, verbose_name='Side Double', blank=True, null=True)
    core_kl_level2_Leg = models.CharField(max_length=50, verbose_name='Leg Lower', blank=True, null=True)
    core_kl_level2_Dead = models.CharField(max_length=50, verbose_name='Dead Bug', blank=True, null=True)
    core_kl_level2_Back = models.CharField(max_length=50, verbose_name='Back Extension', blank=True, null=True)
    core_kl_level2_Sit = models.CharField(max_length=50, verbose_name='Sit-', blank=True, null=True)
    core_kl_level2_Angled = models.CharField(max_length=50, verbose_name='Angled Barbell ', blank=True, null=True)
    core_kl_level2_Bully = models.CharField(max_length=50, verbose_name='Bully w', blank=True, null=True)
    core_kl_level2_Flutter = models.CharField(max_length=50, verbose_name='Flutter Kick', blank=True, null=True)
    core_kl_level2_Hanging = models.CharField(max_length=50, verbose_name='Hanging Knee ', blank=True, null=True)
    core_kl_level2_Three = models.CharField(max_length=50, verbose_name='Three-', blank=True, null=True)
    core_kl_level2_Scissor = models.CharField(max_length=50, verbose_name='Scissor Flutter ', blank=True, null=True)
    core_kl_level2_Mountain = models.CharField(max_length=50, verbose_name='Mountain Climber', blank=True, null=True)
    core_kl_level2_Pullover = models.CharField(max_length=50, verbose_name='Medicine Ball ', blank=True, null=True)
    core_kl_level2_Rotational = models.CharField(max_length=50, verbose_name='Medicine Ball ', blank=True, null=True)
    core_kl_level2_Twist = models.CharField(max_length=50, verbose_name='Medicine Ball ', blank=True, null=True)
    core_kl_level2_Resistance = models.CharField(max_length=60, verbose_name='Resistance Band ', blank=True, null=True)
    core_kl_level2_Rope = models.CharField(max_length=50, verbose_name='Cable Kneeling ', blank=True, null=True)
    core_kl_level2_Twisting = models.CharField(max_length=50, verbose_name='Cable Kneeling ', blank=True, null=True)
    core_kl_level2_Bend = models.CharField(max_length=50, verbose_name='Cable Side ', blank=True, null=True)
    core_kl_level2_LH = models.CharField(max_length=50, verbose_name='Cable Low', blank=True, null=True)
    core_kl_level2_HL = models.CharField(max_length=50, verbose_name='Cable High', blank=True, null=True)
    core_kl_level2_Torso = models.CharField(max_length=50, verbose_name='Cable Torso ', blank=True, null=True)
    core_kl_level2_Double = models.CharField(max_length=50, verbose_name='Side Double', blank=True, null=True)
    core_kl_level2_Diagonal = models.CharField(max_length=50, verbose_name='Diagonal Plate ', blank=True, null=True)
    core_kl_level2_Plate = models.CharField(max_length=50, verbose_name='Plate V', blank=True, null=True)

    core_kl_level3_Bicycle = models.CharField(max_length=50, verbose_name='Bicycle Crunch', blank=True, null=True)
    core_kl_level3_Reverse = models.CharField(max_length=50, verbose_name='Reverse Pendulum ', blank=True, null=True)
    core_kl_level3_pr_Plank = models.CharField(max_length=50, verbose_name='Prone Plank', blank=True, null=True)
    core_kl_level3_st_Plank = models.CharField(max_length=50, verbose_name='Stability Ball Plank to Pike-Up',
                                               blank=True, null=True)
    core_kl_level3_Prone = models.CharField(max_length=50, verbose_name='Prone Plank With Hip Extension', blank=True, null=True)
    core_kl_level3_Bridge = models.CharField(max_length=50, verbose_name='Side Bridge/Side Plank', blank=True, null=True)
    core_kl_level3_Hyperextension = models.CharField(max_length=50, verbose_name='Stability Ball Hyperextension',
                                                     blank=True, null=True)
    core_kl_level3_Crunch = models.CharField(max_length=50, verbose_name='Stability Ball Side Crunch', blank=True, null=True)
    core_kl_level3_Rotating = models.CharField(max_length=50, verbose_name='Stability Ball Rotating Crunch',
                                               blank=True, null=True)
    core_kl_level3_Supine = models.CharField(max_length=50, verbose_name='Stability Ball Supine Bridge', blank=True, null=True)
    core_kl_level3_Barbell = models.CharField(max_length=50, verbose_name='Barbell Rollout', blank=True, null=True)
    core_kl_level3_Lift = models.CharField(max_length=50, verbose_name='Side Double-Leg Lift', blank=True, null=True)
    core_kl_level3_Jackknife = models.CharField(max_length=50, verbose_name='Jackknife', blank=True, null=True)
    core_kl_level3_Rotation = models.CharField(max_length=50, verbose_name='Angled Barbell Rotation', blank=True, null=True)
    core_kl_level3_Hanging = models.CharField(max_length=50, verbose_name='Hanging Knee Raise', blank=True, null=True)
    core_kl_level3_Three = models.CharField(max_length=50, verbose_name='Three-Way Hanging Knee Raise', blank=True, null=True)
    core_kl_level3_Mountain = models.CharField(max_length=50, verbose_name='Mountain Climber', blank=True, null=True)
    core_kl_level3_Medicine = models.CharField(max_length=50, verbose_name='Medicine Ball Rotational Throw',
                                               blank=True, null=True)
    core_kl_level3_Rollout = models.CharField(max_length=50, verbose_name='Rollout', blank=True, null=True)
    core_kl_level3_Kneeling = models.CharField(max_length=50, verbose_name='Cable Kneeling Twisting Rope Crunch',
                                               blank=True, null=True)
    core_kl_level3_Lh = models.CharField(max_length=50, verbose_name='Cable Low/High Woodchop', blank=True, null=True)
    core_kl_level3_HL = models.CharField(max_length=50, verbose_name='Cable High/Low Woodchop', blank=True, null=True)

    core_st_level1_Glute = models.CharField(max_length=50, verbose_name='Glute Bridge w/Strap', blank=True, null=True)
    core_st_level1_Extended = models.CharField(max_length=50, verbose_name='Extended-Arm Plank w/Strap', blank=True, null=True)
    core_st_level1_Bicycle = models.CharField(max_length=50, verbose_name='Bicycle Crunch w/Strap', blank=True, null=True)
    core_st_level1_Kneeling = models.CharField(max_length=50, verbose_name='Kneeling Rollout w/Strap', blank=True, null=True)
    core_st_level1_Lateral = models.CharField(max_length=50, verbose_name='Standing Lateral Twist w/Strap',
                                              blank=True, null=True)
    core_st_level1_Oblique = models.CharField(max_length=50, verbose_name='Standing Oblique Crunch w/Strap',
                                              blank=True, null=True)
    core_st_level1_Rollout = models.CharField(max_length=50, verbose_name='Standing Rollout w/Strap', blank=True, null=True)

    core_st_level2_Glute = models.CharField(max_length=50, verbose_name='Glute Bridge w/Strap', blank=True, null=True)
    core_st_level2_Elbow = models.CharField(max_length=50, verbose_name='Elbow Plank w/Strap', blank=True, null=True)
    core_st_level2_Supine = models.CharField(max_length=50, verbose_name='Supine Plank w/Strap', blank=True, null=True)
    core_st_level2_Single = models.CharField(max_length=50, verbose_name='Single-Leg Plank w/Strap', blank=True, null=True)
    core_st_level2_ex_Plank = models.CharField(max_length=50, verbose_name='Extended-Arm Plank w/Strap', blank=True, null=True)
    core_st_level2_Side = models.CharField(max_length=50, verbose_name='Side Plank w/Strap', blank=True, null=True)
    core_st_level2_Rotational = models.CharField(max_length=50, verbose_name='Rotational Side Plank w/Strap',
                                                 blank=True, null=True)
    core_st_level2_Palov = models.CharField(max_length=50, verbose_name='Palov Press w/Strap', blank=True, null=True)
    core_st_level2_Bicycle = models.CharField(max_length=50, verbose_name='Bicycle Crunch w/Strap', blank=True, null=True)
    core_st_level2_Kneeling = models.CharField(max_length=50, verbose_name='Kneeling Rollout w/Strap', blank=True, null=True)
    core_st_level2_st_Lateral = models.CharField(max_length=50, verbose_name='Standing Lateral Twist w/Strap',
                                                 blank=True, null=True)
    core_st_level2_Power = models.CharField(max_length=50, verbose_name='Power Pull w/Strap', blank=True, null=True)
    core_st_level2_st_Oblique = models.CharField(max_length=50, verbose_name='Standing Oblique Crunch w/Strap',
                                                 blank=True, null=True)
    core_st_level2_ex_Side = models.CharField(max_length=50, verbose_name='Extended-Arm Side Plank w/Strap',
                                              blank=True, null=True)

    core_st_level3_Elbow = models.CharField(max_length=50, verbose_name='Elbow Plank w/Strap', blank=True, null=True)
    core_st_level3_Supine = models.CharField(max_length=50, verbose_name='Supine Plank w/Strap', blank=True, null=True)
    core_st_level3_Single = models.CharField(max_length=50, verbose_name='Single-Leg Plank w/Strap', blank=True, null=True)
    core_st_level3_Side = models.CharField(max_length=50, verbose_name='Side Plank w/Strap', blank=True, null=True)
    core_st_level3_Rotational = models.CharField(max_length=50, verbose_name='Rotational Side Plank w/Strap',
                                                 blank=True, null=True)
    core_st_level3_Palov = models.CharField(max_length=50, verbose_name='Palov Press w/Strap', blank=True, null=True)
    core_st_level3_Power = models.CharField(max_length=50, verbose_name='Power Pull w/Strap', blank=True, null=True)
    core_st_level3_Extended = models.CharField(max_length=50, verbose_name='Extended-Arm Side Plank w/Strap',
                                               blank=True, null=True)
    core_st_level3_Standing = models.CharField(max_length=50, verbose_name='Standing Rollout w/Strap', blank=True, null=True)

    core_rc_level1_Abdominal = models.CharField(max_length=50, verbose_name='Abdominal Crunch w/RB', blank=True, null=True)
    core_rc_level1_Oblique = models.CharField(max_length=50, verbose_name='Oblique Curl-Up w/RB', blank=True, null=True)
    core_rc_level1_Lower = models.CharField(max_length=50, verbose_name='Lower Abdominal Crunch w/RB', blank=True, null=True)
    core_rc_level1_Kneeling = models.CharField(max_length=50, verbose_name='Kneeling Crunch w/RB', blank=True, null=True)
    core_rc_level1_Standing = models.CharField(max_length=50, verbose_name='Standing Back Extension w/RB',
                                               blank=True, null=True)
    core_rc_level2_Abdominal = models.CharField(max_length=50, verbose_name='Abdominal Crunch w/RB', blank=True, null=True)
    core_rc_level2_Oblique = models.CharField(max_length=50, verbose_name='Oblique Curl-Up w/RB', blank=True, null=True)
    core_rc_level2_Lower = models.CharField(max_length=50, verbose_name='Lower Abdominal Crunch w/RB', blank=True, null=True)
    core_rc_level2_Kneeling = models.CharField(max_length=50, verbose_name='Kneeling Crunch w/RB', blank=True, null=True)
    core_rc_level2_Trunk = models.CharField(max_length=50, verbose_name='Trunk Rotation w/RB', blank=True, null=True)
    core_rc_level2_Side = models.CharField(max_length=50, verbose_name='Side Bend w/RB', blank=True, null=True)
    core_rc_level2_Seated = models.CharField(max_length=50, verbose_name='Seated Back Extension w/RB', blank=True, null=True)
    core_rc_level2_Standing = models.CharField(max_length=50, verbose_name='Standing Back Extension w/RB',
                                               blank=True, null=True)
    core_rc_level2_Quadruped = models.CharField(max_length=50, verbose_name='Quadruped Stabilization w/RB',
                                                blank=True, null=True)
    core_rc_level3_Trunk = models.CharField(max_length=50, verbose_name='Trunk Rotation w/RB', blank=True, null=True)
    core_rc_level3_Side = models.CharField(max_length=50, verbose_name='Side Bend w/RB', blank=True, null=True)
    core_rc_level3_Seated = models.CharField(max_length=50, verbose_name='Seated Back Extension w/RB', blank=True, null=True)

    class Meta:
        verbose_name = "Egzersiz Reçetesi"
        verbose_name_plural = 'Core'


class exercise_prescription(models.Model):
    trainer = models.ForeignKey(to=Trainer, verbose_name="Antrenör", on_delete=models.CASCADE, blank=True, null=True)
    personal = models.ForeignKey(to=Personal, verbose_name="Danışan", on_delete=models.CASCADE, blank=True, null=True)
    level = models.ForeignKey(to=exercise_prescription_level, verbose_name="Danışan", on_delete=models.CASCADE, blank=True, null=True)
    chest = models.ForeignKey(to=exercise_prescripion_chest, verbose_name="Danışan", on_delete=models.CASCADE, blank=True, null=True)
    shoulder = models.ForeignKey(to=exercise_prescription_shoulder, verbose_name="Danışan", on_delete=models.CASCADE, blank=True, null=True)
    back = models.ForeignKey(to=exercise_prescription_back, verbose_name="Danışan", on_delete=models.CASCADE, blank=True, null=True)
    biseps = models.ForeignKey(to=exercise_prescription_biseps, verbose_name="Danışan", on_delete=models.CASCADE, blank=True, null=True)
    triseps = models.ForeignKey(to=exercise_prescription_triseps, verbose_name="Danışan", on_delete=models.CASCADE, blank=True, null=True)
    gluteal = models.ForeignKey(to=exercise_prescription_gluteal, verbose_name="Danışan", on_delete=models.CASCADE, blank=True, null=True)
    kuadriseps = models.ForeignKey(to=exercise_prescription_kuadriseps, verbose_name="Danışan", on_delete=models.CASCADE, blank=True, null=True)
    hamstring = models.ForeignKey(to=exercise_prescription_hamstring, verbose_name="Danışan", on_delete=models.CASCADE, blank=True, null=True)
    gastrocnemius = models.ForeignKey(to=exercise_prescription_gastrocnemius, verbose_name="Danışan", on_delete=models.CASCADE, blank=True, null=True)
    core = models.ForeignKey(to=exercise_prescription_core, verbose_name="Danışan", on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(("Date"), default=datetime.now(), blank=True)
    person_level = models.CharField(max_length=20, verbose_name='Kişinin Düzeyini Belirle', blank=True, null=True)
    # Amaç Belirle
    health = models.CharField(max_length=25, verbose_name='Genel Sağlık Gelişimi', blank=True, null=True)
    weak = models.CharField(max_length=30, verbose_name='Zayıflama İncelme', blank=True, null=True)
    metabolik = models.CharField(max_length=30, verbose_name='Metabolik Uygunluk Gelişimi', blank=True, null=True)
    performace = models.CharField(max_length=30, verbose_name='Performans Artışı', blank=True, null=True)
    # Gün sayısı
    monday = models.CharField(max_length=10, verbose_name='Pazartesi', blank=True, null=True)
    tuesday = models.CharField(max_length=10, verbose_name='Salı', blank=True, null=True)
    wednesday = models.CharField(max_length=10, verbose_name='Çarşamba', blank=True, null=True)
    thursday = models.CharField(max_length=10, verbose_name='Perşembe', blank=True, null=True)
    friday = models.CharField(max_length=10, verbose_name='Cuma', blank=True, null=True)
    saturday = models.CharField(max_length=10, verbose_name='Cumartesi', blank=True, null=True)
    sunday = models.CharField(max_length=10, verbose_name='Pazar', blank=True, null=True)
    training_load = models.CharField(max_length=20, verbose_name='Antrenman Yükü Belirle(Yoğunluk Tercihi)',
                                     blank=True, null=True)
    # Antrenman Türü Seç/Sabit Tempolu
    treadmill = models.CharField(max_length=15, verbose_name='Koşu bandı', blank=True, null=True)
    shovel = models.CharField(max_length=15, verbose_name='Kürek', blank=True, null=True)
    bike = models.CharField(max_length=15, verbose_name='Bisikletler', blank=True, null=True)
    mixed_pattern = models.CharField(max_length=15, verbose_name='Karma Desen', blank=True, null=True)
    variable_pace = models.CharField(max_length=20, verbose_name="Değişken (Aralıklı) Tempolu", blank=True, null=True)
    train_time = models.CharField(max_length=20, verbose_name="Antrenman Süresi Belirle", blank=True, null=True)
    rest_interval = models.CharField(max_length=20, verbose_name="Dinlenme Aralığı Belirle", blank=True, null=True)
    train_period = models.CharField(max_length=20, verbose_name="Antrenman Periyotlaması", blank=True, null=True)
    exercise_file = models.CharField(max_length=20, verbose_name="Egzersiz Reçetesi Dosyası", blank=True, null=True)

    def get_absolute_url(self):
        return reverse('fitness-detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('fitness-update', kwargs={'id': self.id})

    def get_trainer_exercise_prescription_delete_url(self):
        return reverse('trainer-exercise_prescription-delete', kwargs={'id': self.id})

    def get_corporate_exercise_prescription_delete_url(self):
        return reverse('corporate-exercise_prescription-delete', kwargs={'id': self.id})

    def get_personal_exercise_prescription_delete_url(self):
        return reverse('personal-exercise_prescription-delete', kwargs={'id': self.id})




    class Meta:
        verbose_name = "Egzersiz Reçetesi"
        verbose_name_plural = 'Kardiyo Programı'