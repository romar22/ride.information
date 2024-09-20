from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

@admin.register(get_user_model())
class UserAdmin(BaseUserAdmin):

    ordering = ('email',)
    list_filter = ('is_staff', 'is_superuser',)
    search_fields = ('email', 'first_name', 'last_name',)

    filter_horizontal = ('groups', 'user_permissions',)
    list_display = ('email', 'first_name', 'last_name',)

    fieldsets = (
        ("Account", {
            'fields': ('email', 'password',),
        }),
        ("Basic Information", {
            'fields': ('first_name', 'last_name')
        }),
        ("Others", {
            'fields': ('is_active', 'is_superuser', 'is_staff')
        }),
        ("Permissions", {
            'fields': ('groups',)
        })
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

admin.site.unregister(Group)