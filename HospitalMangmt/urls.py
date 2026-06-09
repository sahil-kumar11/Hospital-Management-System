"""
URL configuration for HospitalMangmt project.
"""
from django.contrib import admin
from django.urls import path
from hospital.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('', Index, name='index'),
    path('admin_login/', Login, name='login'),
    path('logout/', Logout_admin, name='logout'),
    path('view_doctor/', View_Doctor, name='view_doctor'),
    path('add_doctor/', Add_Doctor, name='add_doctor'),
    path('delete_doctor/<int:id>/', delete_doctor, name='delete_doctor'),
    path('add_patient/', Add_Patient, name='add_patient'),
    path('view_patient/', View_Patient, name='view_patient'),
    path('delete_patient/<int:id>/', delete_patient, name='delete_patient'),
    path('add_appointment/', Add_Appointment, name='add_appointment'),
    path('view_appointment/', View_Appointment, name='view_appointment'),
    path('delete_appointment/<int:id>/', delete_appointment, name='delete_appointment'),
    path('home/', Home, name='home'),
]