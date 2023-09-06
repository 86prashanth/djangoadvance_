from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from .managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField

class JobUser(AbstractBaseUser):
    VERIFICATION_TYPE = [
        ('sms','SMS'),
    ]
    
    phone_number = PhoneNumberField(unique = True)
    verification_method = models.CharField(max_length=10,choices= VERIFICATION_TYPE)
    is_active = models.BooleanField(default= True)
    is_admin = models.BooleanField(default= False)
    is_staff = models.BooleanField(default= False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    objects = UserManager()
    
    def __str__(self):
        return str(self.phone_number)
    
    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
    
    

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    