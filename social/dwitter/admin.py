from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Profile, Dweet
from django.contrib.auth import urls

# Register your models here.


class ProfileInline(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username","password","email"]
    inlines = [ProfileInline]


admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(User, UserAdmin)  # restric User Model By UserAdmin

admin.site.register(Dweet)
# dwitter/admin.py
# ...

# ...
# admin.site.register(Profile)
