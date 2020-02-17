"""meeting_hw3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from alert.views import hello_view
from alert import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('hello/', hello_view, name='hello'),
    path('patients/', views.patients),
    path('patients/admissions/<str:num>', views.admissions, name = 'admission'),
    path('patients/callout/<str:num>', views.callout, name = 'callout'),
    path('patients/cptevents/<str:num>', views.cptevents, name = 'cptevents'),
    path('patients/datetimeevents/<str:num>', views.datetimeevents, name = 'datatimeevents'),
    path('patients/diagnoses_icd/<str:num>', views.diagnoses_icd, name='diagnoses_icd'),
    path('patients/drgcodes/<str:num>', views.drgcodes, name='drgcodes'),
    path('patients/icustays/<str:num>', views.icustays, name='icustays'),
    path('patients/inputevents_cv/<str:num>', views.inputevents_cv, name='inputevents_cv'),
    path('patients/inputevents_mv/<str:num>', views.inputevents_mv, name='inputevents_mv'),
    path('patients/labevents/<str:num>', views.labevents, name='labevents'),
    path('patients/microbiologyevents/<str:num>', views.microbiologyevents, name='microbiologyevents'),
    path('patients/noteevents/<str:num>', views.noteevents, name='noteevents'),
    path('patients/outputevents/<str:num>', views.outputevents, name='outputevents'),
    path('patients/prescriptions/<str:num>', views.prescriptions, name='prescriptions'),
    path('patients/procedureevents_mv/<str:num>', views.procedureevents_mv, name='procedureevents_mv'),
    path('patients/procedures_icd/<str:num>', views.procedures_icd, name='procedures_icd'),
    path('patients/services/<str:num>', views.services, name='services'),
    path('patients/transfers/<str:num>', views.transfers, name='transfers'),
    path('patients/chartevents/<str:num>', views.chartevents, name='chartevents'),
    path('patients/diagnoses_icd/d_icd_diagnoses/<str:num>', views.d_icd_diagnoses, name='d_icd_diagnoses'),
    path('patients/procedures_icd/d_icd_procedures/<str:num>', views.d_icd_procedures, name='d_icd_procedures'),
    path('patients/d_items/<str:num>', views.d_items, name='d_items'),
    path('patients/d_labitems/<str:num>', views.d_labitems, name='d_labitems'),
    path('patients/icustays/find_icustays/<str:num>', views.find_icustays, name='find_icustays'),
    path('patients/admissions/find_hadmid/<str:num>', views.find_hadmid, name='find_hadmid'),
]
