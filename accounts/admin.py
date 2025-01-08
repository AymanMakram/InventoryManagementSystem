from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# # Register the CustomUser model
# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ('email', 'username', 'first_name', 'last_name', 'is_active', 'is_admin', 'date_joined')
#     # list_filter = ('is_active', 'is_admin', 'date_joined')
#     # search_fields = ('email', 'username', 'first_name', 'last_name')
#     # ordering = ('date_joined',)

admin.site.register(CustomUser)