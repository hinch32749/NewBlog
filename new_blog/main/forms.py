from django import forms
from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from .models import Blog, Author, Comment


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description')


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('description', )


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Пароль (повторно)', widget=forms.PasswordInput)

    def clean_password(self):
        password1 = self.cleaned_data['password1']
        if password1:
            password_validation.validate_password(password1)
        return password1

    def clean(self):
        super().clean()
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            errors = {'password2': ValidationError('Ввуденные пароли не совпадают',
                                                   code='password_mismatch')}
            raise ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = Author
        fields = ('username', 'biography', 'email', 'password1', 'password2')


class ChangeProfileForm(forms.Form):
    pass
