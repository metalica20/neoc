from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django import forms
from .models import Profile
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group


class UserForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        if not self.current_user.is_superuser:
            self.fields['groups'].widget.attrs['disabled'] = True
            self.fields['groups'].queryset = Group.objects.filter(user=self.current_user)
            self.fields['user_permissions'].queryset = Permission.objects.filter(
                user=self.current_user
            )

    class Meta:
        model = User
        fields = '__all__'


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_active')
    list_select_related = ('profile', )
    form = UserForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.current_user = request.user
        return form

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
