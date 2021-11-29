from datetime import datetime

from django.contrib.postgres.fields import ArrayField
from django.db import models

# Create your models here.
from registration.models import Trainer, Personal


class athDev_mainTitle(models.Model):
    title = models.CharField(verbose_name='Ana Başlık', max_length=200, blank=True, null=True)

    class Meta:
        verbose_name = "Ana Başlıklar"
        verbose_name_plural = 'Ana Başlıklar'


class athleticDev_subTitle(models.Model):
    maintitle = models.ForeignKey(to=athDev_mainTitle, verbose_name='Ana Başlık Seç', on_delete=models.CASCADE,
                                  blank=True, null=True)
    sub_title = models.CharField(verbose_name='Atletik performans alt başlıkları', max_length=200, blank=True,
                                 null=True)

    class Meta:
        verbose_name = "Alt Başlıklar"
        verbose_name_plural = 'Alt Başlıklar'


class athletticDev_inputs(models.Model):
    trainer = models.ForeignKey(to=Trainer, verbose_name="Antrenör Seç", on_delete=models.CASCADE, blank=True,
                                null=True)
    personal = models.ForeignKey(to=Personal, verbose_name="Danışan Seç", on_delete=models.CASCADE, blank=True,
                                 null=True)
    subtitle = models.ForeignKey(to=athleticDev_subTitle, verbose_name='Alt Başlık Seç', on_delete=models.CASCADE,
                                 blank=True, null=True)
    date = models.DateField(("Date"), default=datetime.now(), blank=True, null=True)
    inputs_name = models.CharField(verbose_name='Input adı', max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = "Inputs Alanı"
        verbose_name_plural = 'Inputs Alanı'


class ath_property(models.Model):
    Type_select = [('text', 'Text'), ('checkbox', 'Checkbox'), ('radio', 'Radio')]
    subtitle = models.ForeignKey(to=athleticDev_subTitle, verbose_name='Alt Başlık Seç', on_delete=models.CASCADE,
                                 blank=True, null=True)
    date = models.DateField(("Date"), default=datetime.now(), blank=True, null=True)
    inputs_title = models.CharField(verbose_name='Inputs Başlık', max_length=200, blank=True, null=True)
    inputs_type = models.CharField(verbose_name='Inputun tipi(text,checkbox,radio)', max_length=50, choices=Type_select,
                                   null=True, blank=True)

    class Meta:
        verbose_name = "Inputs Özellikleri"
        verbose_name_plural = 'Inputs Özellikleri'
