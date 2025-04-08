from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

# Create your views here.

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('accounts:admin_dashboard')
        else:
            return render(request, 'accounts/admin_login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/admin_login.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and not user.is_staff:
            login(request, user)
            return redirect('accounts:user_dashboard')
        else:
            return render(request, 'accounts/user_login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/user_login.html')

@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    context = {
        'total_users': User.objects.count(),
        'active_users': User.objects.filter(is_active=True).count(),
    }
    return render(request, 'accounts/admin_dashboard.html', context)

@login_required
def user_dashboard(request):
    return render(request, 'accounts/user_dashboard.html')
