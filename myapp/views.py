from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Title, Post, Account


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
        elif password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken :(')
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'This user already exists')
                return redirect("register")
            elif secret_key != 1234:
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
    context = {'user' : user, 'user_account' : user_account}
    return render(request, 'profile.html', context)

def profile_update(request):
    if request == "POST":
        pass
    return render(request, 'profile_update.html')

def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, "post.html", {'post' : post})


def calc(request):
    
    calculate = True
    if request.method == "POST":
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

    return render(request, 'calc.html')

    