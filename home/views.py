
from tkinter.tix import Form
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login

from .forms import loginform


# Create your views here.
from .models import jobs, departments
# index_page

def index(request):
    return render(request,'index.html')




# about_page

def about(request):
    return render(request,'about.html')

# application_page

def app(request):
    return render(request,'application.html')




# jobs_page

def job(request):
    dict_job = {
        'job':jobs.objects.all()
    }
    return render(request,'jobs.html',dict_job)



# contact_page

def contact(request):
    return render(request,'contact.html')




# department_page
    
def department(request):
    dict_dept = {
        'dept':departments.objects.all()
    }
    return render(request,'department.html',dict_dept)


    


 # login_page
   
def login(request):
    if request.method=="POST":

        form = loginform(request.POST)
        print(dir(form))
        #username=form.cleaned_data('Email_address')
        username=request.POST['Email_address']
        password=request.POST['password']
        #password=form.cleaned_data('password')
        user = authenticate(username=username, password=password)
        if user is not None:
             return render(request,'login.html')
        else:
            login(request,user)
            dict_job = {
            'job':jobs.objects.all()
            }
            return render(request, 'jobs.html',dict_job)
    return render(request,'login.html')

            

    """
    if request.method == "POST":
        form = loginform(request.POST)
        if form.is_valid():
            form.save()
            dict_job = {
        'job':jobs.objects.all()
    } 
    
            return render(request, 'jobs.html',dict_job)

    form =loginform()
    dict_form={
        'form': form
    }
    return render(request,'login.html',dict_form)



"""
