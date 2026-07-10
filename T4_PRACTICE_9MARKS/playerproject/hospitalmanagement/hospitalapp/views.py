from django.shortcuts import render, redirect, get_object_or_404
from .models import Patient

# Welcome Page
def welcome(request):
    return render(request, 'hospitalapp/welcome.html')

# Home Page (Display + Search)
def home(request):
    query = request.GET.get('q', '')
    if query:
        patients = Patient.objects.filter(name__icontains=query) # Search by first field (name)
    else:
        patients = Patient.objects.all()
    return render(request, 'home.html', {'patients': patients, 'query': query})

# Add Record
def add_patient(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        disease = request.POST['disease']
        doctor = request.POST['doctor']
        Patient.objects.create(name=name, age=age, disease=disease, doctor=doctor)
        return redirect('home')
    return render(request, 'add_edit.html', {'action': 'Add'})

# Edit Record
def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.name = request.POST['name']
        patient.age = request.POST['age']
        patient.disease = request.POST['disease']
        patient.doctor = request.POST['doctor']
        patient.save()
        return redirect('home')
    return render(request, 'add_edit.html', {'patient': patient, 'action': 'Edit'})

# Delete Record
def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    patient.delete()
    return redirect('home')
