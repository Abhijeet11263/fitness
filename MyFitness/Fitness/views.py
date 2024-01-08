from django.shortcuts import render,redirect,HttpResponse
from Fitness.models import Contact
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def Home(request):
    return render(request, "index.html")

@login_required(login_url='login')
def Aboutus(request):
    return render(request, "aboutus.html")

@login_required(login_url='login')
def BlogDetails(request):
    return render (request, "blog-details.html")

@login_required(login_url='login')
def Classes(request):
     return render (request, "class-details.html")

@login_required(login_url='login')
def Services(request):
     return render (request, "services.html")

@login_required(login_url='login')
def Team(request):
     return render (request, "team.html")

@login_required(login_url='login')
def ClassesTimetable(request):
     return render (request, "class-timetable.html")

@login_required(login_url='login')
def BmiCalculator(request):
     return render (request, "bmi-calculator.html")

@login_required(login_url='login')
def Gallery(request):
     return render (request, "gallery.html")

@login_required(login_url='login')
def Blog(request):
     return render (request, "blog.html")

@login_required(login_url='login')
def BlogDetails(request):
     return render (request, "blog-details.html")

@login_required(login_url='login')
def contact(request):
     if request.method == "POST":
          name = request.POST['name']
          email = request.POST['email']
          phone = request.POST['phone']
          comment = request.POST['comment']
          contect = Contact(name=name, email= email, phone=phone, comment =comment)
           
          contect.save()
          messages.success(request,'Your data Has been Submitted Successfully !')
     return render(request,'contact.html')



def LOGIN(request):
    if request.method=="POST":
         username = request.POST.get('username')
         password = request.POST.get('password')
         user=authenticate(request,username=username,password=password)
         if user is not None:
              login(request,user)
              return redirect('index')
         else:
              messages.error(request,'Username or password are not same')
              return redirect('login')
     
    return render(request,'login.html')


def SIGNUP(request):
    if request.method=='POST':
         username = request.POST.get('username')
         email = request.POST.get('email')
         password1 = request.POST.get('password1')
         password2 = request.POST.get('password2')

         if password1!=password2:
               messages.error(request,'Password are not same !')
               return redirect('signup')
         else:
               my_user=User.objects.create_user(username,email,password1)
               my_user.save()
               return redirect('login')
    return render(request, 'signup.html')

def LOGOUT(request):
     logout(request)
     return redirect('login')