from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')  # Redirect to another view, e.g., the login page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


from .forms import TimeCapsuleForm

def create_time_capsule(request):
    if request.method == 'POST':
        form = TimeCapsuleForm(request.POST, request.FILES)
        if form.is_valid():
            time_capsule = form.save(commit=False)
            time_capsule.creator = request.user  # Assign the current user as the creator
            time_capsule.save()
            return redirect('some_view_name')  # Redirect to a confirmation page or the capsule detail view
    else:
        form = TimeCapsuleForm()
    return render(request, 'create_time_capsule.html', {'form': form})
