from django import forms
from crispy_forms.helper import FormHelper
from .models import CustomUser
from crispy_forms.layout import (Layout, Row, Submit, Column)
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':'Password',\
         'onmouseover': 'this.title="password is required"'}), label='')
    confirm_password = forms.CharField(label='', required=True, max_length=254,\
         widget = forms.PasswordInput(attrs={'placeholder':"Confirm Password",\
         'onmouseover': 'this.title="password confirmation is required"'}))
    phone_number = forms.CharField(label='',max_length=10,widget=forms.TextInput\
        (attrs={'placeholder':'Phone Number','onmouseover': 'this.title="phone number is required"'}))
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Username',\
         'onmouseover': 'this.title="username is required"'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs=({'placeholder':'Email',\
         'onmouseover': 'this.title="email is required"'})))
    class Meta:
        model = CustomUser
        fields = ['username', 'phone_number', 'email', 'password', 'confirm_password']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group'),
                css_class='form-row '
            ),
            Row(
                Column('phone_number', css_class='form-group'),
                css_class='form-row '
            ),
             Row(
                Column('email', css_class='form-group'),
                css_class='form-row '
            ),
            Row(
                Column('password', css_class='form-group'),
                css_class='form-row '
            ),
            Row(
                Column('confirm_password', css_class='form-group'),
                css_class='form-row '
            ),
            Row(
                Submit('submit', 'Sign Up', css_class="form_button submit mt-0px")
            ),
        )

    def clean(self):
        super(RegisterForm, self).clean()
        pwd = self.cleaned_data['password']
        cpwd = self.cleaned_data['confirm_password']
        
        if pwd != cpwd:
            self._errors['password'] = self.error_class([''])
            self._errors['confirm_password'] = self.error_class(["Passwords did not match!!"])
        elif pwd == cpwd:
            try:
                validate_password(pwd)
            except ValidationError as exec:
                self._errors['password'] = self.error_class([''])
                self._errors['confirm_password'] = self.error_class([e for e in exec])
        return self.cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder':'Username', \
        'onmouseover':'this.title="username is required"'}))
    password = forms.CharField(label='', widget = forms.PasswordInput(attrs={'placeholder':'Password',\
        'onmouseover':'this.title="password is required"'}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Row(
                Column('username', css_class='form-group'),
                css_class='form-row '
            ),
            Row(
                Column('password', css_class='form-group'),
                css_class='form-row '
            ),
            Row(
                Submit('submit', 'Sign In', css_class="form_button submit")
            ),
        )
