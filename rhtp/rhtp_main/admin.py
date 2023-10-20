from django.contrib import admin

# Register your models here.
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth import get_user_model

from .models import User

class UserCreationform(forms.ModelForm):
    email = forms.EmailField()
    middle_name = forms.CharField(max_length=150)
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)

    
    address = forms.CharField(max_length = 150)
    phone_number = forms.IntegerField()
    gender = forms.CharField(max_length=9)
    
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = [
            'email','first_name','last_name','middle_name','gender','role','password1','password2','address','phone_number',
        ]

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super(UserCreationform, self).__init__(*args, **kwargs)

        for fname, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control input-lg'

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = get_user_model()
        fields = [
            'email','middle_name','first_name','last_name','address','role','phone_number','gender','is_active','is_staff'
        ]


    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

class UserAdmin(BaseUserAdmin):
    ordering = ['last_name','first_name','email']
    list_display=[
        'user_id','first_name','last_name','middle_name','phone_number','address','gender','role'
    ]
    list_filter = ['is_staff','role']
    search_fields=[
        'email','last_name_name','first_name'
    ]
    fieldsets=[
        [None,{'fields':['email','middle_name','first_name','last_name','role']}],
        ['Permissions', {'fields':['is_active','is_staff']}],
        ['Others',{'fields':['address','phone_number']}]
    ]
    add_fieldsets = [
        [None,{
            'classes':['wide',],
            'fields':['email','middle_name','first_name','last_name','role','password1','password2','address','phone_number','is_staff','is_active']
        }]
    ]

admin.site.register(User, UserAdmin)