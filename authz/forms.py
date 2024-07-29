from django import forms
from django.core import validators
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[
            validators.MinLengthValidator(6, 'password must be more than 6 characters'),
            validators.MaxLengthValidator(20, 'password must be less than 20 characters'),
            validators.RegexValidator(
                r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[@#])[A-Za-z\d@#]{6,20}$',
                'Password must contain at least one uppercase letter, one lowercase letter, and one of the characters @ or #'
            )],
        required=True
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput,
        validators=[
            validators.MinLengthValidator(6, 'password must be more than 6 characters'),
            validators.MaxLengthValidator(20, 'password must be less than 20 characters'),
        ]
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('Passwords do not match')
        return password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('This username is already taken')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already taken')
        return email


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(
        widget=forms.PasswordInput,
        max_length=40
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Invalid username or password')
        return cleaned_data
