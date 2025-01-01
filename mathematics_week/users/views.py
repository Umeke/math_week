from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from .forms import SimpleUserCreationForm
from django.contrib.auth import login

from django.shortcuts import render, redirect
from .forms import SimpleUserCreationForm


from problems.models import Problem
def register_view(request):
    if request.method == 'POST':
        form = SimpleUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Құпиясөзді шифрлау
            user.save()
            return render(request, 'users/login.html' )
    else:
        form = SimpleUserCreationForm()
    return render(request, 'users/login.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Пайдаланушының сыныбына сәйкес есептерді алу
                user_grade = user.grade
                problems = Problem.objects.filter(grade=user_grade)
                return render(request, 'problems/problems.html', {'problems': problems})  # Есептерді көрсету
            else:
                messages.error(request, 'Қате логин немесе құпиясөз.')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})



from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from problems.models import Submission

@login_required
def profile_view(request):
    # Пайдаланушының шешкен есептерін алу
    submissions = Submission.objects.filter(user=request.user)
    return render(request, 'users/profile.html', {'user': request.user, 'submissions': submissions})
