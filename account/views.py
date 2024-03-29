from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.contrib.auth.models import User
from .utils import send_registration_email
from .models import UserProfile


def user_logout(request):
    logout(request)
    return redirect('home')

class UserLoginView(CreateView):
    template_name ="account/login.html"
    form = LoginForm
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={"title": "Login", "form": self.form()})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            un = form.cleaned_data["username"]
            pw = form.cleaned_data["password"]
            user = authenticate(username=un, password=pw)
            if not user:
                messages.error(request, "Invalid login credential")
                return redirect('user_login')

            else:
                login(request, user)
                messages.success(request, "Login Successful")
                return redirect('home')
        else:
            return redirect('user_login')


class UserRegisterView(CreateView):
    form = RegisterForm
    template_name = "account/register.html"
    success_url = reverse_lazy("user_login")

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={"title": "Register", "form": self.form()})


    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            if password != confirm_password:
                messages.error(request, 'Passwords did not match.')
                return redirect("user_register")
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                messages.error(request, "User with that username already exists")
                return redirect("user_register")
            data = dict(
                username=form.cleaned_data['username'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                is_active=True
            )
            user = User.objects.create(**data)
            user.set_password(password)
            user.save()
            # send_registration_email(user)
            messages.success(request, "User created successfully.")
            return redirect("user_login")
        else:
            messages.error(request, "Something went wrong.")


class UserProfileView(DetailView):
    template_name = "account/user_profile.html"
    queryset = User.objects.all()


class UserProfileUpdate(CreateView):
    template_name = "account/update_profile.html"
    queryset = User.objects.all()
    def get(self, request, *args, **kwargs):
        id = self.kwargs['pk']
        user = User.objects.get(id=id)
        return render(request, template_name= self.template_name, context = {"user": user})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        user = request.user
        fn = request.POST.get("first_name")
        ln = request.POST.get("last_name")
        email = request.POST.get("email")
        user.first_name = fn
        user.last_name = ln
        user.email = email
        user.save()

        pp = request.FILES.get("pp")
        resume = request.FILES.get("resume")
        pn = request.POST.get("phone_number")
        address = request.POST.get("address")
        up, _ = UserProfile.objects.update_or_create(phone_number=pn, address=address, defaults={"user": user})

        if pp:
            up.profile_picture = pp
        if resume:
            up.resume = resume
        up.save()
        return redirect('user_profile', user.id)
