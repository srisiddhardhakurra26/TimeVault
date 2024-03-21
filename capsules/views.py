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
from django.utils import timezone
def create_time_capsule(request):
    form = TimeCapsuleForm()
    if request.method == 'POST':
        form = TimeCapsuleForm(request.POST, request.FILES)
        if form.is_valid():
            time_capsule = form.save(commit=False)
            time_capsule.creator = request.user  # Assign the current user as the creator
            time_capsule.save()
            return redirect('user_timeline')  # Redirect to a confirmation page or the capsule detail view
    else:
        form.fields['open_date'].widget.attrs.update({'min': timezone.now().date().isoformat()})
    return render(request, 'create_time_capsule.html', {'form': form})



from django.contrib.auth.decorators import login_required
from .models import TimeCapsule
@login_required
def user_timeline(request):
    user_capsules = TimeCapsule.objects.filter(creator=request.user).order_by('open_date')
    return render(request, 'user_timeline.html', {'user_capsules': user_capsules})



from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.utils import timezone
from .models import TimeCapsule
def time_capsule_detail(request, capsule_id):
    capsule = get_object_or_404(TimeCapsule, pk=capsule_id, creator=request.user)
    if capsule.open_date > timezone.now().date():
        return HttpResponse("This time capsule is not yet available.")
    return render(request, 'time_capsule_detail.html', {'capsule': capsule})
