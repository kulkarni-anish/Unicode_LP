from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm
from .models import MyUserModel

class MyUserAdmin(admin.ModelAdmin):
    #form = MyUserChangeForm
    #add_form = MyUserCreationForm
    
    model = MyUserModel
    list_display = ['username', 'email', 'first_name','last_name']   

    fieldsets = (
        (None, {'fields': ('username','email', 'first_name', 'last_name','password','profile_picture')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username','email', 'first_name', 'last_name','password','profile_picture')}),
    )


admin.site.register(MyUserModel, MyUserAdmin)
#admin.site.register(MyUserModel)
# Register your models here.
from .models import ToDo
admin.site.register(ToDo)