from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, MembershipCard

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff')  # Remove date_joined and username
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(MembershipCard)
class MembershipCarAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'membership_number', 'membership_type')