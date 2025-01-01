from django import forms
from .models import CustomUser

class SimpleUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Құпиясөз'}),
        label="Құпиясөз"
    )
    grade = forms.ChoiceField(
        choices=[(i, f"{i}-сынып") for i in range(5, 12)],
        label="Сынып"
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'grade']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Пайдаланушы аты'}),
        }
        labels = {
            'username': 'Пайдаланушы аты',
        }


from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Логин',
        max_length=150,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    password = forms.CharField(
        label='Құпиясөз',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
