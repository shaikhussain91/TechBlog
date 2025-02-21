
# # from django.contrib import admin 


# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from django.utils.translation import gettext_lazy as _
# from .models import *

# class CustomUserAdmin(UserAdmin):
#     model = CustomUser
#     list_display = ("email", "username", "is_staff", "is_active")  # Fields displayed in the user list
#     list_filter = ("is_staff", "is_superuser", "is_active")  # Filters in admin panel
#     ordering = ("email",)  # Order users by email

#     fieldsets = (
#         (None, {"fields": ("email", "username", "password")}),
#         (_("Personal Info"), {"fields": ("first_name", "last_name")}),
#         (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
#         (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
#     )
    

#     add_fieldsets = (
#         (None, {
#             "classes": ("wide",),
#             "fields": ("email", "username", "password1", "password2", "is_active", "is_staff"),
#         }),
#     )

#     search_fields = ("email", "username")  # Enables searching by email or username
#     filter_horizontal = ("groups", "user_permissions")  # Allows adding groups in admin

# # Register CustomUser with the CustomUserAdmin panel
# admin.site.register(CustomUser, CustomUserAdmin)
