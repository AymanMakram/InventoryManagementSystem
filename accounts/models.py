# from django.contrib.auth.models import AbstractBaseUser
# from django.db import models

# class CustomUser(AbstractBaseUser):
#     username = models.CharField(max_length=30, unique=True)
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=50, blank=True)
#     last_name = models.CharField(max_length=50, blank=True)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(auto_now_add=True)


#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['__all__']

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, app_label):
#         return self.is_admin

#     @property
#     def is_staff(self):
#         return self.is_admin