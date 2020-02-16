# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.conf import settings

"""
class Alert(models.Model):
    title = models.CharField(db_column='Title', max_length=255, unique=True)
    stopname_zh = models.CharField(db_column='StopName_Zh_tw', max_length=50, unique=True)
    stopname_en = models.CharField(db_column='StopName_En', max_length=50, unique=True)
    publishtime = models.CharField(db_column='PublishTime', max_length=255, unique=True)
    endtime = models.CharField(db_column='EndTime', max_length=255, unique=True)
    #title = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True, db_column='Title', max_length=255, unique=True)

    class Meta:
        managed = False
        db_table = 'alert'


class SubAlert(models.Model):
    sub_title = models.ForeignKey(Alert, to_field='title', on_delete=models.CASCADE, related_name='Title')
    sub_stopname_zh = models.ForeignKey(Alert, to_field='stopname_zh', on_delete=models.CASCADE, related_name='Stopname_Zh_tw')
    sub_stopname_en = models.ForeignKey(Alert, to_field='stopname_en', on_delete=models.CASCADE, related_name='Stopname_EN')
    sub_publishtime = models.ForeignKey(Alert, to_field='publishtime', on_delete=models.CASCADE, related_name='PublishTime')
    sub_endtime = models.ForeignKey(Alert, to_field='endtime', on_delete=models.CASCADE, related_name='EndTime')

#    alert = models.ForeignKey(Alert, related_name='articles', on_delete=models.CASCADE)



    class Meta:
        managed = False
        db_table = 'sub_alert'
"""


class Teacher(models.Model):
    id = models.IntegerField(db_column='id', unique=True,primary_key = True)
    name = models.CharField(db_column='name', max_length=50)

    class Meta:
        managed = False
        db_table = 'teacher'


class Student(models.Model):
    id = models.IntegerField(db_column='id', unique=True, primary_key=True)
    name = models.CharField(db_column='name', max_length=50)
    teacher = models.ForeignKey('Teacher',on_delete=models.CASCADE, related_name='teacher')

    class Meta:
        managed = False
        db_table = 'student'
