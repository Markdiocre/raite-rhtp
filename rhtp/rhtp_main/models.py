from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class Appointments(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()


class CustomUserManager(BaseUserManager):
    def create_user(self, email,password, **other_fields):   
        email = self.normalize_email(email)
        user = self.model(email=email,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email,password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assined to is_staff=True')
        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assined to is_superuser=True')


        return self.create_user(email, password, **other_fields)

class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = [
        ('MALE',' male'),
        ('FEMALE', 'female'),
        ('OTHERS', 'others')
    ]

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    phone_number = models.IntegerField(null=True)
    address = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CHOICES,max_length=9, default='MALE')

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','middle_name','phone_number','address','gender']

    def __str__(self):
        return self.user_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True