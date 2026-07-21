from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm


def login_view(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user:
                login(request, user)
                return redirect('dashboard')

    return render(
        request,
        'usuarios/login.html',
        {'form': form}
    )