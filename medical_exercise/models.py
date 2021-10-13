from django.db import models
from datetime import datetime
from django.urls import reverse
# Create your models here.
from registration.models import Trainer, Personal


class medical_exercise2(models.Model):
    # FRZNSHLDR / SMR
    frzn_smr_Prone = models.CharField(verbose_name='Prone Pose Anterior Deltoid SMR w/Miniball', max_length=60,
                                      blank=True, null=True)
    frzn_smr_Supine = models.CharField(verbose_name='Supine Pose Posterior Deltoid SMR w/Miniball', max_length=60,
                                       blank=True, null=True)
    frzn_smr_Side = models.CharField(verbose_name='Side Lying Posterior Deltoid SMR w/Miniball', max_length=60,
                                     blank=True, null=True)
    frzn_smr_Standing1 = models.CharField(verbose_name='Standing Poterior Deltoid SMR on Wall w/Miniball',
                                          max_length=60, blank=True, null=True)
    frzn_smr_Standing2 = models.CharField(verbose_name='Standing Lateral Deltoid SMR on Wall w/Miniball', max_length=60,
                                          blank=True, null=True)
    frzn_smr_Standing3 = models.CharField(verbose_name='Standing Anterior Deltoid SMR on Wall w/Miniball',
                                          max_length=60, blank=True, null=True)
    # FRZNSHLDR / STRETCHING
    frzn_str_Assisted = models.CharField(verbose_name='Assisted Cross Body Stretch', max_length=60, blank=True,
                                         null=True)
    frzn_str_Sleeper = models.CharField(verbose_name='Sleeper Stretch', max_length=60, blank=True, null=True)
    frzn_str_Shoulder1 = models.CharField(verbose_name='Shoulder External Rotation Stretch Wall Support', max_length=60,
                                          blank=True, null=True)
    frzn_str_Shoulder2 = models.CharField(verbose_name='Shoulder Abduction Stretch Wall Support', max_length=60,
                                          blank=True, null=True)
    frzn_str_Shoulder3 = models.CharField(verbose_name='Shoulder Internal Rotation Stretch w/Dowel', max_length=60,
                                          blank=True, null=True)
    frzn_str_Lateral = models.CharField(verbose_name='Lateral Chain Stretch', max_length=60, blank=True, null=True)
    frzn_str_Thoracic = models.CharField(verbose_name='Thoracic Rotation Stretch', max_length=60, blank=True, null=True)
    frzn_str_Foam = models.CharField(verbose_name='Foam Roller Prayer Stretch', max_length=60, blank=True, null=True)
    frzn_str_Swiss = models.CharField(verbose_name='Swiss Ball Prayer', max_length=60, blank=True, null=True)
    frzn_str_Praying = models.CharField(verbose_name='Praying type, Quadruped extension', max_length=60, blank=True,
                                        null=True)
    frzn_str_Torso = models.CharField(verbose_name='Torso flexion, over a support w/Wall', max_length=60, blank=True,
                                      null=True)
    frzn_str_One = models.CharField(verbose_name='One-Arm Shoulder Flexor Stretch', max_length=60, blank=True,
                                    null=True)
    frzn_str_Horizontal = models.CharField(verbose_name='Horizontal Abduction of the arm', max_length=60, blank=True,
                                           null=True)
    frzn_str_Overhead = models.CharField(verbose_name='Overhead Arm Vertical Stretch', max_length=60, blank=True,
                                         null=True)
    frzn_str_Neck = models.CharField(verbose_name='Neck & Torso Flexion', max_length=60, blank=True, null=True)
    frzn_str_Forward = models.CharField(verbose_name='Forward Arm Ext', max_length=60, blank=True, null=True)
    frzn_str_Crossing = models.CharField(verbose_name='Crossing The Arms Behind The Back', max_length=60, blank=True,
                                         null=True)
    frzn_str_Lying = models.CharField(verbose_name='Lying on Bench Ext. Rotation', max_length=60, blank=True, null=True)
    frzn_str_Seated = models.CharField(verbose_name='Seated Shoulder Flexor Depressor Retractor Stretch', max_length=60,
                                       blank=True, null=True)
    # FRZNSHLDR / FORCE / IZOMETRIK
    frzn_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Seated Assisted Flexion w/Dowel', max_length=60,
                                               blank=True, null=True)
    frzn_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Supine Assisted Overhead Flexion w/Dowel',
                                               max_length=60, blank=True, null=True)
    frzn_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Table Sliders', max_length=60, blank=True,
                                               null=True)
    frzn_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric Ball Flexion', max_length=60, blank=True,
                                               null=True)
    frzn_frc_izm_Isometric5 = models.CharField(verbose_name='Isometric Banded Shoulder ER w/Yoga Block', max_length=60,
                                               blank=True, null=True)
    # FRZNSHLDR / FORCE / IZOTONIK
    frzn_frc_iztnk_Seated1 = models.CharField(verbose_name='Seated Assisted Flexion w/Dowel', max_length=60, blank=True,
                                              null=True)
    frzn_frc_iztnk_Supine1 = models.CharField(verbose_name='Supine Assisted Overhead Flexion w/Dowel', max_length=60,
                                              blank=True, null=True)
    frzn_frc_iztnk_External1 = models.CharField(verbose_name='External Rotation at Side w/Dowel', max_length=60,
                                                blank=True, null=True)
    frzn_frc_iztnk_External2 = models.CharField(verbose_name='External Rotation at 90 Degrees Abduction', max_length=60,
                                                blank=True, null=True)
    frzn_frc_iztnk_Table = models.CharField(verbose_name='Table Sliders', max_length=60, blank=True, null=True)
    frzn_frc_iztnk_Extension = models.CharField(verbose_name='Extension Lifts w/Dowel', max_length=60, blank=True,
                                                null=True)
    frzn_frc_iztnk_Up = models.CharField(verbose_name='Up and Over Reach', max_length=60, blank=True, null=True)
    frzn_frc_iztnk_AA1 = models.CharField(verbose_name='AA External Rotation 0 Degrees', max_length=60, blank=True,
                                          null=True)
    frzn_frc_iztnk_AA2 = models.CharField(verbose_name='AA External Rotation 90 Degrees', max_length=60, blank=True,
                                          null=True)
    frzn_frc_iztnk_Way = models.CharField(verbose_name='3-Way AA Elevation', max_length=60, blank=True, null=True)
    frzn_frc_iztnk_Dowel1 = models.CharField(verbose_name='Dowel External Rotation', max_length=60, blank=True,
                                             null=True)
    frzn_frc_iztnk_Dowel2 = models.CharField(verbose_name='Dowel Abduction', max_length=60, blank=True, null=True)
    frzn_frc_iztnk_Dowel3 = models.CharField(verbose_name='Dowel External Rotation (90 Degree Abduction)',
                                             max_length=60, blank=True, null=True)
    frzn_frc_iztnk_Dowel4 = models.CharField(verbose_name='Dowel Flexion', max_length=60, blank=True, null=True)
    frzn_frc_iztnk_Ball = models.CharField(verbose_name='Ball Flexion', max_length=60, blank=True, null=True)
    frzn_frc_iztnk_Eccentric = models.CharField(verbose_name='Eccentric Dumbbell Flexion', max_length=60, blank=True,
                                                null=True)
    frzn_frc_iztnk_Pendulum = models.CharField(verbose_name='Pendulum Circles', max_length=60, blank=True, null=True)
    frzn_frc_iztnk_Cane1 = models.CharField(verbose_name='Cane Flexion', max_length=60, blank=True, null=True)
    frzn_frc_iztnk_Cane2 = models.CharField(verbose_name='Cane Abduction', max_length=60, blank=True, null=True)
    frzn_frc_iztnk_Cane3 = models.CharField(verbose_name='Cane Extensión', max_length=60, blank=True, null=True)
    frzn_frc_iztnk_Cane4 = models.CharField(verbose_name='Cane IR', max_length=60, blank=True, null=True)
    frzn_frc_iztnk_Cane5 = models.CharField(verbose_name='Cane ER', max_length=60, blank=True, null=True)
    frzn_frc_iztnk_Working = models.CharField(verbose_name='Working the Clock', max_length=60, blank=True, null=True)
    frzn_frc_iztnk_Prone = models.CharField(verbose_name='Prone Shoulder Extension to Swimmers', max_length=60,
                                            blank=True, null=True)
    frzn_frc_iztnk_Child = models.CharField(verbose_name='Child Pose Lift Offs w/Foam Roller', max_length=60,
                                            blank=True, null=True)
    frzn_frc_iztnk_Banded = models.CharField(verbose_name='Banded Shoulder ER w/Yoga Block', max_length=60, blank=True,
                                             null=True)
    frzn_frc_iztnk_Kneeling1 = models.CharField(verbose_name='½ Kneeling Landmine Press', max_length=60, blank=True,
                                                null=True)
    frzn_frc_iztnk_Lateral = models.CharField(verbose_name='Lateral Raise', max_length=60, blank=True, null=True)
    frzn_frc_iztnk_Kneeling = models.CharField(verbose_name='½ Kneeling Windmill', max_length=60, blank=True, null=True)
    frzn_frc_iztnk_Supine2 = models.CharField(verbose_name='Supine to sidelying  with KB (try bottoms up if you can)',
                                              max_length=60, blank=True, null=True)
    frzn_frc_iztnk_Band = models.CharField(verbose_name='Band Assisted Push-Ups', max_length=60, blank=True, null=True)
    frzn_frc_iztnk_Seated2 = models.CharField(verbose_name='Seated Dowel External Rotation', max_length=60, blank=True,
                                              null=True)
    frzn_frc_iztnk_Seated3 = models.CharField(verbose_name='Seated Dowel Abduction', max_length=60, blank=True,
                                              null=True)
    frzn_frc_iztnk_Seated4 = models.CharField(verbose_name='Seated Dowel Flexion', max_length=60, blank=True, null=True)
    frzn_frc_iztnk_Side = models.CharField(verbose_name='Side Lying Dumbbell External Rotation', max_length=60,
                                           blank=True, null=True)
    frzn_frc_iztnk_Full = models.CharField(verbose_name='Full Can', max_length=60, blank=True, null=True)
    # IMPINGMENT / SMR
    impng_smr_Supine1 = models.CharField(verbose_name='Supine Pose Miniball Rotators Glide', max_length=60, blank=True,
                                         null=True)
    impng_smr_Prone = models.CharField(verbose_name='Prone Pose Anterior Deltoid SMR w/Miniball', max_length=60,
                                       blank=True, null=True)
    impng_smr_Supine2 = models.CharField(verbose_name='Supine Pose Posterior Deltoid SMR w/Miniball', max_length=60,
                                         blank=True, null=True)
    impng_smr_Side = models.CharField(verbose_name='Side Lying Posterior Deltoid SMR w/Miniball', max_length=60,
                                      blank=True, null=True)
    impng_smr_Standing1 = models.CharField(verbose_name='Standing Poterior Deltoid SMR on Wall w/Miniball',
                                           max_length=60, blank=True, null=True)
    impng_smr_Standing2 = models.CharField(verbose_name='Standing Lateral Deltoid SMR on Wall w/Miniball',
                                           max_length=60, blank=True, null=True)
    impng_smr_Standing3 = models.CharField(verbose_name='Standing Anterior Deltoid SMR on Wall w/Miniball',
                                           max_length=60, blank=True, null=True)
    # IMPINGMENT / # IMPINGMENT /
    impng_str_Prone = models.CharField(verbose_name='Prone Biceps Stretch', max_length=60, blank=True, null=True)
    impng_str_Bench = models.CharField(verbose_name='Bench Overhead Stretch', max_length=60, blank=True, null=True)
    impng_str_Foam = models.CharField(verbose_name='Foam Roller Prayer Stretch', max_length=60, blank=True, null=True)
    impng_str_Swiss = models.CharField(verbose_name='Swiss Ball Prayer ', max_length=60, blank=True, null=True)
    impng_str_Praying = models.CharField(verbose_name='Praying type, Quadruped  extension', max_length=60, blank=True,
                                         null=True)
    impng_str_Torso = models.CharField(verbose_name='Torso flexion, over a support w/Wall', max_length=60, blank=True,
                                       null=True)
    impng_str_One = models.CharField(verbose_name='One-Arm Shoulder  Flexor Stretch', max_length=60, blank=True,
                                     null=True)
    impng_str_Horizontal = models.CharField(verbose_name='Horizontal Abduction of the arm', max_length=60, blank=True,
                                            null=True)
    impng_str_Overhead = models.CharField(verbose_name='Overhead Arm Vertical Stretch', max_length=60, blank=True,
                                          null=True)
    impng_str_Neck = models.CharField(verbose_name='Neck & Torso Flexion', max_length=60, blank=True, null=True)
    impng_str_Forward = models.CharField(verbose_name='Forward Arm Ext.', max_length=60, blank=True, null=True)
    impng_str_Crossing = models.CharField(verbose_name='Crossing The Arms Behind The Back', max_length=60, blank=True,
                                          null=True)
    impng_str_Lying = models.CharField(verbose_name='Lying on Bench Ext. Rotation', max_length=60, blank=True,
                                       null=True)
    impng_str_Seated = models.CharField(verbose_name='Seated Shoulder Flexor Depressor Retractor Stretch',
                                        max_length=60, blank=True, null=True)
    # IMPINGMENT / FORCE / IZOMETRIK
    impng_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Inverted Row', max_length=60, blank=True,
                                                null=True)
    impng_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Banded Shoulder Flexion', max_length=60,
                                                blank=True, null=True)
    impng_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Banded Shoulder External Rotaion',
                                                max_length=60, blank=True, null=True)
    impng_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric Brueggers', max_length=60, blank=True,
                                                null=True)
    impng_frc_izm_Isometric5 = models.CharField(verbose_name='Isometric Feet Elevated Dolphing Plank', max_length=60,
                                                blank=True, null=True)
    impng_frc_izm_Prone = models.CharField(verbose_name='Prone External Rotation Hold', max_length=60, blank=True,
                                           null=True)
    # IMPINGMENT / FORCE / IZOTONIK
    impng_frc_iztnk_Rotation = models.CharField(verbose_name='Rotation and ER at 90/90 w/RB', max_length=60, blank=True,
                                                null=True)
    impng_frc_iztnk_Shoulder = models.CharField(verbose_name='Shoulder Press & Raise with Cross Body Resistance',
                                                max_length=60, blank=True, null=True)
    impng_frc_iztnk_Inverted = models.CharField(verbose_name='Inverted Row', max_length=60, blank=True, null=True)
    impng_frc_iztnk_Incline1 = models.CharField(verbose_name='Incline Push-Up', max_length=60, blank=True, null=True)
    impng_frc_iztnk_Banded = models.CharField(verbose_name='Banded Shoulder Flexion', max_length=60, blank=True,
                                              null=True)
    impng_frc_iztnk_Bilateral = models.CharField(verbose_name='Bilateral Ext. Rotation (Varying Angles) w/Band',
                                                 max_length=60, blank=True, null=True)
    impng_frc_iztnk_Incline2 = models.CharField(verbose_name='Incline Plank and Lateral Taps', max_length=60,
                                                blank=True, null=True)
    impng_frc_iztnk_Supine1 = models.CharField(verbose_name='Supine Serratus Scoop w/Band', max_length=60, blank=True,
                                               null=True)
    impng_frc_iztnk_Brueggers = models.CharField(verbose_name='Brueggers', max_length=60, blank=True, null=True)
    impng_frc_iztnk_Row = models.CharField(verbose_name='Row, External Rotation w/Band', max_length=60, blank=True,
                                           null=True)
    impng_frc_iztnk_Push = models.CharField(verbose_name='Push-Up Plus', max_length=60, blank=True, null=True)
    impng_frc_iztnk_Side = models.CharField(verbose_name='Side Plank and Row w/Band', max_length=60, blank=True,
                                            null=True)
    impng_frc_iztnk_Feet = models.CharField(verbose_name='Feet Elevated Dolphin Plank', max_length=60, blank=True,
                                            null=True)
    impng_frc_iztnk_External1 = models.CharField(verbose_name='External Rotation w/Mini Band', max_length=60,
                                                 blank=True, null=True)
    impng_frc_iztnk_Prone1 = models.CharField(verbose_name='Prone Shoulder CARs on Bench', max_length=60, blank=True,
                                              null=True)
    impng_frc_iztnk_Offset = models.CharField(verbose_name='Offset Carries (Overhead/Farmers)', max_length=60,
                                              blank=True, null=True)
    impng_frc_iztnk_Plate = models.CharField(verbose_name='Plate Elevated Unilateral  Shoulder Tap', max_length=60,
                                             blank=True, null=True)
    impng_frc_iztnk_External2 = models.CharField(verbose_name='External Rotation Ball  Roll Ups to Wall', max_length=60,
                                                 blank=True, null=True)
    impng_frc_iztnk_Supine2 = models.CharField(verbose_name='Supine T-Spine Extension w/Foam Roller', max_length=60,
                                               blank=True, null=True)
    impng_frc_iztnk_Prone2 = models.CharField(verbose_name='Prone Angels on Bench', max_length=60, blank=True,
                                              null=True)
    impng_frc_iztnk_Child = models.CharField(verbose_name='Child Pose Reach Bench', max_length=60, blank=True,
                                             null=True)
    impng_frc_iztnk_External3 = models.CharField(verbose_name='External Rotation Lift Off', max_length=60, blank=True,
                                                 null=True)
    impng_frc_iztnk_External4 = models.CharField(verbose_name='External Rotation Pull', max_length=60, blank=True,
                                                 null=True)
    impng_frc_iztnk_Triple = models.CharField(verbose_name='Triple Thread', max_length=60, blank=True, null=True)
    impng_frc_iztnk_Ball = models.CharField(verbose_name='Ball Rollout', max_length=60, blank=True, null=True)
    # GLENOID / SMR
    glnd_smr_Supine = models.CharField(verbose_name='Supine Pose Miniball Rotators Glide', max_length=60, blank=True,
                                       null=True)
    glnd_smr_Prone = models.CharField(verbose_name='Prone Pose Miniball Shoulder Glide', max_length=60, blank=True,
                                      null=True)
    glnd_smr_Wall = models.CharField(verbose_name='Wall Rotators Glide w/Miniball', max_length=60, blank=True,
                                     null=True)
    glnd_smr_Standing = models.CharField(verbose_name='Standing Side Pose Shoulder SMR w/Miniball', max_length=60,
                                         blank=True, null=True)
    glnd_smr_Side = models.CharField(verbose_name='Side Lying Lateral Shoulder SMR w/Miniball', max_length=60,
                                     blank=True, null=True)
    # GLENOID / STRETCHING
    glnd_str_Bench = models.CharField(verbose_name='Bench Overhead Stretch ', max_length=60, blank=True, null=True)
    glnd_str_Foam = models.CharField(verbose_name='Foam Roller Prayer Stretch', max_length=60, blank=True, null=True)
    glnd_str_Swiss = models.CharField(verbose_name='Swiss Ball Prayer ', max_length=60, blank=True, null=True)
    glnd_str_Praying = models.CharField(verbose_name='Praying type, Quadruped extension', max_length=60, blank=True,
                                        null=True)
    glnd_str_Torso = models.CharField(verbose_name='Torso flexion, over a support w/Wal', max_length=60, blank=True,
                                      null=True)
    glnd_str_One = models.CharField(verbose_name='One-Arm Shoulder  Flexor Stretch', max_length=60, blank=True,
                                    null=True)
    glnd_str_Horizontal = models.CharField(verbose_name='Horizontal Abduction of the arm', max_length=60, blank=True,
                                           null=True)
    glnd_str_Overhead = models.CharField(verbose_name='Overhead Arm Vertical Stretch', max_length=60, blank=True,
                                         null=True)
    glnd_str_Neck = models.CharField(verbose_name='Neck & Torso Flexion', max_length=60, blank=True, null=True)
    glnd_str_Forward = models.CharField(verbose_name='Forward Arm Ext.', max_length=60, blank=True, null=True)
    glnd_str_Crossing = models.CharField(verbose_name='Crossing The Arms Behind The Back', max_length=60, blank=True,
                                         null=True)
    glnd_str_Lying = models.CharField(verbose_name='Lying on Bench Ext. Rotation', max_length=60, blank=True, null=True)
    glnd_str_Seated = models.CharField(verbose_name='Seated Shoulder Flexor Depressor Retractor Stretch', max_length=60,
                                       blank=True, null=True)
    # GLENOID / FORCE / IZOMETRIK
    glnd_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Prone One-Arm Y’s', max_length=60, blank=True,
                                               null=True)
    glnd_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Shoulder Tap', max_length=60, blank=True,
                                               null=True)
    glnd_frc_izm_Side = models.CharField(verbose_name='Side Plank on Swissball', max_length=60, blank=True, null=True)
    glnd_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Bird Dog', max_length=60, blank=True, null=True)
    # GLENOID / FORCE / IZOTONIK
    glnd_frc_iztnk_Side = models.CharField(verbose_name='Side Lying External Rotation w/Dumbbell', max_length=60,
                                           blank=True, null=True)
    glnd_frc_iztnk_Standing = models.CharField(verbose_name='Standing Internal Rotation', max_length=60, blank=True,
                                               null=True)
    glnd_frc_iztnk_Prone1 = models.CharField(verbose_name='Prone One-Arm Y’s', max_length=60, blank=True, null=True)
    glnd_frc_iztnk_Kneeling = models.CharField(verbose_name='½ Kneeling Bottom-Up Press w/KB', max_length=60,
                                               blank=True, null=True)
    glnd_frc_iztnk_Hand = models.CharField(verbose_name='Hand Plank Scapular Prot./Retrac.', max_length=60, blank=True,
                                           null=True)
    glnd_frc_iztnk_Shoulder = models.CharField(verbose_name='Shoulder Tap', max_length=60, blank=True, null=True)
    glnd_frc_iztnk_Prone2 = models.CharField(verbose_name='Prone Clock on Hand', max_length=60, blank=True, null=True)
    glnd_frc_iztnk_Single = models.CharField(verbose_name='Single Arm Scapular Push-Up', max_length=60, blank=True,
                                             null=True)
    glnd_frc_iztnk_Arm = models.CharField(verbose_name='Arm Bar, Full Rotation w/KB', max_length=60, blank=True,
                                          null=True)
    glnd_frc_iztnk_Kettlebell = models.CharField(verbose_name='Kettlebell Pull Through', max_length=60, blank=True,
                                                 null=True)
    glnd_frc_iztnk_Dolphin = models.CharField(verbose_name='Dolphin Push-Up Plus', max_length=60, blank=True, null=True)
    glnd_frc_iztnk_Prone3 = models.CharField(verbose_name='Prone Y’s  on Swissball', max_length=60, blank=True,
                                             null=True)
    glnd_frc_iztnk_Bird = models.CharField(verbose_name='Bird Dog (Mobil)', max_length=60, blank=True, null=True)
    glnd_frc_iztnk_Landmine = models.CharField(verbose_name='Landmine Press', max_length=60, blank=True, null=True)
    glnd_frc_iztnk_Pike = models.CharField(verbose_name='Pike Press + Shoulder Tap', max_length=60, blank=True,
                                           null=True)
    glnd_frc_iztnk_Serratus = models.CharField(verbose_name='Serratus Slider w/Foam Roller', max_length=60, blank=True,
                                               null=True)
    glnd_frc_iztnk_Chest = models.CharField(verbose_name='Chest Supported “I,Y,T,W”Lifts', max_length=60, blank=True,
                                            null=True)
    glnd_frc_iztnk_Dumbbell = models.CharField(verbose_name='Dumbbell Lateral Raise', max_length=60, blank=True,
                                               null=True)
    glnd_frc_iztnk_Plank = models.CharField(verbose_name='Plank Hand Walks', max_length=60, blank=True, null=True)

    class Meta:
        verbose_name = "Medikal Egzersiz"
        verbose_name_plural = "Medikal Egzersiz "


class medical_exercise3(models.Model):
    # SHOULDERSTRENGTH / SMR
    shldrstr_smr_Active = models.CharField(verbose_name='Active Pectoralis Release w/Miniball', max_length=60,
                                           blank=True, null=True)
    shldrstr_smr_Prone = models.CharField(verbose_name='Prone Pose Anterior Deltoid SMR w/Miniball', max_length=60,
                                          blank=True, null=True)
    shldrstr_smr_Supine = models.CharField(verbose_name='Supine Pose Posterior Deltoid SMR w/Miniball', max_length=60,
                                           blank=True, null=True)
    shldrstr_smr_Side = models.CharField(verbose_name='Side Lying Posterior Deltoid SMR w/Miniball', max_length=60,
                                         blank=True, null=True)
    shldrstr_smr_Standing1 = models.CharField(verbose_name='Standing Poterior Deltoid SMR on Wall w/Miniball',
                                              max_length=60, blank=True, null=True)
    shldrstr_smr_Standing2 = models.CharField(verbose_name='Standing Lateral Deltoid SMR on Wall w/Miniball',
                                              max_length=60, blank=True, null=True)
    shldrstr_smr_Standing3 = models.CharField(verbose_name='Standing Anterior Deltoid SMR on Wall w/Miniball',
                                              max_length=60, blank=True, null=True)
    # SHOULDERSTRENGTH / STRETCHING
    shldrstr_str_Genie = models.CharField(verbose_name='Genie Stretch', max_length=60, blank=True, null=True)
    shldrstr_str_Sitting = models.CharField(verbose_name='Sitting “X” Stretch', max_length=60, blank=True, null=True)
    shldrstr_str_Kneeling = models.CharField(verbose_name='Kneeling Roll-out Stretch', max_length=60, blank=True,
                                             null=True)
    shldrstr_str_Bench1 = models.CharField(verbose_name='Bench Overhead Stretch', max_length=60, blank=True, null=True)
    shldrstr_str_Prone = models.CharField(verbose_name='Prone Biceps Stretch', max_length=60, blank=True, null=True)
    shldrstr_str_Bench2 = models.CharField(verbose_name='Bench Overhead Stretch', max_length=60, blank=True, null=True)
    shldrstr_str_Foam = models.CharField(verbose_name='Foam Roller Prayer Stretch ', max_length=60, blank=True,
                                         null=True)
    shldrstr_str_Swiss = models.CharField(verbose_name='Swiss Ball Prayer', max_length=60, blank=True, null=True)
    shldrstr_str_Praying = models.CharField(verbose_name='Praying type, Quadruped extension', max_length=60, blank=True,
                                            null=True)
    shldrstr_str_Torso = models.CharField(verbose_name='Torso flexion, over a support w/Wall', max_length=60,
                                          blank=True, null=True)
    shldrstr_str_One = models.CharField(verbose_name='One-Arm Shoulder Flexor Stretch', max_length=60, blank=True,
                                        null=True)
    shldrstr_str_Horizontal = models.CharField(verbose_name='Horizontal Abduction of the arm', max_length=60,
                                               blank=True, null=True)
    shldrstr_str_Overhead = models.CharField(verbose_name='Overhead Arm Vertical Stretch ', max_length=60, blank=True,
                                             null=True)
    shldrstr_str_Neck = models.CharField(verbose_name='Neck & Torso Flexion', max_length=60, blank=True, null=True)
    shldrstr_str_Forward = models.CharField(verbose_name='Forward Arm Ext. ', max_length=60, blank=True, null=True)
    shldrstr_str_Crossing = models.CharField(verbose_name='Crossing The Arms Behind The Back', max_length=60,
                                             blank=True, null=True)
    shldrstr_str_Lying = models.CharField(verbose_name='Lying on Bench Ext. Rotation', max_length=60, blank=True,
                                          null=True)
    shldrstr_str_Seated = models.CharField(verbose_name='Seated Shoulder Flexor Depressor Retractor Stretch',
                                           max_length=60, blank=True, null=True)
    # SHOULDERSTRENGTH / FORCE / IZOMETRIK
    shldrstr_frc_izm_Mini = models.CharField(verbose_name='Mini-Band Tall Kneel Long Pull-Apar', max_length=60,
                                             blank=True, null=True)
    shldrstr_frc_izm_Wall = models.CharField(verbose_name='Wall. Reverse Plank', max_length=60, blank=True, null=True)
    shldrstr_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Single-Arm Overhead Sliders', max_length=60,
                                                   blank=True, null=True)
    shldrstr_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Thoracic Extension', max_length=60,
                                                   blank=True, null=True)
    shldrstr_frc_izm_Half = models.CharField(verbose_name='Half Kneeling “Y” Pull', max_length=60, blank=True,
                                             null=True)
    shldrstr_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Band Pull Apart', max_length=60, blank=True,
                                                   null=True)
    # SHOULDERSTRENGTH / FORCE / IZOTONIK
    shldrstr_frc_iztnk_Quadruped1 = models.CharField(verbose_name='Quadruped Shoulder Sliders', max_length=60,
                                                     blank=True, null=True)
    shldrstr_frc_iztnk_Prone1 = models.CharField(verbose_name='Prone External Rotation (90/90)', max_length=60,
                                                 blank=True, null=True)
    shldrstr_frc_iztnk_Prone2 = models.CharField(verbose_name='Prone Horizontal Abduction', max_length=60, blank=True,
                                                 null=True)
    shldrstr_frc_iztnk_Overhead1 = models.CharField(verbose_name='Overhead Taps', max_length=60, blank=True, null=True)
    shldrstr_frc_iztnk_Prone3 = models.CharField(verbose_name='Prone Swimmers', max_length=60, blank=True, null=True)
    shldrstr_frc_iztnk_Prone4 = models.CharField(verbose_name='Prone Clocks', max_length=60, blank=True, null=True)
    shldrstr_frc_iztnk_Mini = models.CharField(verbose_name='Mini-Band Tall Kneel Long Pull-Apart', max_length=60,
                                               blank=True, null=True)
    shldrstr_frc_iztnk_Prone5 = models.CharField(verbose_name='Prone I-T’s:', max_length=60, blank=True, null=True)
    shldrstr_frc_iztnk_Prone6 = models.CharField(
        verbose_name='Prone Bodyweight Serratus/rap Towel Drags + Band Resistance',
        max_length=60, blank=True, null=True)
    shldrstr_frc_iztnk_Quadruped2 = models.CharField(verbose_name='Quadruped T-Spine Rotation', max_length=60,
                                                     blank=True, null=True)
    shldrstr_frc_iztnk_Active = models.CharField(verbose_name='Active “Bully” Stretch', max_length=60, blank=True,
                                                 null=True)
    shldrstr_frc_iztnk_Kneeling = models.CharField(verbose_name='½ Kneeling Single-arm Overhead Sliders', max_length=60,
                                                   blank=True, null=True)
    shldrstr_frc_iztnk_Overhead2 = models.CharField(verbose_name='Overhead Reach on Longitudinal Foam Roller',
                                                    max_length=60, blank=True, null=True)
    shldrstr_frc_iztnk_Seated = models.CharField(verbose_name='Seated Thorasic Extension', max_length=60, blank=True,
                                                 null=True)
    shldrstr_frc_iztnk_Prone7 = models.CharField(verbose_name='Prone Rotation Press', max_length=60, blank=True,
                                                 null=True)
    shldrstr_frc_iztnk_Half = models.CharField(verbose_name='Half Kneeling “Y” Pull', max_length=60, blank=True,
                                               null=True)
    shldrstr_frc_iztnk_Rollout = models.CharField(verbose_name='Rollout + T-Spine Rotation', max_length=60, blank=True,
                                                  null=True)
    shldrstr_frc_iztnk_External1 = models.CharField(verbose_name='External Rotation Walkouts', max_length=60,
                                                    blank=True, null=True)
    shldrstr_frc_iztnk_External2 = models.CharField(verbose_name='External Rotation + Reah w/Band ', max_length=60,
                                                    blank=True, null=True)
    shldrstr_frc_iztnk_Band = models.CharField(verbose_name='Band Pull Apart', max_length=60, blank=True, null=True)
    # TENNIS / SMR
    tns_smr_Tennis = models.CharField(verbose_name='Tennis Ball SMR at Wall', max_length=60, blank=True, null=True)
    tns_smr_Fore1 = models.CharField(verbose_name='Fore arm flexors SMR w/Miniball', max_length=60, blank=True,
                                     null=True)
    tns_smr_Fore2 = models.CharField(verbose_name='Fore arm extensors SMR w/Miniball', max_length=60, blank=True,
                                     null=True)
    tns_smr_Fore3 = models.CharField(verbose_name='Fore arm flexors SMR w/Foam Roller', max_length=60, blank=True,
                                     null=True)
    tns_smr_Fore4 = models.CharField(verbose_name='Fore arm extensors SMR w/Foam Roller', max_length=60, blank=True,
                                     null=True)
    # TENNIS / # TENNIS /
    tns_str_Forearm = models.CharField(verbose_name='Forearm Extensor Stretch', max_length=60, blank=True, null=True)
    tns_str_Wrist1 = models.CharField(verbose_name='Wrist Flexor Stretch', max_length=60, blank=True, null=True)
    tns_str_Standing1 = models.CharField(verbose_name='Standing Wall Elbow Flexor Stretch', max_length=60, blank=True,
                                         null=True)
    tns_str_Elbow = models.CharField(verbose_name='Elbow Extensor (Anconeus) Stretch', max_length=60, blank=True,
                                     null=True)
    tns_str_Standing2 = models.CharField(verbose_name='Standing Forearm Pronator Stretch', max_length=60, blank=True,
                                         null=True)
    tns_str_Floor1 = models.CharField(verbose_name='Floor Wrist Extensor Stretch', max_length=60, blank=True, null=True)
    tns_str_Floor2 = models.CharField(verbose_name='Floor Wrist Ulnar Deviator and Extensor Stretch', max_length=60,
                                      blank=True, null=True)
    tns_str_Floor3 = models.CharField(verbose_name='Floor Wrist Radial Deviator and Extensor Stretch', max_length=60,
                                      blank=True, null=True)
    tns_str_Wrist2 = models.CharField(verbose_name='Wrist Radial Deviator and Flexor Stretch', max_length=60,
                                      blank=True, null=True)
    tns_str_Wrist3 = models.CharField(verbose_name='Wrist Ulnar Deviator and Flexor Stretch', max_length=60, blank=True,
                                      null=True)
    tns_str_Finger1 = models.CharField(verbose_name='Finger Flexor Stretch', max_length=60, blank=True, null=True)
    tns_str_Finger2 = models.CharField(verbose_name='Finger Extensor Stretch', max_length=60, blank=True, null=True)
    tns_str_Frontal = models.CharField(verbose_name='Frontal Extension of the arms with finger', max_length=60,
                                       blank=True, null=True)
    tns_str_Extension = models.CharField(verbose_name='Extension of the hands facing a Wall', max_length=60, blank=True,
                                         null=True)
    tns_str_Flexion = models.CharField(verbose_name='Flexion of the hand with the forearm extended', max_length=60,
                                       blank=True, null=True)
    tns_str_Finger3 = models.CharField(verbose_name='Finger by finger extension with assistance', max_length=60,
                                       blank=True, null=True)
    tns_str_Finger4 = models.CharField(verbose_name='Finger by finger flexion with assistance', max_length=60,
                                       blank=True, null=True)
    tns_str_Separation = models.CharField(verbose_name='Separation of the fingers', max_length=60, blank=True,
                                          null=True)
    tns_str_Adduction = models.CharField(verbose_name='Adduction of the hand with the elbow extended', max_length=60,
                                         blank=True, null=True)
    tns_str_Pronation = models.CharField(verbose_name='Pronation of the hand with the elbow extended', max_length=60,
                                         blank=True, null=True)
    # TENNIS/FORCE/IZOMETRIK
    tns_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Bottom-Up w/KB', max_length=60, blank=True,
                                              null=True)
    tns_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Wrist Supination/Pronation', max_length=60,
                                              blank=True, null=True)
    tns_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Wrist Extension/Flexion', max_length=60,
                                              blank=True, null=True)
    tns_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric Ball Squeeze', max_length=60, blank=True,
                                              null=True)
    # TENNIS/FORCE/IZOTONIK
    tns_frc_iztnk_Dowel = models.CharField(verbose_name='Dowel Supination/Pronation', max_length=60, blank=True,
                                           null=True)
    tns_frc_iztnk_Radial1 = models.CharField(verbose_name='Radial Nerve Glide', max_length=60, blank=True, null=True)
    tns_frc_iztnk_Grip = models.CharField(verbose_name='Grip Strenght w/Miniball', max_length=60, blank=True, null=True)
    tns_frc_iztnk_Eccentric1 = models.CharField(verbose_name='Eccentric Wrist Extension w/Dumbbell', max_length=60,
                                                blank=True, null=True)
    tns_frc_iztnk_Finger = models.CharField(verbose_name='Finger Spreads', max_length=60, blank=True, null=True)
    tns_frc_iztnk_Eccentric2 = models.CharField(verbose_name='Eccentric 3rd. Digit Extension', max_length=60,
                                                blank=True, null=True)
    tns_frc_iztnk_Wrist = models.CharField(verbose_name='Wrist Extension MWM', max_length=60, blank=True, null=True)
    tns_frc_iztnk_Supination = models.CharField(verbose_name='Supination/Pronation w/Dumbbell', max_length=60,
                                                blank=True, null=True)
    tns_frc_iztnk_Radial2 = models.CharField(verbose_name='Radial Deviatiom w/Dumbbell', max_length=60, blank=True,
                                             null=True)
    tns_frc_iztnk_Flex1 = models.CharField(verbose_name='Flex-Bar Wrist Extension', max_length=60, blank=True,
                                           null=True)
    tns_frc_iztnk_Flex2 = models.CharField(verbose_name='Flex-Bar Supination', max_length=60, blank=True, null=True)
    tns_frc_iztnk_Bottom = models.CharField(verbose_name='Bottom-Up Press w/KB', max_length=60, blank=True, null=True)
    # GOLF / SMR
    glf_smr_Fore1 = models.CharField(verbose_name='Fore arm flexors SMR w/Miniball', max_length=60, blank=True,
                                     null=True)
    glf_smr_Fore2 = models.CharField(verbose_name='Fore arm extensors SMR w/Miniball', max_length=60, blank=True,
                                     null=True)
    glf_smr_Fore3 = models.CharField(verbose_name='Fore arm flexors SMR w/Foam Roller', max_length=60, blank=True,
                                     null=True)
    glf_smr_Fore4 = models.CharField(verbose_name='Fore arm extensors SMR w/Foam Roller', max_length=60, blank=True,
                                     null=True)
    # GOLF / STRETCHING
    glf_str_Wrist1 = models.CharField(verbose_name='Wrist Flexor Stretch', max_length=60, blank=True, null=True)
    glf_str_Prayer = models.CharField(verbose_name='Prayer Stretch', max_length=60, blank=True, null=True)
    glf_str_Standing1 = models.CharField(verbose_name='Standing Wall Elbow FlexorStretch', max_length=60, blank=True,
                                         null=True)
    glf_str_Elbow = models.CharField(verbose_name='Elbow Extensor (Anconeus) Stretch', max_length=60, blank=True,
                                     null=True)
    glf_str_Standing2 = models.CharField(verbose_name='Standing Forearm Pronator Stretch', max_length=60, blank=True,
                                         null=True)
    glf_str_Floor1 = models.CharField(verbose_name='Floor Wrist Extensor Stretch', max_length=60, blank=True, null=True)
    glf_str_Floor2 = models.CharField(verbose_name='Floor Wrist Ulnar Deviator and Extensor Stretch', max_length=60,
                                      blank=True, null=True)
    glf_str_Floor3 = models.CharField(verbose_name='Floor Wrist Radial Deviator and Extensor Stretch', max_length=60,
                                      blank=True, null=True)
    glf_str_Wrist2 = models.CharField(verbose_name='Wrist Radial Deviator and Extensor Stretch', max_length=60,
                                      blank=True, null=True)
    glf_str_Wrist3 = models.CharField(verbose_name='Wrist Ulnar Deviator and Flexor Stretch', max_length=60, blank=True,
                                      null=True)
    glf_str_Finger1 = models.CharField(verbose_name='Finger Flexor Stretch', max_length=60, blank=True, null=True)
    glf_str_Finger2 = models.CharField(verbose_name='Finger Extensor Stretch', max_length=60, blank=True, null=True)
    glf_str_Frontal = models.CharField(verbose_name='Frontal Extension of the arms with finger', max_length=60,
                                       blank=True, null=True)
    glf_str_Extension = models.CharField(verbose_name='Extension of the hands facing a Wall', max_length=60, blank=True,
                                         null=True)
    glf_str_Flexion = models.CharField(verbose_name='Flexion of the hand with the forearm extended', max_length=60,
                                       blank=True, null=True)
    glf_str_Finger3 = models.CharField(verbose_name='Finger by finger extension with assistance', max_length=60,
                                       blank=True, null=True)
    glf_str_Finger4 = models.CharField(verbose_name='Finger by finger flexion with assistance', max_length=60,
                                       blank=True, null=True)
    glf_str_Separation = models.CharField(verbose_name='Separation of the fingers', max_length=60, blank=True,
                                          null=True)
    glf_str_Adduction = models.CharField(verbose_name='Adduction of the hand with the elbow extended', max_length=60,
                                         blank=True, null=True)
    glf_str_Pronation = models.CharField(verbose_name='Pronation of the hand with the elbow extended', max_length=60,
                                         blank=True, null=True)
    # GOLF / FORCE / IZOMETRIK
    glf_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Prayer', max_length=60, blank=True, null=True)
    glf_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Grip Strenght w/Miniball', max_length=60,
                                              blank=True, null=True)
    glf_frc_izm_Wrist1 = models.CharField(verbose_name='Wrist Flexion Isometric Hold', max_length=60, blank=True,
                                          null=True)
    glf_frc_izm_Wrist2 = models.CharField(verbose_name='Wrist Extension Isometric Hold', max_length=60, blank=True,
                                          null=True)
    # GOLF / FORCE / IZOTONIK
    glf_frc_iztn_Eccentric = models.CharField(verbose_name='Eccentric Wrist Extension', max_length=60, blank=True,
                                              null=True)
    glf_frc_iztn_Grip = models.CharField(verbose_name='Grip Strenght w/Miniball', max_length=60, blank=True, null=True)
    glf_frc_iztn_Dowel = models.CharField(verbose_name='Dowel Supination/Pronation', max_length=60, blank=True,
                                          null=True)
    glf_frc_iztn_Nerve = models.CharField(verbose_name='Nerve Glides', max_length=60, blank=True, null=True)
    glf_frc_iztn_Wrist1 = models.CharField(verbose_name='Wrist Extension MWM', max_length=60, blank=True, null=True)
    glf_frc_iztn_Tyler = models.CharField(verbose_name='Tyler Twist', max_length=60, blank=True, null=True)
    glf_frc_iztn_Wrist2 = models.CharField(verbose_name='Wrist Flexion w/Dumbbell', max_length=60, blank=True,
                                           null=True)
    glf_frc_iztn_Ulnar1 = models.CharField(verbose_name='Ulnar Nerve Slider', max_length=60, blank=True, null=True)
    glf_frc_iztn_Pallof = models.CharField(verbose_name='Pallof Press', max_length=60, blank=True, null=True)
    glf_frc_iztn_Shoulder = models.CharField(verbose_name='Shoulder ‘’IR’’ Punches', max_length=60, blank=True,
                                             null=True)
    glf_frc_iztn_Loaded = models.CharField(verbose_name='Loaded Carry w/KB', max_length=60, blank=True, null=True)
    glf_frc_iztn_Below = models.CharField(verbose_name='Below Dowel Pronation/Supination', max_length=60, blank=True,
                                          null=True)
    glf_frc_iztn_Ulnar2 = models.CharField(verbose_name='Ulnar Deviation', max_length=60, blank=True, null=True)

    class Meta:
        verbose_name = "Medikal Egzersiz"
        verbose_name_plural = "Medikal Egzersiz "


class medical_exercise4(models.Model):
    # KARPAL / SMR
    krpl_smr_Wrist1 = models.CharField(verbose_name='Wrist flexors SMR w/Miniball', max_length=60, blank=True,
                                       null=True)
    krpl_smr_Wrist2 = models.CharField(verbose_name='Wrist extensors SMR w/Miniball', max_length=60, blank=True,
                                       null=True)
    krpl_smr_Wrist3 = models.CharField(verbose_name='Wrist flexors SMR w/Foam Roller', max_length=60, blank=True,
                                       null=True)
    krpl_smr_Wrist4 = models.CharField(verbose_name='Wrist extensors SMR w/Foam Roller', max_length=60, blank=True,
                                       null=True)
    # KARPAL / STRETCHING
    krpl_str_Forearm = models.CharField(verbose_name='Forearm Extensor Stretch', max_length=60, blank=True, null=True)
    krpl_str_Wrist1 = models.CharField(verbose_name='Wrist Flexor Stretch', max_length=60, blank=True, null=True)
    krpl_str_Scalene = models.CharField(verbose_name='Scalene Muscle Stretch', max_length=60, blank=True, null=True)
    krpl_str_Standing1 = models.CharField(verbose_name='Standing Wall Elbow Flexor Stretch', max_length=60, blank=True,
                                          null=True)
    krpl_str_Elbow = models.CharField(verbose_name='Elbow Extensor (Anconeus) Stretch', max_length=60, blank=True,
                                      null=True)
    krpl_str_Standing2 = models.CharField(verbose_name='Standing Forearm Pronator Stretch', max_length=60, blank=True,
                                          null=True)
    krpl_str_Floor1 = models.CharField(verbose_name='Floor Wrist Extensor Stretch', max_length=60, blank=True,
                                       null=True)
    krpl_str_Floor2 = models.CharField(verbose_name='Floor Wrist Ulnar Deviator and Extensor Stretch', max_length=60,
                                       blank=True, null=True)
    krpl_str_Floor3 = models.CharField(verbose_name='Floor Wrist Radial Deviator and Extensor Stretch', max_length=60,
                                       blank=True, null=True)
    krpl_str_Wrist2 = models.CharField(verbose_name='Wrist Radial Deviator and Flexor Stretch', max_length=60,
                                       blank=True, null=True)
    krpl_str_Wrist3 = models.CharField(verbose_name='Wrist Ulnar Deviator and FlexorStretch', max_length=60, blank=True,
                                       null=True)
    krpl_str_Finger1 = models.CharField(verbose_name='Finger Flexor Stretch', max_length=60, blank=True, null=True)
    krpl_str_Finger2 = models.CharField(verbose_name='Finger Extensor Stretch', max_length=60, blank=True, null=True)
    krpl_str_Frontal = models.CharField(verbose_name='Frontal Extension of the arms with finger', max_length=60,
                                        blank=True, null=True)
    krpl_str_Extension = models.CharField(verbose_name='Extension of the hands facing a Wall', max_length=60,
                                          blank=True, null=True)
    krpl_str_Flexion = models.CharField(verbose_name='Flexion of the hand with the forearm extended', max_length=60,
                                        blank=True, null=True)
    krpl_str_Finger3 = models.CharField(verbose_name='Finger by finger extension with assistance', max_length=60,
                                        blank=True, null=True)
    krpl_str_Finger4 = models.CharField(verbose_name='Finger by finger flexion with assistance', max_length=60,
                                        blank=True, null=True)
    krpl_str_Separation = models.CharField(verbose_name='Separation of the fingers', max_length=60, blank=True,
                                           null=True)
    krpl_str_Adduction = models.CharField(verbose_name='Adduction of the hand with the elbow extended', max_length=60,
                                          blank=True, null=True)
    krpl_str_Pronation = models.CharField(verbose_name='Pronation of the hand with the elbow extended', max_length=60,
                                          blank=True, null=True)
    # KARPAL / FORCE / IZOMETRIK
    krpl_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Grip Strenght w/Miniball', max_length=60,
                                               blank=True, null=True)
    krpl_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Bottom-Up w/KB', max_length=60, blank=True,
                                               null=True)
    krpl_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Wrist Extension', max_length=60, blank=True,
                                               null=True)
    krpl_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric Wrist Extension', max_length=60, blank=True,
                                               null=True)
    krpl_frc_izm_Phalen = models.CharField(verbose_name='Phalen’s Test', max_length=60, blank=True, null=True)
    # KARPAL / FORCE /
    krpl_frc_iztnk_Wrist1 = models.CharField(verbose_name='Wrist Extension on Bench', max_length=60, blank=True,
                                             null=True)
    krpl_frc_iztnk_Wrist2 = models.CharField(verbose_name='Wrist Mobilization at Wall', max_length=60, blank=True,
                                             null=True)
    krpl_frc_iztnk_Mobil = models.CharField(verbose_name='Mobil Prayer Stretch', max_length=60, blank=True, null=True)
    krpl_frc_iztnk_Wrist3 = models.CharField(verbose_name='Wrist Extension', max_length=60, blank=True, null=True)
    krpl_frc_iztnk_Wrist4 = models.CharField(verbose_name='Wrist Extension', max_length=60, blank=True, null=True)
    krpl_frc_iztnk_Grip = models.CharField(verbose_name='Grip Strenght w/Miniball', max_length=60, blank=True,
                                           null=True)
    krpl_frc_iztnk_Wrist5 = models.CharField(verbose_name='Wrist Nerve Slider', max_length=60, blank=True, null=True)
    krpl_frc_iztnk_Dowel = models.CharField(verbose_name='Dowel Supination/Pronation', max_length=60, blank=True,
                                            null=True)
    krpl_frc_iztnk_Dynamic = models.CharField(verbose_name='Dynamic Pectoral Stretch on Longitudinal Foam Roller',
                                              max_length=60, blank=True, null=True)
    krpl_frc_iztnk_Scalene = models.CharField(verbose_name='Scalene Muscle Stretch (mobil)', max_length=60, blank=True,
                                              null=True)
    krpl_frc_iztnk_Seated = models.CharField(verbose_name='Seated Chin Tuck', max_length=60, blank=True, null=True)
    krpl_frc_iztnk_Quadruped = models.CharField(verbose_name='Quadruped T-Spine', max_length=60, blank=True, null=True)
    krpl_frc_iztnk_Median = models.CharField(verbose_name='Median Nerve Mobilization', max_length=60, blank=True,
                                             null=True)
    # WRIST / SMR
    wrst_smr_Wrist1 = models.CharField(verbose_name='Wrist Flexor SMR w/Foam Roller', max_length=60, blank=True,
                                       null=True)
    wrst_smr_Wrist2 = models.CharField(verbose_name='Wrist Flexor SMR w/Miniball', max_length=60, blank=True, null=True)
    wrst_smr_Wrist3 = models.CharField(verbose_name='Wrist Extensor SMR w/Foam Roller', max_length=60, blank=True,
                                       null=True)
    wrst_smr_Wrist4 = models.CharField(verbose_name='Wrist Extensor SMR w/Miniball', max_length=60, blank=True,
                                       null=True)
    # WRIST / STRETCHING
    wrst_str_Forearm = models.CharField(verbose_name='Forearm Extensor Stretch', max_length=60, blank=True, null=True)
    wrst_str_Standing1 = models.CharField(verbose_name='Standing Wall Elbow Flexor Stretch', max_length=60, blank=True,
                                          null=True)
    wrst_str_Elbow = models.CharField(verbose_name='Elbow Extensor (Anconeus) Stretch', max_length=60, blank=True,
                                      null=True)
    wrst_str_Standing2 = models.CharField(verbose_name='Standing Forearm Pronator Stretch', max_length=60, blank=True,
                                          null=True)
    wrst_str_Floor1 = models.CharField(verbose_name='Floor Wrist Extensor Stretch', max_length=60, blank=True,
                                       null=True)
    wrst_str_Floor2 = models.CharField(verbose_name='Floor Wrist Ulnar Deviator and Extensor Stretch', max_length=60,
                                       blank=True, null=True)
    wrst_str_Floor3 = models.CharField(verbose_name='Floor Wrist Radial Deviator and Extensor Stretch', max_length=60,
                                       blank=True, null=True)
    wrst_str_Wrist1 = models.CharField(verbose_name='Wrist Radial Deviator and Flexor Stretch', max_length=60,
                                       blank=True, null=True)
    wrst_str_Wrist2 = models.CharField(verbose_name='Wrist Ulnar Deviator and Flexor Stretch', max_length=60,
                                       blank=True, null=True)
    wrst_str_Finger1 = models.CharField(verbose_name='Finger Flexor Stretch', max_length=60, blank=True, null=True)
    wrst_str_Finger2 = models.CharField(verbose_name='Finger Extensor Stretch', max_length=60, blank=True, null=True)
    wrst_str_Frontal = models.CharField(verbose_name='Frontal Extension of the arms with finger', max_length=60,
                                        blank=True, null=True)
    wrst_str_Extension = models.CharField(verbose_name='Extension of the hands facing a Wall', max_length=60,
                                          blank=True, null=True)
    wrst_str_Flexion = models.CharField(verbose_name='Flexion of the hand with the forearm extended', max_length=60,
                                        blank=True, null=True)
    wrst_str_Finger3 = models.CharField(verbose_name='Finger by finger extension with assistance', max_length=60,
                                        blank=True, null=True)
    wrst_str_Finger4 = models.CharField(verbose_name='Finger by finger flexion with assistance', max_length=60,
                                        blank=True, null=True)
    wrst_str_Separation = models.CharField(verbose_name='Separation of the fingers', max_length=60, blank=True,
                                           null=True)
    wrst_str_Adduction = models.CharField(verbose_name='Adduction of the hand with the elbow extended', max_length=60,
                                          blank=True, null=True)
    wrst_str_Pronation = models.CharField(verbose_name='Pronation of the hand with the elbow extended', max_length=60,
                                          blank=True, null=True)
    # WRIST / FORCE / IZOMETRIK
    wrst_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Grip Strenght w/Miniball', max_length=60,
                                               blank=True, null=True)
    wrst_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Bottom-Up w/KB', max_length=60, blank=True,
                                               null=True)
    wrst_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Wrist Extension', max_length=60, blank=True,
                                               null=True)
    wrst_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric Wrist Extension', max_length=60, blank=True,
                                               null=True)
    # WRIST / FORCE / IZOTONIK
    wrst_frc_iztnk_Radial = models.CharField(verbose_name='Radial & Ulnar Deviation Palm Down', max_length=60,
                                             blank=True, null=True)
    wrst_frc_iztnk_Dumbbell = models.CharField(verbose_name='Dumbbell Supination/Pronation', max_length=60, blank=True,
                                               null=True)
    wrst_frc_iztnk_Wrist1 = models.CharField(verbose_name='Wrist Extension w/Dumbbell', max_length=60, blank=True,
                                             null=True)
    wrst_frc_iztnk_Wrist2 = models.CharField(verbose_name='Wrist Flexion w/Dumbbell', max_length=60, blank=True,
                                             null=True)
    wrst_frc_iztnk_Finger = models.CharField(verbose_name='Finger Spread', max_length=60, blank=True, null=True)
    wrst_frc_iztnk_Median = models.CharField(verbose_name='Median Nerve Glide', max_length=60, blank=True, null=True)
    wrst_frc_iztnk_Wrist3 = models.CharField(verbose_name='Wrist CARs', max_length=60, blank=True, null=True)
    wrst_frc_iztnk_Extension = models.CharField(verbose_name='Extension Rock Overs', max_length=60, blank=True,
                                                null=True)
    wrst_frc_iztnk_Dart = models.CharField(verbose_name='Dart Throwers', max_length=60, blank=True, null=True)
    # THUMB / SMR
    thmb_smr_Palm = models.CharField(verbose_name='Palm SMR w/Miniball', max_length=60, blank=True, null=True)
    # THUMB / FORCE / IZOTONIK
    thmb_frc_iztnk_Finger1 = models.CharField(verbose_name='Finger Duck', max_length=60, blank=True, null=True)
    thmb_frc_iztnk_Finger2 = models.CharField(verbose_name='Finger Curl', max_length=60, blank=True, null=True)
    thmb_frc_iztnk_Finger3 = models.CharField(verbose_name='Finger Squeeze', max_length=60, blank=True, null=True)
    thmb_frc_iztnk_Trace = models.CharField(verbose_name='Trace', max_length=60, blank=True, null=True)
    thmb_frc_iztnk_Splay = models.CharField(verbose_name='Splay', max_length=60, blank=True, null=True)
    #  MEDIAN /  SMR
    mdn_smr_Wrist1 = models.CharField(verbose_name='Wrist Flexor SMR w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    mdn_smr_Wrist2 = models.CharField(verbose_name='Wrist Flexor SMR w/Miniball', max_length=60, blank=True, null=True)
    mdn_smr_Wrist3 = models.CharField(verbose_name='Wrist Extensor SMR w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    mdn_smr_Wrist4 = models.CharField(verbose_name='Wrist Extensor SMR w/Miniball', max_length=60, blank=True,
                                      null=True)
    #  MEDIAN /  STRETCHING
    mdn_str_Standing1 = models.CharField(verbose_name='Standing Wall Elbow Flexor Stretch', max_length=60, blank=True,
                                         null=True)
    mdn_str_Elbow = models.CharField(verbose_name='Elbow Extensor (Anconeus) Stretch', max_length=60, blank=True,
                                     null=True)
    mdn_str_Standing2 = models.CharField(verbose_name='Standing Forearm Pronator Stretch', max_length=60, blank=True,
                                         null=True)
    mdn_str_Floor1 = models.CharField(verbose_name='Floor Wrist Extensor Stretch', max_length=60, blank=True, null=True)
    mdn_str_Floor2 = models.CharField(verbose_name='Floor Wrist Ulnar Deviator and Extensor Stretch', max_length=60,
                                      blank=True, null=True)
    mdn_str_Floor3 = models.CharField(verbose_name='Floor Wrist Radial Deviator and Extensor Stretch', max_length=60,
                                      blank=True, null=True)
    mdn_str_Wrist1 = models.CharField(verbose_name='Wrist Radial Deviator and Flexor Stretch', max_length=60,
                                      blank=True, null=True)
    mdn_str_Wrist2 = models.CharField(verbose_name='Wrist Ulnar Deviator and Flexor Stretch', max_length=60, blank=True,
                                      null=True)
    mdn_str_Finger1 = models.CharField(verbose_name='Finger Flexor Stretch', max_length=60, blank=True, null=True)
    mdn_str_Finger2 = models.CharField(verbose_name='Finger Extensor Stretch', max_length=60, blank=True, null=True)
    mdn_str_Frontal = models.CharField(verbose_name='Frontal Extension of the  arms with finger', max_length=60,
                                       blank=True, null=True)
    mdn_str_Extension = models.CharField(verbose_name='Extension of the hands facing a Wall', max_length=60, blank=True,
                                         null=True)
    mdn_str_Flexion = models.CharField(verbose_name='Flexion of the hand with the forearm extended', max_length=60,
                                       blank=True, null=True)
    mdn_str_Finger3 = models.CharField(verbose_name='Finger by finger extension with assistance', max_length=60,
                                       blank=True, null=True)
    mdn_str_Finger4 = models.CharField(verbose_name='Finger by finger flexion with assistance', max_length=60,
                                       blank=True, null=True)
    mdn_str_Separation = models.CharField(verbose_name='Separation of the fingers', max_length=60, blank=True,
                                          null=True)
    mdn_str_Adduction = models.CharField(verbose_name='Adduction of the hand with the elbow extended', max_length=60,
                                         blank=True, null=True)
    mdn_str_Pronation = models.CharField(verbose_name='Pronation of the hand with the elbow extended', max_length=60,
                                         blank=True, null=True)
    #  MEDIAN / FORCE / IZOMETRIK
    mdn_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Self Distraction', max_length=60, blank=True,
                                              null=True)
    mdn_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Band Wrist Distraction', max_length=60,
                                              blank=True, null=True)
    mdn_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Grip Strenght w/Miniball', max_length=60,
                                              blank=True, null=True)
    mdn_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric Bottom-Up w/KB', max_length=60, blank=True,
                                              null=True)
    mdn_frc_izm_Isometric5 = models.CharField(verbose_name='Isometric Wrist Extension', max_length=60, blank=True,
                                              null=True)
    mdn_frc_izm_Isometric6 = models.CharField(verbose_name='Isometric Wrist Extension', max_length=60, blank=True,
                                              null=True)
    #  MEDIAN / FORCE / IZOTONIK
    mdn_frc_iztnk_Band = models.CharField(verbose_name='Band Wrist Distraction', max_length=60, blank=True, null=True)
    mdn_frc_iztnk_Kettlebell = models.CharField(verbose_name='Kettlebell Wrist Supination/Pronation', max_length=60,
                                                blank=True, null=True)
    mdn_frc_iztnk_Quadruped = models.CharField(verbose_name='Quadruped Wrist Mobilization', max_length=60, blank=True,
                                               null=True)
    mdn_frc_iztnk_Wrist1 = models.CharField(verbose_name='Wrist Mobilization w/Band', max_length=60, blank=True,
                                            null=True)
    mdn_frc_iztnk_Wrist2 = models.CharField(verbose_name='Wrist Rockbacks', max_length=60, blank=True, null=True)
    mdn_frc_iztnk_Radial = models.CharField(verbose_name='Radial Deviation', max_length=60, blank=True, null=True)
    mdn_frc_iztnk_Ulnar1 = models.CharField(verbose_name='Ulnar Deviation Above', max_length=60, blank=True, null=True)
    mdn_frc_iztnk_Ulnar2 = models.CharField(verbose_name='Ulnar Deviation Below', max_length=60, blank=True, null=True)
    mdn_frc_iztnk_Supine = models.CharField(verbose_name='Supine KB Corkscrews', max_length=60, blank=True, null=True)
    mdn_frc_iztnk_Barbell = models.CharField(verbose_name='Barbell Wrist Extension', max_length=60, blank=True,
                                             null=True)
    mdn_frc_iztnk_Median1 = models.CharField(verbose_name='Median Nerve Mobilization', max_length=60, blank=True,
                                             null=True)
    mdn_frc_iztnk_Median2 = models.CharField(verbose_name='Median Nerve Moblization Variation 1', max_length=60,
                                             blank=True, null=True)

    class Meta:
        verbose_name = "Medikal Egzersiz"
        verbose_name_plural = "Medikal Egzersiz "


class medical_exercise5(models.Model):
    # ROTATOR / SMR
    rtt_smr_Supine = models.CharField(verbose_name='Supine Pose Miniball Rotators Glide', max_length=60, blank=True,
                                      null=True)
    rtt_smr_Prone = models.CharField(verbose_name='Prone Pose Miniball Shoulder Glide', max_length=60, blank=True,
                                     null=True)
    rtt_smr_Wall = models.CharField(verbose_name='Wall Rotators Glide w/Miniball', max_length=60, blank=True, null=True)
    rtt_smr_Standing = models.CharField(verbose_name='Standing Side Pose Shoulder SMR w/Miniball', max_length=60,
                                        blank=True, null=True)
    rtt_smr_Side = models.CharField(verbose_name='Side Lying Lateral Shoulder SMR w/Miniball', max_length=60,
                                    blank=True, null=True)
    # ROTATOR / STRETCHING
    rtt_str_Bench = models.CharField(verbose_name='Bench Overhead Stretch', max_length=60, blank=True, null=True)
    rtt_str_Foam = models.CharField(verbose_name='Foam Roller Prayer Stretch', max_length=60, blank=True, null=True)
    rtt_str_Swiss = models.CharField(verbose_name='Swiss Ball Prayer ', max_length=60, blank=True, null=True)
    rtt_str_Praying = models.CharField(verbose_name='Praying type, Quadruped extension', max_length=60, blank=True,
                                       null=True)
    rtt_str_Torso = models.CharField(verbose_name='Torso flexion, over a support w/Wall', max_length=60, blank=True,
                                     null=True)
    rtt_str_One = models.CharField(verbose_name='One-Arm Shoulder Flexor Stretch', max_length=60, blank=True, null=True)
    rtt_str_Horizontal = models.CharField(verbose_name='Horizontal Abduction of the arm', max_length=60, blank=True,
                                          null=True)
    rtt_str_Overhead = models.CharField(verbose_name='Overhead Arm Vertical Stretch', max_length=60, blank=True,
                                        null=True)
    rtt_str_Neck = models.CharField(verbose_name='Neck & Torso Flexion', max_length=60, blank=True, null=True)
    rtt_str_Forward = models.CharField(verbose_name='Forward Arm Ext.', max_length=60, blank=True, null=True)
    rtt_str_Crossing = models.CharField(verbose_name='Crossing The Arms Behind The Back', max_length=60, blank=True,
                                        null=True)
    rtt_str_Lying = models.CharField(verbose_name='Lying on Bench Ext. Rotation', max_length=60, blank=True, null=True)
    rtt_str_Seated = models.CharField(verbose_name='Seated Shoulder Flexor Depressor Retractor Stretch', max_length=60,
                                      blank=True, null=True)
    # ROTATOR / FORCE / IZOMETRIK
    rtt_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Seated External Rotation', max_length=60,
                                              blank=True, null=True)
    rtt_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Prone Horizontal Abduction', max_length=60,
                                              blank=True, null=True)
    rtt_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric 90/90 External Rotation', max_length=60,
                                              blank=True, null=True)
    rtt_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric Overhead Band Apart', max_length=60, blank=True,
                                              null=True)
    rtt_frc_izm_Variable = models.CharField(verbose_name='Variable Isometric', max_length=60, blank=True, null=True)
    # ROTATOR / FORCE / IZOTONIK
    rtt_frc_iztnk_Seated1 = models.CharField(verbose_name='Seated External Rotation w/Band', max_length=60, blank=True,
                                             null=True)
    rtt_frc_iztnk_Seated2 = models.CharField(verbose_name='Seated Ext. Rotation  and Lift Off w/Band', max_length=60,
                                             blank=True, null=True)
    rtt_frc_iztnk_Seated3 = models.CharField(verbose_name='Seated Ext. Rotation  and Full Scaption w/Band',
                                             max_length=60, blank=True, null=True)
    rtt_frc_iztnk_Side1 = models.CharField(verbose_name='Side Lying External Rotation', max_length=60, blank=True,
                                           null=True)
    rtt_frc_iztnk_Prone1 = models.CharField(verbose_name='Prone Horizontal Abduction', max_length=60, blank=True,
                                            null=True)
    rtt_frc_iztnk_90 = models.CharField(verbose_name='90/90 External Rotation', max_length=60, blank=True, null=True)
    rtt_frc_iztnk_Prone2 = models.CharField(verbose_name='Prone Clocks', max_length=60, blank=True, null=True)
    rtt_frc_iztnk_Standing1 = models.CharField(verbose_name='Standing External Rotation w/Band', max_length=60,
                                               blank=True, null=True)
    rtt_frc_iztnk_Standing2 = models.CharField(verbose_name='Standing Shoulder Uppercut w/Band', max_length=60,
                                               blank=True, null=True)
    rtt_frc_iztnk_Shoulder1 = models.CharField(verbose_name='Shoulder Uppercut and Dynamic  ‘’ER’’', max_length=60,
                                               blank=True, null=True)
    rtt_frc_iztnk_Plank = models.CharField(verbose_name='Plank and KB Carry', max_length=60, blank=True, null=True)
    rtt_frc_iztnk_Prone3 = models.CharField(verbose_name='Prone on Swiss Ball and Ball Drop', max_length=60, blank=True,
                                            null=True)
    rtt_frc_iztnk_Overhead = models.CharField(verbose_name='Overhead Reach w/Band', max_length=60, blank=True,
                                              null=True)
    rtt_frc_iztnk_Resisted1 = models.CharField(verbose_name='Resisted Uppercut', max_length=60, blank=True, null=True)
    rtt_frc_iztnk_Resisted2 = models.CharField(verbose_name='Resisted Punches', max_length=60, blank=True, null=True)
    rtt_frc_iztnk_Resisted3 = models.CharField(verbose_name='Resisted Flexion', max_length=60, blank=True, null=True)
    rtt_frc_iztnk_Side2 = models.CharField(verbose_name='Side Lying Flexion', max_length=60, blank=True, null=True)
    rtt_frc_iztnk_Bilateral = models.CharField(verbose_name='Bilateral External Rotation', max_length=60, blank=True,
                                               null=True)
    rtt_frc_iztnk_Face = models.CharField(verbose_name='Face Pulls', max_length=60, blank=True, null=True)
    rtt_frc_iztnk_Triple = models.CharField(verbose_name='Triple Threat', max_length=60, blank=True, null=True)
    rtt_frc_iztnk_Shoulder2 = models.CharField(verbose_name='Shoulder CARs on Wal', max_length=60, blank=True,
                                               null=True)
    rtt_frc_iztnk_Wall = models.CharField(verbose_name='Wall Thoracic Extension', max_length=60, blank=True, null=True)
    rtt_frc_iztnk_Seated4 = models.CharField(verbose_name='Seated Wall Angles', max_length=60, blank=True, null=True)
    rtt_frc_iztnk_External = models.CharField(verbose_name='External Rotation Walkouts', max_length=60, blank=True,
                                              null=True)
    rtt_frc_iztnk_Horizontal = models.CharField(verbose_name='Horizontal Abduction', max_length=60, blank=True,
                                                null=True)
    rtt_frc_iztnk_Leaning = models.CharField(verbose_name='Leaning Lateral Raise', max_length=60, blank=True, null=True)
    rtt_frc_iztnk_Straight = models.CharField(verbose_name='Straight arm Anterior Lat. Pull Down', max_length=60,
                                              blank=True, null=True)
    rtt_frc_iztnk_Prone4 = models.CharField(verbose_name='Prone 90/90  External Rotation', max_length=60, blank=True,
                                            null=True)
    # WING / SMR
    wng_smr_Side1 = models.CharField(verbose_name='Side Back Glide w/Foam Roller', max_length=60, blank=True, null=True)
    wng_smr_Side2 = models.CharField(verbose_name='Side Back Glide w/Mini Ball', max_length=60, blank=True, null=True)
    wng_smr_Supine = models.CharField(verbose_name='Supine Pose T-Spine Glide w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    wng_smr_Standing1 = models.CharField(verbose_name='Standing T-Spine Glide w/Mini Ball', max_length=60, blank=True,
                                         null=True)
    wng_smr_Standing2 = models.CharField(verbose_name='Standing T-Spine Glide w/Foam Roll', max_length=60, blank=True,
                                         null=True)
    wng_smr_T1 = models.CharField(verbose_name='T- Spine Glide on Longitudinal Foam Roller', max_length=60, blank=True,
                                  null=True)
    wng_smr_T2 = models.CharField(verbose_name='T-Spine Cross Friction', max_length=60, blank=True, null=True)
    # WING / STRETCHING
    wng_str_Bench = models.CharField(verbose_name='Bench Overhead Stretch ', max_length=60, blank=True, null=True)
    wng_str_Foam = models.CharField(verbose_name='Foam Roller Prayer Stretch', max_length=60, blank=True, null=True)
    wng_str_Swiss = models.CharField(verbose_name='Swiss Ball Prayer', max_length=60, blank=True, null=True)
    wng_str_One = models.CharField(verbose_name='One-Arm  Extended Stretch', max_length=60, blank=True, null=True)
    wng_str_Over = models.CharField(verbose_name='Over Head-Arm Vertical Extension', max_length=60, blank=True,
                                    null=True)
    wng_str_Quadruped = models.CharField(verbose_name='Quadruped Prayer Stretch ', max_length=60, blank=True, null=True)
    wng_str_Wall = models.CharField(verbose_name='Wall Support Thoracic Flexion', max_length=60, blank=True, null=True)
    wng_str_Standing = models.CharField(verbose_name='Standing Neck and Trunk Flexion', max_length=60, blank=True,
                                        null=True)
    wng_str_Forward = models.CharField(verbose_name='Forward Arm Extension', max_length=60, blank=True, null=True)
    wng_str_Crossing = models.CharField(verbose_name='Crossing The Arms Behind The Back', max_length=60, blank=True,
                                        null=True)
    wng_str_Lying = models.CharField(verbose_name='Lying on Bench Ext. Rotation', max_length=60, blank=True, null=True)
    wng_str_Seated = models.CharField(verbose_name='Seated Shoulder Flexor Depressor Retractor Stretch', max_length=60,
                                      blank=True, null=True)
    # WING / FORCE / IZOMETRIK
    wng_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Scapular Push-Up Protraction', max_length=60,
                                              blank=True, null=True)
    wng_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Scapular Push-Up Retraction', max_length=60,
                                              blank=True, null=True)
    wng_frc_izm_Foam = models.CharField(verbose_name='Foam Roller Plank', max_length=60, blank=True, null=True)
    wng_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Banded Lower  Trap Raise', max_length=60,
                                              blank=True, null=True)
    wng_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric “V” Wall', max_length=60, blank=True, null=True)
    wng_frc_izm_Isometric5 = models.CharField(verbose_name='Isometric Banded Scapular Push', max_length=60, blank=True,
                                              null=True)
    # WING / FORCE / IZOTONIK
    wng_frc_iztnk_Scapular1 = models.CharField(verbose_name='Scapular Push-Up', max_length=60, blank=True, null=True)
    wng_frc_iztnk_Prone = models.CharField(verbose_name='Prone Foam Roller Plank Roll Out', max_length=60, blank=True,
                                           null=True)
    wng_frc_iztnk_Cone = models.CharField(verbose_name='Cone Mobility', max_length=60, blank=True, null=True)
    wng_frc_iztnk_Quadruped1 = models.CharField(verbose_name='Quadruped Scapular Push/Round Shoulders Ceiling Pause',
                                                max_length=60, blank=True, null=True)
    wng_frc_iztnk_Elevated1 = models.CharField(verbose_name='Elevated Knee Quadruped Scapular Push-Up', max_length=60,
                                               blank=True, null=True)
    wng_frc_iztnk_Overhead = models.CharField(verbose_name='Overhead Back Press w/Band', max_length=60, blank=True,
                                              null=True)
    wng_frc_iztnk_Single = models.CharField(verbose_name='Single Leg Hip Hinge and Unilateral Y’s', max_length=60,
                                            blank=True, null=True)
    wng_frc_iztnk_Banded = models.CharField(verbose_name='Banded Lower Trap Raise', max_length=60, blank=True,
                                            null=True)
    wng_frc_iztnk_Shoulder = models.CharField(verbose_name='Shoulder Protraction+Upward Rotation Strength',
                                              max_length=60, blank=True, null=True)
    wng_frc_iztnk_Quadruped2 = models.CharField(verbose_name='Quadruped Scapular Prot. /Retrac. w/Banded',
                                                max_length=60, blank=True, null=True)
    wng_frc_iztnk_High = models.CharField(verbose_name='High Plank Knee Scapular Prot. /Retrac.33', max_length=60,
                                          blank=True, null=True)
    wng_frc_iztnk_Quadruped3 = models.CharField(verbose_name='Quadruped Rockback', max_length=60, blank=True, null=True)
    wng_frc_iztnk_Supine = models.CharField(verbose_name='Supine Ceiling Punches w/Dumbbell', max_length=60, blank=True,
                                            null=True)
    wng_frc_iztnk_Scapular2 = models.CharField(verbose_name='Scapular Push-Up on Bench', max_length=60, blank=True,
                                               null=True)
    wng_frc_iztnk_Quadruped4 = models.CharField(verbose_name='Quadruped Scapular Push-Up (Fists)', max_length=60,
                                                blank=True, null=True)
    wng_frc_iztnk_Quadruped5 = models.CharField(verbose_name='Quadruped Scapular Push-Up (Fists)', max_length=60,
                                                blank=True, null=True)
    wng_frc_iztnk_Kneeling = models.CharField(verbose_name='Kneeling Serratus Anterior  Banded Roll w/Foam Roller',
                                              max_length=60, blank=True, null=True)
    wng_frc_iztnk_Wall = models.CharField(verbose_name='Wall Slide Lift  Off w/Band', max_length=60, blank=True,
                                          null=True)
    wng_frc_iztnk_One1 = models.CharField(verbose_name='One-Arm  Serratus Anterior Push-Up w/Ped', max_length=60,
                                          blank=True, null=True)
    wng_frc_iztnk_Bear = models.CharField(verbose_name='Bear Crawl Reach', max_length=60, blank=True, null=True)
    wng_frc_iztnk_Plank = models.CharField(verbose_name='Plank Scapular Push-Up', max_length=60, blank=True, null=True)
    wng_frc_iztnk_Elevated2 = models.CharField(verbose_name='Elevated Feet Scapular Push-Up ', max_length=60,
                                               blank=True, null=True)
    wng_frc_iztnk_Scapular3 = models.CharField(verbose_name='Scapular Push-Up and Down Dog', max_length=60, blank=True,
                                               null=True)
    wng_frc_iztnk_Quadruped6 = models.CharField(verbose_name='Quadruped One Arm Scapular Push-Up', max_length=60,
                                                blank=True, null=True)
    wng_frc_iztnk_One2 = models.CharField(verbose_name='One Arm Scapular Push-Up', max_length=60, blank=True, null=True)
    wng_frc_iztnk_Serratus = models.CharField(verbose_name='Serratus Wall Slides', max_length=60, blank=True, null=True)
    wng_frc_iztnk_Spidermans = models.CharField(verbose_name='Spidermans', max_length=60, blank=True, null=True)
    wng_frc_iztnk_V1 = models.CharField(verbose_name='V Wall Slide', max_length=60, blank=True, null=True)
    wng_frc_iztnk_V2 = models.CharField(verbose_name='V Wall Slide with Lift Off', max_length=60, blank=True, null=True)
    wng_frc_iztnk_Resisted = models.CharField(verbose_name='Resisted V Wall Slide with Lift Off', max_length=60,
                                              blank=True, null=True)
    wng_frc_iztnk_Standing1 = models.CharField(verbose_name='Standing Banded Scapular Push', max_length=60, blank=True,
                                               null=True)
    wng_frc_iztnk_Standing2 = models.CharField(verbose_name='Standing Banded Scapular Push and Rotation', max_length=60,
                                               blank=True, null=True)
    # SKOLYOZ/STRETCHING
    sklyz_str_Lateral = models.CharField(verbose_name='Lateral Chain Stretch (Lat and QL)', max_length=60, blank=True,
                                         null=True)
    sklyz_str_Standing = models.CharField(verbose_name='Standing S-Curve Stretch', max_length=60, blank=True, null=True)
    sklyz_str_C = models.CharField(verbose_name='C-Curve Stretch', max_length=60, blank=True, null=True)
    # SKOLYOZ/FORCE/IZOMETRIK
    sklyz_izm_Isometric = models.CharField(verbose_name='Isometric Bird Dog', max_length=60, blank=True, null=True)
    sklyz_izm_Half = models.CharField(verbose_name='Half Kneeling Side Plank', max_length=60, blank=True, null=True)
    sklyz_izm_Side = models.CharField(verbose_name='Side Plank', max_length=60, blank=True, null=True)
    sklyz_izm_Prone = models.CharField(verbose_name='Prone Plank', max_length=60, blank=True, null=True)
    sklyz_izm_Landmine = models.CharField(verbose_name='Landmine Sideplank', max_length=60, blank=True, null=True)
    # SKOLYOZ/FORCE/IZOTONIK
    sklyz_frc_iztnk_Supine = models.CharField(verbose_name='Supine Lumbar Rocks', max_length=60, blank=True, null=True)
    sklyz_frc_iztnk_Thoracic = models.CharField(verbose_name='Thoracic CARs', max_length=60, blank=True, null=True)
    sklyz_frc_iztnk_Side1 = models.CharField(verbose_name='Side Lying T-Spine Rotation w/Band', max_length=60,
                                             blank=True, null=True)
    sklyz_frc_iztnk_Single = models.CharField(verbose_name='Single Arm Farmers Carry', max_length=60, blank=True,
                                              null=True)
    sklyz_frc_iztnk_Knee = models.CharField(verbose_name='Knee to Elbow Bird Dog', max_length=60, blank=True, null=True)
    sklyz_frc_iztnk_Side2 = models.CharField(verbose_name='Side Plank Thread the Needle', max_length=60, blank=True,
                                             null=True)
    sklyz_frc_iztnk_Cable = models.CharField(verbose_name='Cable Twisters', max_length=60, blank=True, null=True)
    sklyz_frc_iztnk_Standing = models.CharField(verbose_name='Standing Pallof Press w/Cable or Band', max_length=60,
                                                blank=True, null=True)
    sklyz_frc_iztnk_Kneeling = models.CharField(verbose_name='½ Kneeling Pallof Press w/Cable or Band', max_length=60,
                                                blank=True, null=True)
    sklyz_frc_iztnk_Lunge = models.CharField(verbose_name='Lunge Stance Landmine Rotation', max_length=60, blank=True,
                                             null=True)
    sklyz_frc_iztnk_Elbow = models.CharField(verbose_name='Elbow Plank Arm Reach', max_length=60, blank=True, null=True)
    sklyz_frc_iztnk_Punch = models.CharField(verbose_name='Punch and Rotation w/Band', max_length=60, blank=True,
                                             null=True)
    sklyz_frc_iztnk_Quadruped = models.CharField(verbose_name='Quadruped T-Spine Roll w/Foam Roller', max_length=60,
                                                 blank=True, null=True)
    sklyz_frc_iztnk_T = models.CharField(verbose_name='T-Spine Rotation on Knee and Hand', max_length=60, blank=True,
                                         null=True)
    # ANKILOZAN/SMR
    ankl_smr_Side1 = models.CharField(verbose_name='Side Back Glide w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    ankl_smr_Side2 = models.CharField(verbose_name='Side Back Glide w/Mini Ball', max_length=60, blank=True, null=True)
    ankl_smr_Supine = models.CharField(verbose_name='Supine Pose T-Spine Glide w/Foam Roller', max_length=60,
                                       blank=True, null=True)
    ankl_smr_Standing1 = models.CharField(verbose_name='Standing T-Spine Glide w/Mini Ball', max_length=60, blank=True,
                                          null=True)
    ankl_smr_Standing2 = models.CharField(verbose_name='Standing T-Spine Glide w/Mini Ball', max_length=60, blank=True,
                                          null=True)
    ankl_smr_Standing3 = models.CharField(verbose_name='Standing T-Spine Glide w/Foam Roller', max_length=60,
                                          blank=True, null=True)
    ankl_smr_T1 = models.CharField(verbose_name='T- Spine Glide on Longitudinal Foam Roller', max_length=60, blank=True,
                                   null=True)
    ankl_smr_T2 = models.CharField(verbose_name='T-Spine Cross Friction', max_length=60, blank=True, null=True)
    # ANKILOZAN/STRETCHING
    ankl_str_Supine = models.CharField(verbose_name='Supine Pose Hamstring Stretch w/RB', max_length=60, blank=True,
                                       null=True)
    ankl_str_Standing1 = models.CharField(verbose_name='Standing Quad Stretch with Nerve Mobilization', max_length=60,
                                          blank=True, null=True)
    ankl_str_Kneeling = models.CharField(verbose_name='½ Kneeling Hip Flexor Stretch', max_length=60, blank=True,
                                         null=True)
    ankl_str_Standing2 = models.CharField(verbose_name='Standing Hip Flexor Stretch', max_length=60, blank=True,
                                          null=True)
    ankl_str_Child = models.CharField(verbose_name='Child’s Pose', max_length=60, blank=True, null=True)
    ankl_str_Glute = models.CharField(verbose_name='Glute/Priformis Stretch', max_length=60, blank=True, null=True)
    # ANKILOZAN/FORCE/IZOMETRIK
    ankl_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Bird Dog', max_length=60, blank=True, null=True)
    ankl_frc_izm_Side = models.CharField(verbose_name='Side Plank', max_length=60, blank=True, null=True)
    ankl_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Dead Bug', max_length=60, blank=True, null=True)
    ankl_frc_izm_Bridge = models.CharField(verbose_name='Bridge with Posterior Pelvic Tilt', max_length=60, blank=True,
                                           null=True)
    # ANKILOZAN/FORCE/IZOTONIK
    ankl_frc_iztnk_Marching = models.CharField(verbose_name='Marching Bridge (Keep Pelvis Stable)', max_length=60,
                                               blank=True, null=True)
    ankl_frc_iztnk_Lower = models.CharField(verbose_name='Lower Abdominal March (Keep Back Flat)', max_length=60,
                                            blank=True, null=True)
    ankl_frc_iztnk_Abdominal = models.CharField(verbose_name='Abdominal Ball Roll', max_length=60, blank=True,
                                                null=True)
    ankl_frc_iztnk_Bird = models.CharField(verbose_name='Bird Dog', max_length=60, blank=True, null=True)
    ankl_frc_iztnk_Supine1 = models.CharField(verbose_name='Supine 90-90 Pullovers', max_length=60, blank=True,
                                              null=True)
    ankl_frc_iztnk_Dead = models.CharField(verbose_name='Dead Bug w/Swissball', max_length=60, blank=True, null=True)
    ankl_frc_iztnk_Supine2 = models.CharField(verbose_name='Supine Alternating Leg Lowering', max_length=60, blank=True,
                                              null=True)
    ankl_frc_iztnk_Child = models.CharField(verbose_name='Child’s Pose (Mobil)', max_length=60, blank=True, null=True)
    ankl_frc_iztnk_Standing = models.CharField(verbose_name='Standing Posterior Pelvic Tilt', max_length=60, blank=True,
                                               null=True)
    ankl_frc_iztnk_Press = models.CharField(verbose_name='Press Ups', max_length=60, blank=True, null=True)
    ankl_frc_iztnk_Femoral = models.CharField(verbose_name='Femoral Nerve Mobilization', max_length=60, blank=True,
                                              null=True)
    ankl_frc_iztnk_Siatic = models.CharField(verbose_name='Siatic Nerve Mobilization', max_length=60, blank=True,
                                             null=True)
    ankl_frc_iztnk_Supin = models.CharField(verbose_name='Supin Pelvic Tilt', max_length=60, blank=True, null=True)

    class Meta:
        verbose_name = "Medikal Egzersiz"
        verbose_name_plural = "Medikal Egzersiz "


class medical_exercise6(models.Model):
    # SPINAL/SMR
    spnl_smr_Side1 = models.CharField(verbose_name='Side Back Glide w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    spnl_smr_Side2 = models.CharField(verbose_name='Side Back Glide w/Mini Ball', max_length=60, blank=True, null=True)
    spnl_smr_Supine = models.CharField(verbose_name='Supine Pose T-Spine Glide w/Foam Roller', max_length=60,
                                       blank=True, null=True)
    spnl_smr_Standing1 = models.CharField(verbose_name='Standing T-Spine Glide w/Mini Ball', max_length=60, blank=True,
                                          null=True)
    spnl_smr_Standing2 = models.CharField(verbose_name='Standing T-Spine Glide w/Foam Roll', max_length=60, blank=True,
                                          null=True)
    spnl_smr_T1 = models.CharField(verbose_name='T- Spine Glide on Longitudinal Foam Roller', max_length=60, blank=True,
                                   null=True)
    spnl_smr_T2 = models.CharField(verbose_name='T-Spine Cross Friction', max_length=60, blank=True, null=True)
    # SPINAL/STRETCHING
    spnl_str_T = models.CharField(verbose_name='T-Spine Ext. w/Wall', max_length=60, blank=True, null=True)
    spnl_str_Seated = models.CharField(verbose_name='Seated Erector Spine Stretch', max_length=60, blank=True,
                                       null=True)
    spnl_str_Butterfly = models.CharField(verbose_name='Butterfly Pose', max_length=60, blank=True, null=True)
    spnl_str_Bridge = models.CharField(verbose_name='Bridge Pose', max_length=60, blank=True, null=True)
    spnl_str_Cat = models.CharField(verbose_name='Cat Pose', max_length=60, blank=True, null=True)
    spnl_str_Cow = models.CharField(verbose_name='Cow Pose', max_length=60, blank=True, null=True)
    spnl_str_Cobra = models.CharField(verbose_name='Cobra Pose', max_length=60, blank=True, null=True)
    spnl_str_Downward = models.CharField(verbose_name='Downward Facing Dog Pose', max_length=60, blank=True, null=True)
    spnl_str_Locust = models.CharField(verbose_name='Locust Pose', max_length=60, blank=True, null=True)
    spnl_str_Pigeon = models.CharField(verbose_name='Pigeon Pose', max_length=60, blank=True, null=True)
    spnl_str_Triangle = models.CharField(verbose_name='Triangle Pose', max_length=60, blank=True, null=True)
    spnl_str_Couch = models.CharField(verbose_name='Couch Stretch', max_length=60, blank=True, null=True)
    spnl_str_Bretzel = models.CharField(verbose_name='Bretzel Stretch', max_length=60, blank=True, null=True)
    spnl_str_Kneeling = models.CharField(verbose_name='1/2 Kneeling Hip Flexor Stretch', max_length=60, blank=True,
                                         null=True)
    spnl_str_Quadruped = models.CharField(verbose_name='Quadruped Posterior Hip Stretch', max_length=60, blank=True,
                                          null=True)
    # SPINAL/FORCE/IZOMETRIK
    spnl_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Bird Dog', max_length=60, blank=True, null=True)
    spnl_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Glute Bridge', max_length=60, blank=True,
                                               null=True)
    spnl_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Ball Bridge', max_length=60, blank=True,
                                               null=True)
    spnl_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric Superman’s', max_length=60, blank=True,
                                               null=True)
    spnl_frc_izm_Inverted = models.CharField(verbose_name='Inverted Chinese Plank', max_length=60, blank=True,
                                             null=True)
    spnl_frc_izm_Isometric5 = models.CharField(verbose_name='Isometric Child Pose', max_length=60, blank=True,
                                               null=True)
    spnl_frc_izm_Isometric6 = models.CharField(verbose_name='Isometric Supine Posterior Pelvic Tilt + Cross Body',
                                               max_length=60, blank=True, null=True)
    # SPINAL/FORCE/IZOTONIK
    spnl_frc_iztnk_Prone1 = models.CharField(verbose_name='Prone Press Up on Elbow', max_length=60, blank=True,
                                             null=True)
    spnl_frc_iztnk_Prone2 = models.CharField(verbose_name='Prone Press Up on Hand', max_length=60, blank=True,
                                             null=True)
    spnl_frc_iztnk_Bird = models.CharField(verbose_name='Bird Dog (Mobil)', max_length=60, blank=True, null=True)
    spnl_frc_iztnk_Superman = models.CharField(verbose_name='Superman’s (Mobil)', max_length=60, blank=True, null=True)
    spnl_frc_iztnk_Glute = models.CharField(verbose_name='Glute Bridge', max_length=60, blank=True, null=True)
    spnl_frc_iztnk_Ball1 = models.CharField(verbose_name='Ball Bridge', max_length=60, blank=True, null=True)
    spnl_frc_iztnk_Hip = models.CharField(verbose_name='Hip Thruster', max_length=60, blank=True, null=True)
    spnl_frc_iztnk_T = models.CharField(verbose_name='T-Spine Extension Wall Mobilization', max_length=60, blank=True,
                                        null=True)
    spnl_frc_iztnk_Up = models.CharField(verbose_name='Up Dog Lumbar Extension', max_length=60, blank=True, null=True)
    spnl_frc_iztnk_Back = models.CharField(verbose_name='Back Extension on Swissball', max_length=60, blank=True,
                                           null=True)
    spnl_frc_iztnk_Standing = models.CharField(verbose_name='Standing Back Extension to Wall', max_length=60,
                                               blank=True, null=True)
    spnl_frc_iztnk_Ball2 = models.CharField(verbose_name='Ball Back Extension', max_length=60, blank=True, null=True)
    spnl_frc_iztnk_Ball3 = models.CharField(verbose_name='Ball Bird Dog', max_length=60, blank=True, null=True)
    spnl_frc_iztnk_Ball4 = models.CharField(verbose_name='Ball Triple Threat', max_length=60, blank=True, null=True)
    spnl_frc_iztnk_Cat = models.CharField(verbose_name='Cat & Camel', max_length=60, blank=True, null=True)
    spnl_frc_iztnk_Supine = models.CharField(verbose_name='Supine Posterior Pelvic Til', max_length=60, blank=True,
                                             null=True)
    spnl_frc_iztnk_Position1 = models.CharField(verbose_name='3 Position Pause Back Squat', max_length=60, blank=True,
                                                null=True)
    spnl_frc_iztnk_Position2 = models.CharField(verbose_name='2 Position Pause Sumo Deadlift', max_length=60,
                                                blank=True, null=True)
    # LOWER / SMR
    lwr_smr_Longiditunal = models.CharField(verbose_name='Longiditunal Foam Roller SMR for Priformis', max_length=60,
                                            blank=True, null=True)
    lwr_smr_Cross1 = models.CharField(verbose_name='Cross Leg Priformis  SMR w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    lwr_smr_Adductors1 = models.CharField(verbose_name='Adductors SMR w/Foam Roller', max_length=60, blank=True,
                                          null=True)
    lwr_smr_Adductors2 = models.CharField(verbose_name='Adductors SMR w/Miniball', max_length=60, blank=True, null=True)
    lwr_smr_Straight = models.CharField(verbose_name='Straight Leg Adductors SMR w/Foam Roller', max_length=60,
                                        blank=True, null=True)
    lwr_smr_Alternating = models.CharField(verbose_name='Alternating Adductors SMR', max_length=60, blank=True,
                                           null=True)
    lwr_smr_Side1 = models.CharField(verbose_name='Side Lying IT-Band SMR W/Foam Roller', max_length=60, blank=True,
                                     null=True)
    lwr_smr_IT = models.CharField(verbose_name='IT-Band  SMR Alternative', max_length=60, blank=True, null=True)
    lwr_smr_Side2 = models.CharField(verbose_name='Side Lying IT-Band SMR w/Mini Ball', max_length=60, blank=True,
                                     null=True)
    lwr_smr_TFL = models.CharField(verbose_name='TFL SMR w/Miniball', max_length=60, blank=True, null=True)
    lwr_smr_Two1 = models.CharField(verbose_name='Two Leg on Foam Roller Hamstring SMR', max_length=60, blank=True,
                                    null=True)
    lwr_smr_One1 = models.CharField(verbose_name='One-Leg Hamstring SMR', max_length=60, blank=True, null=True)
    lwr_smr_Cross2 = models.CharField(verbose_name='Cross Leg Hamstring Hamstring SMR', max_length=60, blank=True,
                                      null=True)
    lwr_smr_Seated = models.CharField(verbose_name='Seated Hamstring SMR SMR w/Mini Ball', max_length=60, blank=True,
                                      null=True)
    lwr_smr_One2 = models.CharField(verbose_name='One-Leg Calf SMR w/Foam Roller', max_length=60, blank=True, null=True)
    lwr_smr_Cross3 = models.CharField(verbose_name='Cross Leg Calf SMR w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    lwr_smr_Two2 = models.CharField(verbose_name='Two Leg On Foam Roller Calf SMR', max_length=60, blank=True,
                                    null=True)
    lwr_smr_Calf = models.CharField(verbose_name='Calf SMR W/Mini Ball', max_length=60, blank=True, null=True)
    lwr_smr_Hip = models.CharField(verbose_name='Hip Flexors SMR w/Foam Roller', max_length=60, blank=True, null=True)
    # LOWER / STRETCHING
    lwr_str_Seated = models.CharField(verbose_name='Seated Figure ‘’4’’ Stretch', max_length=60, blank=True, null=True)
    lwr_str_Supine1 = models.CharField(verbose_name='Supine Figure ‘’4’’ Stretch', max_length=60, blank=True, null=True)
    lwr_str_Gluteus = models.CharField(verbose_name='Gluteus Stretch', max_length=60, blank=True, null=True)
    lwr_str_Kneeling = models.CharField(verbose_name='½ Kneeling Psoas Stretch', max_length=60, blank=True, null=True)
    lwr_str_Standing = models.CharField(verbose_name='Standing Hamstring Stretch', max_length=60, blank=True, null=True)
    lwr_str_QL = models.CharField(verbose_name='90/90 QL Stretch', max_length=60, blank=True, null=True)
    lwr_str_Ragdoll = models.CharField(verbose_name='Ragdoll', max_length=60, blank=True, null=True)
    lwr_str_Low = models.CharField(verbose_name='Low Lunge', max_length=60, blank=True, null=True)
    lwr_str_Half = models.CharField(verbose_name='Half Split', max_length=60, blank=True, null=True)
    lwr_str_Marichyasana = models.CharField(verbose_name='Marichyasana C', max_length=60, blank=True, null=True)
    lwr_str_Child = models.CharField(verbose_name='Child’s Pose', max_length=60, blank=True, null=True)
    lwr_str_Downward = models.CharField(verbose_name='Downward Dog', max_length=60, blank=True, null=True)
    lwr_str_Supine2 = models.CharField(verbose_name='Supine Pigeon', max_length=60, blank=True, null=True)
    # LOWER / FORCE / IZOMETRIK
    lwr_frc_izm_Side = models.CharField(verbose_name='Side Plank', max_length=60, blank=True, null=True)
    lwr_frc_izm_Half = models.CharField(verbose_name='Half Knee Side Plan', max_length=60, blank=True, null=True)
    lwr_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Bird Dog', max_length=60, blank=True, null=True)
    lwr_frc_izm_Prone = models.CharField(verbose_name='Prone Plank', max_length=60, blank=True, null=True)
    lwr_frc_izm_Bridge = models.CharField(verbose_name='Bridge (Isometric)', max_length=60, blank=True, null=True)
    lwr_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Prone Shoulder Squeeze w/Neck Recraction',
                                              max_length=60, blank=True, null=True)
    # LOWER / FORCE / IZOTONIK
    lwr_frc_iztnk_Thoracic = models.CharField(verbose_name='Thoracic-Lumbar Gaping w/Neural Mobility', max_length=60,
                                              blank=True, null=True)
    lwr_frc_iztnk_Lumbar = models.CharField(verbose_name='Lumbar Cat & Camel', max_length=60, blank=True, null=True)
    lwr_frc_iztnk_Active = models.CharField(verbose_name='Active Hip 90/90', max_length=60, blank=True, null=True)
    lwr_frc_iztnk_Hip1 = models.CharField(verbose_name='Hip CARs', max_length=60, blank=True, null=True)
    lwr_frc_iztnk_Bird = models.CharField(verbose_name='Bird-Dog', max_length=60, blank=True, null=True)
    lwr_frc_iztnk_Good = models.CharField(verbose_name='Good Mornings', max_length=60, blank=True, null=True)
    lwr_frc_iztnk_Single1 = models.CharField(verbose_name='Single Leg Hip + 2 point Taps', max_length=60, blank=True,
                                             null=True)
    lwr_frc_iztnk_Side1 = models.CharField(verbose_name='Side Plank + Hip Abduction', max_length=60, blank=True,
                                           null=True)
    lwr_frc_iztnk_Dead = models.CharField(verbose_name='Dead Bug w/Stability Ball', max_length=60, blank=True,
                                          null=True)
    lwr_frc_iztnk_Single2 = models.CharField(verbose_name='Single Leg Deadlift + KB Passes', max_length=60, blank=True,
                                             null=True)
    lwr_frc_iztnk_Prone1 = models.CharField(verbose_name='Prone Plank Alternating Hip Abduction', max_length=60,
                                            blank=True, null=True)
    lwr_frc_iztnk_Side2 = models.CharField(verbose_name='Side Plank with Twist', max_length=60, blank=True, null=True)
    lwr_frc_iztnk_Lower1 = models.CharField(verbose_name='Lower Trunk Rotation w/Swiss Ball', max_length=60, blank=True,
                                            null=True)
    lwr_frc_iztnk_Hip2 = models.CharField(verbose_name='Hip Hinge', max_length=60, blank=True, null=True)
    lwr_frc_iztnk_Side3 = models.CharField(verbose_name='Side Step w/Band', max_length=60, blank=True, null=True)
    lwr_frc_iztnk_Reverse = models.CharField(verbose_name='Reverse Fly w/Band', max_length=60, blank=True, null=True)
    lwr_frc_iztnk_Press = models.CharField(verbose_name='Press Up on Elbow', max_length=60, blank=True, null=True)
    lwr_frc_iztnk_Supine = models.CharField(verbose_name='Supine Siatic Nerve Glide', max_length=60, blank=True,
                                            null=True)
    lwr_frc_iztnk_Lower2 = models.CharField(verbose_name='Lower Turunk Rocking', max_length=60, blank=True, null=True)
    lwr_frc_iztnk_upine = models.CharField(verbose_name='upine Posterior Pelvic Tilt (Mobil)', max_length=60,
                                           blank=True, null=True)
    lwr_frc_iztnk_Bridge = models.CharField(verbose_name='Bridge (Mobil)', max_length=60, blank=True, null=True)
    lwr_frc_iztnk_Prone = models.CharField(verbose_name='Prone Shoulder Squeeze w/Neck Recraction', max_length=60,
                                           blank=True, null=True)
    lwr_frc_iztnk_Cat = models.CharField(verbose_name='Cat Cow (Variations)', max_length=60, blank=True, null=True)
    # POSTERIOR / SMR
    pst_smr_Longiditunal = models.CharField(verbose_name='Longiditunal Foam Roller SMR for Priformis', max_length=60,
                                            blank=True, null=True)
    pst_smr_Cross1 = models.CharField(verbose_name='Cross Leg Priformis SMR w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    pst_smr_Adductors1 = models.CharField(verbose_name='Adductors SMR w/Foam Roller', max_length=60, blank=True,
                                          null=True)
    pst_smr_Adductors2 = models.CharField(verbose_name='Adductors SMR w/Miniball', max_length=60, blank=True, null=True)
    pst_smr_Straight = models.CharField(verbose_name='Straight Leg Adductors SMR w/Foam Roller', max_length=60,
                                        blank=True, null=True)
    pst_smr_Alternating = models.CharField(verbose_name='Alternating Adductors SMR', max_length=60, blank=True,
                                           null=True)
    pst_smr_Side1 = models.CharField(verbose_name='Side Lying IT-Band SMR W/Foam Roller', max_length=60, blank=True,
                                     null=True)
    pst_smr_IT = models.CharField(verbose_name='IT-Band SMR Alternative', max_length=60, blank=True, null=True)
    pst_smr_Side2 = models.CharField(verbose_name='Side Lying IT-Band SMR w/Mini Ball', max_length=60, blank=True,
                                     null=True)
    pst_smr_TFL = models.CharField(verbose_name='TFL SMR w/Miniball', max_length=60, blank=True, null=True)
    pst_smr_Two1 = models.CharField(verbose_name='Two Leg on Foam Roller Hamstring SMR', max_length=60, blank=True,
                                    null=True)
    pst_smr_One1 = models.CharField(verbose_name='One-Leg Hamstring SMR', max_length=60, blank=True, null=True)
    pst_smr_Cross2 = models.CharField(verbose_name='Cross Leg Hamstring SMR w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    pst_smr_Seated = models.CharField(verbose_name='Seated Hamstring SMR w/Mini Ball', max_length=60, blank=True,
                                      null=True)
    pst_smr_One2 = models.CharField(verbose_name='One-Leg Calf SMR w/Foam Roller', max_length=60, blank=True, null=True)
    pst_smr_Cross3 = models.CharField(verbose_name='Cross Leg Calf SMR w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    pst_smr_Two2 = models.CharField(verbose_name='Two Leg On Foam Roller Calf SMR', max_length=60, blank=True,
                                    null=True)
    pst_smr_Calf = models.CharField(verbose_name='Calf SMR W/Mini Ball', max_length=60, blank=True, null=True)
    pst_smr_Hip = models.CharField(verbose_name='Hip Flexors SMR w/Foam Roller', max_length=60, blank=True, null=True)
    # POSTERIOR / STRETCHING
    pst_str_Seated = models.CharField(verbose_name='Seated Figure ‘’4’’ Stretch', max_length=60, blank=True, null=True)
    pst_str_Supine1 = models.CharField(verbose_name='Supine Figure ‘’4’’ Stretch', max_length=60, blank=True, null=True)
    pst_str_Gluteus = models.CharField(verbose_name='Gluteus Stretch', max_length=60, blank=True, null=True)
    pst_str_Kneeling = models.CharField(verbose_name='½ Kneeling Psoas Stretch', max_length=60, blank=True, null=True)
    pst_str_Standing = models.CharField(verbose_name='Standing Hamstring Stretch', max_length=60, blank=True, null=True)
    pst_str_90 = models.CharField(verbose_name='90/90 QL Stretch', max_length=60, blank=True, null=True)
    pst_str_Ragdoll = models.CharField(verbose_name='Ragdoll', max_length=60, blank=True, null=True)
    pst_str_Low = models.CharField(verbose_name='Low Lunge', max_length=60, blank=True, null=True)
    pst_str_Half = models.CharField(verbose_name='Half Split', max_length=60, blank=True, null=True)
    pst_str_Marichyasana = models.CharField(verbose_name='Marichyasana C', max_length=60, blank=True, null=True)
    pst_str_Child = models.CharField(verbose_name='Child’s Pose', max_length=60, blank=True, null=True)
    pst_str_Downward = models.CharField(verbose_name='Downward Dog', max_length=60, blank=True, null=True)
    pst_str_Supine2 = models.CharField(verbose_name='Supine Pigeon', max_length=60, blank=True, null=True)
    # POSTERIOR / FORCE / IZOMETRIK
    pst_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Hip Flexion/Extension', max_length=60, blank=True,
                                              null=True)
    pst_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Bird Dog', max_length=60, blank=True, null=True)
    pst_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Dead Bug', max_length=60, blank=True, null=True)
    pst_frc_izm_Prone = models.CharField(verbose_name='Prone Plank', max_length=60, blank=True, null=True)
    pst_frc_izm_Side = models.CharField(verbose_name='Side Plank', max_length=60, blank=True, null=True)
    pst_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric Birdge on Stability Ball', max_length=60,
                                              blank=True, null=True)
    pst_frc_izm_Isometric5 = models.CharField(verbose_name='Isometric Kneeling Pallof Press', max_length=60, blank=True,
                                              null=True)
    # POSTERIOR / FORCE / IZOTONIK
    pst_frc_iztnk_Standing = models.CharField(verbose_name='Standing Hip Flexion w/Band', max_length=60, blank=True,
                                              null=True)
    pst_frc_iztnk_Cook = models.CharField(verbose_name='Cook Bridge', max_length=60, blank=True, null=True)
    pst_frc_iztnk_Bent = models.CharField(verbose_name='Bent Knee Fall Out', max_length=60, blank=True, null=True)
    pst_frc_iztnk_Bridge = models.CharField(verbose_name='Bridge on Stability Ball', max_length=60, blank=True,
                                            null=True)
    pst_frc_iztnk_Kneeling = models.CharField(verbose_name='Kneeling Pallof Press', max_length=60, blank=True,
                                              null=True)
    pst_frc_iztnk_Supine = models.CharField(verbose_name='Supine Hooklying Anterior-Posterior Tilt', max_length=60,
                                            blank=True, null=True)
    pst_frc_iztnk_Quadruped1 = models.CharField(verbose_name='Quadruped Anterior-Posterior Tilt', max_length=60,
                                                blank=True, null=True)
    pst_frc_iztnk_Quadruped2 = models.CharField(verbose_name='Quadruped Thoracic Locked Anterior-Posterior Tilt',
                                                max_length=60, blank=True, null=True)
    pst_frc_iztnk_Quadruped3 = models.CharField(verbose_name='Quadruped Over Swissball Anterior-Posterior Tilt',
                                                max_length=60, blank=True, null=True)
    pst_frc_iztnk_Sitting = models.CharField(verbose_name='Sitting Anterior-Posterior Tilt', max_length=60, blank=True,
                                             null=True)

    class Meta:
        verbose_name = "Medikal Egzersiz"
        verbose_name_plural = "Medikal Egzersiz "


class medical_exercise7(models.Model):
    spn_smr_Side1 = models.CharField(verbose_name='Side Back Glide w/Foam Roller', max_length=60, blank=True, null=True)
    spn_smr_Side2 = models.CharField(verbose_name='Side Back Glide w/Mini Ball', max_length=60, blank=True, null=True)
    spn_smr_Supine = models.CharField(verbose_name='Supine Pose T-Spine Glide w/Foam Rolle', max_length=60, blank=True,
                                      null=True)
    spn_smr_Standing1 = models.CharField(verbose_name='Standing T-Spine Glide w/Mini Ball', max_length=60, blank=True,
                                         null=True)
    spn_smr_Standing2 = models.CharField(verbose_name='Standing T-Spine Glide w/Foam Roll', max_length=60, blank=True,
                                         null=True)
    spn_smr_T1 = models.CharField(verbose_name='T- Spine Glide on Longitudinal Foam Roller', max_length=60, blank=True,
                                  null=True)
    spn_smr_T2 = models.CharField(verbose_name='T-Spine Cross Friction', max_length=60, blank=True, null=True)

    spn_str_Seated = models.CharField(verbose_name='Seated Erector Spine Stretch', max_length=60, blank=True, null=True)
    spn_str_Wall = models.CharField(verbose_name='Wall T-Spine Extension Stretch', max_length=60, blank=True, null=True)
    spn_str_Butterfly = models.CharField(verbose_name='Butterfly Pose', max_length=60, blank=True, null=True)
    spn_str_Bridge = models.CharField(verbose_name='Bridge Pose', max_length=60, blank=True, null=True)
    spn_str_Cat = models.CharField(verbose_name='Cat Pose', max_length=60, blank=True, null=True)
    spn_str_Cow = models.CharField(verbose_name='Cow Pose', max_length=60, blank=True, null=True)
    spn_str_Cobra = models.CharField(verbose_name='Cobra Pose', max_length=60, blank=True, null=True)
    spn_str_Downward = models.CharField(verbose_name='Downward Facing Dog Pose', max_length=60, blank=True, null=True)
    spn_str_Locust = models.CharField(verbose_name='Locust Pose', max_length=60, blank=True, null=True)
    spn_str_Pigeon = models.CharField(verbose_name='Pigeon Pose', max_length=60, blank=True, null=True)
    spn_str_Triangle = models.CharField(verbose_name='Triangle Pose', max_length=60, blank=True, null=True)
    spn_str_Couch = models.CharField(verbose_name='Couch Stretch', max_length=60, blank=True, null=True)
    spn_str_Bretzel = models.CharField(verbose_name='Bretzel Stretch', max_length=60, blank=True, null=True)
    spn_str_Kneeling = models.CharField(verbose_name='1/2 Kneeling Hip Flexor Stretch', max_length=60, blank=True,
                                        null=True)
    spn_str_Quadruped = models.CharField(verbose_name='Quadruped Posterior Hip Stretch', max_length=60, blank=True,
                                         null=True)

    spn_frc_iztnk_Kneeling1 = models.CharField(verbose_name='Kneeling T-Spine Rotation', max_length=60, blank=True,
                                               null=True)
    spn_frc_iztnk_Seated1 = models.CharField(verbose_name='Seated Thoracic Extension', max_length=60, blank=True,
                                             null=True)
    spn_frc_iztnk_Cat = models.CharField(verbose_name='Cat & Cow', max_length=60, blank=True, null=True)
    spn_frc_iztnk_Dead = models.CharField(verbose_name='Dead Bug', max_length=60, blank=True, null=True)
    spn_frc_iztnk_Bird = models.CharField(verbose_name='Bird Dog', max_length=60, blank=True, null=True)
    spn_frc_iztnk_Kneeling2 = models.CharField(verbose_name='½ Kneeling Open Book', max_length=60, blank=True,
                                               null=True)
    spn_frc_iztnk_Kneeling3 = models.CharField(verbose_name='½ Kneeling Wall Rotation', max_length=60, blank=True,
                                               null=True)
    spn_frc_iztnk_Child = models.CharField(verbose_name='Child Pose Arm Rotation', max_length=60, blank=True, null=True)
    spn_frc_iztnk_Lower = models.CharField(verbose_name='Lower Trunk Rotation', max_length=60, blank=True, null=True)
    spn_frc_iztnk_Long = models.CharField(verbose_name='Long Sitting Hip Int./Ext. Rotation', max_length=60, blank=True,
                                          null=True)
    spn_frc_iztnk_Knee = models.CharField(verbose_name='Knee Across Chest-Dynamic', max_length=60, blank=True,
                                          null=True)
    spn_frc_iztnk_Prone1 = models.CharField(verbose_name='Prone T-Spine Extension', max_length=60, blank=True,
                                            null=True)
    spn_frc_iztnk_Seated2 = models.CharField(verbose_name='Seated Wall Angel', max_length=60, blank=True, null=True)
    spn_frc_iztnk_Supine = models.CharField(verbose_name='Supine Lumbar Rocks', max_length=60, blank=True, null=True)
    spn_frc_iztnk_Prone2 = models.CharField(verbose_name='Prone Scorpion Kickovers', max_length=60, blank=True,
                                            null=True)
    spn_frc_iztnk_Seated3 = models.CharField(verbose_name='Seated Cat & Cow', max_length=60, blank=True, null=True)
    spn_frc_iztnk_Quadruped = models.CharField(verbose_name='Quadruped Thoracic Rotation', max_length=60, blank=True,
                                               null=True)
    spn_frc_iztnk_Standing = models.CharField(verbose_name='Standing Back Bend to Wall', max_length=60, blank=True,
                                              null=True)
    spn_frc_iztnk_Plank = models.CharField(verbose_name='Plank Spine Waves', max_length=60, blank=True, null=True)
    spn_frc_iztnk_Kneeling4 = models.CharField(verbose_name='Kneeling Lateral Spine Reaches', max_length=60, blank=True,
                                               null=True)
    spn_frc_iztnk_Kneeling5 = models.CharField(verbose_name='Kneeling Spine Extension Reach Backs', max_length=60,
                                               blank=True, null=True)
    # LUMBOPELVIK / SMR
    lmb_smr_Longiditunal = models.CharField(verbose_name='Longiditunal Foam Roller SMR for Priformis', max_length=60,
                                            blank=True, null=True)
    lmb_smr_Cross1 = models.CharField(verbose_name='Cross Leg Priformis SMR w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    lmb_smr_Adductors1 = models.CharField(verbose_name='Adductors SMR w/Foam Roller', max_length=60, blank=True,
                                          null=True)
    lmb_smr_Adductors2 = models.CharField(verbose_name='Adductors SMR w/Miniball', max_length=60, blank=True, null=True)
    lmb_smr_Straight = models.CharField(verbose_name='Straight Leg Adductors SMR w/Foam Roller', max_length=60,
                                        blank=True, null=True)
    lmb_smr_Alternating = models.CharField(verbose_name='Alternating Adductors SMR', max_length=60, blank=True,
                                           null=True)
    lmb_smr_Side1 = models.CharField(verbose_name='Side Lying IT-Band SMR W/Foam Roller', max_length=60, blank=True,
                                     null=True)
    lmb_smr_IT = models.CharField(verbose_name='IT-Band SMR Alternative', max_length=60, blank=True, null=True)
    lmb_smr_Side2 = models.CharField(verbose_name='Side Lying IT-Band SMR w/Mini Ball', max_length=60, blank=True,
                                     null=True)
    lmb_smr_TFL = models.CharField(verbose_name='TFL SMR w/Miniball', max_length=60, blank=True, null=True)
    lmb_smr_Two1 = models.CharField(verbose_name='Two Leg on Foam Roller Hamstring SMR', max_length=60, blank=True,
                                    null=True)
    lmb_smr_One1 = models.CharField(verbose_name='One-Leg Hamstring SMR', max_length=60, blank=True, null=True)
    lmb_smr_Cross2 = models.CharField(verbose_name='Cross Leg Hamstring SMR w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    lmb_smr_Seated = models.CharField(verbose_name='Seated Hamstring SMR w/Mini Ball', max_length=60, blank=True,
                                      null=True)
    lmb_smr_One2 = models.CharField(verbose_name='One-Leg Calf SMR w/Foam Roller', max_length=60, blank=True, null=True)
    lmb_smr_Cross3 = models.CharField(verbose_name='Cross Leg Calf SMR w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    lmb_smr_Two2 = models.CharField(verbose_name='Two Leg On Foam Roller Calf SMR', max_length=60, blank=True,
                                    null=True)
    lmb_smr_Calf = models.CharField(verbose_name='Calf SMR W/Mini Ball', max_length=60, blank=True, null=True)
    lmb_smr_Hip = models.CharField(verbose_name='Hip Flexors SMR w/Foam Roller', max_length=60, blank=True, null=True)
    # LUMBOPELVIK / STRETCHING
    lmb_str_Butterfly = models.CharField(verbose_name='Butterfly Pose', max_length=60, blank=True, null=True)
    lmb_str_Bridge = models.CharField(verbose_name='Bridge Pose', max_length=60, blank=True, null=True)
    lmb_str_Cat = models.CharField(verbose_name='Cat Pose', max_length=60, blank=True, null=True)
    lmb_str_Cow = models.CharField(verbose_name='Cow Pose', max_length=60, blank=True, null=True)
    lmb_str_Cobra = models.CharField(verbose_name='Cobra Pose', max_length=60, blank=True, null=True)
    lmb_str_Downward = models.CharField(verbose_name='Downward Facing Dog Pose', max_length=60, blank=True, null=True)
    lmb_str_Locust = models.CharField(verbose_name='Locust Pose', max_length=60, blank=True, null=True)
    lmb_str_Pigeon = models.CharField(verbose_name='Pigeon Pose', max_length=60, blank=True, null=True)
    lmb_str_Triangle = models.CharField(verbose_name='Triangle Pose', max_length=60, blank=True, null=True)
    lmb_str_Couch = models.CharField(verbose_name='Couch Stretch', max_length=60, blank=True, null=True)
    lmb_str_Bretzel = models.CharField(verbose_name='Bretzel Stretch', max_length=60, blank=True, null=True)
    lmb_str_Kneeling = models.CharField(verbose_name='1/2 Kneeling Hip Flexor Stretch', max_length=60, blank=True,
                                        null=True)
    lmb_str_Quadruped = models.CharField(verbose_name='Quadruped Posterior Hip Stretch', max_length=60, blank=True,
                                         null=True)
    # LUMBOPELVIK / FORCE / IZOMETRIK
    lmb_frc_izm_Side = models.CharField(verbose_name='Side Plank', max_length=60, blank=True, null=True)
    lmb_frc_izm_Prone = models.CharField(verbose_name='Prone Plank', max_length=60, blank=True, null=True)
    lmb_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Bird Dog', max_length=60, blank=True, null=True)
    lmb_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Dead Bug', max_length=60, blank=True, null=True)
    lmb_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Pallof Press', max_length=60, blank=True,
                                              null=True)
    # LUMBOPELVIK / FORCE / IZOTONIK
    lmb_frc_iztnk_Dynamic = models.CharField(verbose_name='Dynamic Frog', max_length=60, blank=True, null=True)
    lmb_frc_iztnk_Supine = models.CharField(verbose_name='Supine Hip Internal Rotation', max_length=60, blank=True,
                                            null=True)
    lmb_frc_iztnk_Hip1 = models.CharField(verbose_name='Hip Switch', max_length=60, blank=True, null=True)
    lmb_frc_iztnk_Hip2 = models.CharField(verbose_name='Hip Abduction Liftover', max_length=60, blank=True, null=True)
    lmb_frc_iztnk_Rocker = models.CharField(verbose_name='Rocker to Up Dog', max_length=60, blank=True, null=True)
    lmb_frc_iztnk_Down = models.CharField(verbose_name='Down Dog + Upper and Lower Reach', max_length=60, blank=True,
                                          null=True)
    lmb_frc_iztnk_Cat = models.CharField(verbose_name='Cat & Cow', max_length=60, blank=True, null=True)
    lmb_frc_iztnk_Beast = models.CharField(verbose_name='Beast Crawl', max_length=60, blank=True, null=True)
    lmb_frc_iztnk_Ipsilateral = models.CharField(verbose_name='İpsilateral Dead Bug w/Band', max_length=60, blank=True,
                                                 null=True)
    lmb_frc_iztnk_Single = models.CharField(verbose_name='Single Leg Balance and Rotation', max_length=60, blank=True,
                                            null=True)
    lmb_frc_iztnk_Side = models.CharField(verbose_name='Side Lying Hip CAR’s', max_length=60, blank=True, null=True)
    lmb_frc_iztnk_Barbell = models.CharField(verbose_name='Barbell Unilateral Bias Rotation', max_length=60, blank=True,
                                             null=True)
    #  DIASTAZIS / FORCE / IZOMETRIK
    dst_frc_izm_Side = models.CharField(verbose_name='Side Plank Hold', max_length=60, blank=True, null=True)
    dst_frc_izm_Weighted = models.CharField(verbose_name='Weighted Side Plank', max_length=60, blank=True, null=True)
    dst_frc_iztnk_Wall1 = models.CharField(verbose_name='Wall Dead Bug', max_length=60, blank=True, null=True)
    dst_frc_iztnk_Supine1 = models.CharField(verbose_name='Supine Foot Tap (Dead Bug Pose)', max_length=60, blank=True,
                                             null=True)
    dst_frc_iztnk_Wall2 = models.CharField(verbose_name='Wall Bridge', max_length=60, blank=True, null=True)
    dst_frc_iztnk_Single1 = models.CharField(verbose_name='Single Leg Bridge', max_length=60, blank=True, null=True)
    dst_frc_iztnk_Active = models.CharField(verbose_name='Active Side Plank Lift', max_length=60, blank=True, null=True)
    dst_frc_iztnk_Bear = models.CharField(verbose_name='Bear Crawl Squeeze Ball  (Knee up/Down)', max_length=60,
                                          blank=True, null=True)
    dst_frc_iztnk_Banded1 = models.CharField(verbose_name='Banded Bridge Pull', max_length=60, blank=True, null=True)
    dst_frc_iztnk_Banded2 = models.CharField(verbose_name='Banded Single Leg Pull', max_length=60, blank=True,
                                             null=True)
    dst_frc_iztnk_Supine2 = models.CharField(verbose_name='Supine Heel Drop', max_length=60, blank=True, null=True)
    dst_frc_iztnk_Contralateral = models.CharField(verbose_name='Contralateral Dead Bug (Squeeze Foam Roller)',
                                                   max_length=60, blank=True, null=True)
    dst_frc_iztnk_Adductor = models.CharField(verbose_name='Adductor Bridge (Squeeze Ped)', max_length=60, blank=True,
                                              null=True)
    dst_frc_iztnk_Kneeling = models.CharField(verbose_name='½ Kneeling Pallof Press', max_length=60, blank=True,
                                              null=True)
    dst_frc_iztnk_Single2 = models.CharField(verbose_name='Single Leg Deadlift', max_length=60, blank=True, null=True)
    dst_frc_iztnk_Supine3 = models.CharField(verbose_name='Supine Knee to Floor', max_length=60, blank=True, null=True)
    dst_frc_iztnk_Ipsilateral = models.CharField(verbose_name='İpsilateral Dead Bug', max_length=60, blank=True,
                                                 null=True)
    # GLUTEAL / SMR
    gltl_smr_Longiditunal = models.CharField(verbose_name='Longiditunal Foam Roller SMR for Priformis', max_length=60,
                                             blank=True, null=True)
    gltl_smr_Cross1 = models.CharField(verbose_name='Cross Leg Priformis SMR w/Foam Roller', max_length=60, blank=True,
                                       null=True)
    gltl_smr_Adductors1 = models.CharField(verbose_name='Adductors SMR w/Foam Roller', max_length=60, blank=True,
                                           null=True)
    gltl_smr_Adductors2 = models.CharField(verbose_name='Adductors SMR w/Miniball', max_length=60, blank=True,
                                           null=True)
    gltl_smr_Straight = models.CharField(verbose_name='Straight Leg Adductors SMR  w/Foam Roller', max_length=60,
                                         blank=True, null=True)
    gltl_smr_Alternating = models.CharField(verbose_name='Alternating Adductors SMR', max_length=60, blank=True,
                                            null=True)
    gltl_smr_Side1 = models.CharField(verbose_name='Side Lying IT-Band SMR W/Foam Roller', max_length=60, blank=True,
                                      null=True)
    gltl_smr_IT = models.CharField(verbose_name='IT-Band SMR Alternative', max_length=60, blank=True, null=True)
    gltl_smr_Side2 = models.CharField(verbose_name='Side Lying IT-Band SMR w/Mini Ball', max_length=60, blank=True,
                                      null=True)
    gltl_smr_TFL = models.CharField(verbose_name='TFL SMR w/Miniball', max_length=60, blank=True, null=True)
    gltl_smr_Two1 = models.CharField(verbose_name='Two Leg on Foam  Roller Hamstring SMR', max_length=60, blank=True,
                                     null=True)
    gltl_smr_One1 = models.CharField(verbose_name='One-Leg Hamstring SMR', max_length=60, blank=True, null=True)
    gltl_smr_Cross2 = models.CharField(verbose_name='Cross Leg Hamstring SMR w/Foam Roller', max_length=60, blank=True,
                                       null=True)
    gltl_smr_Seated = models.CharField(verbose_name='Seated Hamstring SMR w/Mini Ball', max_length=60, blank=True,
                                       null=True)
    gltl_smr_One2 = models.CharField(verbose_name='One-Leg Calf SMR w/Foam Roller', max_length=60, blank=True,
                                     null=True)
    gltl_smr_Cross3 = models.CharField(verbose_name='Cross Leg Calf SMR w/Foam Roller', max_length=60, blank=True,
                                       null=True)
    gltl_smr_Two2 = models.CharField(verbose_name='Two Leg On Foam Roller Calf SMR ', max_length=60, blank=True,
                                     null=True)
    gltl_smr_Calf = models.CharField(verbose_name='Calf SMR W/Mini Ball', max_length=60, blank=True, null=True)
    gltl_smr_Hip = models.CharField(verbose_name='Hip Flexors SMR w/Foam Roller', max_length=60, blank=True, null=True)
    # GLUTEAL / STRETCHING
    gltl_str_Seated1 = models.CharField(verbose_name='Seated One-Leg Extended Leg Hip Stretch', max_length=60,
                                        blank=True, null=True)
    gltl_str_Standing1 = models.CharField(verbose_name='Standing Hip External Rotator Stretch', max_length=60,
                                          blank=True, null=True)
    gltl_str_Recumbent1 = models.CharField(verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch',
                                           max_length=60, blank=True, null=True)
    gltl_str_Recumbent2 = models.CharField(
        verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch (Cross Leg)',
        max_length=70, blank=True, null=True)
    gltl_str_L = models.CharField(verbose_name='L-Sit Cross Leg- Priformis Stretch', max_length=60, blank=True,
                                  null=True)
    gltl_str_Standing2 = models.CharField(verbose_name='Standing Bent-Knee Hip Adductor Stretch', max_length=60,
                                          blank=True, null=True)
    gltl_str_Seated2 = models.CharField(verbose_name='Seated Hip Adductor Stretch', max_length=60, blank=True,
                                        null=True)
    gltl_str_Standing3 = models.CharField(verbose_name='Standing Raised-Leg Hip Adductor Stretch', max_length=60,
                                          blank=True, null=True)
    gltl_str_Standing4 = models.CharField(verbose_name='Standing Knee Flexor Stretch', max_length=60, blank=True,
                                          null=True)
    gltl_str_Seated3 = models.CharField(verbose_name='Seated Knee Flexor Stretch ', max_length=60, blank=True,
                                        null=True)
    gltl_str_Raised = models.CharField(verbose_name='Raised- One Leg Knee Flexor Stretch', max_length=60, blank=True,
                                       null=True)
    gltl_str_Supine1 = models.CharField(verbose_name='Supine Lying Raised One-Leg Stretch w/Band', max_length=60,
                                        blank=True, null=True)
    gltl_str_Supine2 = models.CharField(verbose_name='Supine Lying Raised One-Leg Stretch w/Band', max_length=60,
                                        blank=True, null=True)
    gltl_str_One1 = models.CharField(verbose_name='One-Leg ½ Kneeling Knee Extensor Stretch', max_length=60, blank=True,
                                     null=True)
    gltl_str_One2 = models.CharField(verbose_name='One-Leg Standing  Hip Flexor and Knee Extensor Stretch',
                                     max_length=60, blank=True, null=True)
    gltl_str_Lying = models.CharField(verbose_name='Lying Hip Flexor and Knee Extensor Stretch', max_length=60,
                                      blank=True, null=True)
    gltl_str_Supine3 = models.CharField(verbose_name='Supine Pose Lower-Trunk Flexor Stretch', max_length=60,
                                        blank=True, null=True)
    gltl_str_Prone = models.CharField(verbose_name='Prone Pose Lower-Trunk Flexor Stretch', max_length=60, blank=True,
                                      null=True)
    gltl_str_Seated4 = models.CharField(verbose_name='Seated Lower-Trunk Extensor Stretch', max_length=60, blank=True,
                                        null=True)
    gltl_str_Standing5 = models.CharField(verbose_name='Standing Lower-Trunk Lateral Flexor Stretch', max_length=60,
                                          blank=True, null=True)
    gltl_str_Standing6 = models.CharField(verbose_name='Standing Lower-Trunk Flexor Stretch (Arched Back)',
                                          max_length=60, blank=True, null=True)
    gltl_str_Lower = models.CharField(verbose_name='Lower-Trunk Lateral Flexor Stretch (Arched Back)', max_length=60,
                                      blank=True, null=True)
    gltl_str_Supine4 = models.CharField(verbose_name='Supine Lying Side Bend (Oscar Moran-208)', max_length=60,
                                        blank=True, null=True)
    gltl_str_Open = models.CharField(verbose_name='Open Leg Side Bend ', max_length=60, blank=True, null=True)
    # GLUTEAL / FORCE / IZOMETRIK
    gltl_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Bridge', max_length=60, blank=True, null=True)
    gltl_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Hip Thrust', max_length=60, blank=True,
                                               null=True)
    gltl_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Wall Squat', max_length=60, blank=True,
                                               null=True)
    # GLUTEAL / FORCE / IZOTONIK
    gltl_frc_iztnk_Hip1 = models.CharField(verbose_name='Hip Internal Rotation', max_length=60, blank=True, null=True)
    gltl_frc_iztnk_Rotation1 = models.CharField(verbose_name='90/90 Hip Rotation', max_length=60, blank=True, null=True)
    gltl_frc_iztnk_Prone = models.CharField(verbose_name='Prone Hip Internal Rotation', max_length=60, blank=True,
                                            null=True)
    gltl_frc_iztnk_Rotation2 = models.CharField(verbose_name='90/90 Hip Rotation (Advanced)', max_length=60, blank=True,
                                                null=True)
    gltl_frc_iztnk_Deep = models.CharField(verbose_name='Deep Squat with Twist', max_length=60, blank=True, null=True)
    gltl_frc_iztnk_Kneeling1 = models.CharField(verbose_name='½ Kneeling Hip Flexor to Hamstring', max_length=60,
                                                blank=True, null=True)
    gltl_frc_iztnk_Adductor = models.CharField(verbose_name='Adductor Rockbacks', max_length=60, blank=True, null=True)
    gltl_frc_iztnk_Quadruped1 = models.CharField(verbose_name='Quadruped Hip Mobilization (Banded Pull)', max_length=60,
                                                 blank=True, null=True)
    gltl_frc_iztnk_Active = models.CharField(verbose_name='Active Hip 90/90', max_length=60, blank=True, null=True)
    gltl_frc_iztnk_Hip2 = models.CharField(verbose_name='Hip Hinge (Banded Pull)', max_length=60, blank=True, null=True)
    gltl_frc_iztnk_Standing1 = models.CharField(verbose_name='Standing Hip Airplane (with Twist)', max_length=60,
                                                blank=True, null=True)
    gltl_frc_iztnk_Quadruped2 = models.CharField(verbose_name='Quadruped Hip Internal Mobilization (Banded Pull)',
                                                 max_length=60, blank=True, null=True)
    gltl_frc_iztnk_Hip3 = models.CharField(verbose_name='Hip Multi-Directional Mobilization (Banded Pull)',
                                           max_length=60, blank=True, null=True)
    gltl_frc_iztnk_Hip4 = models.CharField(verbose_name='Hip Extension Mobilization', max_length=60, blank=True,
                                           null=True)
    gltl_frc_iztnk_Supine = models.CharField(verbose_name='Supine Flexion Mobilization', max_length=60, blank=True,
                                             null=True)
    gltl_frc_iztnk_Quaruped = models.CharField(verbose_name='Quaruped Hip Car’s', max_length=60, blank=True, null=True)
    gltl_frc_iztnk_Kneeling2 = models.CharField(verbose_name='½ Kneeling Hip Car’s', max_length=60, blank=True,
                                                null=True)
    gltl_frc_iztnk_Single = models.CharField(verbose_name='Single Kneeling Straight Leg Hip Car’s', max_length=60,
                                             blank=True, null=True)
    gltl_frc_iztnk_Standing2 = models.CharField(verbose_name='Standing Hip Car’s', max_length=60, blank=True, null=True)
    gltl_frc_iztnk_Foot = models.CharField(verbose_name='Foot Elevated Single Hip Thrust', max_length=60, blank=True,
                                           null=True)
    gltl_frc_iztnk_Hand = models.CharField(verbose_name='Hand Supported Sinle Leg Deadlift', max_length=60, blank=True,
                                           null=True)
    gltl_frc_iztnk_Hip5 = models.CharField(verbose_name='Hip Step-Up', max_length=60, blank=True, null=True)
    gltl_frc_iztnk_Cross = models.CharField(verbose_name='Cross Over Step Up', max_length=60, blank=True, null=True)
    gltl_frc_iztnk_Rotation3 = models.CharField(verbose_name='90/90 Hip  Rotation (no hand)', max_length=60, blank=True,
                                                null=True)
    gltl_frc_iztnk_Resisted = models.CharField(verbose_name='Resisted 90/90 Hip Thrust', max_length=60, blank=True,
                                               null=True)

    class Meta:
        verbose_name = "Medikal Egzersiz"
        verbose_name_plural = "Medikal Egzersiz "


class medical_exercise8(models.Model):
    # HIP / SMR
    hp_smr_Longiditunal = models.CharField(verbose_name='Longiditunal Foam Roller SMR for Priformis', max_length=60,
                                           blank=True, null=True)
    hp_smr_Cross1 = models.CharField(verbose_name='Cross Leg Priformis SMR w/Foam Roller', max_length=60, blank=True,
                                     null=True)
    hp_smr_Adductors1 = models.CharField(verbose_name='Adductors SMR w/Foam Roller', max_length=60, blank=True,
                                         null=True)
    hp_smr_Adductors2 = models.CharField(verbose_name='Adductors SMR w/Miniball', max_length=60, blank=True, null=True)
    hp_smr_Straight = models.CharField(verbose_name='Straight Leg Adductors SMR w/Foam Roller', max_length=60,
                                       blank=True, null=True)
    hp_smr_Alternating = models.CharField(verbose_name='Alternating Adductors SMR', max_length=60, blank=True,
                                          null=True)
    hp_smr_IT = models.CharField(verbose_name='IT-Band SMR Alternative', max_length=60, blank=True, null=True)
    hp_smr_Side = models.CharField(verbose_name='Side Lying IT-Band SMR w/Mini Ball', max_length=60, blank=True,
                                   null=True)
    hp_smr_TFL = models.CharField(verbose_name='TFL SMR w/Miniball', max_length=60, blank=True, null=True)
    hp_smr_Two1 = models.CharField(verbose_name='Two Leg on Foam Roller Hamstring SMR', max_length=60, blank=True,
                                   null=True)
    hp_smr_One1 = models.CharField(verbose_name='One-Leg Hamstring SMR', max_length=60, blank=True, null=True)
    hp_smr_Cross2 = models.CharField(verbose_name='Cross Leg Hamstring SMR w/Foam Roller', max_length=60, blank=True,
                                     null=True)
    hp_smr_Seated = models.CharField(verbose_name='Seated Hamstring SMR w/Mini Ball', max_length=60, blank=True,
                                     null=True)
    hp_smr_One2 = models.CharField(verbose_name='One-Leg Calf SMR w/Foam Roller', max_length=60, blank=True, null=True)
    hp_smr_Cross3 = models.CharField(verbose_name='Cross Leg Calf SMR w/Foam Roller', max_length=60, blank=True,
                                     null=True)
    hp_smr_Two2 = models.CharField(verbose_name='Two Leg On Foam Roller Calf SMR', max_length=60, blank=True, null=True)
    hp_smr_Calf = models.CharField(verbose_name='Calf SMR W/Mini Ball', max_length=60, blank=True, null=True)
    hp_smr_Hip = models.CharField(verbose_name='Hip Flexors SMR w/Foam Roller', max_length=60, blank=True, null=True)
    hp_str_Seated1 = models.CharField(verbose_name='Seated One-Leg Extended Leg Hip Stretch', max_length=60, blank=True,
                                      null=True)
    hp_str_Standing1 = models.CharField(verbose_name='Standing Hip External Rotator Stretch', max_length=60, blank=True,
                                        null=True)
    hp_str_Recumbent1 = models.CharField(verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch',
                                         max_length=60, blank=True, null=True)
    hp_str_Recumbent2 = models.CharField(
        verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch (Cross Leg)',
        max_length=70, blank=True, null=True)
    hp_str_L = models.CharField(verbose_name='L-Sit Cross Leg- Priformis Stretch', max_length=60, blank=True, null=True)
    hp_str_Standing2 = models.CharField(verbose_name='Standing Bent-Knee Hip Adductor Stretch', max_length=60,
                                        blank=True, null=True)
    hp_str_Seated2 = models.CharField(verbose_name='Seated Hip Adductor Stretch', max_length=60, blank=True, null=True)
    hp_str_Standing3 = models.CharField(verbose_name='Standing Raised-Leg Hip Adductor Stretch', max_length=60,
                                        blank=True, null=True)
    hp_str_Standing4 = models.CharField(verbose_name='Standing Knee Flexor Stretch', max_length=60, blank=True,
                                        null=True)
    hp_str_Seated3 = models.CharField(verbose_name='Seated Knee Flexor Stretch', max_length=60, blank=True, null=True)
    hp_str_Raised = models.CharField(verbose_name='Raised- One Leg Knee Flexor Stretch', max_length=60, blank=True,
                                     null=True)
    hp_str_Supine1 = models.CharField(verbose_name='Supine Lying Raised One-Leg Stretch w/Band', max_length=60,
                                      blank=True, null=True)
    hp_str_Seated4 = models.CharField(verbose_name='Seated Wide Range Extended Leg Stretch', max_length=60, blank=True,
                                      null=True)
    hp_str_One1 = models.CharField(verbose_name='One-Leg ½ Kneeling Knee Extensor Stretch', max_length=60, blank=True,
                                   null=True)
    hp_str_One2 = models.CharField(verbose_name='One-Leg Standing Hip Flexor and Knee Extensor Stretch', max_length=60,
                                   blank=True, null=True)
    hp_str_Lying = models.CharField(verbose_name='Lying Hip Flexor and Knee Extensor Stretch', max_length=60,
                                    blank=True, null=True)
    hp_str_Supine2 = models.CharField(verbose_name='Supine Pose Lower-Trunk Flexor Stretch', max_length=60, blank=True,
                                      null=True)
    hp_str_Prone = models.CharField(verbose_name='Prone Pose Lower-Trunk Flexor Stretch', max_length=60, blank=True,
                                    null=True)
    hp_str_Seated5 = models.CharField(verbose_name='Seated Lower-Trunk Extensor Stretch', max_length=60, blank=True,
                                      null=True)
    hp_str_Standing5 = models.CharField(verbose_name='Standing Lower-Trunk Lateral Flexor Stretch', max_length=60,
                                        blank=True, null=True)
    hp_str_Standing6 = models.CharField(verbose_name='Standing Lower-Trunk Flexor Stretch (Arched Back)', max_length=60,
                                        blank=True, null=True)
    hp_str_Lower = models.CharField(verbose_name='Lower-Trunk Lateral Flexor Stretch (Arched Back)', max_length=60,
                                    blank=True, null=True)
    hp_str_Supine3 = models.CharField(verbose_name='Supine Lying Side Bend (Oscar Moran-208)', max_length=60,
                                      blank=True, null=True)
    hp_str_Open = models.CharField(verbose_name='Open Leg Side Bend ', max_length=60, blank=True, null=True)
    hp_str_Glute = models.CharField(verbose_name='Glute Stretch', max_length=60, blank=True, null=True)
    hp_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Side Lying Hip Abduction w/Band', max_length=60,
                                             blank=True, null=True)
    hp_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Single Leg Hip Thrust', max_length=60, blank=True,
                                             null=True)
    hp_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Hip Thrust', max_length=60, blank=True, null=True)
    hp_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric Single Leg Bridge', max_length=60, blank=True,
                                             null=True)
    hp_frc_izm_Isometric5 = models.CharField(verbose_name='Isometric Banded Squat', max_length=60, blank=True,
                                             null=True)
    hp_frc_izm_Side = models.CharField(verbose_name='Side Plank', max_length=60, blank=True, null=True)
    hp_frc_iztnk_Side1 = models.CharField(verbose_name='Side Lying Resisted Hip Squares Rotation', max_length=60,
                                          blank=True, null=True)
    hp_frc_iztnk_Single1 = models.CharField(verbose_name='Single Leg Hip Thrust w/Swissball', max_length=60, blank=True,
                                            null=True)
    hp_frc_iztnk_Resisted = models.CharField(verbose_name='Resisted Side Stepping', max_length=60, blank=True,
                                             null=True)
    hp_frc_iztnk_Single2 = models.CharField(verbose_name='Single Blance Hip Hinge Cone Tap', max_length=60, blank=True,
                                            null=True)
    hp_frc_iztnk_Lateral = models.CharField(verbose_name='Lateral Lunge w/Weight', max_length=60, blank=True, null=True)
    hp_frc_iztnk_Standing1 = models.CharField(verbose_name='Standing Hip CARs', max_length=60, blank=True, null=True)
    hp_frc_iztnk_Standing2 = models.CharField(verbose_name='Standing Hip Claim Shell', max_length=60, blank=True,
                                              null=True)
    hp_frc_iztnk_Standing3 = models.CharField(verbose_name='Standing Figure ‘4’’ Squat', max_length=60, blank=True,
                                              null=True)
    hp_frc_iztnk_Sun = models.CharField(verbose_name='Sun Rise + Sun Sets', max_length=60, blank=True, null=True)
    hp_frc_iztnk_Quadruped1 = models.CharField(verbose_name='Quadruped CARs', max_length=60, blank=True, null=True)
    hp_frc_iztnk_Side2 = models.CharField(verbose_name='Side Lying Hip Abduction', max_length=60, blank=True, null=True)
    hp_frc_iztnk_Quadruped2 = models.CharField(verbose_name='Quadruped Hydrant w/Band', max_length=60, blank=True,
                                               null=True)
    hp_frc_iztnk_Single3 = models.CharField(verbose_name='Single Leg Bridge', max_length=60, blank=True, null=True)
    hp_frc_iztnk_Standing4 = models.CharField(verbose_name='Standing Hip Abduction', max_length=60, blank=True,
                                              null=True)
    hp_frc_iztnk_Split = models.CharField(verbose_name='Split Squat', max_length=60, blank=True, null=True)
    hp_frc_iztnk_Hip = models.CharField(verbose_name='Hip Circle ‘’Stanky Leg', max_length=60, blank=True, null=True)
    hp_frc_iztnk_Banded = models.CharField(verbose_name='Banded Squat', max_length=60, blank=True, null=True)
    hp_frc_iztnk_Miniband = models.CharField(verbose_name='Miniband Hip Airplane', max_length=60, blank=True, null=True)
    hp_frc_iztnk_Plank = models.CharField(verbose_name='Plank + Hip Extension', max_length=60, blank=True, null=True)
    hp_frc_iztnk_Side3 = models.CharField(verbose_name='Side Plank + Hip Extension', max_length=60, blank=True,
                                          null=True)
    hp_frc_iztnk_Clamshell = models.CharField(verbose_name='Clamshell Kicks', max_length=60, blank=True, null=True)
    # PRIFORMIS / SMR
    prfrms_smr_Figure1 = models.CharField(verbose_name='Figure ‘’4’’ SMR w/Foam Roller', max_length=60, blank=True,
                                          null=True)
    prfrms_smr_Figure2 = models.CharField(verbose_name='Figure ‘’4’’ SMR w/Miniball', max_length=60, blank=True,
                                          null=True)
    # PRIFORMIS / STRETCHING
    prfrms_str_Single = models.CharField(verbose_name='Single Knee to Chest Stretch', max_length=60, blank=True,
                                         null=True)
    prfrms_str_Figure = models.CharField(verbose_name='Figure ‘’4’’ Stretch', max_length=60, blank=True, null=True)
    prfrms_str_Seated1 = models.CharField(verbose_name='Seated Figure ‘’4’’ Stretch', max_length=60, blank=True,
                                          null=True)
    prfrms_str_Seated2 = models.CharField(verbose_name='Seated One-Leg Extended Leg Hip Stretch', max_length=60,
                                          blank=True, null=True)
    prfrms_str_Standing1 = models.CharField(verbose_name='Standing Hip External Rotator Stretch', max_length=60,
                                            blank=True, null=True)
    prfrms_str_Recumbent1 = models.CharField(verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch',
                                             max_length=60, blank=True, null=True)
    prfrms_str_Recumbent2 = models.CharField(
        verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch (Cross Leg)',
        max_length=70, blank=True, null=True)
    prfrms_str_L = models.CharField(verbose_name='L-Sit Cross Leg- Priformis Stretch', max_length=60, blank=True,
                                    null=True)
    prfrms_str_Standing2 = models.CharField(verbose_name='Standing Bent-Knee Hip Adductor Stretch', max_length=60,
                                            blank=True, null=True)
    prfrms_str_Seated3 = models.CharField(verbose_name='Seated Hip Adductor Stretch', max_length=60, blank=True,
                                          null=True)
    prfrms_str_Standing3 = models.CharField(verbose_name='Standing Raised-Leg Hip Adductor Stretch', max_length=60,
                                            blank=True, null=True)
    prfrms_str_Standing4 = models.CharField(verbose_name='Standing Knee Flexor Stretch', max_length=60, blank=True,
                                            null=True)
    prfrms_str_Seated4 = models.CharField(verbose_name='Seated Knee Flexor Stretch', max_length=60, blank=True,
                                          null=True)
    prfrms_str_Raised = models.CharField(verbose_name='Raised- One Leg Knee Flexor Stretch', max_length=60, blank=True,
                                         null=True)
    prfrms_str_Supine1 = models.CharField(verbose_name='Supine Lying Raised One-Leg Stretch w/Band', max_length=60,
                                          blank=True, null=True)
    prfrms_str_Seated5 = models.CharField(verbose_name='Seated Wide Range Extended Leg Stretch', max_length=60,
                                          blank=True, null=True)
    prfrms_str_One1 = models.CharField(verbose_name='One-Leg ½ Kneeling Knee Extensor Stretch', max_length=60,
                                       blank=True, null=True)
    prfrms_str_One2 = models.CharField(verbose_name='One-Leg Standing Hip Flexor and Knee Extensor Stretch',
                                       max_length=60, blank=True, null=True)
    prfrms_str_Lying = models.CharField(verbose_name='Lying Hip Flexor and Knee Extensor Stretch', max_length=60,
                                        blank=True, null=True)
    prfrms_str_Supine2 = models.CharField(verbose_name='Supine Pose Lower-Trunk Flexor Stretch', max_length=60,
                                          blank=True, null=True)
    prfrms_str_Prone = models.CharField(verbose_name='Prone Pose Lower-Trunk Flexor Stretch', max_length=60, blank=True,
                                        null=True)
    prfrms_str_Seated6 = models.CharField(verbose_name='Seated Lower-Trunk Extensor Stretch', max_length=60, blank=True,
                                          null=True)
    prfrms_str_Standing5 = models.CharField(verbose_name='Standing Lower-Trunk Lateral Flexor Stretch', max_length=60,
                                            blank=True, null=True)
    prfrms_str_Standing6 = models.CharField(verbose_name='Standing Lower-Trunk Flexor Stretch (Arched Back)',
                                            max_length=60, blank=True, null=True)
    prfrms_str_Lower = models.CharField(verbose_name='Lower-Trunk Lateral Flexor Stretch (Arched Back)', max_length=60,
                                        blank=True, null=True)
    prfrms_str_Supine3 = models.CharField(verbose_name='Supine Lying Side Bend (Oscar Moran-208)', max_length=60,
                                          blank=True, null=True)
    prfrms_str_Open = models.CharField(verbose_name='Open Leg Side Bend', max_length=60, blank=True, null=True)
    # PRIFORMIS / FORCE / IZOMETRIK
    prfrms_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Bridge Adduction w/Ball', max_length=60,
                                                 blank=True, null=True)
    prfrms_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Bird Dog', max_length=60, blank=True,
                                                 null=True)
    prfrms_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Wall Squat', max_length=60, blank=True,
                                                 null=True)
    prfrms_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric Wall Banded Squat', max_length=60, blank=True,
                                                 null=True)
    prfrms_frc_izm_Glute = models.CharField(verbose_name='Glute Bridge and Adduction Squeeze Ball', max_length=60,
                                            blank=True, null=True)
    prfrms_frc_izm_Isometric5 = models.CharField(verbose_name='Isometric Dead Bug w/Swiss Ball', max_length=60,
                                                 blank=True, null=True)
    # PRIFORMIS / FORCE / IZOTONIK
    prfrms_frc_iztnk_Quadruped1 = models.CharField(verbose_name='Quadruped Pelvic Tilt', max_length=60, blank=True,
                                                   null=True)
    prfrms_frc_iztnk_Prone1 = models.CharField(verbose_name='Prone Press Up on Elbow', max_length=60, blank=True,
                                               null=True)
    prfrms_frc_iztnk_Prone2 = models.CharField(verbose_name='Prone Press Up on Hand', max_length=60, blank=True,
                                               null=True)
    prfrms_frc_iztnk_Bird = models.CharField(verbose_name='Bird Dog with Extremity Abduction', max_length=60,
                                             blank=True, null=True)
    prfrms_frc_iztnk_Wall1 = models.CharField(verbose_name='Wall Banded Squat', max_length=60, blank=True, null=True)
    prfrms_frc_iztnk_Wall2 = models.CharField(verbose_name='Wall Banded Squat w/Swiss Ball', max_length=60, blank=True,
                                              null=True)
    prfrms_frc_iztnk_Hip1 = models.CharField(verbose_name='Hip Thrust and Abduction w/Band', max_length=60, blank=True,
                                             null=True)
    prfrms_frc_iztnk_Contralateral = models.CharField(verbose_name='Contralateral Dead Bug w/Swiss Ball', max_length=60,
                                                      blank=True, null=True)
    prfrms_frc_iztnk_Single1 = models.CharField(verbose_name='Single Leg Resisted Tap', max_length=60, blank=True,
                                                null=True)
    prfrms_frc_iztnk_Siatica = models.CharField(verbose_name='Siatica Nerve Glide', max_length=60, blank=True,
                                                null=True)
    prfrms_frc_iztnk_Hip2 = models.CharField(verbose_name='Hip Thrust and Adduction w/Ball', max_length=60, blank=True,
                                             null=True)
    prfrms_frc_iztnk_Kneeling = models.CharField(verbose_name='½ Kneeling T-Spine Rotation', max_length=60, blank=True,
                                                 null=True)
    prfrms_frc_iztnk_Sitting = models.CharField(verbose_name='Sitting Neural Mobility', max_length=60, blank=True,
                                                null=True)
    prfrms_frc_iztnk_Seated1 = models.CharField(verbose_name='Seated Nerve Floss', max_length=60, blank=True, null=True)
    prfrms_frc_iztnk_Side1 = models.CharField(verbose_name='Side Lying Clam Shell', max_length=60, blank=True,
                                              null=True)
    prfrms_frc_iztnk_Hip3 = models.CharField(verbose_name='Hip Thrust', max_length=60, blank=True, null=True)
    prfrms_frc_iztnk_Butterfly = models.CharField(verbose_name='Butterfly Bridge', max_length=60, blank=True, null=True)
    prfrms_frc_iztnk_Side2 = models.CharField(verbose_name='Side Lying Hip Abduction w/Band', max_length=60, blank=True,
                                              null=True)
    prfrms_frc_iztnk_Banded2 = models.CharField(verbose_name='Banded Squat + Side Lunge', max_length=60, blank=True,
                                                null=True)
    prfrms_frc_iztnk_Banded3 = models.CharField(verbose_name='Banded Side Steps', max_length=60, blank=True, null=True)
    prfrms_frc_iztnk_Shine = models.CharField(verbose_name='Shine Box Hinge', max_length=60, blank=True, null=True)
    prfrms_frc_iztnk_Supine = models.CharField(verbose_name='Supine Pigeon Rocks', max_length=60, blank=True, null=True)
    prfrms_frc_iztnk_Hand = models.CharField(verbose_name='Hand Plank + Hip Extension and Abduction', max_length=60,
                                             blank=True, null=True)
    prfrms_frc_iztnk_External = models.CharField(verbose_name='External Rotation Clam Shell', max_length=60, blank=True,
                                                 null=True)
    prfrms_frc_iztnk_Lateral = models.CharField(verbose_name='Lateral Tap Down', max_length=60, blank=True, null=True)
    prfrms_frc_iztnk_Bridge = models.CharField(verbose_name='Bridge Banded March', max_length=60, blank=True, null=True)
    prfrms_frc_iztnk_Siciatic = models.CharField(verbose_name='Siciatic Mobilization w/Band', max_length=60, blank=True,
                                                 null=True)
    prfrms_frc_iztnk_Extended = models.CharField(verbose_name='Extended Leg Ankle Dorsi/Plantar Flexion w/Foam Roller',
                                                 max_length=60, blank=True, null=True)
    prfrms_frc_iztnk_Hooklying = models.CharField(verbose_name='Hooklying Rotation w/Foam Roller', max_length=60,
                                                  blank=True, null=True)
    prfrms_frc_iztnk_Straight = models.CharField(verbose_name='Straight Leg Raise w/Foam Roller', max_length=60,
                                                 blank=True, null=True)
    prfrms_frc_iztnk_Figure = models.CharField(verbose_name='Figure “4” Rotation w/Foam Roller ', max_length=60,
                                               blank=True, null=True)
    prfrms_frc_iztnk_Anterior = models.CharField(verbose_name='Anterior/Posterior Pelvic Tilt w/Foam Roller',
                                                 max_length=60, blank=True, null=True)
    prfrms_frc_iztnk_Seated4 = models.CharField(verbose_name='Seated Siciatic Nerve Glide', max_length=60, blank=True,
                                                null=True)
    prfrms_frc_iztnk_Standing1 = models.CharField(verbose_name='Standing Siciatic Nerve Glide', max_length=60,
                                                  blank=True, null=True)
    prfrms_frc_iztnk_Resisted = models.CharField(verbose_name='Resisted Cat & Cow', max_length=60, blank=True,
                                                 null=True)
    prfrms_frc_iztnk_Lower = models.CharField(verbose_name='Lower Trunk Rotation', max_length=60, blank=True, null=True)
    prfrms_frc_iztnk_Seated5 = models.CharField(verbose_name='Seated Floor Nerve Floss', max_length=60, blank=True,
                                                null=True)
    prfrms_frc_iztnk_Rock = models.CharField(verbose_name='Rock Backs', max_length=60, blank=True, null=True)
    prfrms_frc_iztnk_Dead = models.CharField(verbose_name='Dead Bug', max_length=60, blank=True, null=True)
    prfrms_frc_iztnk_Bear = models.CharField(verbose_name='Bear Crawl Kick Back', max_length=60, blank=True, null=True)
    prfrms_frc_iztnk_Quadruped2 = models.CharField(verbose_name='Quadruped Hip CAR’s', max_length=60, blank=True,
                                                   null=True)
    prfrms_frc_iztnk_Single2 = models.CharField(verbose_name='Single Leg Dead Lift', max_length=60, blank=True,
                                                null=True)
    prfrms_frc_iztnk_Standing2 = models.CharField(verbose_name='Standing Hip CAR’s', max_length=60, blank=True,
                                                  null=True)
    prfrms_frc_iztnk_Fire = models.CharField(verbose_name='Fire Hydrant', max_length=60, blank=True, null=True)

    class Meta:
        verbose_name = "Medikal Egzersiz"
        verbose_name_plural = "Medikal Egzersiz "


class medical_exercise9(models.Model):
    # SAKRO / SMR
    skr_smr_Longiditunal = models.CharField(verbose_name='Longiditunal Foam Roller SMR for Priformis', max_length=60,
                                            blank=True, null=True)
    skr_smr_Cross1 = models.CharField(verbose_name='Cross Leg Priformis SMR w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    skr_smr_Adductors1 = models.CharField(verbose_name='Adductors SMR w/Foam Roller', max_length=60, blank=True,
                                          null=True)
    skr_smr_Adductors2 = models.CharField(verbose_name='Adductors SMR w/Miniball', max_length=60, blank=True, null=True)
    skr_smr_Straight = models.CharField(verbose_name='Straight Leg Adductors SMR w/Foam Roller', max_length=60,
                                        blank=True, null=True)
    skr_smr_Alternating = models.CharField(verbose_name='Alternating Adductors SMR', max_length=60, blank=True,
                                           null=True)
    skr_smr_Side1 = models.CharField(verbose_name='Side Lying IT-Band SMR W/Foam Roller', max_length=60, blank=True,
                                     null=True)
    skr_smr_IT = models.CharField(verbose_name='IT-Band SMR Alternative', max_length=60, blank=True, null=True)
    skr_smr_Side2 = models.CharField(verbose_name='Side Lying IT-Band SMR w/Mini Ball', max_length=60, blank=True,
                                     null=True)
    skr_smr_TFL = models.CharField(verbose_name='TFL SMR w/Miniball', max_length=60, blank=True, null=True)
    skr_smr_Two1 = models.CharField(verbose_name='Two Leg on Foam Roller Hamstring SMR', max_length=60, blank=True,
                                    null=True)
    skr_smr_One1 = models.CharField(verbose_name='One-Leg Hamstring SMR', max_length=60, blank=True, null=True)
    skr_smr_Cross2 = models.CharField(verbose_name='Cross Leg Hamstring SMR w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    skr_smr_Seated = models.CharField(verbose_name='Seated Hamstring SMR w/Mini Ball ', max_length=60, blank=True,
                                      null=True)
    skr_smr_One2 = models.CharField(verbose_name='One-Leg Calf SMR w/Foam Roller', max_length=60, blank=True, null=True)
    skr_smr_Cross3 = models.CharField(verbose_name='Cross Leg Calf SMR w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    skr_smr_Two2 = models.CharField(verbose_name='Two Leg On Foam Roller Calf SMR', max_length=60, blank=True,
                                    null=True)
    skr_smr_Calf = models.CharField(verbose_name='Calf SMR W/Mini Ball', max_length=60, blank=True, null=True)
    skr_smr_Hip = models.CharField(verbose_name='Hip Flexors SMR w/Foam Roller', max_length=60, blank=True, null=True)
    # SAKRO / STRETCHING
    skr_str_Supine1 = models.CharField(verbose_name='Supine Knee to Chest Stretch', max_length=60, blank=True,
                                       null=True)
    skr_str_Supine2 = models.CharField(verbose_name='Supine Figure ‘’4’’ Stretch (Priformis Glute Stretch)',
                                       max_length=60, blank=True, null=True)
    skr_str_Kneeling = models.CharField(verbose_name='½ Kneeling Hip and Quad Stretch', max_length=60, blank=True,
                                        null=True)
    skr_str_Low = models.CharField(verbose_name='Low Back Rotation Stretch', max_length=60, blank=True, null=True)
    skr_str_Seated1 = models.CharField(verbose_name='Seated One-Leg Extended Leg Hip Stretch', max_length=60,
                                       blank=True, null=True)
    skr_str_Standing1 = models.CharField(verbose_name='Standing Hip External Rotator Stretch', max_length=60,
                                         blank=True, null=True)
    skr_str_Recumbent1 = models.CharField(verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch',
                                          max_length=60, blank=True, null=True)
    skr_str_Recumbent2 = models.CharField(
        verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch (Cross Leg)',
        max_length=70, blank=True, null=True)
    skr_str_L = models.CharField(verbose_name='L-Sit Cross Leg- Priformis Stretch', max_length=60, blank=True,
                                 null=True)
    skr_str_Standing2 = models.CharField(verbose_name='Standing Bent-Knee Hip Adductor Stretch', max_length=60,
                                         blank=True, null=True)
    skr_str_Seated = models.CharField(verbose_name='Seated Hip Adductor Stretch', max_length=60, blank=True, null=True)
    skr_str_Standing3 = models.CharField(verbose_name='Standing Raised-Leg Hip Adductor Stretch', max_length=60,
                                         blank=True, null=True)
    skr_str_Standing4 = models.CharField(verbose_name='Standing Knee Flexor Stretch', max_length=60, blank=True,
                                         null=True)
    skr_str_Seated2 = models.CharField(verbose_name='Seated Knee Flexor Stretch', max_length=60, blank=True, null=True)
    skr_str_Raised = models.CharField(verbose_name='Raised- One Leg Knee Flexor Stretch', max_length=60, blank=True,
                                      null=True)
    skr_str_Supine3 = models.CharField(verbose_name='Supine Lying Raised One-Leg Stretch w/Band', max_length=60,
                                       blank=True, null=True)
    skr_str_Seated3 = models.CharField(verbose_name='Seated Wide Range Extended Leg Stretch', max_length=60, blank=True,
                                       null=True)
    skr_str_One1 = models.CharField(verbose_name='One-Leg ½ Kneeling Knee Extensor Stretch', max_length=60, blank=True,
                                    null=True)
    skr_str_One2 = models.CharField(verbose_name='One-Leg Standing Hip Flexor and Knee Extensor Stretch', max_length=60,
                                    blank=True, null=True)
    skr_str_Lying = models.CharField(verbose_name='Lying Hip Flexor and Knee Extensor Stretch', max_length=60,
                                     blank=True, null=True)
    skr_str_Supine4 = models.CharField(verbose_name='Supine Pose Lower-Trunk Flexor Stretch', max_length=60, blank=True,
                                       null=True)
    skr_str_Prone = models.CharField(verbose_name='Prone Pose Lower-Trunk Flexor Stretch', max_length=60, blank=True,
                                     null=True)
    skr_str_Seated4 = models.CharField(verbose_name='Seated Lower-Trunk Extensor Stretch', max_length=60, blank=True,
                                       null=True)
    skr_str_Standing5 = models.CharField(verbose_name='Standing Lower-Trunk Lateral Flexor Stretch', max_length=60,
                                         blank=True, null=True)
    skr_str_Standing6 = models.CharField(verbose_name='Standing Lower-Trunk Flexor Stretch (Arched Back)',
                                         max_length=60, blank=True, null=True)
    skr_str_Lower = models.CharField(verbose_name='Lower-Trunk Lateral Flexor Stretch (Arched Back)', max_length=60,
                                     blank=True, null=True)
    skr_str_Supine5 = models.CharField(verbose_name='Supine Lying Side Bend (Oscar Moran-208) ', max_length=60,
                                       blank=True, null=True)
    skr_str_Open = models.CharField(verbose_name='Open Leg Side Bend', max_length=60, blank=True, null=True)
    # SAKRO / FORCE / IZOMETRIK
    skr_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Hip Flexion/Extension', max_length=60, blank=True,
                                              null=True)
    skr_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Cook Bridge', max_length=60, blank=True,
                                              null=True)
    skr_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Stability Ball  Bird Dog', max_length=60,
                                              blank=True, null=True)
    skr_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric Hip Adduction Squeeze', max_length=60, blank=True,
                                              null=True)
    skr_frc_izm_Copenhagen = models.CharField(verbose_name='Copenhagen Plank', max_length=60, blank=True, null=True)
    # SAKRO / FORCE / IZOTONIK
    skr_frc_iztnk_Bent = models.CharField(verbose_name='Bent Knee Fall Out', max_length=60, blank=True, null=True)
    skr_frc_iztnk_Side = models.CharField(verbose_name='Side Lying Clamshell', max_length=60, blank=True, null=True)
    skr_frc_iztnk_Cook = models.CharField(verbose_name='Cook Bridge', max_length=60, blank=True, null=True)
    skr_frc_iztnk_Bird = models.CharField(verbose_name='Bird Dog on Stability Ball', max_length=60, blank=True,
                                          null=True)
    skr_frc_iztnk_Banded1 = models.CharField(verbose_name='Banded Hip Extension', max_length=60, blank=True, null=True)
    skr_frc_iztnk_Single1 = models.CharField(verbose_name='Single Leg Dead Lift', max_length=60, blank=True, null=True)
    skr_frc_iztnk_Resistance = models.CharField(verbose_name='Resistance Band Bird Dog', max_length=60, blank=True,
                                                null=True)
    skr_frc_iztnk_Glute = models.CharField(verbose_name='Glute Kickback', max_length=60, blank=True, null=True)
    skr_frc_iztnk_Banded2 = models.CharField(verbose_name='Banded Frog Bridge', max_length=60, blank=True, null=True)
    skr_frc_iztnk_Dynamic = models.CharField(verbose_name='Dynamic Side Plank Clamshell', max_length=60, blank=True,
                                             null=True)
    skr_frc_iztnk_Bear = models.CharField(verbose_name='Bear Crawl Kick Back', max_length=60, blank=True, null=True)
    skr_frc_iztnk_Unstable = models.CharField(verbose_name='Unstable Plank Roll', max_length=60, blank=True, null=True)
    skr_frc_iztnk_Standing1 = models.CharField(verbose_name='Standing Clam shell', max_length=60, blank=True, null=True)
    skr_frc_iztnk_Standing2 = models.CharField(verbose_name='Standing Hip Flexor March', max_length=60, blank=True,
                                               null=True)
    skr_frc_iztnk_Single2 = models.CharField(verbose_name='Single Leg Glute Bridge', max_length=60, blank=True,
                                             null=True)
    skr_frc_iztnk_Wall = models.CharField(verbose_name='Wall Bangers', max_length=60, blank=True, null=True)
    skr_frc_iztnk_Pallof = models.CharField(verbose_name='Pallof Wall Bangers', max_length=60, blank=True, null=True)
    skr_frc_iztnk_Storks = models.CharField(verbose_name='Storks', max_length=60, blank=True, null=True)
    skr_frc_iztnk_Standing3 = models.CharField(verbose_name='Standing Side Crunch', max_length=60, blank=True,
                                               null=True)
    # HIPLABRUM  /  SMR
    hplbrm_smr_Adductors1 = models.CharField(verbose_name='Adductors SMR w/Foam Roller', max_length=60, blank=True,
                                             null=True)
    hplbrm_smr_Adductors2 = models.CharField(verbose_name='Adductors SMR w/Miniball', max_length=60, blank=True,
                                             null=True)
    hplbrm_smr_Straight = models.CharField(verbose_name='Straight Leg Adductors SMR w/Foam Roller', max_length=60,
                                           blank=True, null=True)
    hplbrm_smr_Alternating = models.CharField(verbose_name='Alternating Adductors SMR', max_length=60, blank=True,
                                              null=True)
    hplbrm_smr_Side1 = models.CharField(verbose_name='Side Lying IT-Band SMR W/Foam Roller', max_length=60, blank=True,
                                        null=True)
    hplbrm_smr_IT = models.CharField(verbose_name='IT-Band SMR Alternative', max_length=60, blank=True, null=True)
    hplbrm_smr_Side2 = models.CharField(verbose_name='Side Lying IT-Band SMR w/Mini Ball', max_length=60, blank=True,
                                        null=True)
    hplbrm_smr_TFL = models.CharField(verbose_name='TFL SMR w/Miniball', max_length=60, blank=True, null=True)
    # HIPLABRUM  /  STRETCHING
    hplbrm_str_Seated1 = models.CharField(verbose_name='Seated One-Leg Extended Leg Hip Stretch', max_length=60,
                                          blank=True, null=True)
    hplbrm_str_Standing1 = models.CharField(verbose_name='Standing Hip External Rotator Stretch', max_length=60,
                                            blank=True, null=True)
    hplbrm_str_Recumbent1 = models.CharField(verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch',
                                             max_length=60, blank=True, null=True)
    hplbrm_str_Recumbent2 = models.CharField(
        verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch (Cross Leg)',
        max_length=70, blank=True, null=True)
    hplbrm_str_L = models.CharField(verbose_name='L-Sit Cross Cross Leg- Priformis Stretch', max_length=60, blank=True,
                                    null=True)
    hplbrm_str_Standing2 = models.CharField(verbose_name='Standing Bent-Knee Hip Adductor Stretc', max_length=60,
                                            blank=True, null=True)
    hplbrm_str_Seated2 = models.CharField(verbose_name='Seated Hip Adductor Stretch', max_length=60, blank=True,
                                          null=True)
    hplbrm_str_Standing3 = models.CharField(verbose_name='Standing Raised-Leg Hip Adductor Stretch', max_length=60,
                                            blank=True, null=True)
    hplbrm_str_Standing4 = models.CharField(verbose_name='Standing Knee Flexor Stretch', max_length=60, blank=True,
                                            null=True)
    hplbrm_str_Seated3 = models.CharField(verbose_name='Seated Knee Flexor Stretch', max_length=60, blank=True,
                                          null=True)
    hplbrm_str_Raised = models.CharField(verbose_name='Raised- One Leg Knee Flexor Stretch', max_length=60, blank=True,
                                         null=True)
    hplbrm_str_Supine1 = models.CharField(verbose_name='Supine Lying Raised One-Leg Stretch w/Band', max_length=60,
                                          blank=True, null=True)
    hplbrm_str_Seated4 = models.CharField(verbose_name='Seated Wide Range Extended Leg Stretch', max_length=60,
                                          blank=True, null=True)
    hplbrm_str_One1 = models.CharField(verbose_name='One-Leg ½ Kneeling Knee Extensor Stretch', max_length=60,
                                       blank=True, null=True)
    hplbrm_str_One2 = models.CharField(verbose_name='One-Leg Standing Hip Flexor and Knee Extensor Stretch',
                                       max_length=60, blank=True, null=True)
    hplbrm_str_Lying = models.CharField(verbose_name='Lying Hip Flexor and  Knee Extensor Stretch', max_length=60,
                                        blank=True, null=True)
    hplbrm_str_Supine2 = models.CharField(verbose_name='Supine Pose Lower-Trunk Flexor Stretch', max_length=60,
                                          blank=True, null=True)
    hplbrm_str_Prone = models.CharField(verbose_name='Prone Pose Lower-Trunk Flexor Stretch', max_length=60, blank=True,
                                        null=True)
    hplbrm_str_Seated5 = models.CharField(verbose_name='Seated Lower-Trunk Extensor Stretch', max_length=60, blank=True,
                                          null=True)
    hplbrm_str_Standing5 = models.CharField(verbose_name='Standing Lower-Trunk Lateral Flexor Stretch', max_length=60,
                                            blank=True, null=True)
    hplbrm_str_Standing6 = models.CharField(verbose_name='Standing Lower-Trunk Flexor Stretch (Arched Back)',
                                            max_length=60, blank=True, null=True)
    hplbrm_str_Lower = models.CharField(verbose_name='Lower-Trunk Lateral Flexor Stretch (Arched Back)', max_length=60,
                                        blank=True, null=True)
    hplbrm_str_Supine3 = models.CharField(verbose_name='Supine Lying Side Bend (Oscar Moran-208)', max_length=60,
                                          blank=True, null=True)
    hplbrm_str_Open = models.CharField(verbose_name='Open Leg Side Bend', max_length=60, blank=True, null=True)
    # HIPLABRUM  /  FORCE / IZOMETRIK
    hplbrm_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Glute Bridge', max_length=60, blank=True,
                                                 null=True)
    hplbrm_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Sumo Squat at Wall', max_length=60, blank=True,
                                                 null=True)
    hplbrm_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Copenhagen Plank-on Knee', max_length=60,
                                                 blank=True, null=True)
    hplbrm_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric Banded March', max_length=60, blank=True,
                                                 null=True)
    # HIPLABRUM  /  FORCE / IZOTONIK
    hplbrm_frc_iztnk_Side = models.CharField(verbose_name='Side Lying Hip Abduction', max_length=60, blank=True,
                                             null=True)
    hplbrm_frc_iztnk_Quadruped1 = models.CharField(verbose_name='Quadruped Fire Hydrant', max_length=60, blank=True,
                                                   null=True)
    hplbrm_frc_iztnk_Single1 = models.CharField(verbose_name='Single Leg Bridge', max_length=60, blank=True, null=True)
    hplbrm_frc_iztnk_Hip = models.CharField(verbose_name='Hip Flexor March w/Band', max_length=60, blank=True,
                                            null=True)
    hplbrm_frc_iztnk_Sumo = models.CharField(verbose_name='Sumo Squat', max_length=60, blank=True, null=True)
    hplbrm_frc_iztnk_Active = models.CharField(verbose_name='Active Copenhagen Plank-on Knees', max_length=60,
                                               blank=True, null=True)
    hplbrm_frc_iztnk_Miniband1 = models.CharField(verbose_name='Miniband Bent Knee Boxes', max_length=60, blank=True,
                                                  null=True)
    hplbrm_frc_iztnk_Miniband2 = models.CharField(verbose_name='Miniband Straight Leg Boxes', max_length=60, blank=True,
                                                  null=True)
    hplbrm_frc_iztnk_Hips = models.CharField(verbose_name='Hips Elevated Psoas March w/Band', max_length=60, blank=True,
                                             null=True)
    hplbrm_frc_iztnk_Box = models.CharField(verbose_name='Box Squat', max_length=60, blank=True, null=True)
    hplbrm_frc_iztnk_Single2 = models.CharField(verbose_name='Single Leg Dead Lift (Knee Propped)', max_length=60,
                                                blank=True, null=True)
    hplbrm_frc_iztnk_Standing1 = models.CharField(verbose_name='Standing Clamshells w/Band', max_length=60, blank=True,
                                                  null=True)
    hplbrm_frc_iztnk_Prone = models.CharField(verbose_name='Prone Hip Int. Rotation Pull Apart w/Band', max_length=60,
                                              blank=True, null=True)
    hplbrm_frc_iztnk_Banded1 = models.CharField(verbose_name='Banded Lateral Lunge', max_length=60, blank=True,
                                                null=True)
    hplbrm_frc_iztnk_Banded2 = models.CharField(verbose_name='Banded Hip Thruster w/Swiss Ball', max_length=60,
                                                blank=True, null=True)
    hplbrm_frc_iztnk_Quadruped2 = models.CharField(verbose_name='Quadruped Banded Hip Abduction and Reach',
                                                   max_length=60, blank=True, null=True)
    hplbrm_frc_iztnk_Standing2 = models.CharField(verbose_name='Standing Hip Extension w/Band', max_length=60,
                                                  blank=True, null=True)
    hplbrm_frc_iztnk_Groiner = models.CharField(verbose_name='Groiner with Lateral Band Glide', max_length=60,
                                                blank=True, null=True)
    hplbrm_frc_iztnk_Quadruped3 = models.CharField(verbose_name=' Quadruped Lateral Rock with Band Lateral Glide',
                                                   max_length=60, blank=True, null=True)
    hplbrm_frc_iztnk_Shin = models.CharField(verbose_name='Shin Box- Alternating External Rotation', max_length=60,
                                             blank=True, null=True)
    hplbrm_frc_iztnk_Sidelying = models.CharField(verbose_name='Sidelying Clam with Band', max_length=60, blank=True,
                                                  null=True)
    hplbrm_frc_iztnk_Goblet = models.CharField(verbose_name='Goblet Squat-Slow Tempo', max_length=60, blank=True,
                                               null=True)

    grn_smr_Adductors1 = models.CharField(verbose_name='Adductors SMR w/Foam Roller', max_length=60, blank=True,
                                          null=True)
    grn_smr_Adductors2 = models.CharField(verbose_name='Adductors SMR w/Miniball', max_length=60, blank=True, null=True)
    grn_smr_Straight = models.CharField(verbose_name='Straight Leg Adductors SMR w/Foam Roller', max_length=60,
                                        blank=True, null=True)
    grn_smr_Alternating = models.CharField(verbose_name='Alternating Adductors SMR', max_length=60, blank=True,
                                           null=True)
    grn_smr_Side1 = models.CharField(verbose_name='Side Lying IT-Band SMR W/Foam Roller', max_length=60, blank=True,
                                     null=True)
    grn_smr_IT = models.CharField(verbose_name='IT-Band SMR Alternative', max_length=60, blank=True, null=True)
    grn_smr_Side2 = models.CharField(verbose_name='Side Lying IT-Band SMR w/Mini Ball', max_length=60, blank=True,
                                     null=True)
    grn_smr_TFL = models.CharField(verbose_name='TFL SMR w/Miniball', max_length=60, blank=True, null=True)
    grn_str_Seated1 = models.CharField(verbose_name='Seated One-Leg Extended Leg Hip Stretch', max_length=60,
                                       blank=True, null=True)
    grn_str_Standing1 = models.CharField(verbose_name='Standing Hip External Rotator Stretch', max_length=60,
                                         blank=True, null=True)
    grn_str_Recumbent1 = models.CharField(verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch',
                                          max_length=60, blank=True, null=True)
    grn_str_Recumbent2 = models.CharField(
        verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch (Cross Leg)',
        max_length=70, blank=True, null=True)
    grn_str_L = models.CharField(verbose_name='L-Sit Cross Leg-Priformis Stretch', max_length=60, blank=True, null=True)
    grn_str_Standing2 = models.CharField(verbose_name='Standing Bent-Knee Hip Adductor Stretch', max_length=60,
                                         blank=True, null=True)
    grn_str_Seated2 = models.CharField(verbose_name='Seated Hip Adductor Stretch', max_length=60, blank=True, null=True)
    grn_str_Standing3 = models.CharField(verbose_name='Standing Raised-Leg Hip Adductor Stretch', max_length=60,
                                         blank=True, null=True)
    grn_str_Standing4 = models.CharField(verbose_name='Standing Knee Flexor Stretch', max_length=60, blank=True,
                                         null=True)
    grn_str_Seated3 = models.CharField(verbose_name='Seated Knee Flexor Stretch', max_length=60, blank=True, null=True)
    grn_str_Raised = models.CharField(verbose_name='Raised- One Leg Knee Flexor Stretch', max_length=60, blank=True,
                                      null=True)
    grn_str_Supine1 = models.CharField(verbose_name='Supine Lying Raised One-Leg Stretch w/Band', max_length=60,
                                       blank=True, null=True)
    grn_str_Seated4 = models.CharField(verbose_name='Seated Wide Range Extended Leg Stretch', max_length=60, blank=True,
                                       null=True)
    grn_str_One1 = models.CharField(verbose_name='One-Leg ½ Kneeling Knee Extensor Stretch', max_length=60, blank=True,
                                    null=True)
    grn_str_One2 = models.CharField(verbose_name='One-Leg Standing Hip Flexor and Knee Extensor Stretch', max_length=60,
                                    blank=True, null=True)
    grn_str_Lying = models.CharField(verbose_name='Lying Hip Flexor and Knee Extensor Stretch', max_length=60,
                                     blank=True, null=True)
    grn_str_Supine2 = models.CharField(verbose_name='Supine Pose Lower-Trunk Flexor Stretch', max_length=60, blank=True,
                                       null=True)
    grn_str_Prone = models.CharField(verbose_name='Prone Pose Lower-Trunk Flexor Stretch', max_length=60, blank=True,
                                     null=True)
    grn_str_Seated5 = models.CharField(verbose_name='Seated Lower-Trunk Extensor Stretch', max_length=60, blank=True,
                                       null=True)
    grn_str_Standing5 = models.CharField(verbose_name='Standing Lower-Trunk Lateral Flexor Stretch', max_length=60,
                                         blank=True, null=True)
    grn_str_Standing6 = models.CharField(verbose_name='Standing Lower-Trunk Flexor Stretch (Arched Back)',
                                         max_length=60, blank=True, null=True)
    grn_str_Lower = models.CharField(verbose_name='Lower-Trunk Lateral Flexor Stretch (Arched Back)', max_length=60,
                                     blank=True, null=True)
    grn_str_Supine3 = models.CharField(verbose_name='Supine Lying Side Bend (Oscar Moran-208)', max_length=60,
                                       blank=True, null=True)
    grn_str_Open = models.CharField(verbose_name='Open Leg Side Bend', max_length=60, blank=True, null=True)
    grn_frc_iztnk_Donkey = models.CharField(verbose_name='Donkey Kicks', max_length=60, blank=True, null=True)
    grn_frc_iztnk_Quadruped1 = models.CharField(verbose_name='Quadruped Fire Hydrants', max_length=60, blank=True,
                                                null=True)
    grn_frc_iztnk_Hip1 = models.CharField(verbose_name='Hip Extension with Slider', max_length=60, blank=True,
                                          null=True)
    grn_frc_iztnk_Alternating = models.CharField(verbose_name='Alternating Hip Extension', max_length=60, blank=True,
                                                 null=True)
    grn_frc_iztnk_Supine = models.CharField(verbose_name='Supine Hip CARs', max_length=60, blank=True, null=True)
    grn_frc_iztnk_Leg = models.CharField(verbose_name='Leg Fallouts', max_length=60, blank=True, null=True)
    grn_frc_iztnk_Side1 = models.CharField(verbose_name='Side Lying Hip CARs ', max_length=60, blank=True, null=True)
    grn_frc_iztnk_Side2 = models.CharField(verbose_name='Side Hip CARs Leg Straight', max_length=60, blank=True,
                                           null=True)
    grn_frc_iztnk_Quadruped2 = models.CharField(verbose_name='Quadruped Hip CARs', max_length=60, blank=True, null=True)
    grn_frc_iztnk_Quadruped3 = models.CharField(verbose_name='Quadruped Hip CARs Leg Straight', max_length=60,
                                                blank=True, null=True)
    grn_frc_iztnk_Hip2 = models.CharField(verbose_name='Hip 90/90', max_length=60, blank=True, null=True)
    grn_frc_iztnk_Standing = models.CharField(verbose_name='Standing Hip CARs', max_length=60, blank=True, null=True)
    grn_frc_iztnk_Adductor = models.CharField(verbose_name='Adductor One Leg Rock', max_length=60, blank=True,
                                              null=True)
    grn_frc_iztnk_Active = models.CharField(verbose_name='Active ½ Kneeling Hip Stretch', max_length=60, blank=True,
                                            null=True)
    grn_frc_iztnk_Frogger = models.CharField(verbose_name='Frogger Rocks', max_length=60, blank=True, null=True)

    class Meta:
        verbose_name = "Medikal Egzersiz"
        verbose_name_plural = "Medikal Egzersiz "


class medical_exercise10(models.Model):
    # HAMSTRING / SMR
    hmstr_smr_Two = models.CharField(verbose_name='Two Leg on Foam Roller Hamstring SMR', max_length=60, blank=True,
                                     null=True)
    hmstr_smr_One = models.CharField(verbose_name='One-Leg Hamstring SMR', max_length=60, blank=True, null=True)
    hmstr_smr_Cross = models.CharField(verbose_name='Cross Leg Hamstring SMR w/Foam Roller', max_length=60, blank=True,
                                       null=True)
    hmstr_smr_Seated = models.CharField(verbose_name='Seated Hamstring SMR w/Mini Ball', max_length=60, blank=True,
                                        null=True)
    # HAMSTRING / STRETCHING
    hmstr_str_Kneeling = models.CharField(verbose_name='Kneeling Hamstring Stretch', max_length=60, blank=True,
                                          null=True)
    hmstr_str_Pancake = models.CharField(verbose_name='Pancake Lean Complex (mobil)', max_length=60, blank=True,
                                         null=True)
    hmstr_str_Seated1 = models.CharField(verbose_name='Seated One-Leg Extended Leg Hip Stretch', max_length=60,
                                         blank=True, null=True)
    hmstr_str_Standing1 = models.CharField(verbose_name='Standing Hip External Rotator Stretch', max_length=60,
                                           blank=True, null=True)
    hmstr_str_Recumbent1 = models.CharField(verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch',
                                            max_length=60, blank=True, null=True)
    hmstr_str_Recumbent2 = models.CharField(
        verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch (Cross Leg)',
        max_length=70, blank=True, null=True)
    hmstr_str_L = models.CharField(verbose_name='L-Sit Cross Leg- Priformis Stretch', max_length=60, blank=True,
                                   null=True)
    hmstr_str_Standing2 = models.CharField(verbose_name='Standing Bent-Knee Hip Adductor Stretch', max_length=60,
                                           blank=True, null=True)
    hmstr_str_Seated2 = models.CharField(verbose_name='Seated Hip Adductor Stretch', max_length=60, blank=True,
                                         null=True)
    hmstr_str_Standing3 = models.CharField(verbose_name='Standing Raised-Leg Hip Adductor Stretch', max_length=60,
                                           blank=True, null=True)
    hmstr_str_Standing4 = models.CharField(verbose_name='Standing Knee Flexor Stretch', max_length=60, blank=True,
                                           null=True)
    hmstr_str_Seated3 = models.CharField(verbose_name='Seated Knee Flexor Stretch', max_length=60, blank=True,
                                         null=True)
    hmstr_str_Raised = models.CharField(verbose_name='Raised- One Leg Knee Flexor Stretch', max_length=60, blank=True,
                                        null=True)
    hmstr_str_Supine1 = models.CharField(verbose_name='Supine Lying Raised One-Leg Stretch w/Band', max_length=60,
                                         blank=True, null=True)
    hmstr_str_Seated4 = models.CharField(verbose_name='Seated Wide Range Extended Leg Stretch', max_length=60,
                                         blank=True, null=True)
    hmstr_str_One1 = models.CharField(verbose_name='One-Leg ½ Kneeling Knee Extensor Stretch', max_length=60,
                                      blank=True, null=True)
    hmstr_str_One2 = models.CharField(verbose_name='One-Leg Standing Hip Flexor and Knee Extensor Stretch',
                                      max_length=60, blank=True, null=True)
    hmstr_str_Lying = models.CharField(verbose_name='Lying Hip Flexor and Knee Extensor Stretch', max_length=60,
                                       blank=True, null=True)
    hmstr_str_Supine2 = models.CharField(verbose_name='Supine Pose Lower-Trunk Flexor Stretch', max_length=60,
                                         blank=True, null=True)
    hmstr_str_Prone = models.CharField(verbose_name='Prone Pose Lower-Trunk Flexor Stretch', max_length=60, blank=True,
                                       null=True)
    hmstr_str_Seated5 = models.CharField(verbose_name='Seated Lower-Trunk Extensor Stretch', max_length=60, blank=True,
                                         null=True)
    hmstr_str_Standing5 = models.CharField(verbose_name='Standing Lower-Trunk Lateral Flexor Stretch', max_length=60,
                                           blank=True, null=True)
    hmstr_str_Standing6 = models.CharField(verbose_name='Standing Lower-Trunk Flexor Stretch (Arched Back)',
                                           max_length=60, blank=True, null=True)
    hmstr_str_Lower = models.CharField(verbose_name='Lower-Trunk Lateral Flexor Stretch (Arched Back)', max_length=60,
                                       blank=True, null=True)
    hmstr_str_Supine3 = models.CharField(verbose_name='Supine Lying Side Bend (Oscar Moran-208)', max_length=60,
                                         blank=True, null=True)
    hmstr_str_Open = models.CharField(verbose_name='Open Leg Side Bend', max_length=60, blank=True, null=True)
    # HAMSTRING / FORCE / IZOMETRIK
    hmstr_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Knee Bent', max_length=60, blank=True,
                                                null=True)
    hmstr_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Knee Straight', max_length=60, blank=True,
                                                null=True)
    hmstr_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Bridge', max_length=60, blank=True, null=True)
    hmstr_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric Single Leg Bridge', max_length=60, blank=True,
                                                null=True)
    hmstr_frc_izm_Isometric5 = models.CharField(verbose_name='Isometric Wall Squat', max_length=60, blank=True,
                                                null=True)
    # HAMSTRING / FORCE / IZOTONIK
    hmstr_frc_iztnk_Side = models.CharField(verbose_name='Side Lying Clam Shells', max_length=60, blank=True, null=True)
    hmstr_frc_iztnk_Single = models.CharField(verbose_name='Single Leg Dead Lift', max_length=60, blank=True, null=True)
    hmstr_frc_iztnk_Bulgarian = models.CharField(verbose_name='Bulgarian Squat', max_length=60, blank=True, null=True)
    hmstr_frc_iztnk_Hamstring1 = models.CharField(verbose_name='Hamstring Slider', max_length=60, blank=True, null=True)
    hmstr_frc_iztnk_Supine1 = models.CharField(verbose_name='Supine Hamstring Sliders', max_length=60, blank=True,
                                               null=True)
    hmstr_frc_iztnk_Heel = models.CharField(verbose_name='Heel Elevated Hip Hinge', max_length=60, blank=True,
                                            null=True)
    hmstr_frc_iztnk_Kickstand = models.CharField(verbose_name='Kickstand RDL', max_length=60, blank=True, null=True)
    hmstr_frc_iztnk_Seated1 = models.CharField(verbose_name='Seated Nerve Glide', max_length=60, blank=True, null=True)
    hmstr_frc_iztnk_Hamstring2 = models.CharField(verbose_name='Hamstring Kickstand Scoops', max_length=60, blank=True,
                                                  null=True)
    hmstr_frc_iztnk_Standing1 = models.CharField(verbose_name='Standing Hamstring Stretch to Inchworms', max_length=60,
                                                 blank=True, null=True)
    hmstr_frc_iztnk_Seated2 = models.CharField(verbose_name='Seated Hamstring Kick Outs', max_length=60, blank=True,
                                               null=True)
    hmstr_frc_iztnk_Supine2 = models.CharField(verbose_name='Supine Straight Leg Drops', max_length=60, blank=True,
                                               null=True)
    hmstr_frc_iztnk_Pancake = models.CharField(verbose_name='Pancake Lean Complex (mobil)', max_length=60, blank=True,
                                               null=True)
    hmstr_frc_iztnk_Hamstring3 = models.CharField(verbose_name='Hamstring Bridge Walkouts', max_length=60, blank=True,
                                                  null=True)
    hmstr_frc_iztnk_Hamstring4 = models.CharField(verbose_name='Hamstring Bridge', max_length=60, blank=True, null=True)
    hmstr_frc_iztnk_Hamstring5 = models.CharField(verbose_name='Hamstring Extenders', max_length=60, blank=True,
                                                  null=True)
    hmstr_frc_iztnk_Standing2 = models.CharField(verbose_name='Standing Frontal Leg Swing', max_length=60, blank=True,
                                                 null=True)
    hmstr_frc_iztnk_Standing3 = models.CharField(verbose_name='Standing Sagittal Leg Swing', max_length=60, blank=True,
                                                 null=True)
    hmstr_frc_iztnk_Supine3 = models.CharField(verbose_name='Supine Hamstring Curl w/Slider', max_length=60, blank=True,
                                               null=True)
    hmstr_frc_iztnk_Prone = models.CharField(verbose_name='Prone Eccentrics', max_length=60, blank=True, null=True)
    hmstr_frc_iztnk_Bridge = models.CharField(verbose_name='Bridge Walkouts', max_length=60, blank=True, null=True)
    hmstr_frc_iztnk_Nordic = models.CharField(verbose_name='Nordic Hamstring Curl', max_length=60, blank=True,
                                              null=True)
    # INHIBISYON / SMR
    inhb_smr_Side = models.CharField(verbose_name='Quadriceps w/Foam Roller', max_length=60, blank=True, null=True)
    inhb_smr_Single = models.CharField(verbose_name='Quadriceps SMR w/Miniball', max_length=60, blank=True, null=True)
    inhb_smr_Bulgarian = models.CharField(verbose_name='Side Lying IT-Band SMR W/Foam Roller', max_length=60,
                                          blank=True, null=True)
    inhb_smr_Hamstring1 = models.CharField(verbose_name='IT-Band SMR Alternative', max_length=60, blank=True, null=True)
    inhb_smr_Supine = models.CharField(verbose_name='Side Lying IT-Band SMR w/Mini Ball', max_length=60, blank=True,
                                       null=True)
    inhb_smr_Heel = models.CharField(verbose_name='TFL SMR w/Miniball', max_length=60, blank=True, null=True)
    inhb_smr_Kickstand = models.CharField(verbose_name='Two Leg on Foam  Roller Hamstring SMR', max_length=60,
                                          blank=True, null=True)
    inhb_smr_Seated = models.CharField(verbose_name='One-Leg Hamstring SMR', max_length=60, blank=True, null=True)
    inhb_smr_Hamstring2 = models.CharField(verbose_name='Cross Leg Hamstring SMR w/Foam Roller', max_length=60,
                                           blank=True, null=True)
    inhb_smr_Standing = models.CharField(verbose_name='Seated Hamstring SMR w/Mini Ball', max_length=60, blank=True,
                                         null=True)
    # INHIBISYON / STRETCHING
    inhb_str_Tall = models.CharField(verbose_name='Tall Kneeling Quadriceps Stretch', max_length=60, blank=True,
                                     null=True)
    inhb_str_Seated1 = models.CharField(verbose_name='Seated One-Leg Extended Leg Hip Stretch', max_length=60,
                                        blank=True, null=True)
    inhb_str_Standing1 = models.CharField(verbose_name='Standing Hip External Rotator Stretch', max_length=60,
                                          blank=True, null=True)
    inhb_str_Recumbent1 = models.CharField(verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch',
                                           max_length=60, blank=True, null=True)
    inhb_str_Recumbent2 = models.CharField(
        verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch (Cross Leg)',
        max_length=70, blank=True, null=True)
    inhb_str_L = models.CharField(verbose_name='L-Sit Cross Leg- Priformis Stretch', max_length=60, blank=True,
                                  null=True)
    inhb_str_Standing2 = models.CharField(verbose_name='Standing Bent-Knee Hip Adductor Stretch', max_length=60,
                                          blank=True, null=True)
    inhb_str_Seated = models.CharField(verbose_name='Seated Hip Adductor Stretch', max_length=60, blank=True, null=True)
    inhb_str_Standing3 = models.CharField(verbose_name='Standing Raised-Leg Hip Adductor Stretch', max_length=60,
                                          blank=True, null=True)
    inhb_str_Standing4 = models.CharField(verbose_name='Standing Knee Flexor Stretch ', max_length=60, blank=True,
                                          null=True)
    inhb_str_Seated2 = models.CharField(verbose_name='Seated Knee Flexor Stretch ', max_length=60, blank=True,
                                        null=True)
    inhb_str_Raised = models.CharField(verbose_name='Raised- One Leg Knee Flexor Stretch', max_length=60, blank=True,
                                       null=True)
    inhb_str_Supine = models.CharField(verbose_name='Supine Lying Raised One-Leg Stretch w/Band', max_length=60,
                                       blank=True, null=True)
    inhb_str_Seated3 = models.CharField(verbose_name='Seated Wide Range Extended Leg Stretch', max_length=60,
                                        blank=True, null=True)
    inhb_str_One1 = models.CharField(verbose_name='One-Leg ½ Kneeling Knee Extensor Stretch', max_length=60, blank=True,
                                     null=True)
    inhb_str_One2 = models.CharField(verbose_name='One-Leg Standing Hip Flexor and Knee Extensor Stretch',
                                     max_length=60, blank=True, null=True)
    inhb_str_Lying = models.CharField(verbose_name='Lying Hip Flexor and Knee Extensor Stretch', max_length=60,
                                      blank=True, null=True)
    # INHIBISYON / FORCE / IZOMETRIK
    inhb_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Wall Squat', max_length=60, blank=True,
                                               null=True)
    inhb_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Hip Bridge', max_length=60, blank=True,
                                               null=True)
    inhb_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Single Leg Hip Bridge', max_length=60,
                                               blank=True, null=True)
    inhb_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric Knee Bent', max_length=60, blank=True, null=True)
    inhb_frc_izm_Isometric5 = models.CharField(verbose_name='Isometric Knee Straight', max_length=60, blank=True,
                                               null=True)
    # INHIBISYON / FORCE / IZOTONIK
    inhb_frc_iztnk_Hamstring = models.CharField(verbose_name='Hamstring Curl w/Swiss Ball', max_length=60, blank=True,
                                                null=True)
    inhb_frc_iztnk_Straight = models.CharField(verbose_name='Straight Leg Bridge to Curl w/Swiss Ball', max_length=60,
                                               blank=True, null=True)
    inhb_frc_iztnk_Bridge = models.CharField(verbose_name='Bridge to Eccentric Curl w/Swiss Ball', max_length=60,
                                             blank=True, null=True)
    inhb_frc_iztnk_Hip1 = models.CharField(verbose_name='Hip Hinge', max_length=60, blank=True, null=True)
    inhb_frc_iztnk_Hip2 = models.CharField(verbose_name='Hip Hinge + Half Squat', max_length=60, blank=True, null=True)
    inhb_frc_iztnk_Full = models.CharField(verbose_name='Full Squat Hinge', max_length=60, blank=True, null=True)
    inhb_frc_iztnk_Active = models.CharField(verbose_name='Active Hamstring Stretch', max_length=60, blank=True,
                                             null=True)
    inhb_frc_iztnk_Heel = models.CharField(verbose_name='Heel Elevated Goblet Squat', max_length=60, blank=True,
                                           null=True)
    inhb_frc_iztnk_Single1 = models.CharField(verbose_name='Single Leg Eccentric- 2 Up/1 Down', max_length=60,
                                              blank=True, null=True)
    inhb_frc_iztnk_Lateral = models.CharField(verbose_name='Lateral Step Down', max_length=60, blank=True, null=True)
    inhb_frc_iztnk_Single2 = models.CharField(verbose_name='Single Leg Skater Kicks', max_length=60, blank=True,
                                              null=True)
    inhb_frc_iztnk_Assisted = models.CharField(verbose_name='Assisted Reverse Nordic Curl', max_length=60, blank=True,
                                               null=True)
    # IT / SMR
    it_smr_Side1 = models.CharField(verbose_name='Side Lying IT-Band SMR W/Foam Roller', max_length=60, blank=True,
                                    null=True)
    it_smr_IT = models.CharField(verbose_name='IT-Band SMR SMR Alternative', max_length=60, blank=True, null=True)
    it_smr_Side2 = models.CharField(verbose_name='Side Lying IT-Band SMR w/Mini Ball', max_length=60, blank=True,
                                    null=True)
    it_smr_TFL = models.CharField(verbose_name='TFL SMR w/Miniball', max_length=60, blank=True, null=True)
    # IT / STRETCHING
    it_str_Seated1 = models.CharField(verbose_name='Seated One-Leg Extended Leg Hip Stretch', max_length=60, blank=True,
                                      null=True)
    it_str_Standing1 = models.CharField(verbose_name='Standing Hip External Rotator Stretch', max_length=60, blank=True,
                                        null=True)
    it_str_Recumbent1 = models.CharField(verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch',
                                         max_length=60, blank=True, null=True)
    it_str_Recumbent2 = models.CharField(
        verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch (Cross Leg)',
        max_length=70, blank=True, null=True)
    it_str_L = models.CharField(verbose_name='L-Sit Cross Leg- Priformis Stretch', max_length=60, blank=True, null=True)
    it_str_Standing2 = models.CharField(verbose_name='Standing Bent-Knee Hip Adductor Stretch', max_length=60,
                                        blank=True, null=True)
    it_str_Seated2 = models.CharField(verbose_name='Seated Hip Adductor Stretch', max_length=60, blank=True, null=True)
    it_str_Standing3 = models.CharField(verbose_name='Standing Raised-Leg Hip Adductor Stretch', max_length=60,
                                        blank=True, null=True)
    it_str_Standing4 = models.CharField(verbose_name='Standing Knee Flexor Stretch', max_length=60, blank=True,
                                        null=True)
    it_str_Seated3 = models.CharField(verbose_name='Seated Knee Flexor Stretch', max_length=60, blank=True, null=True)
    it_str_Raised = models.CharField(verbose_name='Raised- One Leg Knee Flexor Stretch', max_length=60, blank=True,
                                     null=True)
    it_str_Supine = models.CharField(verbose_name='Supine Lying Raised One-Leg Stretch w/Band', max_length=60,
                                     blank=True, null=True)
    it_str_Seated4 = models.CharField(verbose_name='Seated Wide Range Extended Leg Stretch', max_length=60, blank=True,
                                      null=True)
    it_str_One1 = models.CharField(verbose_name='One-Leg ½ Kneeling Knee Extensor Stretch', max_length=60, blank=True,
                                   null=True)
    it_str_One2 = models.CharField(verbose_name='One-Leg Standing Hip Flexor and Knee Extensor Stretch', max_length=60,
                                   blank=True, null=True)
    it_str_Lying = models.CharField(verbose_name='Lying Hip Flexor and Knee Extensor Stretch', max_length=60,
                                    blank=True, null=True)
    it_str_TFL = models.CharField(verbose_name='TFL Stretch', max_length=60, blank=True, null=True)
    # IT / FORCE / IZOMETRIK
    it_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Bird Dog on  Stability Ball', max_length=60,
                                             blank=True, null=True)
    it_frc_izm_Side = models.CharField(verbose_name='Side Plank', max_length=60, blank=True, null=True)
    it_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric RNT Lunge', max_length=60, blank=True, null=True)
    it_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Banded Hip External Rotation', max_length=60,
                                             blank=True, null=True)
    # IT / FORCE / IZOTONIK
    it_frc_iztnk_Single1 = models.CharField(verbose_name='Single Leg Airplane Twist', max_length=60, blank=True,
                                            null=True)
    it_frc_iztnk_Side1 = models.CharField(verbose_name='Side Lying Clamshell', max_length=60, blank=True, null=True)
    it_frc_iztnk_Bird = models.CharField(verbose_name='Bird Dog on Stability Ball', max_length=60, blank=True,
                                         null=True)
    it_frc_iztnk_Elevated = models.CharField(verbose_name='Elevated Bridge with March', max_length=60, blank=True,
                                             null=True)
    it_frc_iztnk_Side2 = models.CharField(verbose_name='Side Plank w/Hip Abduction', max_length=60, blank=True,
                                          null=True)
    it_frc_iztnk_Single2 = models.CharField(verbose_name='Single Lef RDL with March', max_length=60, blank=True,
                                            null=True)
    it_frc_iztnk_Modified = models.CharField(verbose_name='Modified Downward Dog', max_length=60, blank=True, null=True)
    it_frc_iztnk_Hip = models.CharField(verbose_name='Hip CARs', max_length=60, blank=True, null=True)
    it_frc_iztnk_Lazy = models.CharField(verbose_name='Lazy Priformis Stretch (Mobil)', max_length=60, blank=True,
                                         null=True)
    it_frc_iztnk_Clamshell = models.CharField(verbose_name='Clamshell Kick', max_length=60, blank=True, null=True)
    it_frc_iztnk_Quadruped = models.CharField(verbose_name='Quadruped Fire Hydrant', max_length=60, blank=True,
                                              null=True)
    it_frc_iztnk_Side3 = models.CharField(verbose_name='Side Lying Hip Abduction', max_length=60, blank=True, null=True)
    it_frc_iztnk_Lateral1 = models.CharField(verbose_name='Lateral Pelvic Dip', max_length=60, blank=True, null=True)
    it_frc_iztnk_Step = models.CharField(verbose_name='Step Down', max_length=60, blank=True, null=True)
    it_frc_iztnk_RNT = models.CharField(verbose_name='RNT Lunge', max_length=60, blank=True, null=True)
    it_frc_iztnk_Standing = models.CharField(verbose_name='Standing Fire Hydrant', max_length=60, blank=True, null=True)
    it_frc_iztnk_Side4 = models.CharField(verbose_name='Side Steps', max_length=60, blank=True, null=True)
    it_frc_iztnk_Lateral2 = models.CharField(verbose_name='Lateral Side Step + Cursty Lunge', max_length=60, blank=True,
                                             null=True)
    it_frc_iztnk_Lateral3 = models.CharField(verbose_name='Lateral Tap Down', max_length=60, blank=True, null=True)
    it_frc_iztnk_Seated = models.CharField(verbose_name='Seated External Rotation on Swiss Ball', max_length=60,
                                           blank=True, null=True)
    it_frc_iztnk_Miniband = models.CharField(verbose_name='Miniband Around the World', max_length=60, blank=True,
                                             null=True)
    it_frc_iztnk_Medial = models.CharField(verbose_name='Medial Single Leg Dead Lift', max_length=60, blank=True,
                                           null=True)
    it_frc_iztnk_3 = models.CharField(verbose_name='3 Way Banded Hip External Rotation', max_length=60, blank=True,
                                      null=True)
    it_frc_iztnk_Reverse = models.CharField(verbose_name='Reverse Lunge + Step Over Combo (with medial band pull)',
                                            max_length=60, blank=True, null=True)

    class Meta:
        verbose_name = "Medikal Egzersiz"
        verbose_name_plural = "Medikal Egzersiz "


class medical_exercise11(models.Model):
    # MENISKUS / SMR
    mnsks_smr_Longiditunal = models.CharField(verbose_name='Longiditunal Foam Roller SMR for Priformis', max_length=60,
                                              blank=True, null=True)
    mnsks_smr_Cross1 = models.CharField(verbose_name='Cross Leg Priformis SMR w/Foam Roller', max_length=60, blank=True,
                                        null=True)
    mnsks_smr_Adductors1 = models.CharField(verbose_name='Adductors SMR w/Foam Roller', max_length=60, blank=True,
                                            null=True)
    mnsks_smr_Adductors2 = models.CharField(verbose_name='Adductors SMR w/Miniball', max_length=60, blank=True,
                                            null=True)
    mnsks_smr_Straight = models.CharField(verbose_name='Straight Leg Adductors SMR w/Foam Roller', max_length=60,
                                          blank=True, null=True)
    mnsks_smr_Alternating = models.CharField(verbose_name='Alternating Adductors SMR', max_length=60, blank=True,
                                             null=True)
    mnsks_smr_Side1 = models.CharField(verbose_name='Side Lying IT-Band SMR W/Foam Roller', max_length=60, blank=True,
                                       null=True)
    mnsks_smr_IT = models.CharField(verbose_name='IT-Band SMR Alternative', max_length=60, blank=True, null=True)
    mnsks_smr_Side2 = models.CharField(verbose_name='Side Lying IT-Band SMR w/Mini Ball', max_length=60, blank=True,
                                       null=True)
    mnsks_smr_TFL = models.CharField(verbose_name='TFL SMR w/Miniball', max_length=60, blank=True, null=True)
    mnsks_smr_Two = models.CharField(verbose_name='Two Leg on Foam Roller Hamstring SMR', max_length=60, blank=True,
                                     null=True)
    mnsks_smr_One = models.CharField(verbose_name='One-Leg Hamstring SMR', max_length=60, blank=True, null=True)
    mnsks_smr_Cross2 = models.CharField(verbose_name='Cross Leg Hamstring SMR w/Foam Roller', max_length=60, blank=True,
                                        null=True)
    mnsks_smr_Seated = models.CharField(verbose_name='Seated Hamstring SMR w/Mini Ball', max_length=60, blank=True,
                                        null=True)
    # MENISKUS /  STRETCHING
    mnsks_str_Seated1 = models.CharField(verbose_name='Seated One-Leg Extended Leg Hip Stretch', max_length=60,
                                         blank=True, null=True)
    mnsks_str_Standing1 = models.CharField(verbose_name='Standing Hip External Rotator Stretch', max_length=60,
                                           blank=True, null=True)
    mnsks_str_Recumbent1 = models.CharField(verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch',
                                            max_length=60, blank=True, null=True)
    mnsks_str_Recumbent2 = models.CharField(
        verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch (Cross Leg)',
        max_length=70, blank=True, null=True)
    mnsks_str_L = models.CharField(verbose_name='L-Sit Cross- Priformis Stretch ', max_length=60, blank=True, null=True)
    mnsks_str_Standing2 = models.CharField(verbose_name='Standing Bent-Knee Hip Adductor Stretch', max_length=60,
                                           blank=True, null=True)
    mnsks_str_Seated2 = models.CharField(verbose_name='Seated Hip Adductor Stretch', max_length=60, blank=True,
                                         null=True)
    mnsks_str_Standing3 = models.CharField(verbose_name='Standing Raised-Leg Hip Adductor Stretch', max_length=60,
                                           blank=True, null=True)
    mnsks_str_Standing4 = models.CharField(verbose_name='Standing Knee Flexor Stretch', max_length=60, blank=True,
                                           null=True)
    mnsks_str_Seated3 = models.CharField(verbose_name='Seated Knee Flexor Stretch', max_length=60, blank=True,
                                         null=True)
    mnsks_str_Raised = models.CharField(verbose_name='Raised- One Leg Knee Flexor Stretch', max_length=60, blank=True,
                                        null=True)
    mnsks_str_Supine = models.CharField(verbose_name='Supine Lying Raised One-Leg Stretch w/Band', max_length=60,
                                        blank=True, null=True)
    mnsks_str_Seated4 = models.CharField(verbose_name='Seated Wide Range Extended Leg Stretch ', max_length=60,
                                         blank=True, null=True)
    mnsks_str_One1 = models.CharField(verbose_name='One-Leg ½ Kneeling Knee Extensor Stretch', max_length=60,
                                      blank=True, null=True)
    mnsks_str_One2 = models.CharField(verbose_name='One-Leg Standing Hip Flexor and Knee Extensor Stretc',
                                      max_length=60, blank=True, null=True)
    mnsks_str_Lying = models.CharField(verbose_name='Lying Hip Flexor and Knee Extensor Stretch', max_length=60,
                                       blank=True, null=True)
    # MENISKUS / FORCE / IZOMETRIK
    mnsks_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Spanish Squat', max_length=60, blank=True,
                                                null=True)
    mnsks_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Banded Lunge', max_length=60, blank=True,
                                                null=True)
    mnsks_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Bridge', max_length=60, blank=True, null=True)
    mnsks_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric Squat w/Bosu Ball', max_length=60, blank=True,
                                                null=True)
    mnsks_frc_izm_Straight = models.CharField(verbose_name='Straight Side Plank', max_length=60, blank=True, null=True)
    mnsks_frc_izm_Sustained = models.CharField(verbose_name='Sustained Squat Calf Raise', max_length=60, blank=True,
                                               null=True)
    mnsks_frc_izm_Isometric5 = models.CharField(verbose_name='Isometric Seated Hip External Rotation', max_length=60,
                                                blank=True, null=True)
    mnsks_frc_izm_Isometric6 = models.CharField(verbose_name='Isometric Straight Leg Raise (contracted muscle)',
                                                max_length=60, blank=True, null=True)
    mnsks_frc_izm_Isometric7 = models.CharField(verbose_name='Isometric Straight Leg w/Swiss Ball', max_length=60,
                                                blank=True, null=True)
    mnsks_frc_izm_Isometric8 = models.CharField(verbose_name='Isometric Quadriceps Contracted', max_length=60,
                                                blank=True, null=True)
    # MENISKUS / FORCE /  IZOTONIK
    mnsks_frc_iztnk_Single1 = models.CharField(verbose_name='Single Leg Hip Hinge Taps', max_length=60, blank=True,
                                               null=True)
    mnsks_frc_iztnk_Posterior = models.CharField(verbose_name='Posterior Tibialis Calf Raise', max_length=60,
                                                 blank=True, null=True)
    mnsks_frc_iztnk_Spanish = models.CharField(verbose_name='Spanish Squat', max_length=60, blank=True, null=True)
    mnsks_frc_iztnk_Static1 = models.CharField(verbose_name='Static Lunge w/Resisted Medial Pull', max_length=60,
                                               blank=True, null=True)
    mnsks_frc_iztnk_Bridge = models.CharField(verbose_name='Bridge Walk Outs', max_length=60, blank=True, null=True)
    mnsks_frc_iztnk_Lunge = models.CharField(verbose_name='Lunge with Resisted Lateral Pull', max_length=60, blank=True,
                                             null=True)
    mnsks_frc_iztnk_Single2 = models.CharField(verbose_name='Single Leg Stance with Press Into RDL', max_length=60,
                                               blank=True, null=True)
    mnsks_frc_iztnk_Static2 = models.CharField(verbose_name='Static Lunge Pallof Press', max_length=60, blank=True,
                                               null=True)
    mnsks_frc_iztnk_Cursty = models.CharField(verbose_name='Cursty & Sumo Squat on Bosu', max_length=60, blank=True,
                                              null=True)
    mnsks_frc_iztnk_Seated1 = models.CharField(verbose_name='Seated Tibial Rotation', max_length=60, blank=True,
                                               null=True)
    mnsks_frc_iztnk_Box = models.CharField(verbose_name='Box Squat', max_length=60, blank=True, null=True)
    mnsks_frc_iztnk_Goblet = models.CharField(verbose_name='Goblet Squat to Box', max_length=60, blank=True, null=True)
    mnsks_frc_iztnk_Elevated1 = models.CharField(verbose_name='Elevated 3 Way Eccentric Foot Taps', max_length=60,
                                                 blank=True, null=True)
    mnsks_frc_iztnk_Modified = models.CharField(verbose_name='Modified Skater Squat', max_length=60, blank=True,
                                                null=True)
    mnsks_frc_iztnk_Reverse = models.CharField(verbose_name='Reverse Nordic', max_length=60, blank=True, null=True)
    mnsks_frc_iztnk_Hex = models.CharField(verbose_name='Hex Bar Deadlift', max_length=60, blank=True, null=True)
    mnsks_frc_iztnk_Elevated2 = models.CharField(verbose_name='Elevated Anterior Heel Taps', max_length=60, blank=True,
                                                 null=True)
    mnsks_frc_iztnk_Lateral = models.CharField(verbose_name='Lateral Lunge', max_length=60, blank=True, null=True)
    mnsks_frc_iztnk_Quad = models.CharField(verbose_name='Quad to TKE w/Band', max_length=60, blank=True, null=True)
    mnsks_frc_iztnk_Stability1 = models.CharField(verbose_name='Stability Ball Passes', max_length=60, blank=True,
                                                  null=True)
    mnsks_frc_iztnk_Plank = models.CharField(verbose_name='Plank ‘’KB’’ Drag Throughts', max_length=60, blank=True,
                                             null=True)
    mnsks_frc_iztnk_Standing1 = models.CharField(verbose_name='Standing Hip Abduction', max_length=60, blank=True,
                                                 null=True)
    mnsks_frc_iztnk_Standing2 = models.CharField(verbose_name='Standing Hip Adduction', max_length=60, blank=True,
                                                 null=True)
    mnsks_frc_iztnk_Standing3 = models.CharField(verbose_name='Standing Hip Flexion', max_length=60, blank=True,
                                                 null=True)
    mnsks_frc_iztnk_Standing4 = models.CharField(verbose_name='Standing Hip Extension', max_length=60, blank=True,
                                                 null=True)
    mnsks_frc_iztnk_Seated = models.CharField(verbose_name='Seated Hip Ext. Rot. w/Band', max_length=60, blank=True,
                                              null=True)
    mnsks_frc_iztnk_Straight = models.CharField(verbose_name='Straight Leg Raise', max_length=60, blank=True, null=True)
    mnsks_frc_iztnk_Seated2 = models.CharField(verbose_name='Seated Hamstring Curl', max_length=60, blank=True,
                                               null=True)
    mnsks_frc_iztnk_Seated3 = models.CharField(verbose_name='Seated Calf Raise', max_length=60, blank=True, null=True)
    mnsks_frc_iztnk_Walking1 = models.CharField(verbose_name='Walking Knee Bend/Kick Outs', max_length=60, blank=True,
                                                null=True)
    mnsks_frc_iztnk_Walking2 = models.CharField(verbose_name='Walking Butt Kicks', max_length=60, blank=True, null=True)
    mnsks_frc_iztnk_Walking3 = models.CharField(verbose_name='Walking Hamstring Kicks', max_length=60, blank=True,
                                                null=True)
    mnsks_frc_iztnk_High = models.CharField(verbose_name='High Toe Walks', max_length=60, blank=True, null=True)
    mnsks_frc_iztnk_Stability2 = models.CharField(verbose_name='Stability Ball Straight Leg Bridge', max_length=60,
                                                  blank=True, null=True)
    mnsks_frc_iztnk_Knee = models.CharField(verbose_name='Knee Flexion/Extension Mobility', max_length=60, blank=True,
                                            null=True)
    mnsks_frc_iztnk_Hamstring = models.CharField(verbose_name='Hamstring Curl w/Swiss Ball', max_length=60, blank=True,
                                                 null=True)
    mnsks_frc_iztnk_Bent = models.CharField(verbose_name='Bent Knee Glute Bridge  w/Swiss Ball', max_length=60,
                                            blank=True, null=True)
    mnsks_frc_iztnk_Star = models.CharField(verbose_name='Star Reach', max_length=60, blank=True, null=True)
    # ACL / SMR
    acl_smr_Longiditunal = models.CharField(verbose_name='Longiditunal Foam Roller SMR for Priformis', max_length=60,
                                            blank=True, null=True)
    acl_smr_Cross1 = models.CharField(verbose_name='Cross Leg Priformis SMR w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    acl_smr_Adductors1 = models.CharField(verbose_name='Adductors SMR w/Foam Roller', max_length=60, blank=True,
                                          null=True)
    acl_smr_Adductors2 = models.CharField(verbose_name='Adductors SMR w/Miniball', max_length=60, blank=True, null=True)
    acl_smr_Straight = models.CharField(verbose_name='Straight Leg Adductors SMR w/Foam Roller', max_length=60,
                                        blank=True, null=True)
    acl_smr_Alternating = models.CharField(verbose_name='Alternating Adductors SMR', max_length=60, blank=True,
                                           null=True)
    acl_smr_Side1 = models.CharField(verbose_name='Side Lying IT-Band SMR W/Foam Roller', max_length=60, blank=True,
                                     null=True)
    acl_smr_IT = models.CharField(verbose_name='IT-Band SMR Alternative', max_length=60, blank=True, null=True)
    acl_smr_Side2 = models.CharField(verbose_name='Side Lying IT-Band SMR w/Mini Ball', max_length=60, blank=True,
                                     null=True)
    acl_smr_TFL = models.CharField(verbose_name='TFL SMR w/Miniball', max_length=60, blank=True, null=True)
    acl_smr_Two = models.CharField(verbose_name='Two Leg on Foam Roller Hamstring SMR', max_length=60, blank=True,
                                   null=True)
    acl_smr_One = models.CharField(verbose_name='One-Leg Hamstring SMR', max_length=60, blank=True, null=True)
    acl_smr_Cross2 = models.CharField(verbose_name='Cross Leg Hamstring SMR w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    acl_smr_Seated = models.CharField(verbose_name='Seated Hamstring SMR w/Mini Ball', max_length=60, blank=True,
                                      null=True)
    # ACL /  STRETCHING
    acl_str_Seated1 = models.CharField(verbose_name='Seated One-Leg Extended Leg Hip Stretch', max_length=60,
                                       blank=True, null=True)
    acl_str_Standing1 = models.CharField(verbose_name='Standing Hip External Rotator Stretch', max_length=60,
                                         blank=True, null=True)
    acl_str_Recumbent1 = models.CharField(verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch',
                                          max_length=60, blank=True, null=True)
    acl_str_Recumbent2 = models.CharField(
        verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch (Cross Leg)',
        max_length=70, blank=True, null=True)
    acl_str_L = models.CharField(verbose_name='L-Sit Cross  Leg- Priformis Stretch', max_length=60, blank=True,
                                 null=True)
    acl_str_Standing2 = models.CharField(verbose_name='Standing Bent-Knee Hip Adductor Stretch', max_length=60,
                                         blank=True, null=True)
    acl_str_Seated2 = models.CharField(verbose_name='Seated Hip Adductor Stretch', max_length=60, blank=True, null=True)
    acl_str_Standing3 = models.CharField(verbose_name='Standing Raised-Leg Hip Adductor Stretch', max_length=60,
                                         blank=True, null=True)
    acl_str_Standing4 = models.CharField(verbose_name='Standing Knee Flexor Stretch', max_length=60, blank=True,
                                         null=True)
    acl_str_Seated3 = models.CharField(verbose_name='Seated Knee Flexor Stretch', max_length=60, blank=True, null=True)
    acl_str_Raised = models.CharField(verbose_name='Raised- One Leg Knee Flexor Stretch', max_length=60, blank=True,
                                      null=True)
    acl_str_Supine = models.CharField(verbose_name='Supine Lying Raised One-Leg Stretch w/Band', max_length=60,
                                      blank=True, null=True)
    acl_str_Seated4 = models.CharField(verbose_name='Seated Wide Range Extended Leg Stretch', max_length=60, blank=True,
                                       null=True)
    acl_str_One1 = models.CharField(verbose_name='One-Leg ½ Kneeling Knee Extensor Stretch', max_length=60, blank=True,
                                    null=True)
    acl_str_One2 = models.CharField(verbose_name='One-Leg Standing Hip Flexor and Knee Extensor Stretch', max_length=60,
                                    blank=True, null=True)
    acl_str_Lying = models.CharField(verbose_name='Lying Hip Flexor and Knee Extensor Stretch', max_length=60,
                                     blank=True, null=True)
    #  ACL /  FORCE / IZOMETRIK
    acl_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Prone Hamstring Curl w/Band', max_length=60,
                                              blank=True, null=True)
    acl_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Banded Lunge', max_length=60, blank=True,
                                              null=True)
    acl_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Seated Knee Ext. Ball Pushes', max_length=60,
                                              blank=True, null=True)
    acl_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric Quad Contraction', max_length=60, blank=True,
                                              null=True)
    acl_frc_izm_Single = models.CharField(verbose_name='Single Leg Balance', max_length=60, blank=True, null=True)
    # ACL /  FORCE / IZOTONIK
    acl_frc_iztnk_Single1 = models.CharField(verbose_name='Single Leg Dead Lift and Internal Rotation', max_length=60,
                                             blank=True, null=True)
    acl_frc_iztnk_Hamstring1 = models.CharField(verbose_name='Hamstring Curl w/Stability Ball', max_length=60,
                                                blank=True, null=True)
    acl_frc_iztnk_Prone1 = models.CharField(verbose_name='Prone Hamstring Curl w/Band', max_length=60, blank=True,
                                            null=True)
    acl_frc_iztnk_Standing = models.CharField(verbose_name='Standing Clamshells', max_length=60, blank=True, null=True)
    acl_frc_iztnk_Banded1 = models.CharField(verbose_name='Banded Hip Thrust', max_length=60, blank=True, null=True)
    acl_frc_iztnk_Revese = models.CharField(verbose_name='Revese Lunge (Assisted Band)', max_length=60, blank=True,
                                            null=True)
    acl_frc_iztnk_Bulgarian = models.CharField(verbose_name='Bulgarian Squat', max_length=60, blank=True, null=True)
    acl_frc_iztnk_Seated = models.CharField(verbose_name='Seated Knee Ext. Ball Pushes', max_length=60, blank=True,
                                            null=True)
    acl_frc_iztnk_Straight = models.CharField(verbose_name='Straight Leg Raise', max_length=60, blank=True, null=True)
    acl_frc_iztnk_Knee1 = models.CharField(verbose_name='Knee Planks', max_length=60, blank=True, null=True)
    acl_frc_iztnk_Knee2 = models.CharField(verbose_name='Knee ROM on Wall', max_length=60, blank=True, null=True)
    acl_frc_iztnk_TKE = models.CharField(verbose_name='TKE w/Band', max_length=60, blank=True, null=True)
    acl_frc_iztnk_Banded2 = models.CharField(verbose_name='Banded Box Squat', max_length=60, blank=True, null=True)
    acl_frc_iztnk_Deadlift = models.CharField(verbose_name='Deadlift w/KB', max_length=60, blank=True, null=True)
    acl_frc_iztnk_Calf = models.CharField(verbose_name='Calf Raise', max_length=60, blank=True, null=True)
    acl_frc_iztnk_Banded3 = models.CharField(verbose_name='Banded Pike TKE', max_length=60, blank=True, null=True)
    acl_frc_iztnk_One = models.CharField(verbose_name='One Leg Banded Pike TKE', max_length=60, blank=True, null=True)
    acl_frc_iztnk_Banded4 = models.CharField(verbose_name='Banded Tantrums', max_length=60, blank=True, null=True)
    acl_frc_iztnk_Single2 = models.CharField(verbose_name='Single Leg Slide Board Banded Hamstring Curls',
                                             max_length=60, blank=True, null=True)
    acl_frc_iztnk_Nordic = models.CharField(verbose_name='Nordic Hamstring Curls', max_length=60, blank=True, null=True)
    acl_frc_iztnk_Hamstring2 = models.CharField(verbose_name='Hamstring Curls w/Strap', max_length=60, blank=True,
                                                null=True)
    acl_frc_iztnk_Prone2 = models.CharField(verbose_name='Prone Hamstring Curl', max_length=60, blank=True, null=True)
    acl_frc_iztnk_Lateral = models.CharField(verbose_name='Lateral Step Down Tap', max_length=60, blank=True, null=True)
    # PATELLO / SMR
    ptl_smr_Longiditunal = models.CharField(verbose_name='Longiditunal Foam Roller SMR for Priformis', max_length=60,
                                            blank=True, null=True)
    ptl_smr_Cross1 = models.CharField(verbose_name='Cross Leg Priformis SMR  w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    ptl_smr_Adductors1 = models.CharField(verbose_name='Adductors SMR w/Foam Roller', max_length=60, blank=True,
                                          null=True)
    ptl_smr_Adductors2 = models.CharField(verbose_name='Adductors SMR w/Miniball', max_length=60, blank=True, null=True)
    ptl_smr_Straight = models.CharField(verbose_name='Straight Leg Adductors SMR w/Foam Roller', max_length=60,
                                        blank=True, null=True)
    ptl_smr_Alternating = models.CharField(verbose_name='Alternating Adductors SMR', max_length=60, blank=True,
                                           null=True)
    ptl_smr_Side1 = models.CharField(verbose_name='Side Lying IT-Band SMR W/Foam Roller', max_length=60, blank=True,
                                     null=True)
    ptl_smr_IT = models.CharField(verbose_name='IT-Band SMR Alternative', max_length=60, blank=True, null=True)
    ptl_smr_Side2 = models.CharField(verbose_name='Side Lying IT-Band SMR w/Mini Ball', max_length=60, blank=True,
                                     null=True)
    ptl_smr_TFL = models.CharField(verbose_name='TFL SMR w/Miniball', max_length=60, blank=True, null=True)
    ptl_smr_Two = models.CharField(verbose_name='Two Leg on Foam Roller Hamstring SMR', max_length=60, blank=True,
                                   null=True)
    ptl_smr_One = models.CharField(verbose_name='One-Leg Hamstring SMR', max_length=60, blank=True, null=True)
    ptl_smr_Cross2 = models.CharField(verbose_name='Cross Leg Hamstring SMR w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    ptl_smr_Seated = models.CharField(verbose_name='Seated Hamstring SMR w/Mini Ball', max_length=60, blank=True,
                                      null=True)

    class Meta:
        verbose_name = "Medikal Egzersiz"
        verbose_name_plural = "Medikal Egzersiz "


class medical_exercise12(models.Model):
    # PATELLO / STRETCHING
    ptl_str_Seated1 = models.CharField(verbose_name='Seated One-Leg Extended Leg Hip Stretch', max_length=60,
                                       blank=True, null=True)
    ptl_str_Standing1 = models.CharField(verbose_name='Standing Hip External Rotator Stretch', max_length=60,
                                         blank=True, null=True)
    ptl_str_Recumbent1 = models.CharField(verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch',
                                          max_length=60, blank=True, null=True)
    ptl_str_Recumbent2 = models.CharField(verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch',
                                          max_length=60, blank=True, null=True)
    ptl_str_L = models.CharField(verbose_name='L-Sit Cross Leg- Priformis Stretch', max_length=60, blank=True,
                                 null=True)
    ptl_str_Standing2 = models.CharField(verbose_name='Standing Bent-Knee Hip Adductor Stretch', max_length=60,
                                         blank=True, null=True)
    ptl_str_Seated2 = models.CharField(verbose_name='Seated Hip Adductor Stretch', max_length=60, blank=True, null=True)
    ptl_str_Standing3 = models.CharField(verbose_name='Standing Raised-Leg Hip Adductor Stretch', max_length=60,
                                         blank=True, null=True)
    ptl_str_Standing4 = models.CharField(verbose_name='Standing Knee Flexor Stretch', max_length=60, blank=True,
                                         null=True)
    ptl_str_Seated3 = models.CharField(verbose_name='Seated Knee Flexor Stretch', max_length=60, blank=True, null=True)
    ptl_str_Raised = models.CharField(verbose_name='Raised- One Leg Leg Knee Flexor Stretch', max_length=60, blank=True,
                                      null=True)
    ptl_str_Supine = models.CharField(verbose_name='Supine Lying Raised One-Leg Stretch w/Band', max_length=60,
                                      blank=True, null=True)
    ptl_str_Seated4 = models.CharField(verbose_name='Seated Wide Range Extended Leg Stretch', max_length=60, blank=True,
                                       null=True)
    ptl_str_One1 = models.CharField(verbose_name='One-Leg ½ Kneeling Knee Extensor Stretch', max_length=60, blank=True,
                                    null=True)
    ptl_str_One2 = models.CharField(verbose_name='One-Leg Standing Hip Flexor and Knee Extensor Stretch', max_length=60,
                                    blank=True, null=True)
    ptl_str_Lying = models.CharField(verbose_name='Lying Hip Flexor and Knee Extensor Stretch', max_length=60,
                                     blank=True, null=True)
    # PATELLO / FORCE / IZOMETRIK
    ptl_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Unilateral Hip Bridge', max_length=60, blank=True,
                                              null=True)
    ptl_frc_izm_Side = models.CharField(verbose_name='Side Plank', max_length=60, blank=True, null=True)
    ptl_frc_izm_Half = models.CharField(verbose_name='Half Kneeling Side Plank', max_length=60, blank=True, null=True)
    ptl_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric High Box Down', max_length=60, blank=True,
                                              null=True)
    ptl_frc_izm_Split = models.CharField(verbose_name='Split Squat Hold', max_length=60, blank=True, null=True)
    ptl_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Spanish Squat', max_length=60, blank=True,
                                              null=True)
    ptl_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric Asisted Squat', max_length=60, blank=True,
                                              null=True)
    # PATELLO / FORCE / IZOTONIK
    plt_frc_iztnk_Unilateral = models.CharField(verbose_name='Unilateral Hip Bridge', max_length=60, blank=True,
                                                null=True)
    plt_frc_iztnk_Banded = models.CharField(verbose_name='Banded Side Steps', max_length=60, blank=True, null=True)
    plt_frc_iztnk_Side1 = models.CharField(verbose_name='Side Lying Hip Abduction', max_length=60, blank=True,
                                           null=True)
    plt_frc_iztnk_Rear = models.CharField(verbose_name='Rear Foot Elevated Split Squat', max_length=60, blank=True,
                                          null=True)
    plt_frc_iztnk_Push = models.CharField(verbose_name='Push the Band Out', max_length=60, blank=True, null=True)
    plt_frc_iztnk_Step = models.CharField(verbose_name='Step-Up w/RB', max_length=60, blank=True, null=True)
    plt_frc_iztnk_Side2 = models.CharField(verbose_name='Side Lying Clamshells', max_length=60, blank=True, null=True)
    plt_frc_iztnk_Hip1 = models.CharField(verbose_name='Hip Thruster', max_length=60, blank=True, null=True)
    plt_frc_iztnk_Tibial = models.CharField(verbose_name='Tibial Rotation with Knee Extension', max_length=60,
                                            blank=True, null=True)
    plt_frc_iztnk_Patellar = models.CharField(verbose_name='Patellar Mobilization', max_length=60, blank=True,
                                              null=True)
    plt_frc_iztnk_Terminal = models.CharField(verbose_name='Terminal Knee Extension w/RB', max_length=60, blank=True,
                                              null=True)
    plt_frc_iztnk_Anterior = models.CharField(verbose_name='Anterior/Posterior Step Down', max_length=60, blank=True,
                                              null=True)
    plt_frc_iztnk_Quick = models.CharField(verbose_name='Quick Drop High Box Heel Taps', max_length=60, blank=True,
                                           null=True)
    plt_frc_iztnk_Quadruped = models.CharField(verbose_name='Quadruped Knee Ext. w/Band', max_length=60, blank=True,
                                               null=True)
    plt_frc_iztnk_Counterbalance = models.CharField(verbose_name='Counterbalance Pistol to Box', max_length=60,
                                                    blank=True, null=True)
    plt_frc_iztnk_Spanish = models.CharField(verbose_name='Spanish Squat', max_length=60, blank=True, null=True)
    plt_frc_iztnk_Seated1 = models.CharField(verbose_name='Seated Knee Extension w/Band', max_length=60, blank=True,
                                             null=True)
    plt_frc_iztnk_Lunge = models.CharField(verbose_name='Lunge Pulse', max_length=60, blank=True, null=True)
    plt_frc_iztnk_Single1 = models.CharField(verbose_name='Single Leg Deadlift w/KB', max_length=60, blank=True,
                                             null=True)
    plt_frc_iztnk_Box = models.CharField(verbose_name='Box Squat', max_length=60, blank=True, null=True)
    plt_frc_iztnk_Hip2 = models.CharField(verbose_name='Hip Thrust Alternative 1', max_length=60, blank=True, null=True)
    plt_frc_iztnk_Dead = models.CharField(verbose_name='Dead Bug Variation w/RB', max_length=60, blank=True, null=True)
    plt_frc_iztnk_Single2 = models.CharField(verbose_name='Single Leg Dead Lift w/RB', max_length=60, blank=True,
                                             null=True)
    plt_frc_iztnk_Reverse = models.CharField(verbose_name='Reverse Lunge w/RB', max_length=60, blank=True, null=True)
    plt_frc_iztnk_Asisted1 = models.CharField(verbose_name='Asisted Single Leg Sit', max_length=60, blank=True,
                                              null=True)
    plt_frc_iztnk_Asisted2 = models.CharField(verbose_name='Asisted Squat', max_length=60, blank=True, null=True)
    plt_frc_iztnk_Bend = models.CharField(verbose_name='Bend Knee Side Lying Hip Abduction', max_length=60, blank=True,
                                          null=True)
    plt_frc_iztnk_Standing = models.CharField(verbose_name='Standing Ankle Mobility', max_length=60, blank=True,
                                              null=True)
    plt_frc_iztnk_Seated2 = models.CharField(verbose_name='Seated Hip Mobility', max_length=60, blank=True, null=True)
    # RUNNER / SMR
    rnn_smr_Longiditunal = models.CharField(verbose_name='Longiditunal Foam Roller SMR for Priformis', max_length=60,
                                            blank=True, null=True)
    rnn_smr_Cross1 = models.CharField(verbose_name='Cross Leg Priformis SMR w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    rnn_smr_Adductors1 = models.CharField(verbose_name='Adductors SMR w/Foam Roller', max_length=60, blank=True,
                                          null=True)
    rnn_smr_Adductors2 = models.CharField(verbose_name='Adductors SMR w/Miniball', max_length=60, blank=True, null=True)
    rnn_smr_Straight = models.CharField(verbose_name='Straight Leg Adductors SMR w/Foam Roller', max_length=60,
                                        blank=True, null=True)
    rnn_smr_Alternating = models.CharField(verbose_name='Alternating Adductors SMR', max_length=60, blank=True,
                                           null=True)
    rnn_smr_Side1 = models.CharField(verbose_name='Side Lying IT-Band SMR W/Foam Roller', max_length=60, blank=True,
                                     null=True)
    rnn_smr_IT = models.CharField(verbose_name='IT-Band SMR Alternative', max_length=60, blank=True, null=True)
    rnn_smr_Side2 = models.CharField(verbose_name='Side Lying IT-Band SMR w/Mini Ball', max_length=60, blank=True,
                                     null=True)
    rnn_smr_TFL = models.CharField(verbose_name='TFL SMR w/Miniball', max_length=60, blank=True, null=True)
    rnn_smr_Two = models.CharField(verbose_name='Two Leg on Foam Roller Hamstring SMR', max_length=60, blank=True,
                                   null=True)
    rnn_smr_One = models.CharField(verbose_name='One-Leg Hamstring SMR', max_length=60, blank=True, null=True)
    rnn_smr_Cross2 = models.CharField(verbose_name='Cross Leg Hamstring SMR w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    rnn_smr_Seated = models.CharField(verbose_name='Seated Hamstring SMR w/Mini Ball', max_length=60, blank=True,
                                      null=True)
    # RUNNER / STRETCHING
    rnn_str_Seated1 = models.CharField(verbose_name='Seated One-Leg Extended Leg Hip Stretch', max_length=60,
                                       blank=True, null=True)
    rnn_str_Standing1 = models.CharField(verbose_name='Standing Hip External Rotator Stretch', max_length=60,
                                         blank=True, null=True)
    rnn_str_Recumbent1 = models.CharField(verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch',
                                          max_length=60, blank=True, null=True)
    rnn_str_Recumbent2 = models.CharField(
        verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch (Cross Leg)',
        max_length=70, blank=True, null=True)
    rnn_str_L = models.CharField(verbose_name='L-Sit Cross Leg- Priformis Stretch', max_length=60, blank=True,
                                 null=True)
    rnn_str_Standing2 = models.CharField(verbose_name='Standing Bent-Knee Hip Adductor Stretch', max_length=60,
                                         blank=True, null=True)
    rnn_str_Seated2 = models.CharField(verbose_name='Seated Hip Adductor Stretch', max_length=60, blank=True, null=True)
    rnn_str_Standing3 = models.CharField(verbose_name='Standing Raised-Leg Hip Adductor Stretch', max_length=60,
                                         blank=True, null=True)
    rnn_str_Standing4 = models.CharField(verbose_name='Standing Knee Flexor Stretch', max_length=60, blank=True,
                                         null=True)
    rnn_str_Seated3 = models.CharField(verbose_name='Seated Knee Flexor Stretch', max_length=60, blank=True, null=True)
    rnn_str_Raised = models.CharField(verbose_name='Raised- One Leg Knee Flexor Stretch', max_length=60, blank=True,
                                      null=True)
    rnn_str_Supine = models.CharField(verbose_name='Supine Lying Raised One-Leg Stretch w/Band', max_length=60,
                                      blank=True, null=True)
    rnn_str_Seated4 = models.CharField(verbose_name='Seated Wide Range Extended  Leg Stretch', max_length=60,
                                       blank=True, null=True)
    rnn_str_One1 = models.CharField(verbose_name='One-Leg ½ Kneeling Knee Extensor Stretch', max_length=60, blank=True,
                                    null=True)
    rnn_str_One2 = models.CharField(verbose_name='One-Leg Standing Standing Hip Flexor and Knee Extensor Stretch',
                                    max_length=60, blank=True, null=True)
    rnn_str_Lying = models.CharField(verbose_name='Lying Hip Flexor and Knee Extensor Stretch', max_length=60,
                                     blank=True, null=True)
    # RUNNER / FORCE / IZOMETRIK
    rnn_frc_izm_Knee = models.CharField(verbose_name='Knee Flexion Gapping w/Towel', max_length=60, blank=True,
                                        null=True)
    rnn_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Prone Hamstring Curl w/Band', max_length=60,
                                              blank=True, null=True)
    rnn_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Banded Lunge', max_length=60, blank=True,
                                              null=True)
    rnn_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Seated Knee Ext. Ball Pushes', max_length=60,
                                              blank=True, null=True)
    rnn_frc_izm_Isometric4 = models.CharField(verbose_name='Isometric Quad Contraction', max_length=60, blank=True,
                                              null=True)
    rnn_frc_izm_Single = models.CharField(verbose_name='Single Leg Balance', max_length=60, blank=True, null=True)
    # RUNNER / FORCE / IZOTONIK
    rnn_frc_iztnk_Tibial = models.CharField(verbose_name='Tibial Rotation w/Slider', max_length=60, blank=True,
                                            null=True)
    rnn_frc_iztnk_Seated1 = models.CharField(verbose_name='Seated Tibial Rotation and Knee Ext.', max_length=60,
                                             blank=True, null=True)
    rnn_frc_iztnk_Seated2 = models.CharField(verbose_name='Seated Tbial Rotation', max_length=60, blank=True, null=True)
    rnn_frc_iztnk_Side = models.CharField(verbose_name='Side Lying Hip Abduction w/Band', max_length=60, blank=True,
                                          null=True)
    rnn_frc_iztnk_Lateral1 = models.CharField(verbose_name='Lateral Step Down', max_length=60, blank=True, null=True)
    rnn_frc_iztnk_Anterior = models.CharField(verbose_name='Anterior Step Down', max_length=60, blank=True, null=True)
    rnn_frc_iztnk_Posterior = models.CharField(verbose_name='Posterior Step Down', max_length=60, blank=True, null=True)
    rnn_frc_iztnk_Modified = models.CharField(verbose_name='Modified Side Plank and Reach', max_length=60, blank=True,
                                              null=True)
    rnn_frc_iztnk_Nordic = models.CharField(verbose_name='Nordic Curl', max_length=60, blank=True, null=True)
    rnn_frc_iztnk_Lateral2 = models.CharField(verbose_name='Lateral Hop and Hold', max_length=60, blank=True, null=True)
    rnn_frc_iztnk_Single = models.CharField(verbose_name='Single Leg Heel Raise', max_length=60, blank=True, null=True)
    rnn_frc_iztnk_Banded = models.CharField(verbose_name='Banded Squat', max_length=60, blank=True, null=True)
    rnn_frc_iztnk_Standing = models.CharField(verbose_name='Standing Siatic Nerve Glide', max_length=60, blank=True,
                                              null=True)
    rnn_frc_iztnk_Ankle = models.CharField(verbose_name='Ankle ‘’DF’’ Mobilization', max_length=60, blank=True,
                                           null=True)
    # MEDIAL / SMR
    mdl_smr_One = models.CharField(verbose_name='One-Straight Leg T.A. SMR w/Foam Roller', max_length=60, blank=True,
                                   null=True)
    mdl_smr_Seated = models.CharField(verbose_name='Seated T.A. SMR w/Mini Ball', max_length=60, blank=True, null=True)
    mdl_smr_Alternating = models.CharField(verbose_name='Alternating T.A SMR w/Foam Roller', max_length=60, blank=True,
                                           null=True)
    mdl_smr_Cross = models.CharField(verbose_name='Cross Leg T.A. SMR w/Foam Rolle', max_length=60, blank=True,
                                     null=True)
    # MEDIAL / STRETCHING
    mdl_str_Calf1 = models.CharField(verbose_name='Calf Stretch Leg Straight', max_length=60, blank=True, null=True)
    mdl_str_Calf2 = models.CharField(verbose_name='Calf Stretch Knee Bent', max_length=60, blank=True, null=True)
    mdl_str_Seated1 = models.CharField(verbose_name='Seated One-Leg Extended Leg Hip Stretch', max_length=60,
                                       blank=True, null=True)
    mdl_str_Standing1 = models.CharField(verbose_name='Standing Hip External Rotator Stretch', max_length=60,
                                         blank=True, null=True)
    mdl_str_Recumbent1 = models.CharField(verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch',
                                          max_length=60, blank=True, null=True)
    mdl_str_Recumbent2 = models.CharField(
        verbose_name='Recumbent Hip External Rotator and Hip Extensor Stretch (Cross Leg)',
        max_length=70, blank=True, null=True)
    mdl_str_L = models.CharField(verbose_name='L-Sit Cross  Leg- Priformis Stretch', max_length=60, blank=True,
                                 null=True)
    mdl_str_Standing2 = models.CharField(verbose_name='Standing Bent-Knee Hip Adductor Stretch', max_length=60,
                                         blank=True, null=True)
    mdl_str_Seated2 = models.CharField(verbose_name='Seated Hip Adductor Stretch', max_length=60, blank=True, null=True)
    mdl_str_Standing3 = models.CharField(verbose_name='Standing Raised-Leg Hip Adductor Stretch', max_length=60,
                                         blank=True, null=True)
    mdl_str_Standing4 = models.CharField(verbose_name='Standing Knee Flexor Stretch', max_length=60, blank=True,
                                         null=True)
    mdl_str_Seated3 = models.CharField(verbose_name='Seated Knee Flexor Stretch', max_length=60, blank=True, null=True)
    mdl_str_Raised = models.CharField(verbose_name='Raised- One Leg Knee Flexor Stretch', max_length=60, blank=True,
                                      null=True)
    mdl_str_Supine = models.CharField(verbose_name='Supine Lying Raised One-Leg Stretch w/Band', max_length=60,
                                      blank=True, null=True)
    mdl_str_Seated4 = models.CharField(verbose_name='Seated Wide Range Extended Leg Stretch', max_length=60, blank=True,
                                       null=True)
    mdl_str_One1 = models.CharField(verbose_name='One-Leg ½ Kneeling Knee Extensor Stretch', max_length=60, blank=True,
                                    null=True)
    mdl_str_One2 = models.CharField(verbose_name='One-Leg Standing Hip Flexor and Knee Extensor Stretch', max_length=60,
                                    blank=True, null=True)
    mdl_str_Lying = models.CharField(verbose_name='Lying Hip Flexor and Knee Extensor Stretch', max_length=60,
                                     blank=True, null=True)
    # MEDIAL / FORCE / IZOMETRIK
    mdl_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Plantar Flexion w/Kettlebell', max_length=60,
                                              blank=True, null=True)
    mdl_frc_izm_Quadruped = models.CharField(verbose_name='Quadruped Raise Knee and Hold', max_length=60, blank=True,
                                             null=True)
    mdl_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Dorsi Flexion', max_length=60, blank=True,
                                              null=True)
    mdl_frc_izm_Isometric3 = models.CharField(verbose_name='Isometric Plantar Flexion', max_length=60, blank=True,
                                              null=True)
    # MEDIAL / FORCE / IZOTONIK
    mdl_frc_iztnk_Plantar1 = models.CharField(verbose_name='Plantar/ Dorsi Flexion w/Kettlebell', max_length=60,
                                              blank=True, null=True)
    mdl_frc_iztnk_Plantar2 = models.CharField(verbose_name='Plantar Flexion/İnversion w/Band', max_length=60,
                                              blank=True, null=True)
    mdl_frc_iztnk_Active = models.CharField(verbose_name='Active Quadruped Raise Knee and Hold', max_length=60,
                                            blank=True, null=True)
    mdl_frc_iztnk_Heel1 = models.CharField(verbose_name='Heel Walks', max_length=60, blank=True, null=True)
    mdl_frc_iztnk_Eccentric = models.CharField(verbose_name='Eccentric Dorsiflexion w/Dowel', max_length=60, blank=True,
                                               null=True)
    mdl_frc_iztnk_Controlled = models.CharField(verbose_name='Controlled Foot Lowering', max_length=60, blank=True,
                                                null=True)
    mdl_frc_iztnk_Arch = models.CharField(verbose_name='Arch-Ups', max_length=60, blank=True, null=True)
    mdl_frc_iztnk_Band1 = models.CharField(verbose_name='Band İnversion', max_length=60, blank=True, null=True)
    mdl_frc_iztnk_Standing1 = models.CharField(verbose_name='Standing Calf Raise w/Band', max_length=60, blank=True,
                                               null=True)
    mdl_frc_iztnk_Standing2 = models.CharField(verbose_name='Standing Calf Raise Toes İn', max_length=60, blank=True,
                                               null=True)
    mdl_frc_iztnk_Single1 = models.CharField(verbose_name='Single Leg Dumbbell Pass', max_length=60, blank=True,
                                             null=True)
    mdl_frc_iztnk_Band2 = models.CharField(verbose_name='Band Eversion and Plantar Flexion (Elevated Heel)',
                                           max_length=60, blank=True, null=True)
    mdl_frc_iztnk_Band3 = models.CharField(verbose_name='Band Eversion (Alternative 1)', max_length=60, blank=True,
                                           null=True)
    mdl_frc_iztnk_Monster = models.CharField(verbose_name='Monster Walk Band at Toe', max_length=60, blank=True,
                                             null=True)
    mdl_frc_iztnk_Single2 = models.CharField(verbose_name='Single Leg Calf Raise (Eversion Focus)', max_length=60,
                                             blank=True, null=True)
    mdl_frc_iztnk_Heel2 = models.CharField(verbose_name='Heel Elevated Seated Drosiflexion w/KB', max_length=60,
                                           blank=True, null=True)
    mdl_frc_iztnk_Single3 = models.CharField(verbose_name='Single Leg Rotation w/Band', max_length=60, blank=True,
                                             null=True)
    mdl_frc_iztnk_Bent = models.CharField(verbose_name='Bent Knee Calf Raise', max_length=60, blank=True, null=True)
    mdl_frc_iztnk_Plantar3 = models.CharField(verbose_name='Plantar Flexion Walk', max_length=60, blank=True, null=True)
    mdl_frc_iztnk_Calf = models.CharField(verbose_name='Calf Raise Squeezing Tennis Ball', max_length=60, blank=True,
                                          null=True)
    mdl_frc_iztnk_Ankle = models.CharField(verbose_name='Ankle Dorsi Flexion + Isometric Control of Eversion',
                                           max_length=60, blank=True, null=True)
    mdl_frc_iztnk_Seated = models.CharField(verbose_name='Seated Banded Inversion', max_length=60, blank=True,
                                            null=True)
    mdl_frc_iztnk_Banded = models.CharField(verbose_name='Banded Dorsi Flexion + Eversion', max_length=60, blank=True,
                                            null=True)
    mdl_frc_iztnk_Heels = models.CharField(verbose_name='Heels Elevated Toe Lift', max_length=60, blank=True, null=True)
    mdl_frc_iztnk_Squeeze = models.CharField(verbose_name='Squeeze Ball Heel Raise  + Toe Raise', max_length=60,
                                             blank=True, null=True)
    mdl_frc_iztnk_Toe = models.CharField(verbose_name='“KB” Toe Lift Up and Hip Flexion', max_length=60, blank=True,
                                         null=True)

    class Meta:
        verbose_name = "Medikal Egzersiz"
        verbose_name_plural = "Medikal Egzersiz "


class medical_exercise13(models.Model):
    # ANKLE / SMR
    ankl1_smr_Bottom1 = models.CharField(verbose_name='Bottom of Foot Glide w/Mini Ball', max_length=60, blank=True,
                                         null=True)
    ankl1_smr_Bottom2 = models.CharField(verbose_name='Bottom of Foot Glide w/Foam Roller', max_length=60, blank=True,
                                         null=True)
    ankl1_smr_Seated1 = models.CharField(verbose_name='Seated Bottom of Foot Glide w/Miniball-Foam Roller',
                                         max_length=60, blank=True, null=True)
    ankl1_smr_One1 = models.CharField(verbose_name='One-Straight Leg T.A. SMR w/Foam Rolle', max_length=60, blank=True,
                                      null=True)
    ankl1_smr_Seated2 = models.CharField(verbose_name='Seated T.A. SMR w/Mini Ball', max_length=60, blank=True,
                                         null=True)
    ankl1_smr_Alternating = models.CharField(verbose_name='Alternating T.A SMR w/Foam Roller', max_length=60,
                                             blank=True, null=True)
    ankl1_smr_Cross1 = models.CharField(verbose_name='Cross Leg T.A. SMR w/Foam Roller', max_length=60, blank=True,
                                        null=True)
    ankl1_smr_One2 = models.CharField(verbose_name='One-Leg Calf SMR w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    ankl1_smr_Cross2 = models.CharField(verbose_name='Cross Leg Calf SMR w/Foam Roller', max_length=60, blank=True,
                                        null=True)
    ankl1_smr_Two = models.CharField(verbose_name='Two Leg On Foam Roller Calf SMR', max_length=60, blank=True,
                                     null=True)
    ankl1_smr_Calf = models.CharField(verbose_name='Calf SMR W/Mini Ball', max_length=60, blank=True, null=True)
    # ANKLE / STRETCHING
    ankl1_str_Bear = models.CharField(verbose_name='Bear Position Big Toe Stretch', max_length=60, blank=True,
                                      null=True)
    ankl1_str_Foot = models.CharField(verbose_name='Foot on Wall Calf Stretch', max_length=60, blank=True, null=True)
    ankl1_str_Quadruped = models.CharField(verbose_name='Quadruped Rock Back-Big Toe Ext. Bias', max_length=60,
                                           blank=True, null=True)
    ankl1_str_Seated1 = models.CharField(verbose_name='Seated Toe Extensor Stretch', max_length=60, blank=True,
                                         null=True)
    ankl1_str_Seated2 = models.CharField(verbose_name='Seated Toe Extensor and Foot Everter Stretch', max_length=60,
                                         blank=True, null=True)
    ankl1_str_Seated3 = models.CharField(verbose_name='Seated Toe Extensor and Foot Inverter Stretch', max_length=60,
                                         blank=True, null=True)
    ankl1_str_Seated4 = models.CharField(verbose_name='Seated Toe Flexor Stretch', max_length=60, blank=True, null=True)
    ankl1_str_Seated5 = models.CharField(verbose_name='Seated Toe Flexor and Foot Everter Stretch', max_length=60,
                                         blank=True, null=True)
    ankl1_str_Seated6 = models.CharField(verbose_name='Seated Toe Flexor and Foot Inverter Stretch', max_length=60,
                                         blank=True, null=True)
    ankl1_str_Standing = models.CharField(verbose_name='Standing Toe Extensor Stretch', max_length=60, blank=True,
                                          null=True)
    ankl1_str_Single = models.CharField(verbose_name='Single Plantar Flexor Stretch', max_length=60, blank=True,
                                        null=True)
    # ANKLE / FORCE / IZOMETRIK
    ankl1_frc_izm_Single1 = models.CharField(verbose_name='Single Leg Bosu Balance', max_length=60, blank=True,
                                             null=True)
    ankl1_frc_izm_Tandem = models.CharField(verbose_name='Tandem Stance Balance (Eyes Open/Closed)', max_length=60,
                                            blank=True, null=True)
    ankl1_frc_izm_Single2 = models.CharField(verbose_name='Single Leg Balance w/RB', max_length=60, blank=True,
                                             null=True)
    ankl1_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Wall Squat', max_length=60, blank=True,
                                                null=True)
    ankl1_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Wall Squat w/Plantar Flexioned', max_length=60,
                                                blank=True, null=True)
    # ANKLE / FORCE / IZOTONIK
    ankl1_frc_iztnk_Eccentric = models.CharField(verbose_name='Eccentric Calf Raise', max_length=60, blank=True,
                                                 null=True)
    ankl1_frc_iztnk_Banded1 = models.CharField(verbose_name='Banded Side Steps', max_length=60, blank=True, null=True)
    ankl1_frc_iztnk_Reverse = models.CharField(verbose_name='Reverse Lunge on Bosu', max_length=60, blank=True,
                                               null=True)
    ankl1_frc_iztnk_Single1 = models.CharField(verbose_name='Single Leg Hip Hinge', max_length=60, blank=True,
                                               null=True)
    ankl1_frc_iztnk_Heel1 = models.CharField(verbose_name='Heel Toe Walking', max_length=60, blank=True, null=True)
    ankl1_frc_iztnk_Sliders = models.CharField(verbose_name='Sliders (No Shoes)', max_length=60, blank=True, null=True)
    ankl1_frc_iztnk_Single2 = models.CharField(verbose_name='Single Leg Squat Catch on Bosu', max_length=60, blank=True,
                                               null=True)
    ankl1_frc_iztnk_Lateral = models.CharField(verbose_name='Lateral Bounding w/RB', max_length=60, blank=True,
                                               null=True)
    ankl1_frc_iztnk_Side = models.CharField(verbose_name='Side Step w/Mini Band', max_length=60, blank=True, null=True)
    ankl1_frc_iztnk_Single3 = models.CharField(verbose_name='Single Leg RDL,Kettlebell Handoff', max_length=60,
                                               blank=True, null=True)
    ankl1_frc_iztnk_Single4 = models.CharField(verbose_name='Single Leg Dead Lift and Forward Reach', max_length=60,
                                               blank=True, null=True)
    ankl1_frc_iztnk_Banded2 = models.CharField(verbose_name='Banded Eversion', max_length=60, blank=True, null=True)
    ankl1_frc_iztnk_Kneeling = models.CharField(verbose_name='½ Kneeling DF Mobility', max_length=60, blank=True,
                                                null=True)
    ankl1_frc_iztnk_Heel2 = models.CharField(verbose_name='Heel Raise', max_length=60, blank=True, null=True)
    ankl1_frc_iztnk_Single5 = models.CharField(verbose_name='Single Leg Toe Tap', max_length=60, blank=True, null=True)
    ankl1_frc_iztnk_Standing = models.CharField(verbose_name='Standing Hydrants', max_length=60, blank=True, null=True)
    ankl1_frc_iztnk_Miniband1 = models.CharField(verbose_name='Miniband Inversion', max_length=60, blank=True,
                                                 null=True)
    ankl1_frc_iztnk_Miniband2 = models.CharField(verbose_name='Miniband Plantar Flexion', max_length=60, blank=True,
                                                 null=True)
    ankl1_frc_iztnk_Miniband3 = models.CharField(verbose_name='Miniband Big Toe Flexion', max_length=60, blank=True,
                                                 null=True)
    ankl1_frc_iztnk_Miniband4 = models.CharField(verbose_name='Miniband Dorsi Flexion', max_length=60, blank=True,
                                                 null=True)
    ankl1_frc_iztnk_Transverse1 = models.CharField(verbose_name='Transverse Lateral Woodpecker', max_length=60,
                                                   blank=True, null=True)
    ankl1_frc_iztnk_Transverse2 = models.CharField(verbose_name='Transverse Medial Woodpecker', max_length=60,
                                                   blank=True, null=True)
    ankl1_frc_iztnk_Sagittal = models.CharField(verbose_name='Sagittal Anterior Woodpecker', max_length=60, blank=True,
                                                null=True)
    ankl1_frc_iztnk_Dribble1 = models.CharField(verbose_name='Dribble Forward Wall Pass on Ped', max_length=60,
                                                blank=True, null=True)
    ankl1_frc_iztnk_Dribble2 = models.CharField(verbose_name='Dribble Lateral Wall Pass on Ped', max_length=60,
                                                blank=True, null=True)
    ankl1_frc_iztnk_Dribble3 = models.CharField(verbose_name='Dribble Medial Wall Pass on Ped', max_length=60,
                                                blank=True, null=True)
    ankl1_frc_iztnk_Rotational = models.CharField(verbose_name='Rotational Dribbling on Ped', max_length=60, blank=True,
                                                  null=True)
    # RUPTURU / SMR
    rptr_smr_Bottom1 = models.CharField(verbose_name='Bottom of Foot Glide w/Mini Ball', max_length=60, blank=True,
                                        null=True)
    rptr_smr_Bottom2 = models.CharField(verbose_name='Bottom of Foot Glide w/Foam Roller', max_length=60, blank=True,
                                        null=True)
    rptr_smr_Seated1 = models.CharField(verbose_name='Seated Bottom of Foot Glide w/Miniball-Foam Roller',
                                        max_length=60, blank=True, null=True)
    rptr_smr_One1 = models.CharField(verbose_name='One-Straight Leg T.A. SMR w/Foam Roller', max_length=60, blank=True,
                                     null=True)
    rptr_smr_Seated2 = models.CharField(verbose_name='Seated T.A.  SMR w/Mini Ball', max_length=60, blank=True,
                                        null=True)
    rptr_smr_Alternating = models.CharField(verbose_name='Alternating T.A SMR w/Foam Roller', max_length=60, blank=True,
                                            null=True)
    rptr_smr_Cross1 = models.CharField(verbose_name='Cross Leg T.A.  SMR w/Foam Roller', max_length=60, blank=True,
                                       null=True)
    rptr_smr_One2 = models.CharField(verbose_name='One-Leg Calf SMR w/Foam Roller', max_length=60, blank=True,
                                     null=True)
    rptr_smr_Cross2 = models.CharField(verbose_name='Cross Leg Calf SMR w/Foam Roller', max_length=60, blank=True,
                                       null=True)
    rptr_smr_Two = models.CharField(verbose_name='Two Leg On Foam Roller  Calf SMR', max_length=60, blank=True,
                                    null=True)
    rptr_smr_Calf = models.CharField(verbose_name='Calf SMR W/Mini Mini Ball', max_length=60, blank=True, null=True)
    # RUPTURU / STRETCHING
    rptr_str_Bear = models.CharField(verbose_name='Bear Position Big Toe Stretch ', max_length=60, blank=True,
                                     null=True)
    rptr_str_Foot = models.CharField(verbose_name='Foot on Wall Calf Stretch', max_length=60, blank=True, null=True)
    rptr_str_Quadruped = models.CharField(verbose_name='Quadruped Rock Back - Big  Toe Ext. Bias', max_length=60,
                                          blank=True, null=True)
    rptr_str_Seated1 = models.CharField(verbose_name='Seated Toe Extensor Stretch ', max_length=60, blank=True,
                                        null=True)
    rptr_str_Seated2 = models.CharField(verbose_name='Seated Toe Extensor and Foot Everter Stretch', max_length=60,
                                        blank=True, null=True)
    rptr_str_Seated3 = models.CharField(verbose_name='Seated Toe Extensor and Foot Inverter Stretch', max_length=60,
                                        blank=True, null=True)
    rptr_str_Seated4 = models.CharField(verbose_name='Seated Toe Flexor Stretch', max_length=60, blank=True, null=True)
    rptr_str_Seated5 = models.CharField(verbose_name='Seated Toe Flexor and Foot Everter Stretch', max_length=60,
                                        blank=True, null=True)
    rptr_str_Seated6 = models.CharField(verbose_name='Seated Toe Flexor and Foot Inverter Stretch', max_length=60,
                                        blank=True, null=True)
    rptr_str_Standing = models.CharField(verbose_name='Standing Toe Extensor Stretch', max_length=60, blank=True,
                                         null=True)
    rptr_str_Single = models.CharField(verbose_name='Single Plantar Flexor Stretch', max_length=60, blank=True,
                                       null=True)
    # RUPTURU / FORCE / IZOMETRIK
    rptr_frc_izm_Isometric = models.CharField(verbose_name='Isometric Hold Calf Raise', max_length=60, blank=True,
                                              null=True)
    rptr_frc_izm_Single = models.CharField(verbose_name='Single Leg Calf Raise (Isometric Hold)', max_length=60,
                                           blank=True, null=True)
    rptr_frc_izm_Bent = models.CharField(verbose_name='Bent Knee Split Stance Isometric ', max_length=60, blank=True,
                                         null=True)
    rptr_frc_izm_Seated = models.CharField(verbose_name='Seated Ankle Isometric Hold w/Band', max_length=60, blank=True,
                                           null=True)
    # RUPTURU / FORCE / IZOTONIK
    rptr_frc_iztnk_Low = models.CharField(verbose_name='Low Ankle Walks', max_length=60, blank=True, null=True)
    rptr_frc_iztnk_Lunge = models.CharField(verbose_name='Lunge w/Calf Raise', max_length=60, blank=True, null=True)
    rptr_frc_iztnk_Single1 = models.CharField(verbose_name='Single Leg Deadlift (Transport Dumbbell)', max_length=60,
                                              blank=True, null=True)
    rptr_frc_iztnk_Active = models.CharField(verbose_name='Active Foot Dumbbell Passes', max_length=60, blank=True,
                                             null=True)
    rptr_frc_iztnk_Single2 = models.CharField(verbose_name='Single Leg Calf Raise', max_length=60, blank=True,
                                              null=True)
    rptr_frc_iztnk_Bent = models.CharField(verbose_name='Bent Knee Calf Raise', max_length=60, blank=True, null=True)
    rptr_frc_iztnk_Standing = models.CharField(verbose_name='Standing Short Foot', max_length=60, blank=True, null=True)
    rptr_frc_iztnk_Split = models.CharField(verbose_name='Split Stance Soleus Raise', max_length=60, blank=True,
                                            null=True)
    rptr_frc_iztnk_Single3 = models.CharField(verbose_name='Single Leg Heel Raise w/Weight Shif', max_length=60,
                                              blank=True, null=True)
    rptr_frc_iztnk_Ankle = models.CharField(verbose_name='Ankle DF movement with mobilization', max_length=60,
                                            blank=True, null=True)
    rptr_frc_iztnk_Soleus = models.CharField(
        verbose_name='Soleus Isometric Holds with Lateral  Stepping in a Mini Squat',
        max_length=60, blank=True, null=True)
    rptr_frc_iztnk_Eccentrics = models.CharField(verbose_name='Eccentrics Calf Raise', max_length=60, blank=True,
                                                 null=True)
    rptr_frc_iztnk_Big = models.CharField(verbose_name='Big Toe Rocking in Quadruped ', max_length=60, blank=True,
                                          null=True)
    # FOOT / SMR
    ft_smr_Bottom1 = models.CharField(verbose_name='Bottom of Foot Glide w/Mini Ball', max_length=60, blank=True,
                                      null=True)
    ft_smr_Bottom2 = models.CharField(verbose_name='Bottom of Foot Glide w/Foam Roller', max_length=60, blank=True,
                                      null=True)
    ft_smr_Seated1 = models.CharField(verbose_name='Seated Bottom of Foot Glide w/Miniball-Foam Roller', max_length=60,
                                      blank=True, null=True)
    ft_smr_One1 = models.CharField(verbose_name='One-Straight Leg T.A. SMR w/Foam Roller', max_length=60, blank=True,
                                   null=True)
    ft_smr_Seated2 = models.CharField(verbose_name='Seated T.A. SMR w/Mini Ball', max_length=60, blank=True, null=True)
    ft_smr_Alternating = models.CharField(verbose_name='Alternating T.A  SMR w/Foam Roller', max_length=60, blank=True,
                                          null=True)
    ft_smr_Cross1 = models.CharField(verbose_name='Cross Leg T.A. SMR w/Foam Roller', max_length=60, blank=True,
                                     null=True)
    ft_smr_One = models.CharField(verbose_name='One-Leg Calf SMR w/Foam Roller', max_length=60, blank=True, null=True)
    ft_smr_Cross2 = models.CharField(verbose_name='Cross Leg Calf SMR w/Foam Roller', max_length=60, blank=True,
                                     null=True)
    ft_smr_Two = models.CharField(verbose_name='Two Leg On Foam Roller Calf SMR', max_length=60, blank=True, null=True)
    ft_smr_Calf = models.CharField(verbose_name='Calf SMR W/Mini Ball', max_length=60, blank=True, null=True)
    # FOOT / STRETCHING
    ft_str_Bear = models.CharField(verbose_name='Bear Position Big Toe Stretch', max_length=60, blank=True, null=True)
    ft_str_Foot = models.CharField(verbose_name='Foot on Wall Calf Stretch', max_length=60, blank=True, null=True)
    ft_str_Quadruped = models.CharField(verbose_name='Quadruped Rock Back - Big Toe Ext. Bias', max_length=60,
                                        blank=True, null=True)
    ft_str_Seated1 = models.CharField(verbose_name='Seated Toe Extensor Stretch', max_length=60, blank=True, null=True)
    ft_str_Seated2 = models.CharField(verbose_name='Seated Toe Extensor and  Foot Everter Stretch', max_length=60,
                                      blank=True, null=True)
    ft_str_Seated3 = models.CharField(verbose_name='Seated Toe Extensor and  Foot Inverter Stretch', max_length=60,
                                      blank=True, null=True)
    ft_str_Seated4 = models.CharField(verbose_name='Seated Toe Flexor Stretch', max_length=60, blank=True, null=True)
    ft_str_Seated5 = models.CharField(verbose_name='Seated Toe Flexor and  Foot Everter Stretch', max_length=60,
                                      blank=True, null=True)
    ft_str_Seated6 = models.CharField(verbose_name='Seated Toe Flexor and  Foot Inverter Stretch', max_length=60,
                                      blank=True, null=True)
    ft_str_Standing = models.CharField(verbose_name='Standing Toe Extensor Stretch', max_length=60, blank=True,
                                       null=True)
    ft_str_Single = models.CharField(verbose_name='Single Plantar Flexor Stretch ', max_length=60, blank=True,
                                     null=True)
    # FOOT / FORCE / IZOMETRIK
    ft_frc_izm_Talocrural = models.CharField(verbose_name='Talocrural Joint Distraction', max_length=60, blank=True,
                                             null=True)
    ft_frc_izm_Isometric1 = models.CharField(verbose_name='Isometric Heel Raise', max_length=60, blank=True, null=True)
    ft_frc_izm_Isometric2 = models.CharField(verbose_name='Isometric Single Leg Heel Raise', max_length=60, blank=True,
                                             null=True)
    # FOOT / FORCE / IZOTONIK
    ft_frc_iztnk_Ankle1 = models.CharField(verbose_name='Ankle ‘’DF’’ Mobility w/RB', max_length=60, blank=True,
                                           null=True)
    ft_frc_iztnk_Standing = models.CharField(verbose_name='Standing Ankle Inversion w/RB', max_length=60, blank=True,
                                             null=True)
    ft_frc_iztnk_Controlled = models.CharField(verbose_name='Controlled Pronation', max_length=60, blank=True,
                                               null=True)
    ft_frc_iztnk_Arch = models.CharField(verbose_name='Arch Control Resisted Calf Raise', max_length=60, blank=True,
                                         null=True)
    ft_frc_iztnk_Single = models.CharField(verbose_name='Single Leg Hinge Arch Strength Focus', max_length=60,
                                           blank=True, null=True)
    ft_frc_iztnk_Big1 = models.CharField(verbose_name='Big Toe Mobilization', max_length=60, blank=True, null=True)
    ft_frc_iztnk_Calf = models.CharField(verbose_name='Calf Raise Squeezing Tennis Ball', max_length=60, blank=True,
                                         null=True)
    ft_frc_iztnk_Toes = models.CharField(verbose_name='Toes Elevated Heel Raise', max_length=60, blank=True, null=True)
    ft_frc_iztnk_Bent = models.CharField(verbose_name='Bent Knee Single Leg Calf Raise', max_length=60, blank=True,
                                         null=True)
    ft_frc_iztnk_Half = models.CharField(verbose_name='Half Kneeling Dorsi Flexion', max_length=60, blank=True,
                                         null=True)
    ft_frc_iztnk_Ankle2 = models.CharField(verbose_name='Ankle CARs', max_length=60, blank=True, null=True)
    ft_frc_iztnk_Active = models.CharField(verbose_name='Active Kneeling Plantar/Dorsi Flexion Stretching',
                                           max_length=60, blank=True, null=True)
    ft_frc_iztnk_Ankle3 = models.CharField(verbose_name='Ankle Mobilization Stand up from Kneeling', max_length=60,
                                           blank=True, null=True)
    ft_frc_iztnk_Big2 = models.CharField(verbose_name='Big Toe Side Step', max_length=60, blank=True, null=True)
    ft_frc_iztnk_Toe = models.CharField(verbose_name='Toe Mobilization', max_length=60, blank=True, null=True)
    ft_frc_iztnk_Resisted = models.CharField(verbose_name='Resisted Big Toe, Ankle Eversion/Inversion', max_length=60,
                                             blank=True, null=True)
    #  FOOTPAIN / SMR
    ftpn_smr_Bottom1 = models.CharField(verbose_name='Bottom of Foot Glide w/Mini Ball', max_length=60, blank=True,
                                        null=True)
    ftpn_smr_Bottom2 = models.CharField(verbose_name='Bottom of Foot Glide w/Foam Roller', max_length=60, blank=True,
                                        null=True)
    ftpn_smr_Seated1 = models.CharField(verbose_name='Seated Bottom of Foot Glide w/Miniball-Foam Roller',
                                        max_length=60, blank=True, null=True)
    ftpn_smr_One1 = models.CharField(verbose_name='One-Straight Leg T.A. SMR w/Foam Roller', max_length=60, blank=True,
                                     null=True)
    ftpn_smr_Seated2 = models.CharField(verbose_name='Seated T.A. SMR w/Mini Ball', max_length=60, blank=True,
                                        null=True)
    ftpn_smr_Alternating = models.CharField(verbose_name='Alternating T.A SMR w/Foam Roller', max_length=60, blank=True,
                                            null=True)
    ftpn_smr_Cross1 = models.CharField(verbose_name='Cross Leg T.A. SMR w/Foam Roller', max_length=60, blank=True,
                                       null=True)
    ftpn_smr_One2 = models.CharField(verbose_name='One-Leg Calf SMR w/Foam Roller', max_length=60, blank=True,
                                     null=True)
    ftpn_smr_Cross2 = models.CharField(verbose_name='Cross Leg Calf SMR  w/Foam Roller', max_length=60, blank=True,
                                       null=True)
    ftpn_smr_Two = models.CharField(verbose_name='Two Leg On Foam Roller Calf SMR', max_length=60, blank=True,
                                    null=True)
    ftpn_smr_Calf = models.CharField(verbose_name='Calf SMR W/Mini Ball', max_length=60, blank=True, null=True)
    ftpn_str_Bear = models.CharField(verbose_name='Bear Position Big Toe Stretch', max_length=60, blank=True, null=True)
    ftpn_str_Foot = models.CharField(verbose_name='Foot on Wall Calf Stretch', max_length=60, blank=True, null=True)
    ftpn_str_Quadruped = models.CharField(verbose_name='Quadruped Rock Back - Big Toe Ext. Bias', max_length=60,
                                          blank=True, null=True)
    ftpn_str_Seated1 = models.CharField(verbose_name='Seated Toe Extensor Stretch', max_length=60, blank=True,
                                        null=True)
    ftpn_str_Seated2 = models.CharField(verbose_name='Seated Toe Extensor and  Foot Everter Stretch', max_length=60,
                                        blank=True, null=True)
    ftpn_str_Seated3 = models.CharField(verbose_name='Seated Toe Extensor and  Foot Inverter Stretch', max_length=60,
                                        blank=True, null=True)
    ftpn_str_Seated4 = models.CharField(verbose_name='Seated Toe Flexor Stretch', max_length=60, blank=True, null=True)
    ftpn_str_Seated5 = models.CharField(verbose_name='Seated Toe Flexor and Foot Everter Stretch', max_length=60,
                                        blank=True, null=True)
    ftpn_str_Seated6 = models.CharField(verbose_name='Seated Toe Flexor and Foot Inverter Stretch', max_length=60,
                                        blank=True, null=True)
    ftpn_str_Standing = models.CharField(verbose_name='Standing Toe Extensor Stretch', max_length=60, blank=True,
                                         null=True)
    ftpn_str_Single = models.CharField(verbose_name='Single Plantar Flexor Stretch', max_length=60, blank=True,
                                       null=True)
    ftn_fcr_izm_Tandem = models.CharField(verbose_name='Tandem Stance Balance (Eyes Open/Close)', max_length=60,
                                          blank=True, null=True)
    ftn_fcr_izm_Half = models.CharField(verbose_name='Half Kneeling Isometric Plantar Flexion', max_length=60,
                                        blank=True, null=True)
    ftn_fcr_izm_Isometric1 = models.CharField(verbose_name='Isometric Heel Raise', max_length=60, blank=True, null=True)
    ftn_fcr_izm_Isometric2 = models.CharField(verbose_name='Isometric Single Leg Heel Raise', max_length=60, blank=True,
                                              null=True)
    ftn_fcr_iztnk_Heel = models.CharField(verbose_name='Heel Raise', max_length=60, blank=True, null=True)
    ftn_fcr_iztnk_Standing1 = models.CharField(verbose_name='Standing Arch-Raise', max_length=60, blank=True, null=True)
    ftn_fcr_iztnk_Single1 = models.CharField(verbose_name='Single Leg Arch Raise', max_length=60, blank=True, null=True)
    ftn_fcr_iztnk_Single2 = models.CharField(verbose_name='Single Leg Stance 3  point Taps', max_length=60, blank=True,
                                             null=True)
    ftn_fcr_iztnk_Standing2 = models.CharField(verbose_name='Standing Toe Spreads', max_length=60, blank=True,
                                               null=True)
    ftn_fcr_iztnk_Controlled = models.CharField(verbose_name='Controlled Pronation w/Band', max_length=60, blank=True,
                                                null=True)
    ftn_fcr_iztnk_Towel = models.CharField(verbose_name='Towel Scrunches', max_length=60, blank=True, null=True)
    ftn_fcr_iztnk_Calf = models.CharField(verbose_name='Calf Raise Squeeze Tennis Ball', max_length=60, blank=True,
                                          null=True)
    ftn_fcr_iztnk_Tandem = models.CharField(verbose_name='Tandem Walking', max_length=60, blank=True, null=True)
    ftn_fcr_iztnk_Half = models.CharField(verbose_name='Half Kneeling Ankle Dorsiflexion Mobilization', max_length=60,
                                          blank=True, null=True)
    ftn_fcr_iztnk_Big = models.CharField(verbose_name='Big Toe Extension Mobilization', max_length=60, blank=True,
                                         null=True)
    ftn_fcr_iztnk_Active1 = models.CharField(verbose_name='Active Plantar Fascia Stretching Variation 1', max_length=60,
                                             blank=True, null=True)
    ftn_fcr_iztnk_Active2 = models.CharField(verbose_name='Active Plantar Fascia Stretching Variation 2', max_length=60,
                                             blank=True, null=True)
    ftn_fcr_iztnk_Single3 = models.CharField(verbose_name='Single Foot Resisted Big  Toe Flexion', max_length=60,
                                             blank=True, null=True)
    ftn_fcr_iztnk_Resisted1 = models.CharField(verbose_name='Resisted Big Toe,Switch Flexion', max_length=60,
                                               blank=True, null=True)
    ftn_fcr_iztnk_Resisted2 = models.CharField(verbose_name='Resisted Big Toe and Akle Plantar Flexion', max_length=60,
                                               blank=True, null=True)

    class Meta:
        verbose_name = "Medikal Egzersiz"
        verbose_name_plural = "Medikal Egzersiz "


class medical_exercise1(models.Model):
    trainer = models.ForeignKey(to=Trainer, verbose_name="Antrenör", on_delete=models.CASCADE, blank=True, null=True)
    personal = models.ForeignKey(to=Personal, verbose_name="Danışan", on_delete=models.CASCADE, blank=True, null=True)
    medical2 = models.ForeignKey(to=medical_exercise2, verbose_name="Medical Egzersiz 2", on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    medical3 = models.ForeignKey(to=medical_exercise3, verbose_name="Medical Egzersiz 3", on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    medical4 = models.ForeignKey(to=medical_exercise4, verbose_name="Medical Egzersiz 4", on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    medical5 = models.ForeignKey(to=medical_exercise5, verbose_name="Medical Egzersiz 5", on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    medical6 = models.ForeignKey(to=medical_exercise6, verbose_name="Medical Egzersiz 6", on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    medical7 = models.ForeignKey(to=medical_exercise7, verbose_name="Medical Egzersiz 7", on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    medical8 = models.ForeignKey(to=medical_exercise8, verbose_name="Medical Egzersiz 8", on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    medical9 = models.ForeignKey(to=medical_exercise9, verbose_name="Medical Egzersiz 9", on_delete=models.CASCADE,
                                 blank=True,
                                 null=True)
    medical10 = models.ForeignKey(to=medical_exercise10, verbose_name="Medical Egzersiz 10", on_delete=models.CASCADE,
                                  blank=True,
                                  null=True)
    medical11 = models.ForeignKey(to=medical_exercise11, verbose_name="Medical Egzersiz 11", on_delete=models.CASCADE,
                                  blank=True,
                                  null=True)
    medical12 = models.ForeignKey(to=medical_exercise12, verbose_name="Medical Egzersiz 12", on_delete=models.CASCADE,
                                  blank=True,
                                  null=True)
    medical13 = models.ForeignKey(to=medical_exercise13, verbose_name="Medical Egzersiz 13", on_delete=models.CASCADE,
                                  blank=True,
                                  null=True)
    date = models.DateField(("Date"), default=datetime.now(), blank=True)
    # POSTREHAP/ SMR
    pstr_smr_Extensor = models.CharField(verbose_name='Neck Extensor Release Variation', max_length=60, blank=True,
                                         null=True)
    pstr_smr_Rotator = models.CharField(verbose_name='Neck Rotator Release Variation', max_length=60, blank=True,
                                        null=True)
    pstr_smr_Half = models.CharField(verbose_name='Half Standing Shoulder Release', max_length=60, blank=True,
                                     null=True)
    pstr_smr_Standing = models.CharField(verbose_name='Standing Thoracic Release', max_length=60, blank=True, null=True)
    pstr_smr_Suboccipital = models.CharField(verbose_name='Suboccipital Release', max_length=60, blank=True, null=True)
    pstr_smr_Thoracic1 = models.CharField(verbose_name='Thoracic Extension Release', max_length=60, blank=True,
                                          null=True)
    pstr_smr_Thoracic2 = models.CharField(verbose_name='Thoracic Lateral Extension Release', max_length=60, blank=True,
                                          null=True)
    pstr_smr_Thoracic3 = models.CharField(verbose_name='Thoracic Mobility Kneeling Roll Release', max_length=60,
                                          blank=True, null=True)
    pstr_smr_Thoracic4 = models.CharField(verbose_name='Thoracic Mobility Rolling Release', max_length=60, blank=True,
                                          null=True)
    pstr_smr_Thoracic5 = models.CharField(verbose_name='Thoracic Mobility Standing Roll Release', max_length=60,
                                          blank=True, null=True)
    pstr_smr_Thoracic6 = models.CharField(verbose_name='Thoracic Mobility Release Variation 1', max_length=60,
                                          blank=True, null=True)
    pstr_smr_Thoracic7 = models.CharField(verbose_name='Thoracic Mobility Release Variation 2', max_length=60,
                                          blank=True, null=True)
    pstr_smr_Thoracic8 = models.CharField(verbose_name='Thoracic Mobility Release Variation 3', max_length=60,
                                          blank=True, null=True)
    pstr_smr_Thoracic9 = models.CharField(verbose_name='Thoracic Rotation Release', max_length=60, blank=True,
                                          null=True)
    pstr_smr_Posterior = models.CharField(verbose_name='Posterior Dynamic Release', max_length=60, blank=True,
                                          null=True)
    pstr_smr_Weighted = models.CharField(verbose_name='Weighted Thoracic Extension Release', max_length=60, blank=True,
                                         null=True)
    # POSTREHAP/ STRETCHING
    pstr_str_Cervical1 = models.CharField(verbose_name='Cervical Extensors Stretch', max_length=60, blank=True,
                                          null=True)
    pstr_str_Cervical2 = models.CharField(verbose_name='Cervical Flexor Stretch', max_length=60, blank=True, null=True)
    pstr_str_Cervical3 = models.CharField(verbose_name='Cervical Lateral Flexor Stretch', max_length=60, blank=True,
                                          null=True)
    pstr_str_Cervical4 = models.CharField(verbose_name='Cervical Rotator (Extensor) Stretch', max_length=60, blank=True,
                                          null=True)
    pstr_str_Cervical5 = models.CharField(verbose_name='Cervical Rotator (Flexor) Stretch', max_length=60, blank=True,
                                          null=True)
    pstr_str_Levator = models.CharField(verbose_name='Levator Scapula Stretch', max_length=60, blank=True, null=True)
    pstr_str_Anchor = models.CharField(verbose_name='Anchor Stretch (Scalene)', max_length=60, blank=True, null=True)
    pstr_str_Skalen = models.CharField(verbose_name='Skalen Stretch', max_length=60, blank=True, null=True)
    pstr_str_Chest = models.CharField(verbose_name='Chest Stretch', max_length=60, blank=True, null=True)
    pstr_str_Medial = models.CharField(verbose_name='Medial-Ulnar Stretch', max_length=60, blank=True, null=True)
    pstr_str_SCM = models.CharField(verbose_name='SCM Stretch', max_length=60, blank=True, null=True)
    pstr_str_Upper1 = models.CharField(verbose_name='Upper Trapezius Stretch', max_length=60, blank=True, null=True)
    pstr_str_Upper2 = models.CharField(verbose_name='Upper Trapezius Stretch w/Cervical Rotation', max_length=60,
                                       blank=True, null=True)
    pstr_str_Dynamic = models.CharField(verbose_name='Dynamic Thoracic Extension Stretch', max_length=60, blank=True,
                                        null=True)
    # POSTREHAP/ FORCE / IZOMETRIK
    pstr_frc_izm_Cervical1 = models.CharField(verbose_name='Cervical Extension Isometric', max_length=60, blank=True,
                                              null=True)
    pstr_frc_izm_Cervical2 = models.CharField(verbose_name='Cervical Isometric Flexion', max_length=60, blank=True,
                                              null=True)
    pstr_frc_izm_Prone = models.CharField(verbose_name='Prone Chin Tuck Isometric', max_length=60, blank=True,
                                          null=True)
    pstr_frc_izm_Cervical3 = models.CharField(verbose_name='Cervical Lateral Flexion Isometric', max_length=60,
                                              blank=True, null=True)
    pstr_frc_izm_Cervical4 = models.CharField(verbose_name='Cervical Rotation Isometric', max_length=60, blank=True,
                                              null=True)
    pstr_frc_izm_Seated = models.CharField(verbose_name='Seated Chin Tuck Isometric', max_length=60, blank=True,
                                           null=True)
    pstr_frc_izm_Neck1 = models.CharField(verbose_name='Neck Flexion Isometric Endurance', max_length=60, blank=True,
                                          null=True)
    pstr_frc_izm_Neck2 = models.CharField(verbose_name='Neck Flexor Isometrics', max_length=60, blank=True, null=True)
    pstr_frc_izm_Standing1 = models.CharField(verbose_name='Standing Lateral Flexion Isometric', max_length=60,
                                              blank=True, null=True)
    pstr_frc_izm_Standing2 = models.CharField(verbose_name='Standing Stability Ball Isometric', max_length=60,
                                              blank=True, null=True)
    # POSTREHAP/ FORCE / IZOTONIK
    pstr_frc_iztnk_Arm1 = models.CharField(verbose_name='Arm H Raise w/Banded', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Arm2 = models.CharField(verbose_name='Arm Raise w/Banded', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Arm3 = models.CharField(verbose_name='Arm Y Raise', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Arm4 = models.CharField(verbose_name='Arm Y to T Raise', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Arm5 = models.CharField(verbose_name='Arm Y to W Raise', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Bilateral = models.CharField(verbose_name='Bilateral Extension Rotation w/Banded in Plank Positio',
                                                max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Cervical1 = models.CharField(verbose_name='Cervical Extension', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Cervical2 = models.CharField(verbose_name='Cervical Extension w/Banded', max_length=60, blank=True,
                                                null=True)
    pstr_frc_iztnk_Straight1 = models.CharField(verbose_name='Straight Arm Cervical Extension w/Banded', max_length=60,
                                                blank=True, null=True)
    pstr_frc_iztnk_Cervical3 = models.CharField(verbose_name='Cervical Flexion', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Cervical4 = models.CharField(verbose_name='Cervical Flexion w/Banded', max_length=60, blank=True,
                                                null=True)
    pstr_frc_iztnk_Straight2 = models.CharField(verbose_name='Straight Arm Cervical Lateral Flexion w/Banded',
                                                max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Cervical5 = models.CharField(verbose_name='Cervical Lateral Flexion', max_length=60, blank=True,
                                                null=True)
    pstr_frc_iztnk_Cervical6 = models.CharField(verbose_name='Cervical Lateral Flexion w/Banded', max_length=60,
                                                blank=True, null=True)
    pstr_frc_iztnk_Cervical7 = models.CharField(verbose_name='Cervical Rotation', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Cervical8 = models.CharField(verbose_name='Cervical Rotation w/Banded', max_length=60, blank=True,
                                                null=True)
    pstr_frc_iztnk_Wall1 = models.CharField(verbose_name='Wall Cervical Rotation w/Softball', max_length=60, blank=True,
                                            null=True)
    pstr_frc_iztnk_Chin1 = models.CharField(verbose_name='Chin Nods', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Prone1 = models.CharField(verbose_name='Prone Chin Tuck', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Prone2 = models.CharField(verbose_name='Prone Chin Tuck w/Banded', max_length=60, blank=True,
                                             null=True)
    pstr_frc_iztnk_Prone3 = models.CharField(verbose_name='Prone Y – W Raise', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Quadruped1 = models.CharField(verbose_name='Quadruped Chin Tuck', max_length=60, blank=True,
                                                 null=True)
    pstr_frc_iztnk_Quadruped2 = models.CharField(verbose_name='Quadruped Chin Tuck w/Banded', max_length=60, blank=True,
                                                 null=True)
    pstr_frc_iztnk_Quadruped3 = models.CharField(verbose_name='Quadruped Chin Tuck w/Cervical Rotation', max_length=60,
                                                 blank=True, null=True)
    pstr_frc_iztnk_Seated = models.CharField(verbose_name='Seated Chin Tuck w/Banded', max_length=60, blank=True,
                                             null=True)
    pstr_frc_iztnk_Wall2 = models.CharField(verbose_name='Wall Chin Tuck', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Supine = models.CharField(verbose_name='Supine Chin Tuck w/Hold', max_length=60, blank=True,
                                             null=True)
    pstr_frc_iztnk_Middle = models.CharField(verbose_name='Middle Back Mobility', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Shoulder = models.CharField(verbose_name='Shoulder Abduction w/Banded', max_length=60, blank=True,
                                               null=True)
    pstr_frc_iztnk_Side1 = models.CharField(verbose_name='Side Lying External Rotation', max_length=60, blank=True,
                                            null=True)
    pstr_frc_iztnk_Side2 = models.CharField(verbose_name='Side Lying Thoracic Rotation', max_length=60, blank=True,
                                            null=True)
    pstr_frc_iztnk_Thoracic1 = models.CharField(verbose_name='Thoracic Mobility Resisted Middle  Back Mobility',
                                                max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Thoracic2 = models.CharField(verbose_name='Thoracic Mobility Rolling w/Banded', max_length=60,
                                                blank=True, null=True)
    pstr_frc_iztnk_Thoracic3 = models.CharField(verbose_name='Thoracic Mobility Wall Twist w/Banded', max_length=60,
                                                blank=True, null=True)
    pstr_frc_iztnk_Thoracic4 = models.CharField(verbose_name='Thoracic Mobility Wall Twist', max_length=60, blank=True,
                                                null=True)
    pstr_frc_iztnk_Banded = models.CharField(verbose_name='Banded Row', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Cervical9 = models.CharField(verbose_name='Cervical Extension on/Stability Ball', max_length=60,
                                                blank=True, null=True)
    pstr_frc_iztnk_Cervical10 = models.CharField(verbose_name='Cervical Flexion/Extension', max_length=60, blank=True,
                                                 null=True)
    pstr_frc_iztnk_Chin2 = models.CharField(verbose_name='Chin Tuck + Horizontal Abduction', max_length=60, blank=True,
                                            null=True)
    pstr_frc_iztnk_Chin3 = models.CharField(verbose_name='Chin Tuck + Prone W', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Chin4 = models.CharField(verbose_name='Chin Tuck on Towel', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Diaghram1 = models.CharField(verbose_name='Diaghram Breathing w/Kettlebell-1', max_length=60,
                                                blank=True, null=True)
    pstr_frc_iztnk_Diaghram2 = models.CharField(verbose_name='Diaghram Breathing w/Kettlebell-2', max_length=60,
                                                blank=True, null=True)
    pstr_frc_iztnk_Diaghram3 = models.CharField(verbose_name='Diaghram Breathing-1', max_length=60, blank=True,
                                                null=True)
    pstr_frc_iztnk_Diaghram4 = models.CharField(verbose_name='Diaghram Breathing-2', max_length=60, blank=True,
                                                null=True)
    pstr_frc_iztnk_Dynamic = models.CharField(verbose_name='Dynamic Retraction', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Elevated = models.CharField(verbose_name='Elevated Neck Bridge', max_length=60, blank=True,
                                               null=True)
    pstr_frc_iztnk_Inverted = models.CharField(verbose_name='Inverted Row', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Low = models.CharField(verbose_name='Low Trap Lift w/Chin Tuck', max_length=60, blank=True,
                                          null=True)
    pstr_frc_iztnk_Lower = models.CharField(verbose_name=' Lower Trap Strength + Thoracic Extension', max_length=60,
                                            blank=True, null=True)
    pstr_frc_iztnk_Lunge = models.CharField(verbose_name='Lunge Reverse Woodchops', max_length=60, blank=True,
                                            null=True)
    pstr_frc_iztnk_Modified = models.CharField(verbose_name='Modified Prone Swimmers', max_length=60, blank=True,
                                               null=True)
    pstr_frc_iztnk_Neck1 = models.CharField(verbose_name='Neck Retraction Strength', max_length=60, blank=True,
                                            null=True)
    pstr_frc_iztnk_Neck2 = models.CharField(verbose_name='Neck Rotation w/Retraction', max_length=60, blank=True,
                                            null=True)
    pstr_frc_iztnk_Prone4 = models.CharField(verbose_name='Prone Divers', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Prone5 = models.CharField(verbose_name='Prone Retraction w/Arm 90/90', max_length=60, blank=True,
                                             null=True)
    pstr_frc_iztnk_Prone6 = models.CharField(verbose_name='Prone Scapular + Cervical Retraction', max_length=60,
                                             blank=True, null=True)
    pstr_frc_iztnk_Shoulder1 = models.CharField(verbose_name='Shoulder Mobility-1', max_length=60, blank=True,
                                                null=True)
    pstr_frc_iztnk_Shoulder2 = models.CharField(verbose_name='Shoulder Mobility-2', max_length=60, blank=True,
                                                null=True)
    pstr_frc_iztnk_Side3 = models.CharField(verbose_name='Side Lying Lateral Flexor Curl', max_length=60, blank=True,
                                            null=True)
    pstr_frc_iztnk_Side4 = models.CharField(verbose_name='Side Lying Rotations', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Standing1 = models.CharField(verbose_name='Standing Row', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Standing2 = models.CharField(verbose_name='Standing T', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Standing3 = models.CharField(verbose_name='Standing Y', max_length=60, blank=True, null=True)
    pstr_frc_iztnk_Wall3 = models.CharField(verbose_name='Wall Angels w/Chin Tuck', max_length=60, blank=True,
                                            null=True)
    # STIFFNESS / SMR
    stff_smr_Neck1 = models.CharField(verbose_name='Neck Extensor Release Variation', max_length=60, blank=True,
                                      null=True)
    stff_smr_Neck2 = models.CharField(verbose_name='Neck Rotator Release Variation', max_length=60, blank=True,
                                      null=True)
    stff_smr_Half = models.CharField(verbose_name='Half Standing Shoulder Release', max_length=60, blank=True,
                                     null=True)
    stff_smr_Standing = models.CharField(verbose_name='Standing Thoracic Release', max_length=60, blank=True, null=True)
    stff_smr_Suboccipital = models.CharField(verbose_name='Suboccipital Release', max_length=60, blank=True, null=True)
    stff_smr_Thoracic1 = models.CharField(verbose_name='Thoracic Extension Release', max_length=60, blank=True,
                                          null=True)
    stff_smr_Thoracic2 = models.CharField(verbose_name='Thoracic Lateral Extension Release', max_length=60, blank=True,
                                          null=True)
    stff_smr_Thoracic3 = models.CharField(verbose_name='Thoracic Mobility Kneeling Roll Release', max_length=60,
                                          blank=True, null=True)
    stff_smr_Thoracic4 = models.CharField(verbose_name='Thoracic Mobility Rolling Release', max_length=60, blank=True,
                                          null=True)
    stff_smr_Thoracic5 = models.CharField(verbose_name='Thoracic Mobility Standing Roll Release', max_length=60,
                                          blank=True, null=True)
    stff_smr_Thoracic6 = models.CharField(verbose_name='Thoracic Mobility Release Variation', max_length=60, blank=True,
                                          null=True)
    stff_smr_Thoracic7 = models.CharField(verbose_name='Thoracic Mobility Release Variation', max_length=60, blank=True,
                                          null=True)
    stff_smr_Thoracic8 = models.CharField(verbose_name='Thoracic Mobility Release Variation', max_length=60, blank=True,
                                          null=True)
    stff_smr_Thoracic9 = models.CharField(verbose_name='Thoracic Rotation Release', max_length=60, blank=True,
                                          null=True)
    stff_smr_Posterior = models.CharField(verbose_name='Posterior Dynamic Release', max_length=60, blank=True,
                                          null=True)
    stff_smr_Weighted = models.CharField(verbose_name='Weighted Thoracic Extension Release', max_length=60, blank=True,
                                         null=True)
    # STIFFNESS / STRETCHING
    stff_str_Cervical1 = models.CharField(verbose_name='Cervical Extensors Stretch', max_length=60, blank=True,
                                          null=True)
    stff_str_Cervical2 = models.CharField(verbose_name='Cervical Flexor Stretch', max_length=60, blank=True, null=True)
    stff_str_Cervical3 = models.CharField(verbose_name='Cervical Lateral Flexor Stretch', max_length=60, blank=True,
                                          null=True)
    stff_str_Cervical4 = models.CharField(verbose_name='Cervical Rotator (Extensor) Stretch', max_length=60, blank=True,
                                          null=True)
    stff_str_Cervical5 = models.CharField(verbose_name='Cervical Rotator (Flexor) Stretch', max_length=60, blank=True,
                                          null=True)
    stff_str_Levator = models.CharField(verbose_name='Levator Scapula Stretch', max_length=60, blank=True, null=True)
    stff_str_Anchor = models.CharField(verbose_name='Anchor Stretch (Scalene)', max_length=60, blank=True, null=True)
    stff_str_Skalen = models.CharField(verbose_name='Skalen Stretch', max_length=60, blank=True, null=True)
    stff_str_Chest = models.CharField(verbose_name='Chest Stretch', max_length=60, blank=True, null=True)
    stff_str_Medial = models.CharField(verbose_name='Medial-Ulnar Stretch', max_length=60, blank=True, null=True)
    stff_str_SCM = models.CharField(verbose_name='SCM Stretch', max_length=60, blank=True, null=True)
    stff_str_Upper1 = models.CharField(verbose_name='Upper Trapezius Stretch', max_length=60, blank=True, null=True)
    stff_str_Upper2 = models.CharField(verbose_name='Upper Trapezius Stretch w/Cervical Rotation', max_length=60,
                                       blank=True, null=True)
    stff_str_Dynamic = models.CharField(verbose_name='Dynamic Thoracic Extension Stretch', max_length=60, blank=True,
                                        null=True)
    # STIFFNESS / FORCE / IZOMETRIK
    stff_frc_izm_Cervical1 = models.CharField(verbose_name='Cervical Extension Isometric', max_length=60, blank=True,
                                              null=True)
    stff_frc_izm_Cervical2 = models.CharField(verbose_name='Cervical Isometric Flexion', max_length=60, blank=True,
                                              null=True)
    stff_frc_izm_Prone = models.CharField(verbose_name='Prone Chin Tuck Isometric', max_length=60, blank=True,
                                          null=True)
    stff_frc_izm_Cervical3 = models.CharField(verbose_name='Cervical Lateral Flexion Isometric', max_length=60,
                                              blank=True, null=True)
    stff_frc_izm_Cervical4 = models.CharField(verbose_name='Cervical Rotation Isometric', max_length=60, blank=True,
                                              null=True)
    stff_frc_izm_Seated = models.CharField(verbose_name='Seated Chin Tuck Isometric', max_length=60, blank=True,
                                           null=True)
    stff_frc_izm_Neck1 = models.CharField(verbose_name='Neck Flexion Isometric Endurance', max_length=60, blank=True,
                                          null=True)
    stff_frc_izm_Neck2 = models.CharField(verbose_name='Neck Flexor Isometrics', max_length=60, blank=True, null=True)
    stff_frc_izm_Standing1 = models.CharField(verbose_name='Standing Lateral Flexion Isometric', max_length=60,
                                              blank=True, null=True)
    stff_frc_izm_Standing2 = models.CharField(verbose_name='Standing Stability Ball Isometric', max_length=60,
                                              blank=True, null=True)
    # STIFFNESS / FORCE / IZOTONIK
    stff_frc_iztnk_Cervical1 = models.CharField(verbose_name='Cervical Flexion/Extension', max_length=60, blank=True,
                                                null=True)
    stff_frc_iztnk_Cervical2 = models.CharField(verbose_name='Cervical Rotation', max_length=60, blank=True, null=True)
    stff_frc_iztnk_Seated1 = models.CharField(verbose_name='Seated Chin Tuck Rotation', max_length=60, blank=True,
                                              null=True)
    stff_frc_iztnk_Quadruped = models.CharField(verbose_name='Quadruped Chin Tuck and Rotation', max_length=60,
                                                blank=True, null=True)
    stff_frc_iztnk_Seated2 = models.CharField(verbose_name='Seated Back at Ball  and Wall Shoulder Flexion w/Dowel',
                                              max_length=60, blank=True, null=True)
    stff_frc_iztnk_Kneeling = models.CharField(verbose_name='Kneeling Rockback Elbow on Wall', max_length=60,
                                               blank=True, null=True)
    stff_frc_iztnk_Sidelying = models.CharField(verbose_name='Sidelying Sweeps with Neck Rotation', max_length=60,
                                                blank=True, null=True)
    stff_frc_iztnk_3 = models.CharField(verbose_name='Seated Cervical-Thoracic Lateral Flexion with Rotation Away',
                                        max_length=60, blank=True, null=True)
    stff_frc_iztnk_SCM1 = models.CharField(verbose_name='SCM Pincer Grip', max_length=60, blank=True, null=True)
    stff_frc_iztnk_SCM2 = models.CharField(verbose_name='SCM Broad Contact', max_length=60, blank=True, null=True)
    stff_frc_iztnk_Scalene = models.CharField(verbose_name='Scalene, anterior, medial, posterior Stretch (Mobil)',
                                              max_length=60, blank=True, null=True)
    stff_frc_iztnk_Upper = models.CharField(verbose_name='Upper Spiral Line', max_length=60, blank=True, null=True)
    stff_frc_iztnk_Dynamic = models.CharField(verbose_name='Dynamic Pectoral Stretch w', max_length=60, blank=True,
                                              null=True)
    stff_frc_iztnk_Lateral = models.CharField(verbose_name='Lateral Raise', max_length=60, blank=True, null=True)
    stff_frc_iztnk_Scapular = models.CharField(verbose_name='Scapular Shrug', max_length=60, blank=True, null=True)
    stff_frc_iztnk_Prone = models.CharField(verbose_name='Prone Swimmer', max_length=60, blank=True, null=True)
    stff_frc_iztnk_Banded = models.CharField(verbose_name='Banded Retraction', max_length=60, blank=True, null=True)
    stff_frc_iztnk_Neck = models.CharField(verbose_name='Neck Flexor Curl', max_length=60, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('fitness-detail', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('fitness-update', kwargs={'id': self.id})

    def get_trainer_medical_exercise1_delete_url(self):
        return reverse('trainer-medical-exercise-delete', kwargs={'id': self.id})

    def get_corporate_medical_exercise1_delete_url(self):
        return reverse('corporate-medical-exercise-delete', kwargs={'id': self.id})

    def get_personal_medical_exercise1_delete_url(self):
        return reverse('personal-medical-exercise-delete', kwargs={'id': self.id})

    class Meta:
        verbose_name = "Medikal Egzersiz"
        verbose_name_plural = "Medikal Egzersiz "
