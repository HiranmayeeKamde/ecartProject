from django.contrib import admin
from .models import UserProfile,Account

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Account)