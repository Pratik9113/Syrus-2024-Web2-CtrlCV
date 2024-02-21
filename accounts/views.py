# # from django.shortcuts import render
# # from django.contrib import messages
# # from django.contrib.auth.models import User
# # from django.http import HttpResponseRedirect
# # from django.contrib.auth.models import authenticate,login,logout

# # # Create your views here.


# # def loginPage(request):
# #     if request.method == 'POST':
# #         email = request.Post.get('email')
# #         password = request.Post.get('password')
        
        
# #         # already exits 
# #         user_obj = User.objects.filter(username = email, password = password)
        
# #         if  not user_obj.exists():
# #             messages.warning(request,'Account not found ')
# #             return HttpResponseRedirect(request.path_info)
        
        
# #         if user_obj[0].profile.is_email_verified:
# #             messages.success(request , 'Your account si not verified ')
# #             return HttpResponseRedirect(request.path_info)
        
# #         user_obg = authenticate(username = email,password = password)
# #         if user_obj :
# #             login(request, user_obj)
# #             return redirect('/')
        
        
# #         messages.success(request , 'Inavalid ')
# #         return HttpResponseRedirect(request.path_info)
    
# #     return render(request, "accounts/login.html")

# # def registerPage(request):
    
# #     if request.method == 'POST':
# #         name = request.Post.get('name')
# #         email = request.Post.get('email')
# #         password = request.Post.get('password')
# #         user_obj = User.object.filter(username = email)
        
# #         # already exits 
# #         user_obj = User.objects.filter(username = email)
        
# #         if user_obj.exists():
# #             messages.warning(request,'email is already registered')
# #             return HttpResponseRedirect(request.path_info)
        
# #         user_obg = User.objects.create(name = name, email = email)
# #         user_obj.set_password(password)
# #         user_obj.save()
        
# #         messages.success(request , 'an email has been sent on your mail')
# #         return HttpResponseRedirect(request.path_info)
    
# #     return render(request, "accounts/register.html")

# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.http import HttpResponseRedirect, HttpResponse
# from django.contrib.auth import authenticate, login
# from .models import Profile

# def loginPage(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         # Check if the user exists
#         user_obj = User.objects.filter(username=email)

#         if not user_obj.exists():
#             messages.warning(request, 'Account not found')
#             return HttpResponseRedirect(request.path_info)
        
#         user_obj = authenticate(username=email, password=password)
        
#         if not user_obj:
#             messages.success(request, 'Invalid credentials')
#             return HttpResponseRedirect(request.path_info)
        
#         if not user_obj.profile.is_email_verified:
#             messages.success(request, 'Your account is not verified')
#             return HttpResponseRedirect(request.path_info)
        
#         login(request, user_obj)
#         return redirect('/')
    
#     return render(request, "accounts/login.html")

# def registerPage(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
        
#         # Check if the user already exists
#         user_obj = User.objects.filter(username=email)
        
#         if user_obj.exists():
#             messages.warning(request, 'Email is already registered')
#             return HttpResponseRedirect(request.path_info)
        
#         # Create a new user with a hashed password
#         user_obj = User.objects.create_user(username=email, password=password)
#         user_obj.name = name  # Assuming 'name' is a field in your user model
#         user_obj.save()
        
#         messages.success(request, 'An email has been sent to your mail')
#         return HttpResponseRedirect(request.path_info)
    
#     return render(request, "accounts/register.html")

# def activate_email(request , email_token):
#     try:
#         user = Profile.objects.get(email_token= email_token)
#         user.is_email_verified = True
#         user.save()
#         return redirect('/')
#     except Exception as e:
#         return HttpResponse('Invalid Email token')

from cmath import log
from tkinter import E
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from .models import Profile
# from .views import home

def loginPage(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)


        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username = email , password= password)
        if user_obj:
            login(request , user_obj)
            return redirect(reverse('home'))

        

        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/login.html')


def registerPage(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        print(email)

        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/register.html')




def activate_email(request , email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token')
    
    
# def home(request):
#     return render(request ,'home/index.html')