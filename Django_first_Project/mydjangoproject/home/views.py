from django.shortcuts import render     # render()
from django.http import HttpResponse


from .forms import BookingForm
from .models import Departments, Doctors # F models.py department we have created

# Create your views here.
def index(request):
    return render(request, 'index.html')  # here passing html file, render(), person dictionary as argument to index.html 

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "confirmation.html")

    form = BookingForm()
    dict_form = {
        'form' : form 
    }
    return render(request, 'booking.html', dict_form)

def doctors(request):
    dict_docs = {
        'doctors' : Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)

def contact(request):
    return render(request, 'contact.html')

def department(request):
    dict_dept = {                           # dictionary is gathering the informtion and passing to template
        'dept' : Departments.objects.all()  # pulling department-all fields
    }
    return render(request, 'department.html', dict_dept)  # passing the dictionary to html 'dict_dept'
    