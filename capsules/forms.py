from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


from .models import TimeCapsule

class TimeCapsuleForm(forms.ModelForm):
    class Meta:
        model = TimeCapsule
        fields = ['open_date', 'message', 'image']
        widgets = {
            'open_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_open_date(self):
        open_date = self.cleaned_data.get('open_date')
        if open_date < timezone.now().date():
            raise ValidationError("The open date cannot be in the past.")
        return open_date