from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    # если нужно добавить чейзе в дефолте вместо -----
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['pole'].empty_label = 'Категория не выбрана'

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-input'}),
        #
        # }

    def clean_username(self):
        #Проверка поля, обязательно после clean_добавить поле которое необходимо проверить
        username = self.cleaned_data['username']
        print(username)
        if len(username) > 10:
            raise ValidationError('Длинна превышает 10 сисмволов')
        return username

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


