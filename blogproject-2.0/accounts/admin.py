from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','email','yashash_manzil','is_staff']
    fieldsets = (
        (None, {
            "fields": (
                ('username','email','yashash_manzil',)
            ),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields': ('username','email','yashash_manzil',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)