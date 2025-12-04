from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def home(request):
    return render(request, "home.html")

def gundem(request):
    return render(request, "gundem.html")

def etkinlikler(request):   
    return render(request, "etkinlikler.html")

def duyurular(request):
    return render(request, "duyurular.html")

def kulup(request):
    return render(request, "kulup_ve_topluluklar.html")

def password_reset_request(request):   
    return render(request, "password_reset.html")


def register_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Şifreler eşleşmiyor.")
            return render(request, "register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Bu kullanıcı adı zaten kullanılıyor.")
            return render(request, "register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Bu e-posta zaten kayıtlı.")
            return render(request, "register.html")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )
        user.save()
        messages.success(request, "Kayıt başarılı! Şimdi giriş yapabilirsiniz.")
        return redirect("login")

    return render(request, "register.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect("home")
