from django.shortcuts import render, redirect
from .models import Airway
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from .forms import signupform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.views.generic import ListView
from django.db.models import Q
# Create your views here.


def list_ticket(request):
    object_list = Airway.objects.all()
    return render(request, 'myapp/list.html', {'object_list': object_list})


def ticket_detail(request, id):
    idd = Airway.objects.get(id=id)
    return render(request, 'myapp/details.html', {'data': idd})


def register(request):
    if request.method == 'POST':
        fn = UserCreationForm(request.POST)
        if fn.is_valid():
            uname = fn.cleaned_data['username']
            upass = fn.cleaned_data['password1']
            user = User.objects.create_user(username=uname, password=upass)
            user.save()
            print(uname)
            print(upass)
            return redirect('/login')
    else:
        fn = UserCreationForm()
    return render(request, 'myapp/signup.html', {'form': fn})


def user_login(request):
    if request.method == 'POST':
        fn = AuthenticationForm(request=request, data=request.POST)
        if fn.is_valid():
            uname = fn.cleaned_data['username']
            upass = fn.cleaned_data['password']
            u = authenticate(request.POST)
            return redirect('/list')
    else:
        fn = AuthenticationForm(request.POST)
    return render(request, 'myapp/login.html', {'form': fn})


def user_logout(request):
    logout(request)
    return redirect('/login')


class SearchResultsView(ListView):
    model = Airway
    template_name = "myapp/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Airway.objects.filter(
            Q(From__icontains=query) | Q(To__icontains=query))
        return object_list
