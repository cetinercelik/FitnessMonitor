from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

from registration.models import Trainer, Personal


class corrective_exercise2(models.Model):
    # KNEE / SMR
    kn_smr_Longiditunal = models.CharField(max_length=50, verbose_name='Longiditunal Foam Roller SMR for Priformis',
                                           blank=True, null=True)
    kn_smr_crs_Priformis = models.CharField(max_length=50, verbose_name='Cross Leg Priformis SMR w/Foam Roller',
                                            blank=True, null=True)
    kn_smr_Roller = models.CharField(max_length=50, verbose_name='Adductors SMR w/Foam Roller', blank=True, null=True)
    kn_smr_Miniball = models.CharField(max_length=50, verbose_name='Adductors SMR w/Miniball', blank=True, null=True)
    kn_smr_Straight = models.CharField(max_length=50, verbose_name='Straight Leg Adductors SMR w/Foam Roller',
                                       blank=True, null=True)
    kn_smr_Alternating = models.CharField(max_length=50, verbose_name='Alternating Adductors SMR', blank=True,
                                          null=True)
    kn_smr_sd_Foam = models.CharField(max_length=50, verbose_name='Side Lying IT-Band SMR W/Foam Roller', blank=True,
                                      null=True)
    kn_smr_IT = models.CharField(max_length=50, verbose_name='IT-Band SMR Alternative', blank=True, null=True)
    kn_smr_sd_Mini = models.CharField(max_length=50, verbose_name='Side Lying IT-Band SMR w/Mini Ball', blank=True,
                                      null=True)
    kn_smr_Mini = models.CharField(max_length=50, verbose_name='TFL SMR w/Minibal', blank=True, null=True)
    kn_smr_Two = models.CharField(max_length=50, verbose_name='Two Leg on Foam Roller Hamstring SMR', blank=True,
                                  null=True)
    kn_smr_OneLeg = models.CharField(max_length=50, verbose_name='One-Leg Hamstring SMR', blank=True, null=True)
    kn_smr_crs_Hamstring = models.CharField(max_length=50, verbose_name='Cross Leg Hamstring SMR w/Foam Roller',
                                            blank=True, null=True)
    kn_smr_Seated = models.CharField(max_length=50, verbose_name='Seated Hamstring SMR w/Mini Ball', blank=True,
                                     null=True)
    # STRETCHING
    kn_str_std_Extended = models.CharField(max_length=50, verbose_name='Seated One-Leg Extended Leg Hip Stretch',
                                           blank=True, null=True)
    kn_str_stn_External = models.CharField(max_length=50, verbose_name='Standing Hip External Rotator Stretch',
                                           blank=True, null=True)
    kn_str_Recumbent1 = models.CharField(max_length=60,
                                         verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch',
                                         blank=True, null=True)
    kn_str_Recumbent2 = models.CharField(max_length=70,
                                         verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch (Cross Leg)',
                                         blank=True, null=True)
    kn_str_Lsit = models.CharField(max_length=50, verbose_name='L-Sit Cross Leg- Priformis Stretch', blank=True,
                                   null=True)
    kn_str_stn_Bent = models.CharField(max_length=50, verbose_name='Standing Bent-Knee Hip Adductor Stretch',
                                       blank=True, null=True)
    kn_str_std_Hip = models.CharField(max_length=50, verbose_name='Seated Hip Adductor Stretch', blank=True, null=True)
    kn_str_stn_Raised = models.CharField(max_length=50, verbose_name='Standing Raised-Leg Hip Adductor Stretch',
                                         blank=True, null=True)
    kn_str_stn_Knee = models.CharField(max_length=50, verbose_name='Standing Knee Flexor Stretch', blank=True,
                                       null=True)
    kn_str_std_Knee = models.CharField(max_length=50, verbose_name='Seated Knee Flexor Stretch', blank=True, null=True)
    kn_str_Raised = models.CharField(max_length=50, verbose_name='Raised- One Leg Knee Flexor Stretch', blank=True,
                                     null=True)
    kn_str_Supine = models.CharField(max_length=50, verbose_name='Supine Lying Raised One-Leg Stretch w/Band',
                                     blank=True, null=True)
    kn_str_std_Wide = models.CharField(max_length=50, verbose_name='Seated Wide Range Extended Leg Stretch', blank=True,
                                       null=True)
    kn_str_one_Kneeling = models.CharField(max_length=50, verbose_name='One-Leg ½ Kneeling Knee Extensor Stretch',
                                           blank=True, null=True)
    kn_str_one_Standing = models.CharField(max_length=60,
                                           verbose_name='One-Leg Standing Hip Flexor and Knee Extensor Stretch',
                                           blank=True, null=True)
    kn_str_Lying = models.CharField(max_length=50, verbose_name='Lying Hip Flexor and Knee Extensor Stretch',
                                    blank=True, null=True)
    # Force
    kn_frc_Star = models.CharField(max_length=50, verbose_name='Star Stability & Mobility', blank=True, null=True)
    kn_frc_Land = models.CharField(max_length=50, verbose_name='Land Mine Lateral Squat', blank=True, null=True)
    kn_frc_ltr_Tap = models.CharField(max_length=50, verbose_name='Lateral Tap', blank=True, null=True)
    kn_frc_Heel = models.CharField(max_length=50, verbose_name='Heel Elevated ¼ Squat', blank=True, null=True)
    kn_frc_Banded = models.CharField(max_length=50, verbose_name='Banded ‘’Spanish’’ Squat', blank=True, null=True)
    kn_frc_ltr_Step = models.CharField(max_length=50, verbose_name='Lateral Step Down', blank=True, null=True)
    kn_frc_Rear = models.CharField(max_length=50, verbose_name='Rear Foot Elevated Split Squat', blank=True, null=True)
    kn_frc_rvr_Nordic = models.CharField(max_length=50, verbose_name='Reverse Nordic Curl', blank=True, null=True)
    kn_frc_Bench = models.CharField(max_length=50, verbose_name='Bench Pistol Squat', blank=True, null=True)
    kn_frc_Fire = models.CharField(max_length=50, verbose_name='Fire Hydrant', blank=True, null=True)
    kn_frc_sngl_Squat = models.CharField(max_length=50, verbose_name='Single Leg Squat', blank=True, null=True)
    kn_frc_Double = models.CharField(max_length=50, verbose_name='Double Leg Drop-Jump', blank=True, null=True)
    kn_frc_sngl_Drop = models.CharField(max_length=50, verbose_name='Single Leg Drop-Jump', blank=True, null=True)
    kn_frc_Split = models.CharField(max_length=50, verbose_name='Split Stance Lunge w/Band', blank=True, null=True)
    kn_frc_sngl_Wall = models.CharField(max_length=50, verbose_name='Sinle Leg Wall Sit w/Band', blank=True, null=True)
    kn_frc_Quadruped = models.CharField(max_length=50, verbose_name='Quadruped Rock Back', blank=True, null=True)
    kn_frc_Runner = models.CharField(max_length=50, verbose_name='Runner Lunge', blank=True, null=True)
    kn_frc_Standing = models.CharField(max_length=50, verbose_name='Standing Clam Shell', blank=True, null=True)
    kn_frc_rvr_Lunge = models.CharField(max_length=50, verbose_name='Reverse Lunge w/Band', blank=True, null=True)
    kn_frc_Goblet = models.CharField(max_length=50, verbose_name='Goblet Squat w/Band', blank=True, null=True)
    kn_frc_sp_Pose = models.CharField(max_length=50, verbose_name='Supine Pose Hip External Rotation w/Band',
                                      blank=True, null=True)
    kn_frc_sngl_Hip = models.CharField(max_length=50, verbose_name='Single Leg Hip Thrust', blank=True, null=True)
    kn_frc_Bridge = models.CharField(max_length=50, verbose_name='Bridge Leg Extension', blank=True, null=True)
    kn_frc_sngl_Thrust = models.CharField(max_length=50, verbose_name='Single Leg Hip Thrust w/Swiss Ball', blank=True,
                                          null=True)
    kn_frc_sp_Elevated = models.CharField(max_length=50, verbose_name='Supine Elevated March w/Band', blank=True,
                                          null=True)
    kn_frc_Wall = models.CharField(max_length=50, verbose_name='Wall Squat and Hold', blank=True, null=True)
    kn_frc_Step = models.CharField(max_length=50, verbose_name='Step-Up ', blank=True, null=True)
    kn_frc_Alternating = models.CharField(max_length=50, verbose_name='Alternating Kick Stand Lunge Back', blank=True,
                                          null=True)
    kn_frc_Posterior = models.CharField(max_length=50, verbose_name='Posterior Step-Down', blank=True, null=True)
    kn_frc_Lateral = models.CharField(max_length=50, verbose_name='Lateral Sliders Lunge', blank=True, null=True)
    kn_frc_Elevated = models.CharField(max_length=50, verbose_name='Elevated Curtsy Lunge', blank=True, null=True)
    # LOMBER/SMR
    lmbr_smr_Longiditunal = models.CharField(max_length=50, verbose_name='Longiditunal Foam Roller SMR for Priformis',
                                             blank=True, null=True)
    lmbr_smr_crs_Priformis = models.CharField(max_length=50, verbose_name='Cross Leg Priformis SMR w/Foam Roller',
                                              blank=True, null=True)
    lmbr_smr_add_Foam = models.CharField(max_length=50, verbose_name='Adductors SMR w/Foam Roller', blank=True,
                                         null=True)
    lmbr_smr_add_Miniball = models.CharField(max_length=50, verbose_name='Adductors SMR w/Miniball', blank=True,
                                             null=True)
    lmbr_smr_Straight = models.CharField(max_length=50, verbose_name='Straight Leg Adductors SMR w/Foam Roller',
                                         blank=True, null=True)
    lmbr_smr_Alternating = models.CharField(max_length=50, verbose_name='Alternating Adductors SMR', blank=True,
                                            null=True)
    lmbr_smr_sd_Foam = models.CharField(max_length=50, verbose_name='Side Lying IT-Band SMR  W/Foam Roller', blank=True,
                                        null=True)
    lmbr_smr_IT = models.CharField(max_length=50, verbose_name='IT-Band SMR Alternative', blank=True, null=True)
    lmbr_smr_sd_Mini = models.CharField(max_length=50, verbose_name='Side Lying IT-Band SMR w/Mini Bal', blank=True,
                                        null=True)
    lmbr_smr_TFL = models.CharField(max_length=50, verbose_name='TFL SMR w/Miniball', blank=True, null=True)
    lmbr_smr_tw_Hamstring = models.CharField(max_length=50, verbose_name='Two Leg on Foam Roller Hamstring SMR',
                                             blank=True, null=True)
    lmbr_smr_one_Hamstring = models.CharField(max_length=50, verbose_name='One-Leg Hamstring SMR', blank=True,
                                              null=True)
    lmbr_smr_crs_Hamstring = models.CharField(max_length=50, verbose_name='Cross Leg Hamstring SMR w//Foam Roller',
                                              blank=True, null=True)
    lmbr_smr_Seated = models.CharField(max_length=50, verbose_name='Seated Hamstring SMR w/Mini Ball', blank=True,
                                       null=True)
    lmbr_smr_one = models.CharField(max_length=50, verbose_name='One-Leg Calf SMR w/Foam Roller', blank=True, null=True)
    lmbr_smr_crs_Calf = models.CharField(max_length=50, verbose_name='Cross Leg Calf SMR w/Foam Roller', blank=True,
                                         null=True)
    lmbr_smr_tw_Foam = models.CharField(max_length=50, verbose_name='Two Leg On Foam Roller Calf SMR', blank=True,
                                        null=True)
    lmbr_smr_Calf = models.CharField(max_length=50, verbose_name='Calf SMR W/Mini Ball', blank=True, null=True)
    lmbr_smr_Hip = models.CharField(max_length=50, verbose_name='Hip Flexors SMR w/Foam Roller', blank=True, null=True)
    # STRETCHING
    lmbr_str_std_Extended = models.CharField(max_length=50, verbose_name='Seated One-Leg Extended Leg  Hip Stretch',
                                             blank=True, null=True)
    lmbr_str_stdn_Hip = models.CharField(max_length=50, verbose_name='Standing Hip External Rotator Stretch',
                                         blank=True, null=True)
    lmbr_str_Recumbent1 = models.CharField(max_length=60,
                                           verbose_name='Recumbent Hip External Rotator and Hip  Extensor Stretch',
                                           blank=True, null=True)
    lmbr_str_Recumbent = models.CharField(max_length=70,
                                          verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch (Cross Leg)',
                                          blank=True, null=True)
    lmbr_str_Lsit = models.CharField(max_length=50, verbose_name='L-Sit Cross Leg- Priformis Stretch', blank=True,
                                     null=True)
    lmbr_str_stdn_Bent = models.CharField(max_length=50, verbose_name='Standing Bent-Knee Hip Adductor Stretch',
                                          blank=True, null=True)
    lmbr_str_std_Hip = models.CharField(max_length=50, verbose_name='Seated Hip Adductor Stretch', blank=True,
                                        null=True)
    lmbr_str_stdn_Raised = models.CharField(max_length=50, verbose_name='Standing Raised-Leg Hip Adductor Stretch',
                                            blank=True, null=True)
    lmbr_str_stdn_Knee = models.CharField(max_length=50, verbose_name='Standing Knee Flexor Stretch', blank=True,
                                          null=True)
    lmbr_str_std_Knee = models.CharField(max_length=50, verbose_name='Seated Knee Flexor Stretch', blank=True,
                                         null=True)
    lmbr_str_Raised = models.CharField(max_length=50, verbose_name='Raised- One Leg Knee Flexor Stretch', blank=True,
                                       null=True)
    lmbr_str_sp_Lying = models.CharField(max_length=50, verbose_name='Supine Lying Raised One-Leg Stretch w/Band',
                                         blank=True, null=True)
    lmbr_str_std_Wide = models.CharField(max_length=50, verbose_name='Seated Wide Range Extended Leg Stretch',
                                         blank=True, null=True)
    lmbr_str_one_Kneeling = models.CharField(max_length=50, verbose_name='One-Leg ½ Kneeling Knee  Extensor Stretch',
                                             blank=True, null=True)
    lmbr_str_one_Standing = models.CharField(max_length=60,
                                             verbose_name='One-Leg Standing Hip Flexor  and Knee Extensor Stretch',
                                             blank=True, null=True)
    lmbr_str_Lying = models.CharField(max_length=50, verbose_name='Lying Hip Flexor and Knee Extensor Stretch',
                                      blank=True, null=True)
    lmbr_str_sp_Pose = models.CharField(max_length=50, verbose_name='Supine Pose Lower-Trunk Flexor Stretch',
                                        blank=True, null=True)
    lmbr_str_Prone = models.CharField(max_length=50, verbose_name='Prone Pose Lower-Trunk Flexor Stretch', blank=True,
                                      null=True)
    lmbr_str_std_Lower = models.CharField(max_length=50, verbose_name='Seated Lower-Trunk Extensor Stretch', blank=True,
                                          null=True)
    lmbr_str_stdn_Lateral = models.CharField(max_length=50, verbose_name='Standing Lower-Trunk Lateral Flexor Stretch',
                                             blank=True, null=True)
    lmbr_str_stdn_Flexor = models.CharField(max_length=50,
                                            verbose_name='Standing Lower-Trunk Flexor Stretch (Arched Back)',
                                            blank=True, null=True)
    lmbr_str_Lower = models.CharField(max_length=50, verbose_name='Lower-Trunk Lateral Flexor Stretch (Arched Back)',
                                      blank=True, null=True)
    lmbr_str_sp_Side = models.CharField(max_length=50, verbose_name='Supine Lying Side Bend (Oscar Moran-208) ',
                                        blank=True, null=True)
    lmbr_str_Open = models.CharField(max_length=50, verbose_name='Open Leg Side Bend', blank=True, null=True)
    # FORCE
    lmbr_frc_hp_External = models.CharField(max_length=50, verbose_name='Hip External/Internal Rotation Mobility',
                                            blank=True, null=True)
    lmbr_frc_prn_Swimmers = models.CharField(max_length=50, verbose_name='Prone Swimmers', blank=True, null=True)
    lmbr_frc_qd_Thoracic = models.CharField(max_length=50, verbose_name='Quadruped Thoracic Rotation', blank=True,
                                            null=True)
    lmbr_frc_prn_Scorpion = models.CharField(max_length=50, verbose_name='Prone Scorpion Kick-Overs', blank=True,
                                             null=True)
    lmbr_frc_Side = models.CharField(max_length=50, verbose_name='Side Lying Thoracic Reach Arounds', blank=True,
                                     null=True)
    lmbr_frc_Pancake = models.CharField(max_length=50, verbose_name='Pancake Walkouts', blank=True, null=True)
    lmbr_frc_Supine = models.CharField(max_length=50, verbose_name='Supine Figure 4', blank=True, null=True)
    lmbr_frc_Shoulder = models.CharField(max_length=50, verbose_name='Shoulder Extension Crap Lifts', blank=True,
                                         null=True)
    lmbr_frc_hp_Flexor = models.CharField(max_length=50, verbose_name='Hip Flexor / Hamstring Combo', blank=True,
                                          null=True)
    lmbr_frc_Dead = models.CharField(max_length=50, verbose_name='Dead Bug Variations', blank=True, null=True)
    lmbr_frc_brd_Variations = models.CharField(max_length=70,
                                               verbose_name='Bridge Variations (özellikle bacak arasında bir cisim sıkıştırarak)',
                                               blank=True, null=True)
    lmbr_frc_br_Crawl = models.CharField(max_length=50, verbose_name='Bear Crawl Straight Leg', blank=True, null=True)
    lmbr_frc_ltr_Line = models.CharField(max_length=50, verbose_name='Lateral Line Stretch', blank=True, null=True)
    lmbr_frc_ct_Cow = models.CharField(max_length=60,
                                       verbose_name='Cat Cow Varyasyonları (özellikle resisted seçenekler)', blank=True,
                                       null=True)
    lmbr_frc_Resisted = models.CharField(max_length=50, verbose_name='Resisted Bird Dog', blank=True, null=True)
    lmbr_frc_Weighted = models.CharField(max_length=50, verbose_name='Weighted Trunk Rotations', blank=True, null=True)
    lmbr_frc_The = models.CharField(max_length=50, verbose_name='The Bretzel Stretch', blank=True, null=True)
    lmbr_frc_Anti = models.CharField(max_length=50, verbose_name='Anti-Rotation Walk Ups', blank=True, null=True)
    lmbr_frc_prn_Elbows = models.CharField(max_length=50, verbose_name='Prone Extension on Elbows', blank=True,
                                           null=True)
    lmbr_frc_prn_Hands = models.CharField(max_length=50, verbose_name='Prone Extension on Hands', blank=True, null=True)
    lmbr_frc_Straight = models.CharField(max_length=50, verbose_name='Straight Leg Raise', blank=True, null=True)
    lmbr_frc_hp_March = models.CharField(max_length=50, verbose_name='Hip Flexor March w/Band', blank=True, null=True)
    lmbr_frc_prn_Cars = models.CharField(max_length=50, verbose_name='Prone Hip Cars', blank=True, null=True)
    lmbr_frc_Shin = models.CharField(max_length=50, verbose_name='90/90 to Shin Box Step Through', blank=True,
                                     null=True)
    lmbr_frc_Kneeling = models.CharField(max_length=50, verbose_name='½ Kneeling Hip Flexor / Hamstring Mob',
                                         blank=True, null=True)
    lmbr_frc_Hand = models.CharField(max_length=50, verbose_name='Hand Plank w/Hip Flexion and Extension', blank=True,
                                     null=True)
    lmbr_frc_qd_Hip = models.CharField(max_length=50, verbose_name='Quadruped Hip Extension to Abduction', blank=True,
                                       null=True)
    lmbr_frc_br_Sit = models.CharField(max_length=50, verbose_name='Bear Sit Kick Outs', blank=True, null=True)
    lmbr_frc_Worlds = models.CharField(max_length=50, verbose_name='Worlds Greated Stretch', blank=True, null=True)
    lmbr_frc_Deep = models.CharField(max_length=50, verbose_name='Deep Squat Mobility w/Strap', blank=True, null=True)
    lmbr_frc_ct_Camel = models.CharField(max_length=50, verbose_name='Cat & Camel', blank=True, null=True)
    lmbr_frc_Rock = models.CharField(max_length=50, verbose_name='Rock Backs', blank=True, null=True)
    lmbr_frc_qd_Plank = models.CharField(max_length=50, verbose_name='Quadruped Plank', blank=True, null=True)
    lmbr_frc_Lateral = models.CharField(max_length=50, verbose_name='Lateral Reach', blank=True, null=True)
    lmbr_frc_Segmental = models.CharField(max_length=50, verbose_name='Segmental Flexion', blank=True, null=True)
    lmbr_frc_Child = models.CharField(max_length=50, verbose_name='Child Pose and Reach', blank=True, null=True)
    lmbr_frc_lw_Trunk = models.CharField(max_length=50, verbose_name='Lower Trunk Rotation', blank=True, null=True)
    lmbr_frc_prn_Elbow = models.CharField(max_length=50, verbose_name='Prone Extension on Elbow', blank=True, null=True)
    lmbr_frc_prn_Hand = models.CharField(max_length=50, verbose_name='Prone Extension on Hand', blank=True, null=True)
    lmbr_frc_dbl_Knee = models.CharField(max_length=50, verbose_name='Double Knee Supine Flexion', blank=True,
                                         null=True)
    lmbr_frc_stdn_Sidebend = models.CharField(max_length=50, verbose_name='Standing Sidebend', blank=True, null=True)
    lmbr_frc_hp_Hinge = models.CharField(max_length=50, verbose_name='Hip Hinge', blank=True, null=True)
    lmbr_frc_Thoracic = models.CharField(max_length=50, verbose_name='Thoracic-Lumbar Gapping', blank=True, null=True)
    lmbr_frc_brd_March = models.CharField(max_length=50, verbose_name='Bridge March w/RB', blank=True, null=True)
    lmbr_frc_Stability = models.CharField(max_length=50, verbose_name='Stability Ball Bird-Dog', blank=True, null=True)
    lmbr_frc_Lower = models.CharField(max_length=50, verbose_name='Lower Trunk Rotation w/Stability Ball', blank=True,
                                      null=True)
    lmbr_frc_stdn_Foot = models.CharField(max_length=50, verbose_name='Standing Foot Taps and Isometric Pallof Press',
                                          blank=True, null=True)
    lmbr_frc_sngl_Bridge = models.CharField(max_length=50, verbose_name='Single Leg Bridge', blank=True, null=True)
    lmbr_frc_Sumo = models.CharField(max_length=50, verbose_name='Sumo Hip Hinge Squat', blank=True, null=True)
    lmbr_frc_hp_Thrust = models.CharField(max_length=50, verbose_name='Hip Thrust', blank=True, null=True)
    lmbr_frc_pstr_Pelvic = models.CharField(max_length=50, verbose_name='Posterior Pelvic Tilt Glute Bridge',
                                            blank=True, null=True)
    lmbr_frc_pstr_Tilt = models.CharField(max_length=50, verbose_name='Posterior Tilt and Banded Marches', blank=True,
                                          null=True)
    lmbr_frc_Plank = models.CharField(max_length=50, verbose_name='Plank (Posterior Tilt)', blank=True, null=True)
    lmbr_frc_std_Pelvic = models.CharField(max_length=50, verbose_name='Standing Pelvic Tilt', blank=True, null=True)
    lmbr_frc_Reverse = models.CharField(max_length=50, verbose_name='Reverse Scorpion ', blank=True, null=True)
    lmbr_frc_sngl_Heel = models.CharField(max_length=50, verbose_name='Single Heel Tap ', blank=True, null=True)
    lmbr_frc_dbl_Heel = models.CharField(max_length=50, verbose_name='Double Heel Tap', blank=True, null=True)
    lmbr_frc_stdn_Pallof = models.CharField(max_length=50, verbose_name='Standing Pallof Press', blank=True, null=True)
    lmbr_frc_Pallof = models.CharField(max_length=50, verbose_name='½ Kneeling Pallof Press', blank=True, null=True)

    class Meta:
        verbose_name = 'Düzeltici Egzersiz Reçetesi'
        verbose_name_plural = 'Düzeltici Egzersiz Reçetesi'


class corrective_exercise3(models.Model):
    # TORAKAL / SMR
    trkl_smr_sd_Foam = models.CharField(max_length=50, verbose_name='Side Back Glide w/Foam Roller', blank=True,
                                        null=True)
    trkl_smr_sd_Mini = models.CharField(max_length=50, verbose_name='Side Back Glide w/Mini Ball', blank=True,
                                        null=True)
    trkl_smr_Supine = models.CharField(max_length=50, verbose_name='Supine Pose T-Spine Glide w/Foam Roller',
                                       blank=True, null=True)
    trkl_smr_stdn_Mini = models.CharField(max_length=50, verbose_name='Standing T- Spine Glide w/Mini Ball', blank=True,
                                          null=True)
    trkl_smr_stdn_Foam = models.CharField(max_length=50, verbose_name='Standing T-Spine Glide w/Foam Roll', blank=True,
                                          null=True)
    trkl_smr_tsp_Glide = models.CharField(max_length=50, verbose_name='T- Spine Glide on Longitudinal Foam Roller',
                                          blank=True, null=True)
    trkl_smr_tsp_Cross = models.CharField(max_length=50, verbose_name='T-Spine Cross Friction', blank=True, null=True)
    # STRETCHING
    trkl_str_Kneel = models.CharField(max_length=50, verbose_name='Kneel Down, Length Arms Away From The Wal',
                                      blank=True, null=True)
    trkl_str_Tspine = models.CharField(max_length=50, verbose_name='T-Spine Hold and Stretch w/Foam Roller', blank=True,
                                       null=True)
    trkl_str_Trunk = models.CharField(max_length=50, verbose_name='Trunk Rotation with Elbow Flexed', blank=True,
                                      null=True)
    trkl_str_Bench = models.CharField(max_length=50, verbose_name='Bench Overhead Stretch', blank=True, null=True)
    trkl_str_Foam = models.CharField(max_length=50, verbose_name='Foam Roller Prayer Stretch', blank=True, null=True)
    trkl_str_Swiss = models.CharField(max_length=50, verbose_name='Swiss Ball Prayer', blank=True, null=True)
    trkl_str_onearm = models.CharField(max_length=50, verbose_name='One-Arm Extended Stretch', blank=True, null=True)
    trkl_str_over = models.CharField(max_length=50, verbose_name='Over Head-Arm Vertical Extension', blank=True,
                                     null=True)
    trkl_str_Quadruped = models.CharField(max_length=50, verbose_name='Quadruped Prayer Stretch', blank=True, null=True)
    trkl_str_Wall = models.CharField(max_length=50, verbose_name='Wall Support Thoracic Flexion', blank=True, null=True)
    trkl_str_Standing = models.CharField(max_length=50, verbose_name='Standing Neck and Trunk Flexion', blank=True,
                                         null=True)
    trkl_str_Forward = models.CharField(max_length=50, verbose_name='Forward Arm Extension', blank=True, null=True)
    # FORCE
    trkl_frc_sws_IS = models.CharField(max_length=50, verbose_name='Swissball Shoulder I’s', blank=True, null=True)
    trkl_frc_sws_YS = models.CharField(max_length=50, verbose_name='Swissball Shoulder Y’s', blank=True, null=True)
    trkl_frc_sws_TS = models.CharField(max_length=50, verbose_name='Swissball Shoulder T’s', blank=True, null=True)
    trkl_frc_Brueggers = models.CharField(max_length=50, verbose_name='Brueggers', blank=True, null=True)
    trkl_frc_thrc_Sprinklers = models.CharField(max_length=50, verbose_name='Thoracic Sprinklers', blank=True,
                                                null=True)
    trkl_frc_Standing = models.CharField(max_length=50, verbose_name='Standing Thoracic Extension w/Bar or Wall',
                                         blank=True, null=True)
    trkl_frc_Windshields = models.CharField(max_length=50, verbose_name='Windshields Wipers', blank=True, null=True)
    trkl_frc_Prayer = models.CharField(max_length=50, verbose_name='Prayer Swipers', blank=True, null=True)
    trkl_frc_Kneeling = models.CharField(max_length=50, verbose_name='½ Kneeling Open Books', blank=True, null=True)
    trkl_frc_Superman = models.CharField(max_length=50, verbose_name='Superman 2.0', blank=True, null=True)
    trkl_frc_prn_YS = models.CharField(max_length=50, verbose_name='Prone Y’s', blank=True, null=True)
    trkl_frc_Tspine = models.CharField(max_length=50, verbose_name='T-Spine Windmill w/Dowel', blank=True, null=True)
    trkl_frc_Deep = models.CharField(max_length=50, verbose_name='Deep Squat Pass Through', blank=True, null=True)
    trkl_frc_Overhead = models.CharField(max_length=50, verbose_name='Overhead Squat w/Dowel', blank=True, null=True)
    trkl_frc_Good = models.CharField(max_length=50, verbose_name='Good Morning Windmill w/Dowel', blank=True, null=True)
    trkl_frc_Lat = models.CharField(max_length=50, verbose_name='Lat Pull Down w/Dowel', blank=True, null=True)
    trkl_frc_std_Windmills = models.CharField(max_length=50, verbose_name='Seated Windmills', blank=True, null=True)
    trkl_frc_Dowel = models.CharField(max_length=50, verbose_name='Dowel Thoracic Rotation', blank=True, null=True)
    trkl_frc_Child = models.CharField(max_length=50, verbose_name='Child Pose & Cat Camel', blank=True, null=True)
    trkl_frc_thrc_Extension = models.CharField(max_length=50, verbose_name='Thoracic Extension w/Foam Roller',
                                               blank=True, null=True)
    trkl_frc_ct_Camel = models.CharField(max_length=50, verbose_name='Cat & Camel', blank=True, null=True)
    trkl_frc_ct_Cow = models.CharField(max_length=50, verbose_name='Cat & Cow', blank=True, null=True)
    trkl_frc_prn_Press = models.CharField(max_length=50, verbose_name='Prone Press-Up', blank=True, null=True)
    trkl_frc_sq_Blades = models.CharField(max_length=50, verbose_name='Squeeze Shoulder Blades and Neck Extension',
                                          blank=True, null=True)
    trkl_frc_thrc_Spine = models.CharField(max_length=50, verbose_name='Thoracic Spine Extension on Bench', blank=True,
                                           null=True)
    trkl_frc_st_Back = models.CharField(max_length=50, verbose_name='Sit Back to Heels T-Spine Cat & Camel', blank=True,
                                        null=True)
    trkl_frc_Lean = models.CharField(max_length=50, verbose_name='Lean Forward and Raise Arm Up', blank=True, null=True)
    trkl_frc_st_Down = models.CharField(max_length=50, verbose_name='Sit Down İnto a Squat and Raise Arms-UP Overhead',
                                        blank=True, null=True)
    trkl_frc_Floor = models.CharField(max_length=50, verbose_name='Floor Sliders', blank=True, null=True)
    trkl_frc_Wall = models.CharField(max_length=50, verbose_name='Wall Angels', blank=True, null=True)
    trkl_frc_sq_Pull = models.CharField(max_length=50, verbose_name='Squeeze Shoulders and Pull Down on Bench',
                                        blank=True, null=True)
    trkl_frc_Hands = models.CharField(max_length=50, verbose_name='Hands Behind Neck + Blades Together', blank=True,
                                      null=True)
    trkl_frc_Thumbs = models.CharField(max_length=50, verbose_name='Thumbs Up ‘’W’’ Raise', blank=True, null=True)
    trkl_frc_Straight = models.CharField(max_length=50, verbose_name='Straight Arm ‘’Y’’ Raise on Bench', blank=True,
                                         null=True)
    trkl_frc_Open = models.CharField(max_length=50, verbose_name='Open Book- Hand Behind Back', blank=True, null=True)
    trkl_frc_Lying = models.CharField(max_length=50, verbose_name='Lying Open Book', blank=True, null=True)
    trkl_frc_Bent = models.CharField(max_length=50, verbose_name='Bent Over Open Book-Hand Behind Back', blank=True,
                                     null=True)
    trkl_frc_qd_Hand = models.CharField(max_length=50, verbose_name='Quadruped Open Book- Hand Behind Back', blank=True,
                                        null=True)
    trkl_frc_qd_Arm = models.CharField(max_length=50, verbose_name='Quadruped Open Book- Arm Behind Back', blank=True,
                                       null=True)
    # ROUND / SMR
    rnd_smr_Supine = models.CharField(max_length=50, verbose_name='Supine Pose Miniball Rotators Glide', blank=True,
                                      null=True)
    rnd_smr_Prone = models.CharField(max_length=50, verbose_name='Prone Pose Miniball Shoulder Glide', blank=True,
                                     null=True)
    rnd_smr_Wall = models.CharField(max_length=50, verbose_name='Wall Rotators Glide w/Miniball', blank=True, null=True)
    rnd_smr_Standing = models.CharField(max_length=50, verbose_name='Standing Side Pose Shoulder SMR w/Miniball',
                                        blank=True, null=True)
    rnd_smr_Side = models.CharField(max_length=50, verbose_name='Side Lying Lateral Shoulder SMR w/Miniball',
                                    blank=True, null=True)
    # STRETCHING
    rnd_str_Bench = models.CharField(max_length=50, verbose_name='Bench Overhead Stretch ', blank=True, null=True)
    rnd_str_Foam = models.CharField(max_length=50, verbose_name='Foam Roller Prayer Stretch', blank=True, null=True)
    rnd_str_Swiss = models.CharField(max_length=50, verbose_name='Swiss Ball Prayer', blank=True, null=True)
    rnd_str_Praying = models.CharField(max_length=50, verbose_name='Praying type, Quadruped extension', blank=True,
                                       null=True)
    rnd_str_Torso = models.CharField(max_length=50, verbose_name='Torso flexion, over a support w/Wal', blank=True,
                                     null=True)
    rnd_str_OneArm = models.CharField(max_length=50, verbose_name='One-Arm Shoulder Flexor Stretch', blank=True,
                                      null=True)
    rnd_str_Horizontal = models.CharField(max_length=50, verbose_name='Horizontal Abduction of the arm', blank=True,
                                          null=True)
    rnd_str_Overhead = models.CharField(max_length=50, verbose_name='Overhead Arm Vertical Stretch', blank=True,
                                        null=True)
    rnd_str_Neck = models.CharField(max_length=50, verbose_name='Neck & Torso Flexion', blank=True, null=True)
    rnd_str_Forward = models.CharField(max_length=50, verbose_name='Forward Arm Ext', blank=True, null=True)
    rnd_str_Crossing = models.CharField(max_length=50, verbose_name='Crossing The Arms Behind The Back', blank=True,
                                        null=True)
    rnd_str_Lying = models.CharField(max_length=50, verbose_name='Lying on Bench Ext. Rotation', blank=True, null=True)
    rnd_str_Seated = models.CharField(max_length=55, verbose_name='Seated Shoulder Flexor Depressor Retractor Stretch',
                                      blank=True, null=True)
    # FORCE
    rnd_frc_sd_Lying = models.CharField(max_length=50, verbose_name='Side Lying Bottom-Up Shoulder Rotation w/KB',
                                        blank=True, null=True)
    rnd_frc_kn_Shoulder = models.CharField(max_length=50,
                                           verbose_name='½ Kneeling Bottom-Up Shoulder Ext. Rotation w/KB', blank=True,
                                           null=True)
    rnd_frc_sp_Pose = models.CharField(max_length=50, verbose_name='Supine Pose Bottom-Up Shoulder Rotation w/KB',
                                       blank=True, null=True)
    rnd_frc_kn_Press = models.CharField(max_length=50, verbose_name='½ Kneeling Bottom-Up Press w/KB', blank=True,
                                        null=True)
    rnd_frc_qd_Pose = models.CharField(max_length=50, verbose_name='Quadruped Pose Around The World w/RB', blank=True,
                                       null=True)
    rnd_frc_sd_Plank = models.CharField(max_length=50, verbose_name='Side Plank External Rotation w/RB', blank=True,
                                        null=True)
    rnd_frc_qd_Row = models.CharField(max_length=50, verbose_name='Quadruped Row w/RB', blank=True, null=True)
    rnd_frc_sd_External = models.CharField(max_length=50, verbose_name='Side Lying External Rotation', blank=True,
                                           null=True)
    rnd_frc_sd_Lateral = models.CharField(max_length=50, verbose_name='Side Lying Lateral Raise', blank=True, null=True)
    rnd_frc_Eccentric = models.CharField(max_length=50, verbose_name='Eccentric Rotation to Press', blank=True,
                                         null=True)
    rnd_frc_Dynamic = models.CharField(max_length=50, verbose_name='Dynamic Stabilization', blank=True, null=True)
    rnd_frc_wl_Slides = models.CharField(max_length=50, verbose_name='Wall Slides Lift and Pulses', blank=True,
                                         null=True)
    rnd_frc_wl_Clock = models.CharField(max_length=50, verbose_name='Wall Clock w/RB', blank=True, null=True)
    rnd_frc_wl_External = models.CharField(max_length=50, verbose_name='Wall External Rotation w/RB', blank=True,
                                           null=True)
    rnd_frc_Press = models.CharField(max_length=50, verbose_name='Press and Reach w/RB', blank=True, null=True)
    rnd_frc_Elbow = models.CharField(max_length=50, verbose_name='Elbow Down Dog', blank=True, null=True)
    rnd_frc_YRaise = models.CharField(max_length=50, verbose_name='‘’Y’’ Raise on Bench', blank=True, null=True)
    rnd_frc_Scaption = models.CharField(max_length=50, verbose_name='Scaption (90-180)', blank=True, null=True)
    rnd_frc_TS = models.CharField(max_length=50, verbose_name='T’s Thumbs Up', blank=True, null=True)
    rnd_frc_WA = models.CharField(max_length=50, verbose_name='W-A', blank=True, null=True)
    rnd_frc_Swissball = models.CharField(max_length=50, verbose_name='Swissball/Foamroller Prayer', blank=True,
                                         null=True)
    rnd_frc_External = models.CharField(max_length=50, verbose_name='External Ball Roll Ups', blank=True, null=True)
    rnd_frc_Lateral = models.CharField(max_length=50, verbose_name='Lateral Ball Circless', blank=True, null=True)
    rnd_frc_Walkout = models.CharField(max_length=50, verbose_name='Walkout + Uppercut with Rotation', blank=True,
                                       null=True)
    rnd_frc_High = models.CharField(max_length=50, verbose_name='High Plank Walk Ups', blank=True, null=True)
    rnd_frc_sd_Rotation = models.CharField(max_length=50, verbose_name='Side Plank Rotation w/KB', blank=True,
                                           null=True)
    rnd_frc_Pulsing = models.CharField(max_length=50, verbose_name='Pulsing Overhead Reach', blank=True, null=True)
    rnd_frc_Rollout = models.CharField(max_length=50, verbose_name='Rollout and Thoracic Rotation w/Foam Roller',
                                       blank=True, null=True)
    rnd_frc_Bench = models.CharField(max_length=50, verbose_name='Bench Overhead Stretch (Mobil)', blank=True,
                                     null=True)
    rnd_frc_Band = models.CharField(max_length=50, verbose_name='Band Pull Apart', blank=True, null=True)
    rnd_frc_stdn_Reach = models.CharField(max_length=50, verbose_name='Standing External Rotation and Reach w/RB',
                                          blank=True, null=True)
    rnd_frc_PushUp = models.CharField(max_length=50, verbose_name='Push Up Pose Latera Tap w/RBl', blank=True,
                                      null=True)
    rnd_frc_Alternating = models.CharField(max_length=50, verbose_name='Alternating Diagonal', blank=True, null=True)
    rnd_frc_Abduction = models.CharField(max_length=50, verbose_name='Abduction Arcs', blank=True, null=True)
    rnd_frc_Internal90 = models.CharField(max_length=50, verbose_name='90/90 İnternal Rotation', blank=True, null=True)
    rnd_frc_External90 = models.CharField(max_length=50, verbose_name='90/90 External Rotation', blank=True, null=True)
    rnd_frc_prn_Snow = models.CharField(max_length=50, verbose_name='Prone Snow Angel', blank=True, null=True)
    rnd_frc_OneArm = models.CharField(max_length=50, verbose_name='One Arm Overhead Lift  Off w/Foam Roller',
                                      blank=True, null=True)
    rnd_frc_Shoulder = models.CharField(max_length=50, verbose_name='Shoulder Flexion- AAROM w/Dowel', blank=True,
                                        null=True)
    rnd_frc_sp_Arm = models.CharField(max_length=50, verbose_name='Supine Pose Extended Arm Shoulder Extension',
                                      blank=True, null=True)
    rnd_frc_sp_External = models.CharField(max_length=50, verbose_name='Supine Pose Shoulder External Rotation',
                                           blank=True, null=True)
    rnd_frc_sp_Internal = models.CharField(max_length=50, verbose_name='Supine Pose Shoulder Internal Rotation',
                                           blank=True, null=True)
    rnd_frc_stdn_Dowelqq = models.CharField(max_length=50, verbose_name='Standing External Rotation w/Dowel',
                                            blank=True, null=True)

    class Meta:
        verbose_name = 'Düzeltici Egzersiz Reçetesi'
        verbose_name_plural = 'Düzeltici Egzersiz Reçetesi'


class corrective_exercise4(models.Model):
    # PROTRACTED / SMR
    prt_smr_sd_Foam = models.CharField(max_length=50, verbose_name='Side Back Glide w/Foam Roller', blank=True,
                                       null=True)
    prt_smr_sd_Mini = models.CharField(max_length=50, verbose_name='Side Back Glide w/Mini Ball', blank=True, null=True)
    prt_smr_Supine = models.CharField(max_length=50, verbose_name='Supine Pose T-Spine Glide w/Foam Roller', blank=True,
                                      null=True)
    prt_smr_stn_Mini = models.CharField(max_length=50, verbose_name='Standing T- Spine Glide w/Mini Ball', blank=True,
                                        null=True)
    prt_smr_stn_Foam = models.CharField(max_length=50, verbose_name='Standing T-Spine Glide w/Foam Roll', blank=True,
                                        null=True)
    prt_smr_tsp_Glide = models.CharField(max_length=50, verbose_name='T- Spine Glide on Longitudinal Foam Roller',
                                         blank=True, null=True)
    prt_smr_tsp_Cross = models.CharField(max_length=50, verbose_name='T-Spine Cross Friction', blank=True, null=True)
    # STRETCHING
    prt_str_Bench = models.CharField(max_length=50, verbose_name='Bench Overhead Stretch', blank=True, null=True)
    prt_str_Foam = models.CharField(max_length=50, verbose_name='Foam Roller Prayer Stretch', blank=True, null=True)
    prt_str_Swiss = models.CharField(max_length=50, verbose_name='Swiss Ball Prayer', blank=True, null=True)
    prt_str_OneArm = models.CharField(max_length=50, verbose_name='One-Arm Extended Stretch', blank=True, null=True)
    prt_str_Over = models.CharField(max_length=50, verbose_name='Over Head-Arm Vertical Extension', blank=True,
                                    null=True)
    prt_str_Quadruped = models.CharField(max_length=50, verbose_name='Quadruped Prayer Stretch', blank=True, null=True)
    prt_str_Wall = models.CharField(max_length=50, verbose_name='Wall Support Thoracic Flexion', blank=True, null=True)
    prt_str_Standing = models.CharField(max_length=50, verbose_name='Standing Neck and Trunk Flexio', blank=True,
                                        null=True)
    prt_str_Forward = models.CharField(max_length=50, verbose_name='Forward Arm Extension', blank=True, null=True)
    prt_str_Crossing = models.CharField(max_length=50, verbose_name='Crossing The Arms Behind The Back', blank=True,
                                        null=True)
    prt_str_Lying = models.CharField(max_length=50, verbose_name='Lying on Bench Ext. Rotation', blank=True, null=True)
    prt_str_Seated = models.CharField(max_length=55, verbose_name='Seated Shoulder Flexor Depressor Retractor Stretch',
                                      blank=True, null=True)
    # FORCE
    prt_frc_shld_Walk = models.CharField(max_length=50, verbose_name='Shoulder Internal Rotation Walk Out', blank=True,
                                         null=True)
    prt_frc_shld_Band = models.CharField(max_length=50, verbose_name='Shoulder Internal Rotation w/Band', blank=True,
                                         null=True)
    prt_frc_prn_Shoulder = models.CharField(max_length=50, verbose_name='Prone Shoulder Internal Rotation ', blank=True,
                                            null=True)
    prt_frc_Shoulder = models.CharField(max_length=50, verbose_name='Shoulder 90/90  Internal Rotation w/Band',
                                        blank=True, null=True)
    prt_frc_plnk_Foam = models.CharField(max_length=50, verbose_name='Plank Foam Roller Glide w/RB', blank=True,
                                         null=True)
    prt_frc_bnd_Bear = models.CharField(max_length=50, verbose_name='Banded Bear Hugs (Cover Slide)', blank=True,
                                        null=True)
    prt_frc_bnd_Punches = models.CharField(max_length=50, verbose_name='Banded Punches', blank=True, null=True)
    prt_frc_bnd_Uppercuts = models.CharField(max_length=50, verbose_name='Banded Uppercuts', blank=True, null=True)
    prt_frc_Scaption = models.CharField(max_length=50, verbose_name='Scaption Raises (to  1200 or more)', blank=True,
                                        null=True)
    prt_frc_srt_Foam = models.CharField(max_length=50, verbose_name='Serratus Foam Roll Wall  Slides w/Band',
                                        blank=True, null=True)
    prt_frc_Chest = models.CharField(max_length=50, verbose_name='Chest Press Plus', blank=True, null=True)
    prt_frc_Landmine = models.CharField(max_length=50, verbose_name='Landmine Press Plus', blank=True, null=True)
    prt_frc_Dolphin = models.CharField(max_length=50, verbose_name='Dolphin Press', blank=True, null=True)
    prt_frc_PushUp = models.CharField(max_length=50, verbose_name='Push-Up Plus to Down Dog', blank=True, null=True)
    prt_frc_Single = models.CharField(max_length=50, verbose_name='Single-arm Elevated Serratus Press', blank=True,
                                      null=True)
    prt_frc_prn_Arm = models.CharField(max_length=50, verbose_name='Prone Arm Behind Neck Shoulder Ext. Rotation',
                                       blank=True, null=True)
    prt_frc_Quadruped = models.CharField(max_length=50, verbose_name='Quadruped Pose Extended Arm and Lift', blank=True,
                                         null=True)
    prt_frc_stdn_TS = models.CharField(max_length=50, verbose_name='Standing T’s w/Band', blank=True, null=True)
    prt_frc_stdn_AS = models.CharField(max_length=50, verbose_name='Standing A’s w/Band', blank=True, null=True)
    prt_frc_stdn_YS = models.CharField(max_length=50, verbose_name='Standing Y’s w/Band', blank=True, null=True)
    prt_frc_bnt_WS = models.CharField(max_length=50, verbose_name='Bent Over W’', blank=True, null=True)
    prt_frc_bnt_YS = models.CharField(max_length=50, verbose_name='Bent Over Y’', blank=True, null=True)
    prt_frc_dwl_Thoracic = models.CharField(max_length=50, verbose_name='Dowel Thoracic Rotation', blank=True,
                                            null=True)
    prt_frc_dwl_Pullover = models.CharField(max_length=50, verbose_name='Dowel Pullover', blank=True, null=True)
    prt_frc_dwl_Floor = models.CharField(max_length=50, verbose_name='Dowel Floor Swipers', blank=True, null=True)
    prt_frc_qd_Scapular = models.CharField(max_length=50, verbose_name='Quad Pose Scapular Prot', blank=True, null=True)
    prt_frc_Rock = models.CharField(max_length=50, verbose_name='Rock From Side to', blank=True, null=True)
    prt_frc_Wrist = models.CharField(max_length=50, verbose_name='Wrist Push-Up', blank=True, null=True)
    prt_frc_dwl_Press = models.CharField(max_length=50, verbose_name='Dowel Z Press', blank=True, null=True)
    prt_frc_Overhead = models.CharField(max_length=50, verbose_name='Overhead Shrugs', blank=True, null=True)
    prt_frc_prn_Dowel = models.CharField(max_length=50, verbose_name='Prone Dowel Press', blank=True, null=True)
    prt_frc_qd_Single = models.CharField(max_length=50, verbose_name='Quad Pose Single Arm Scapular Punch', blank=True,
                                         null=True)
    prt_frc_srt_Hops = models.CharField(max_length=50, verbose_name='Serratus Hops', blank=True, null=True)
    prt_frc_prn_Scapular = models.CharField(max_length=50, verbose_name='Prone Scapular Squeezes', blank=True,
                                            null=True)
    prt_frc_prn_Chicken = models.CharField(max_length=50, verbose_name='Prone Chicken Wings ', blank=True, null=True)
    prt_frc_prn_W = models.CharField(max_length=50, verbose_name='Prone W', blank=True, null=True)
    prt_frc_prn_T = models.CharField(max_length=50, verbose_name='Prone T', blank=True, null=True)
    prt_frc_Advanced = models.CharField(max_length=50, verbose_name='Advanced Prone T', blank=True, null=True)
    prt_frc_srt_Slider = models.CharField(max_length=50, verbose_name='Serratus Slider in Bear Position', blank=True,
                                          null=True)
    prt_frc_Weighted = models.CharField(max_length=50, verbose_name='Weighted Serratus Reach', blank=True, null=True)
    prt_frc_plnk_Walk = models.CharField(max_length=50, verbose_name='Plank Walk Overs', blank=True, null=True)
    prt_frc_prn_WRow = models.CharField(max_length=50, verbose_name='Prone W’Row w/Band', blank=True, null=True)
    # FORWARD / SMR
    frwd_smr_nck_Extensor = models.CharField(max_length=50, verbose_name='Neck Extensor Release Variation', blank=True,
                                             null=True)
    frwd_smr_nck_Rotator = models.CharField(max_length=50, verbose_name='Neck Rotator Release Variation', blank=True,
                                            null=True)
    frwd_smr_Half = models.CharField(max_length=50, verbose_name='Half Standing Shoulder Release', blank=True,
                                     null=True)
    frwd_smr_Standing = models.CharField(max_length=50, verbose_name='Standing Thoracic Release', blank=True, null=True)
    frwd_smr_Suboccipital = models.CharField(max_length=50, verbose_name='Suboccipital Release', blank=True, null=True)
    frwd_smr_thrc_Extension = models.CharField(max_length=50, verbose_name='Thoracic Extension Release', blank=True,
                                               null=True)
    frwd_smr_thrc_Lateral = models.CharField(max_length=50, verbose_name='Thoracic Lateral Extension Release',
                                             blank=True, null=True)
    frwd_smr_thrc_Kneeling = models.CharField(max_length=50, verbose_name='Thoracic Mobility Kneeling Roll Release',
                                              blank=True, null=True)
    frwd_smr_thrc_Rolling = models.CharField(max_length=50, verbose_name='Thoracic Mobility Rolling Release',
                                             blank=True, null=True)
    frwd_smr_thrc_Standing = models.CharField(max_length=50, verbose_name='Thoracic Mobility Standing Roll Release',
                                              blank=True, null=True)
    frwd_smr_thrc_Variation1 = models.CharField(max_length=50, verbose_name='Thoracic Mobility Release Variation 1',
                                                blank=True, null=True)
    frwd_smr_thrc_Variation2 = models.CharField(max_length=50, verbose_name='Thoracic Mobility Release Variation 2',
                                                blank=True, null=True)
    frwd_smr_thrc_Variation3 = models.CharField(max_length=50, verbose_name='Thoracic Mobility Release Variation 3',
                                                blank=True, null=True)
    frwd_smr_thrc_Rotation = models.CharField(max_length=50, verbose_name='Thoracic Rotation Release', blank=True,
                                              null=True)
    frwd_smr_Posterior = models.CharField(max_length=50, verbose_name='Posterior Dynamic Release', blank=True,
                                          null=True)
    frwd_smr_Weighted = models.CharField(max_length=50, verbose_name='Weighted Thoracic Extension Release', blank=True,
                                         null=True)
    # STRETCHING
    frwd_str_crv_Extensors = models.CharField(max_length=50, verbose_name='Cervical Extensors Stretch', blank=True,
                                              null=True)
    frwd_str_crv_Flexor = models.CharField(max_length=50, verbose_name='Cervical Flexor Stretch', blank=True, null=True)
    frwd_str_crv_Lateral = models.CharField(max_length=50, verbose_name='Cervical Lateral Flexor Stretch', blank=True,
                                            null=True)
    frwd_str_crv_Rotator1 = models.CharField(max_length=50, verbose_name='Cervical Rotator (Extensor) Stretch',
                                             blank=True, null=True)
    frwd_str_crv_Rotator2 = models.CharField(max_length=50, verbose_name='Cervical Rotator (Flexor) Stretch',
                                             blank=True, null=True)
    frwd_str_Levator = models.CharField(max_length=50, verbose_name='Levator Scapula Stretch', blank=True, null=True)
    frwd_str_Anchor = models.CharField(max_length=50, verbose_name='Anchor Stretch (Scalene)', blank=True, null=True)
    frwd_str_Skalen = models.CharField(max_length=50, verbose_name='Skalen Stretch', blank=True, null=True)
    frwd_str_Chest = models.CharField(max_length=50, verbose_name='Chest Stretch', blank=True, null=True)
    frwd_str_Medial = models.CharField(max_length=50, verbose_name='Medial-Ulnar Stretch', blank=True, null=True)
    frwd_str_SCM = models.CharField(max_length=50, verbose_name='SCM Stretch', blank=True, null=True)
    frwd_str_up_Stretch = models.CharField(max_length=50, verbose_name='Upper Trapezius Stretch', blank=True, null=True)
    frwd_str_up_Cervical = models.CharField(max_length=50, verbose_name='Upper Trapezius Stretch w/Cervical Rotation',
                                            blank=True, null=True)
    frwd_str_Dynamic = models.CharField(max_length=50, verbose_name='Dynamic Thoracic Extension Stretch', blank=True,
                                        null=True)
    # FORCE
    frwd_frc_arm_H = models.CharField(max_length=50, verbose_name='Arm H Raise w/Banded', blank=True, null=True)
    frwd_frc_arm_Raise = models.CharField(max_length=50, verbose_name='Arm Raise w/Banded', blank=True, null=True)
    frwd_frc_arm_YRaise = models.CharField(max_length=50, verbose_name='Arm Y Raise', blank=True, null=True)
    frwd_frc_arm_TRaise = models.CharField(max_length=50, verbose_name='Arm Y to T Raise', blank=True, null=True)
    frwd_frc_arm_WRaise = models.CharField(max_length=50, verbose_name='Arm Y to W Raise', blank=True, null=True)
    frwd_frc_Bilateral = models.CharField(max_length=60,
                                          verbose_name='Bilateral Extension Rotation w/Banded in Plank Position',
                                          blank=True, null=True)
    frwd_frc_crv_Extension = models.CharField(max_length=50, verbose_name='Cervical Extension', blank=True, null=True)
    frwd_frc_crv_Isometric = models.CharField(max_length=50, verbose_name='Cervical Extension Isometric', blank=True,
                                              null=True)
    frwd_frc_crv_Banded = models.CharField(max_length=50, verbose_name='Cervical Extension w/Banded', blank=True,
                                           null=True)
    frwd_frc_Straight = models.CharField(max_length=50, verbose_name='Straight Arm Cervical Extension w/Banded',
                                         blank=True, null=True)
    frwd_frc_crv_Flexion = models.CharField(max_length=50, verbose_name='Cervical Flexion', blank=True, null=True)
    frwd_frc_crv_IsFlexion = models.CharField(max_length=50, verbose_name='Cervical Isometric Flexion', blank=True,
                                              null=True)
    frwd_frc_crv_flxBanded = models.CharField(max_length=50, verbose_name='Cervical Flexion w/Banded', blank=True,
                                              null=True)
    frwd_frc_crv_Arm = models.CharField(max_length=50, verbose_name='Straight Arm Cervical Lateral Flexion w/Banded',
                                        blank=True, null=True)
    frwd_frc_crv_LtrFlexion = models.CharField(max_length=50, verbose_name='Cervical Lateral Flexion', blank=True,
                                               null=True)
    frwd_frc_crv_LtrIsometric = models.CharField(max_length=50, verbose_name='Cervical Lateral Flexion Isometric',
                                                 blank=True, null=True)
    frwd_frc_crv_LtrBanded = models.CharField(max_length=50, verbose_name='Cervical Lateral Flexion w/Banded',
                                              blank=True, null=True)
    frwd_frc_crv_Rotation = models.CharField(max_length=50, verbose_name='Cervical Rotation', blank=True, null=True)
    frwd_frc_crv_RtIsometric = models.CharField(max_length=50, verbose_name='Cervical Rotation Isometric', blank=True,
                                                null=True)
    frwd_frc_crv_RtBanded = models.CharField(max_length=50, verbose_name='Cervical Rotation w/Banded', blank=True,
                                             null=True)
    frwd_frc_wll_Cervical = models.CharField(max_length=50, verbose_name='Wall Cervical Rotation w/Softball',
                                             blank=True, null=True)
    frwd_frc_Chin = models.CharField(max_length=50, verbose_name='Chin Nods', blank=True, null=True)
    frwd_frc_prn_Tuck = models.CharField(max_length=50, verbose_name='Prone Chin Tuck', blank=True, null=True)
    frwd_frc_prn_Isometric = models.CharField(max_length=50, verbose_name='Prone Chin Tuck Isometric', blank=True,
                                              null=True)
    frwd_frc_prn_Banded = models.CharField(max_length=50, verbose_name='Prone Chin Tuck w/Banded', blank=True,
                                           null=True)
    frwd_frc_prn_YW = models.CharField(max_length=50, verbose_name='Prone Y – W Raise', blank=True, null=True)
    frwd_frc_qd_Tuck = models.CharField(max_length=50, verbose_name='Quadruped Chin Tuck', blank=True, null=True)
    frwd_frc_qd_Banded = models.CharField(max_length=50, verbose_name='Quadruped Chin Tuck w/Banded', blank=True,
                                          null=True)
    frwd_frc_qd_Cervical = models.CharField(max_length=50, verbose_name='Quadruped Chin Tuck w/Cervical Rotation',
                                            blank=True, null=True)
    frwd_frc_std_Isometric = models.CharField(max_length=50, verbose_name='Seated Chin Tuck Isometric', blank=True,
                                              null=True)
    frwd_frc_std_Banded = models.CharField(max_length=50, verbose_name='Seated Chin Tuck w/Banded', blank=True,
                                           null=True)
    frwd_frc_wll_Chin = models.CharField(max_length=50, verbose_name='Wall Chin Tuck', blank=True, null=True)
    frwd_frc_nck_Endurance = models.CharField(max_length=50, verbose_name='Neck Flexion Isometric Endurance',
                                              blank=True, null=True)
    frwd_frc_Supine = models.CharField(max_length=50, verbose_name='Supine Chin Tuck w/Hold', blank=True, null=True)
    frwd_frc_Middle = models.CharField(max_length=50, verbose_name='Middle Back Mobility', blank=True, null=True)
    frwd_frc_Shoulder = models.CharField(max_length=50, verbose_name='Shoulder Abduction w/Banded', blank=True,
                                         null=True)
    frwd_frc_sd_External = models.CharField(max_length=50, verbose_name='Side Lying External Rotation', blank=True,
                                            null=True)
    frwd_frc_sd_Thoracic = models.CharField(max_length=50, verbose_name='Side Lying Thoracic Rotation', blank=True,
                                            null=True)
    frwd_frc_thrc_Resisted = models.CharField(max_length=50,
                                              verbose_name='Thoracic Mobility Resisted Middle Back Mobility',
                                              blank=True, null=True)
    frwd_frc_thrc_Rolling = models.CharField(max_length=50, verbose_name='Thoracic Mobility Rolling w/Banded',
                                             blank=True, null=True)
    frwd_frc_thrc_Twist1 = models.CharField(max_length=50, verbose_name='Thoracic Mobility Wall Twist w/Banded',
                                            blank=True, null=True)
    frwd_frc_thrc_Twist2 = models.CharField(max_length=50, verbose_name='Thoracic Mobility Wall Twist', blank=True,
                                            null=True)
    frwd_frc_Banded = models.CharField(max_length=50, verbose_name='Banded Row', blank=True, null=True)
    frwd_frc_crvc_Extension = models.CharField(max_length=50, verbose_name='Cervical Extension on/Stability',
                                               blank=True, null=True)
    frwd_frc_crvc_Flexion = models.CharField(max_length=50, verbose_name='Cervical Flexion/Extension', blank=True,
                                             null=True)
    frwd_frc_ch_Horizontal = models.CharField(max_length=50, verbose_name='Chin Tuck + Horizontal Abduction',
                                              blank=True, null=True)
    frwd_frc_ch_Prone = models.CharField(max_length=50, verbose_name='Chin Tuck + Prone W', blank=True, null=True)
    frwd_frc_ch_Towel = models.CharField(max_length=50, verbose_name='Chin Tuck on Towel', blank=True, null=True)
    frwd_frc_dghr_Breathing1 = models.CharField(max_length=50, verbose_name='Diaghram Breathing w/Kettlebell-1',
                                                blank=True, null=True)
    frwd_frc_dghr_Breathing2 = models.CharField(max_length=50, verbose_name='Diaghram Breathing w/Kettlebell-2',
                                                blank=True, null=True)
    frwd_frc_dghr_Breathing3 = models.CharField(max_length=50, verbose_name='Diaghram Breathing-1', blank=True,
                                                null=True)
    frwd_frc_dghr_Breathing4 = models.CharField(max_length=50, verbose_name='Diaghram Breathing-2', blank=True,
                                                null=True)
    frwd_frc_Dynamic = models.CharField(max_length=50, verbose_name='Dynamic Retraction', blank=True, null=True)
    frwd_frc_Elevated = models.CharField(max_length=50, verbose_name='Elevated Neck Bridge', blank=True, null=True)
    frwd_frc_Inverted = models.CharField(max_length=50, verbose_name='Inverted Row', blank=True, null=True)
    frwd_frc_Low = models.CharField(max_length=50, verbose_name='Low Trap Lift w/Chin Tuck', blank=True, null=True)
    frwd_frc_Lower = models.CharField(max_length=50, verbose_name='Lower Trap Strength + Thoracic Extension',
                                      blank=True, null=True)
    frwd_frc_Lunge = models.CharField(max_length=50, verbose_name='Lunge Reverse Woodchops', blank=True, null=True)
    frwd_frc_Modified = models.CharField(max_length=50, verbose_name='Modified Prone Swimmers', blank=True, null=True)
    frwd_frc_nck_Flexor = models.CharField(max_length=50, verbose_name='Neck Flexor Isometrics', blank=True, null=True)
    frwd_frc_nck_Retraction = models.CharField(max_length=50, verbose_name='Neck Retraction Strength', blank=True,
                                               null=True)
    frwd_frc_nck_Rotation = models.CharField(max_length=50, verbose_name='Neck Rotation w/Retraction', blank=True,
                                             null=True)
    frwd_frc_prn_Divers = models.CharField(max_length=50, verbose_name='Prone Divers', blank=True, null=True)
    frwd_frc_prn_Retraction = models.CharField(max_length=50, verbose_name='Prone Retraction w/Arm  90/90', blank=True,
                                               null=True)
    frwd_frc_prn_Scapular = models.CharField(max_length=50, verbose_name='Prone Scapular + Cervical Retraction',
                                             blank=True, null=True)
    frwd_frc_shld_Mobility1 = models.CharField(max_length=50, verbose_name='Shoulder Mobility-1', blank=True, null=True)
    frwd_frc_shld_Mobility2 = models.CharField(max_length=50, verbose_name='Shoulder Mobility-2', blank=True, null=True)
    frwd_frc_sd_Lateral = models.CharField(max_length=50, verbose_name='Side Lying Lateral Flexor Curl', blank=True,
                                           null=True)
    frwd_frc_sd_Rotations = models.CharField(max_length=50, verbose_name='Side Lying Rotations', blank=True, null=True)
    frwd_frc_stdn_Lateral = models.CharField(max_length=50, verbose_name='Standing Lateral Flexion Isometric',
                                             blank=True, null=True)
    frwd_frc_stdn_Row = models.CharField(max_length=50, verbose_name='Standing Row', blank=True, null=True)
    frwd_frc_stdn_Stability = models.CharField(max_length=50, verbose_name='Standing Stability Ball Isometric',
                                               blank=True, null=True)
    frwd_frc_stdn_T = models.CharField(max_length=50, verbose_name='Standing T', blank=True, null=True)
    frwd_frc_stdn_Y = models.CharField(max_length=50, verbose_name='Standing Y', blank=True, null=True)
    frwd_frc_wll_Angels = models.CharField(max_length=50, verbose_name='Wall Angels w/Chin Tuck', blank=True, null=True)

    class Meta:
        verbose_name = 'Düzeltici Egzersiz Reçetesi'
        verbose_name_plural = 'Düzeltici Egzersiz Reçetesi'


class corrective_exercise(models.Model):
    trainer = models.ForeignKey(to=Trainer, verbose_name="Antrenör", on_delete=models.CASCADE, blank=True, null=True)
    personal = models.ForeignKey(to=Personal, verbose_name="Danışan", on_delete=models.CASCADE, blank=True, null=True)
    corrective2 = models.ForeignKey(to=corrective_exercise2, verbose_name="Düzeltici 2", on_delete=models.CASCADE, blank=True, null=True)
    corrective3 = models.ForeignKey(to=corrective_exercise3, verbose_name="Düzeltici 3", on_delete=models.CASCADE, blank=True, null=True)
    corrective4 = models.ForeignKey(to=corrective_exercise4, verbose_name="Düzeltici 4", on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(("Date"), default=datetime.now(), blank=True)
    person_level = models.CharField(max_length=50, verbose_name='Kişinin Düzeyini Belirle', blank=True, null=True)
    # Düzeltici Egzersiz/Amaç belirleem
    forward1 = models.CharField(max_length=50, verbose_name='Forward Head Posture', blank=True, null=True)
    servikal1 = models.CharField(max_length=50, verbose_name='Servikal Lordoz Artışı', blank=True, null=True)
    round1 = models.CharField(max_length=50, verbose_name='Round Shoulder Sendromu', blank=True, null=True)
    elevated1 = models.CharField(max_length=50, verbose_name='Elevated Scapula Sendromu', blank=True, null=True)
    protracted1 = models.CharField(max_length=50, verbose_name='Protracted Scapula Sendromu', blank=True, null=True)
    internal1 = models.CharField(max_length=50, verbose_name='Internal Arm Sendromu', blank=True, null=True)
    torakal1 = models.CharField(max_length=50, verbose_name='Torakal Kifoz Artışı', blank=True, null=True)
    lomber1 = models.CharField(max_length=50, verbose_name='Lomber Lordoz Artışı', blank=True, null=True)
    anterior1 = models.CharField(max_length=50, verbose_name='Anterior Pelvik Tilt Sendromu', blank=True, null=True)
    genu1 = models.CharField(max_length=50, verbose_name='Genu Valgus Sendromu', blank=True, null=True)
    dorsi1 = models.CharField(max_length=50, verbose_name='Dorsi-fleksiyon Kaybı', blank=True, null=True)
    over1 = models.CharField(max_length=50, verbose_name='Over-pronasyon Sendromu', blank=True, null=True)
    # Gün sayısı
    monday = models.CharField(max_length=50, verbose_name='Pazartesi', blank=True, null=True)
    tuesday = models.CharField(max_length=50, verbose_name='Salı', blank=True, null=True)
    wednesday = models.CharField(max_length=50, verbose_name='Çarşamba', blank=True, null=True)
    thursday = models.CharField(max_length=50, verbose_name='Perşembe', blank=True, null=True)
    friday = models.CharField(max_length=50, verbose_name='Cuma', blank=True, null=True)
    saturday = models.CharField(max_length=50, verbose_name='Cumartesi', blank=True, null=True)
    sunday = models.CharField(max_length=50, verbose_name='Pazar', blank=True, null=True)
    train_time = models.CharField(max_length=20, verbose_name="Antrenman Süresi Belirle", blank=True, null=True)
    set_number1 = models.CharField(max_length=5, verbose_name="Set Sayısı", blank=True, null=True)
    over_number1 = models.CharField(max_length=5, verbose_name="Tekrar Sayısı", blank=True, null=True)
    tempo1 = models.CharField(max_length=10, verbose_name="Tempo (TUT)", blank=True, null=True)
    # Setler arası dinlenme
    sets_between1 = models.CharField(max_length=10, verbose_name="Setler Arası Dinlenme", blank=True, null=True)
    move_between1 = models.CharField(max_length=10, verbose_name="Hareketler Arası Dinlenme", blank=True, null=True)
    exercise_file = models.CharField(max_length=20, verbose_name="Egzersiz Reçetesi Dosyası", blank=True, null=True)
    # OVERPRONASYON/SMR
    ovr_smr_Mini = models.CharField(max_length=50, verbose_name='Bottom of Foot Glide w/Mini Ball', blank=True,
                                    null=True)
    ovr_smr_Foam = models.CharField(max_length=50, verbose_name='Bottom of Foot Glide w/Foam Roller', blank=True,
                                    null=True)
    ovr_smr_Bottom = models.CharField(max_length=50, verbose_name='Seated Bottom of Foot Glide w/Miniball-Foam Roller',
                                      blank=True, null=True)
    ovr_smr_OneStraight = models.CharField(max_length=50, verbose_name='One-Straight Leg T.A SMR w/Foam Roller',
                                           blank=True, null=True)
    ovr_smr_TA = models.CharField(max_length=50, verbose_name='Seated T.A. SMR w/Mini Ball', blank=True, null=True)
    ovr_smr_Alternating = models.CharField(max_length=50, verbose_name='Alternating T.A SMR w/Foam Roller', blank=True,
                                           null=True)
    ovr_smr_crs_TA = models.CharField(max_length=50, verbose_name='Cross Leg T.A. SMR w/Foam Roller', blank=True,
                                      null=True)
    ovr_smr_OneLeg = models.CharField(max_length=50, verbose_name='One-Leg Calf SMR w/Foam Roller', blank=True,
                                      null=True)
    ovr_smr_crs_Calf = models.CharField(max_length=50, verbose_name='Cross Leg Calf SMR w/Foam Roller', blank=True,
                                        null=True)
    ovr_smr_Two = models.CharField(max_length=50, verbose_name='Two Leg On Foam Roller Calf SMR', blank=True, null=True)
    ovr_smr_Calf = models.CharField(max_length=50, verbose_name='Calf SMR W/Mini', blank=True, null=True)
    # STRETCHING
    ovr_str_Bear = models.CharField(max_length=50, verbose_name='Bear Position Big Toe Stretch', blank=True, null=True)
    ovr_str_Foot = models.CharField(max_length=50, verbose_name='Foot on Wall Calf Stretch', blank=True, null=True)
    ovr_str_Quadruped = models.CharField(max_length=50, verbose_name='Quadruped Rock Back - Big Toe Ext. Bias',
                                         blank=True, null=True)
    ovr_str_std_Extensor1 = models.CharField(max_length=50, verbose_name='Seated Toe Extensor Stretch', blank=True,
                                             null=True)
    ovr_str_std_Extensor2 = models.CharField(max_length=50, verbose_name='Seated Toe Extensor and Foot Everter Stretch',
                                             blank=True, null=True)
    ovr_str_std_Extensor3 = models.CharField(max_length=50,
                                             verbose_name='Seated Toe Extensor and Foot Inverter Stretch', blank=True,
                                             null=True)
    ovr_str_std_Flexor1 = models.CharField(max_length=50, verbose_name='Seated Toe Flexor Stretch ', blank=True,
                                           null=True)
    ovr_str_std_Flexor2 = models.CharField(max_length=50, verbose_name='Seated Toe Flexor and Foot Everter Stretch',
                                           blank=True, null=True)
    ovr_str_std_Flexor3 = models.CharField(max_length=50, verbose_name='Seated Toe Flexor and Foot Inverter Stretch',
                                           blank=True, null=True)
    ovr_str_Standing = models.CharField(max_length=50, verbose_name='Standing Toe Extensor Stretch', blank=True,
                                        null=True)
    ovr_str_Single = models.CharField(max_length=50, verbose_name='Single Plantar Flexor Stretch', blank=True,
                                      null=True)
    # FORCE
    ovr_frc_Isometric = models.CharField(max_length=50, verbose_name='Isometric March on Heel', blank=True, null=True)
    ovr_frc_dr_Taps = models.CharField(max_length=50, verbose_name='Dorsiflexor Taps', blank=True, null=True)
    ovr_frc_dr_Curl = models.CharField(max_length=50, verbose_name='Dorsiflexor Curl w/Band', blank=True, null=True)
    ovr_frc_Deep = models.CharField(max_length=50, verbose_name='Deep Squat & Ankle Mobility', blank=True, null=True)
    ovr_frc_Standing = models.CharField(max_length=50, verbose_name='Standing Unilateral Knee Extension', blank=True,
                                        null=True)
    ovr_frc_Kneeling = models.CharField(max_length=50, verbose_name='½ Kneeling Dorsiflexion', blank=True, null=True)
    ovr_frc_Unilateral = models.CharField(max_length=50, verbose_name='Unilateral Heel Drops', blank=True, null=True)
    ovr_frc_Posterior = models.CharField(max_length=50, verbose_name='Posterior Bounce  and Touch Down', blank=True,
                                         null=True)
    ovr_frc_Lateral = models.CharField(max_length=50, verbose_name='Lateral Bounce  and Touch Down', blank=True,
                                       null=True)
    ovr_frc_OneLeg = models.CharField(max_length=50, verbose_name='One Leg Rotational Stability', blank=True, null=True)
    ovr_frc_Ankle = models.CharField(max_length=50, verbose_name='Ankle Lift and Forward Step', blank=True, null=True)
    ovr_frc_Calf = models.CharField(max_length=50, verbose_name='Calf Raise', blank=True, null=True)
    ovr_frc_elv_Calf = models.CharField(max_length=50, verbose_name='Elevated Calf Raise', blank=True, null=True)
    ovr_frc_sngl_Elevated = models.CharField(max_length=50, verbose_name='Single Leg Elevated Calf Raise', blank=True,
                                             null=True)
    ovr_frc_Active = models.CharField(max_length=50, verbose_name='Active Calf Rolling w/Foam Roller', blank=True,
                                      null=True)
    ovr_frc_sngl_Reach = models.CharField(max_length=50, verbose_name='Single Reach with Band Feedback', blank=True,
                                          null=True)
    ovr_frc_Bent = models.CharField(max_length=50, verbose_name='Bent Knee Heel Raises w/Ball', blank=True, null=True)
    ovr_frc_sngl_Passes = models.CharField(max_length=50, verbose_name='Single Leg Passes on Foam', blank=True,
                                           null=True)
    ovr_frc_Banded = models.CharField(max_length=50, verbose_name='Banded Inversion', blank=True, null=True)
    ovr_frc_Toe = models.CharField(max_length=50, verbose_name='Toe Raise', blank=True, null=True)
    ovr_frc_elv_Hallucis = models.CharField(max_length=50, verbose_name='Elevated Hallucis Flexion', blank=True,
                                            null=True)
    ovr_frc_Bear = models.CharField(max_length=50, verbose_name='Bear Position Big Toe Stretch (Mobil)', blank=True,
                                    null=True)
    ovr_frc_ft_Wall = models.CharField(max_length=50, verbose_name='Foot on Wall Calf Stretch (Mobil)', blank=True,
                                       null=True)
    ovr_frc_Quadruped = models.CharField(max_length=50, verbose_name='Quadruped Rock Back- Big Toe Ext. Bias',
                                         blank=True, null=True)
    ovr_frc_Sole = models.CharField(max_length=50, verbose_name='Sole to Sole', blank=True, null=True)
    ovr_frc_ft_ArchUp = models.CharField(max_length=50, verbose_name='Foot Arch-Up', blank=True, null=True)
    ovr_frc_sngl_ArchUp = models.CharField(max_length=50, verbose_name='Single Leg  Arch-Up', blank=True, null=True)
    ovr_frc_Clam = models.CharField(max_length=50, verbose_name='Clam Shells ', blank=True, null=True)
    ovr_frc_ToeTowel = models.CharField(max_length=50, verbose_name='Toe-Towel Flexion', blank=True, null=True)
    ovr_frc_ToSpread = models.CharField(max_length=50, verbose_name='Toe Spread', blank=True, null=True)
    ovr_frc_ToeObject = models.CharField(max_length=50, verbose_name='Toe-Object Pickup', blank=True, null=True)
    ovr_frc_Self = models.CharField(max_length=50, verbose_name='Self Big Toe Mobilization', blank=True, null=True)
    # DORSI / SMR
    drs_smr_OneStraight = models.CharField(max_length=50, verbose_name='One-Straight Leg T.A. SMR w/Foam Roller',
                                           blank=True, null=True)
    drs_smr_Seated = models.CharField(max_length=50, verbose_name='Seated T.A. SMR w/Mini Ball', blank=True, null=True)
    drs_smr_Alternating = models.CharField(max_length=50, verbose_name='Alternating T.A SMR w/Foam Roller', blank=True,
                                           null=True)
    drs_smr_Cross = models.CharField(max_length=50, verbose_name='Cross Leg T.A. SMR w/Foam Roller', blank=True,
                                     null=True)
    # STRETCHING
    drs_str_Bear = models.CharField(max_length=50, verbose_name='Bear Position Big Toe Stretch', blank=True, null=True)
    drs_str_Foot = models.CharField(max_length=50, verbose_name='Foot on Wall Calf Stretch', blank=True, null=True)
    drs_str_Quadruped = models.CharField(max_length=50, verbose_name='Quadruped Rock Back - Big Toe Ext. Bias',
                                         blank=True, null=True)
    drs_str_std_Extensor1 = models.CharField(max_length=50, verbose_name='Seated Toe Extensor Stretch', blank=True,
                                             null=True)
    drs_str_std_Extensor2 = models.CharField(max_length=50, verbose_name='Seated Toe Extensor and Foot Everter Stretch',
                                             blank=True, null=True)
    drs_str_std_Extensor3 = models.CharField(max_length=50,
                                             verbose_name='Seated Toe Extensor and Foot Inverter Stretch', blank=True,
                                             null=True)
    drs_str_std_Flexor1 = models.CharField(max_length=50, verbose_name='Seated Toe Flexor Stretch ', blank=True,
                                           null=True)
    drs_str_std_Flexor2 = models.CharField(max_length=50, verbose_name='Seated Toe Flexor and Foot Everter Stretch',
                                           blank=True, null=True)
    drs_str_std_Flexor3 = models.CharField(max_length=50, verbose_name='Seated Toe Flexor and Foot Inverter Stretch',
                                           blank=True, null=True)
    drs_str_Standing = models.CharField(max_length=50, verbose_name='Standing Toe Extensor Stretch', blank=True,
                                        null=True)
    drs_str_Single = models.CharField(max_length=50, verbose_name='Single Plantar Flexor Stretch', blank=True,
                                      null=True)
    # FORCE
    drs_frc_Isometric = models.CharField(max_length=50, verbose_name='Isometric March on Heel', blank=True, null=True)
    drs_frc_dr_Taps = models.CharField(max_length=50, verbose_name='Dorsiflexor Taps', blank=True, null=True)
    drs_frc_dr_Curl = models.CharField(max_length=50, verbose_name='Dorsiflexor Curl w/Band', blank=True, null=True)
    drs_frc_Deep = models.CharField(max_length=50, verbose_name='Deep Squat & Ankle Mobility', blank=True, null=True)
    drs_frc_Standing = models.CharField(max_length=50, verbose_name='Standing Unilateral Knee Extension', blank=True,
                                        null=True)
    drs_frc_Kneeling = models.CharField(max_length=50, verbose_name='½ Kneeling Dorsiflexion', blank=True, null=True)
    drs_frc_Unilateral = models.CharField(max_length=50, verbose_name='Unilateral Heel Drops', blank=True, null=True)
    drs_frc_Posterior = models.CharField(max_length=50, verbose_name='Posterior Bounce and Touch Down', blank=True,
                                         null=True)
    drs_frc_Lateral = models.CharField(max_length=50, verbose_name='Lateral Bounce and Touch Down', blank=True,
                                       null=True)
    drs_frc_OneLeg = models.CharField(max_length=50, verbose_name='One Leg Rotational Stability', blank=True, null=True)
    drs_frc_Ankle = models.CharField(max_length=50, verbose_name='Ankle Lift and  Forward Step', blank=True, null=True)
    drs_frc_Calf = models.CharField(max_length=50, verbose_name='Calf Raise', blank=True, null=True)
    drs_frc_elv_Calf = models.CharField(max_length=50, verbose_name='Elevated Calf Raise', blank=True, null=True)
    drs_frc_sngl_Elevated = models.CharField(max_length=50, verbose_name='Single Leg Elevated Calf Raise', blank=True,
                                             null=True)
    drs_frc_Active = models.CharField(max_length=50, verbose_name='Active Calf Rolling w/Foam Roller', blank=True,
                                      null=True)
    drs_frc_sngl_Reach = models.CharField(max_length=50, verbose_name='Single Reach with Band Feedback', blank=True,
                                          null=True)
    drs_frc_Bent = models.CharField(max_length=50, verbose_name='Bent Knee Heel Raises w/Ball', blank=True, null=True)
    drs_frc_sngl_Passes = models.CharField(max_length=50, verbose_name='Single Leg Passes on Foam', blank=True,
                                           null=True)
    drs_frc_Banded = models.CharField(max_length=50, verbose_name='Banded Inversion', blank=True, null=True)
    drs_frc_Toe = models.CharField(max_length=50, verbose_name='Toe Raise', blank=True, null=True)
    drs_frc_elv_Hallucis = models.CharField(max_length=50, verbose_name='Elevated Hallucis Flexion', blank=True,
                                            null=True)
    drs_frc_Bear = models.CharField(max_length=50, verbose_name='Bear Position Big Toe Stretch (Mobil)', blank=True,
                                    null=True)
    drs_frc_ft_Wall = models.CharField(max_length=50, verbose_name='Foot on Wall Calf Stretch (Mobil)', blank=True,
                                       null=True)
    drs_frc_Quadruped = models.CharField(max_length=50, verbose_name='Quadruped Rock Back-Big Toe Ext. Bias',
                                         blank=True, null=True)

    def get_absolute_url(self):
        return reverse('corrective-exercise-detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('corrective-exercise-update', kwargs={'id': self.id})

    def get_trainer_corrective_exercise_delete_url(self):
        return reverse('trainer-corrective_exercise-delete', kwargs={'id': self.id})

    def get_corporate_corrective_exercise_delete_url(self):
        return reverse('corporate-corrective_exercise-delete', kwargs={'id': self.id})

    def get_personal_corrective_exercise_delete_url(self):
        return reverse('personal-corrective_exercise-delete', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Düzeltici Egzersiz Reçetesi'
        verbose_name_plural = 'Düzeltici Egzersiz Reçetesi'
