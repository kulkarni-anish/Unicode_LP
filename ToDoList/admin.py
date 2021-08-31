from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm
from .models import MyUserModel

class MyUserAdmin(UserAdmin):
    form = MyUserCreationForm
    
    model = MyUserModel
    list_display = ['username', 'email', 'first_name','last_name']

    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name')}),
    )    
    add_fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name')}),
    )

admin.site.register(MyUserModel, MyUserAdmin)

# Register your models here.
from .models import ToDo
admin.site.register(ToDo)