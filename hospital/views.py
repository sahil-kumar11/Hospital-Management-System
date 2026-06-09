from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import*
from django.contrib.auth import authenticate, login, logout
from .models import Doctor

# Create your views here.

def About(request):
    return render(request, 'about.html')

def Contact(request):
    return render(request, 'contact.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    # Change this - redirect to home instead of about
    return redirect('home')

def Login(request):
    error = ""
    
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        
        user = authenticate(username=u, password=p)
        
        if user is not None:
            if user.is_staff:
                login(request, user)
                error = "no"
                # Redirect to home after successful login
                return render(request, 'login.html', {'error': error})
            else:
                error = "yes"
        else:
            error = "yes"
    
    d = {'error': error}
    return render(request, 'login.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    
    logout(request)
    return redirect('login')

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    
    doc = Doctor.objects.all()
    d = {'doc':doc}
    return render(request,'view_doctor.html',d)

def Add_Doctor(request):
    
    if not request.user.is_staff:
        return redirect('login')
    
    if request.method == "POST":
        
        n = request.POST['name']
        m = request.POST['mobile']
        s = request.POST['special']
        
        Doctor.objects.create(
            name=n,
            mobile=m,
            special=s
        )
        
        return redirect('view_doctor')
    
    return render(request, 'add_doctor.html')

def delete_doctor(request, id):
    if not request.user.is_staff:
        return redirect('login')
    
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    
    return redirect('view_doctor')

def Add_Patient(request):
    
    if not request.user.is_staff:
        return redirect('login')
    
    if request.method == "POST":
        
        n = request.POST['name']
        m = request.POST['mobile']
        g = request.POST['gender']
        a = request.POST['address']
        
        Patient.objects.create(
            name=n,
            mobile=m,
            gender=g,
            address=a
        )
        
        return redirect('view_patient')
    
    return render(request, 'add_patient.html')

def View_Patient(request):
    
    if not request.user.is_staff:
        return redirect('login')
    
    patient = Patient.objects.all()
    
    d = {'patient': patient}
    
    return render(request, 'view_patient.html', d)

def delete_patient(request, id):
    
    if not request.user.is_staff:
        return redirect('login')
    
    patient = Patient.objects.get(id=id)
    patient.delete()
    
    return redirect('view_patient')

def Add_Appointment(request):
    
    if not request.user.is_staff:
        return redirect('login')
    
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    
    if request.method == "POST":
        
        d = request.POST['doctor']
        p = request.POST['patient']
        da = request.POST['date1']
        t = request.POST['time1']
        
        Appointment.objects.create(
            doctor_id=d,
            patient_id=p,
            date1=da,
            time1=t
        )
        
        return redirect('view_appointment')
    
    return render(request, 'add_appointment.html', {
        'doctors': doctors,
        'patients': patients
    })

def View_Appointment(request):
    
    if not request.user.is_staff:
        return redirect('login')
    
    appointment = Appointment.objects.all()
    
    return render(request, 'view_appointment.html', {
        'appointment': appointment
    })

def delete_appointment(request, id):
    
    if not request.user.is_staff:
        return redirect('login')
    
    Appointment.objects.get(id=id).delete()
    
    return redirect('view_appointment')

def Home(request):
    
    if not request.user.is_staff:
        return redirect('login')
    
    dcount = Doctor.objects.all().count()
    pcount = Patient.objects.all().count()
    acount = Appointment.objects.all().count()
    
    return render(request, 'home.html', {
        'dcount': dcount,
        'pcount': pcount,
        'acount': acount
    })