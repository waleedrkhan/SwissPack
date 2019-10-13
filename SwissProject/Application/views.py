import hashlib, os
from django.http import HttpResponse
from django.conf import settings
from .models import Products, Users
from django.shortcuts import render
from django.contrib import messages
from bs4 import BeautifulSoup
import json


def signup(request):
    if request.method == 'POST':
        print ("this ispostr : ",request.POST)

        if request.POST.get("btn") == 'login':
            user = request.POST.get('login_user', '')
            pswd = request.POST.get('login_pswd', '')
            if not user or not pswd:
                return render (request, 'Application/signup.html')
            elif user and pswd:
                password = hashlib.sha256(pswd.encode('utf-8')).hexdigest()
                try:
                    user_db = Users.objects.get(email_id=user)
                except Users.DoesNotExist as e:
                    print ("no user found")
                    messages.success(request, "No User found. Try Again") 
                    return render(request, 'Application/signup.html')
                if user_db:
                    print ("user found")
                    if user_db.email_id == user and user_db.password == password:
                        print ("success login")
                        context = {'data':[user_db]}
                        return render(request, 'Application/profile.html', context)
                    else:
                        print ("login failed")
                        messages.success(request, "Incorrect username or password") 
                        return render(request, 'Application/signup.html')
                else:
                    return render(request, 'Application/signup.html')
            else:
                return render(request, 'Application/signup.html')

        elif request.POST.get("btn") == 'signup':
            fname = request.POST.get('signup_fname', '')
            lname = request.POST.get('signup_lname', '')
            email = request.POST.get('signup_email', '')
            pswd = request.POST.get('signup_pswd', '')
            re_pswd = request.POST.get('signup_re_pswd', '')
            if not fname or not lname or not email or not pswd or not re_pswd:
                print ("entries missing")
                return render(request, 'Application/signup.html')
            elif fname and lname and email and pswd and re_pswd:
                try:
                    user = Users.objects.get(email_id = email)
                    if user:
                        print ("user already exists")
                        return render(request, 'Application/signup.html')
                except Users.DoesNotExist as e:
                    if pswd == re_pswd:
                        user = Users(firstname=fname,lastname=lname, username=email, email_id=email, password=hashlib.sha256(pswd.encode('utf-8')).hexdigest())
                        user.save()
                        print ("success")
                        context= {'data': user}
                        return render(request, 'Application/profile.html')
                    else:
                        print ("pasword doesnot match")
                        return render(request, 'Application/signup.html')

        elif request.POST.get("btn") == "reset":
            email = request.POST.get("reset_email",'')
            pswd = request.POST.get("reset_pswd", '')
            re_pswd = request.POST.get("reset_re_pswd", '')
            if not email or not pswd or not re_pswd:
                print ("entries missing")
                return render(request, 'Application/signup.html')
            elif email and pswd and re_pswd and pswd==re_pswd:
                try:
                    user = Users.objects.get(email_id=email)
                    if user:
                        user.password = hashlib.sha256(pswd.encode('utf-8')).hexdigest()
                        user.save()
                        print ("password updated")
                except Users.DoesNotExist as e:
                    print ("user does not exist")
                    return render(request, 'Application/signup.html')

            return render(request, 'Application/signup.html')

    elif request.method == 'GET':
        return render (request, 'Application/signup.html')

def login(request):
    if request.method == 'POST':
        if request.POST.get("btn") == "LogIn":
            user_name = request.POST.get('username')
            password = hashlib.sha256(request.POST.get('password').encode('utf-8')).hexdigest()
            try:
                user = Users.objects.get(username=user_name)
            except Users.DoesNotExist as e:
                print ("no user found")
                messages.success(request, "No User found. Try Again") 
                return render(request, 'Application/login.html')
            if user:
                if user.name == user_name and user.password == password:
                    print ("success login")
                    return render(request, 'Application/home.html')
                else:
                    print ("login failed")
                    messages.success(request, "Incorrect username or password") 
                    return render(request, 'Application/login.html')
        elif request.POST.get('btn') == "SignUp":
            user_name = request.POST.get('username')
            password = hashlib.sha256(request.POST.get('password').encode('utf-8')).hexdigest()

    return render(request, 'Application/login.html')

def industries(request):
    return render(request, 'Application/industries.html')

def aboutus(request):
    return render(request, 'Application/aboutus.html')

def swiss_labs(request):
    return render(request, 'Application/swiss-labs.html')

def swiss_product_range(request):
    return render(request, 'Application/product_range.html')

def index(request):
    return render(request, 'Application/home.html')

def babyfood(request):
    return render (request, 'Application/babyfood.html')

def productpage(request):
    return render (request, 'Application/productpage.html')

def item_function(request):
    return render (request, 'Application/object.html')

def swiss_products(request):
    data = Products.objects.all()
    obj = Products.objects.get(name='car')

    context = {'data':data}
    return render(request, 'Application/products.html', context)

def material(request):
    return render(request, 'Application/material.html')

def design(request):
    return render(request, 'Application/design.html')

def services(request):
    return render(request, 'Application/services.html')

def sample(request):
    return render(request, 'Application/sample.html')

def update_html(f_name, **kwargs):
    with open ('Application/templates/Application/{}'.format(f_name)) as f:
        contents = f.read()
        update_flag = False
        soup = BeautifulSoup(contents, 'html.parser')
        h1_list = soup.find_all('h1')
        i=0
        for item in h1_list:
            if kwargs.get('h1_new'):
                item.string.replace_with(kwargs['h1_new'][i])
                i+=1
                update_flag=True
        
        h2_list = soup.find_all('h2')
        i=0
        for item in h2_list:
            if kwargs.get('h2'):
                item.string.replace_with(kwargs['h2_new'][i])   
                i+=1
                update_flag=True             

        h4_list = soup.find_all('h4')
        i=0
        for item in h4_list:
            if kwargs.get('h4'):
                item.string.replace_with(kwargs['h4_new'][i])
                i+=1
                update_flag=True

        para_list = soup.find_all('p')
        i=0
        for item in para_list:
            if kwargs.get('para'):
                item.string.replace_with(kwargs['para'][i])
                i+=1
                update_flag=True

        with open("Application/templates/Application/{}".format(f_name), "wb") as f_output:
            f_output.write(soup.prettify("utf-8"))

    return update_flag

def get_html(f_name):
    h1 = []
    h2 = []
    h4 = []
    para = []
    with open ('Application/templates/Application/{}'.format(f_name)) as f:
        contents = f.read()
        update_flag = False
        soup = BeautifulSoup(contents, 'html.parser')
        h1_list = soup.find_all('h1')
        for item in h1_list:
            h1.append(item.text)
        
        h2_list = soup.find_all('h2')
        for item in h2_list:
            h2.append(item.text)

        h4_list = soup.find_all('h4')
        for item in h4_list:
            h4.append(item.text)

        para_list = soup.find_all('p')
        for item in para_list:
            para.append(item.text)  

        with open("Application/templates/Application/example_modified.html", "wb") as f_output:
            f_output.write(soup.prettify("utf-8"))

    return h1, h2, h4, para,

def edit_html(request):
    files = os.listdir('Application/templates/Application/')
    context = {'data':files}
    if request.method == 'POST':
        h1 = request.POST.getlist('h1', '')
        h2 = request.POST.getlist('h2', '')
        h4 = request.POST.getlist('h4', '')
        para = request.POST.getlist('para', '')
        update_flag = update_html(settings.FILE_NAME, h1_new=h1, h2_new=h2, h4_new=h4, para_new=para)

        return render(request, 'Application/admin_edit.html', context)
    elif request.method == 'GET':
        f_name = request.GET.get('name', '')
        settings.FILE_NAME = f_name
        if f_name:
            h1, h2, h4, para = get_html(f_name)                
            context['h1'] = h1
            context['h2'] = h2
            context['h4'] = h4
            context['para'] = para
            return render(request, 'Application/admin_edit.html', context)
        
        return render(request, 'Application/admin_edit.html', context)