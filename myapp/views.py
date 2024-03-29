from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Title, Post, Account
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


from collections import OrderedDict

from .google_spreadsheets import *
from datetime import date

#needed variables

date = date.today()
date = str(date)


# Create your views here.
def index(request):
    posts = Post.objects.all()
    titles = Title.objects.all()
    return render(request, "index.html", {"titles": titles, "posts" : posts})

def register(request):
    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        secret_key = request.POST['secret_key']
        
        if len(password) < 8:
            messages.info(request, 'Password too short, a minimum of 8 characters is required')
            return redirect("register")

        elif username == "":
            messages.info(request, 'Please enter a username')
            return redirect("register")
        
        elif email == "":
            messages.info(request, 'Please emter an email')
            return redirect("register")
        
        elif password == "" or password2 == "":
            messages.info(request, 'Please enter a password')
            return redirect("register")
        
        elif secret_key == "":
            messages.info(request, 'Please enter a key provided by ')
            return redirect("register")

        elif password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken :(')
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'This user already exists')
                return redirect("register")
            elif secret_key != "1234":
                messages.info(request, 'Please contact the admin for a valid key')
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        
        else:
            messages.info(request, "Passwords do not match")
            return redirect("register")
        

    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else: 
            messages.info(request, "Invalid credentials")
            return redirect('login')


    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def profile(request):
    user = request.user
    user_account = Account.objects.filter(user=user.id)
    worksheets = get_worksheets()
    user_name = str(user)
    if user_name not in worksheets:
        make_sheet(user_name)
    data = read_main_spreadsheet()
    user_data = None
    for i in range(1, len(data)):
        if str(data[i][0]) == str(user):
            user_data = data[i]
    individual_data = read_individual_spreadsheet(user_name)
    try:
        baseline_data = individual_data[0]
        current_data = individual_data[len(individual_data) - 1]
    except: # prevents an out of range error if the spreadsheet is empty for new users
        baseline_data = None
        current_data = None

    context = {"user_data" : user_data, "baseline_data" : baseline_data, "current_data" : current_data}
    return render(request, 'profile.html', context)


def update_profile(request):
    user = request.user
    data = read_main_spreadsheet()
    user_data = None
    position = len(data) + 1
    for i in range(1, len(data)):
        if str(data[i][0]) == str(user):
            user_data = data[i]
            position = i
            break
    if request.method == "POST":
        try:
            username = str(user)
            FirstName = request.POST['FirstName']
            LastName = request.POST['LastName']
            Birthday = request.POST['Birthday']
            try:
                bd = Birthday.split("-")
                ParsedBday = f"{bd[1]}/{bd[2]}/{bd[0]}"
            except:
                ParsedBday = "1/1/1111"
            Age = f'=ROUNDDOWN(YEARFRAC(D{position + 1}, TODAY(), 1))'
            Gender = request.POST['Gender']
            Height = request.POST['Height']
            email = request.POST['email']
        except:
            messages.info(request, 'Please make sure that all fields are filled')
        info = [username, FirstName, LastName, ParsedBday, Age, Gender, Height, email]
        if user_data == None:
            length = len(read_main_spreadsheet()) + 1
            write_main_spreadsheet(length, info)
        elif str(data[position][0]) == str(user):
            write_main_spreadsheet(position + 1 , info)
        else:
            messages.info(request, 'ERROR')
        return redirect('/profile')
    context = {"user_data" : user_data}
    return render(request, 'update_profile.html', context)

def add_stats(request):
    user = request.user
    user_name = str(user)
    if request.method == "POST":
        try:
            body_weight_kg  = request.POST['body_weight_kg']
            body_fat_p = request.POST['body_fat_p']
            visceral_fat = request.POST['visceral_fat']
            bone_mass_kg = request.POST['bone_mass_kg']
            bmr = request.POST['bmr']
            metabolic_age = request.POST['metabolic_age']
            muscle_mass_kg = request.POST['muscle_mass_kg']
            physique_rating = request.POST['physique_rating']
            water = request.POST['water']
        except:
            messages.info(request, 'Please make sure that all fields are filled')
        data = [date,
           body_weight_kg, 
            body_fat_p, 
            visceral_fat, 
            bone_mass_kg, 
            bmr, 
            metabolic_age,
            muscle_mass_kg, 
            physique_rating, 
            water,
            (int(body_weight_kg) * int(body_fat_p)) / 100,
            (int(muscle_mass_kg) / int(body_weight_kg)) * 100]

        sheet = read_individual_spreadsheet(user_name)
        position_to_add = len(sheet) + 1
        write_individual_spreadsheet(user=user_name, position_to_add=position_to_add, data=data)
        return redirect('/profile')
    return render(request, 'add_stats.html')


def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, "post.html", {'post' : post})


def calc(request):
    
    calculate = True
    if request.method == "POST":
        try:
            body_weight_kg  = request.POST['body_weight_kg']
            body_fat_p = request.POST['body_fat_p']
            visceral_fat = request.POST['visceral_fat']
            bone_mass_kg = request.POST['bone_mass_kg']
            bmr = request.POST['bmr']
            metabolic_age = request.POST['metabolic_age']
            muscle_mass_kg = request.POST['muscle_mass_kg']
            physique_rating = request.POST['physique_rating']
            water = request.POST['water']
            body_fat_kg = (int(body_weight_kg) * int(body_fat_p)) / 100
            muscle_mass_p = (int(muscle_mass_kg) / int(body_weight_kg)) * 100
            calculate = True

            context = {'body_weight_kg' : body_weight_kg, 
            'body_fat_p' : body_fat_p, 
            'visceral_fat': visceral_fat, 
            'bone_mass_kg' : bone_mass_kg, 
            'bmr' : bmr, 
            'metabolic_age' : metabolic_age,
            'muscle_mass_kg' : muscle_mass_kg, 
            'physique_rating' : physique_rating, 
            'water' : water, 
            'body_fat_kg' : body_fat_kg, 
            'muscle_mass_p' : muscle_mass_p,
            'calculate' : calculate }
            return render(request, 'calc.html', context)
        except:
            messages.info(request, 'Please make sure that all fields are filled')
            
    return render(request, 'calc.html')