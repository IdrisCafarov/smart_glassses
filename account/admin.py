from django.contrib import admin
# from accounts.forms import MyUserChangeForm, MyUserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from django import forms

from .models import *




User = get_user_model()


# admin.site.register(GuideImage)


# class ImageInline(admin.StackedInline):
#     model = GuideImage
#     max_num = 5
#     extra = 1

######################################################



admin.site.register(Disease)



######################################################

@admin.register(User)
class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': (
            'usertype','first_name', 'last_name','image','video','company_name','birthday','adress','phone')}),
        (_('Permissions'), {'fields': ('is_active','is_admin','is_user','is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ("first_name", "last_name", 'email', 'password1', 'password2'),
        }),
    )
    # # The forms to add and change user instances
    # form = MyUserChangeForm
    # add_form = MyUserCreationForm
    list_display = ('first_name','last_name','email','is_superuser','is_active')
    list_display_links=('first_name','last_name','email')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups','is_admin','is_user')
    # inlines = [ImageInline,]
    # search_fields = ('first_name', 'last_name', 'email')
    # ordering = ('-date_joined',)
    # filter_horizontal = ('groups', 'user_permissions',)



################## User #######################

class DiseaseInline(admin.StackedInline):
    model = UserDisease
    max_num = 10
    extra = 2




class UserUserAdmin(UserAdmin):

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_user=True)#HERE it is the flag for differentiating between Client and Partner

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserUserAdmin, self).get_inline_instances(request, obj)

    def has_add_permission(self, request, obj=None):
        return False

    fieldsets = (
        (None, {'fields': ('first_name', 'last_name', 'email','image')}),
       # ('Full name', {'fields': ()}),
        ('Permissions', {'fields': ('is_active',)}),
    )
    inlines = [DiseaseInline]
    list_display = ('email','first_name','last_name','is_active')



class UserUser(User):
    class Meta:
        proxy = True
        verbose_name = 'User'



admin.site.register(UserUser, UserUserAdmin)




















admin.site.register(CallHelp)
