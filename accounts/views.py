from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:  # Admin user
                return redirect('accounts:admin_dashboard')
            else:  # Regular user
                return redirect('accounts:user_dashboard')
        else:
            return render(request, 'main/home.html', {'error': 'Invalid username or password'})
    return render(request, 'main/home.html')

@user_passes_test(lambda u: u.is_staff)
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('accounts:user_dashboard')
    context = {
        'total_users': User.objects.count(),
        'active_users': User.objects.filter(is_active=True).count(),
    }
    return render(request, 'accounts/admin_dashboard.html', context)

@login_required
def user_dashboard(request):
    if request.user.is_staff:
        return redirect('accounts:admin_dashboard')
    return render(request, 'accounts/user_dashboard.html')
