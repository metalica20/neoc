from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import Permission
from django.contrib.auth.models import Group
from django_select2.forms import (
    ModelSelect2Widget,
)
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import (
    UserChangeForm
)

from federal.models import (
    Municipality,
    District,
)
from .permissions import get_queryset_for_user
from .models import Profile


class ProfileForm(forms.ModelForm):
    district = forms.ModelChoiceField(
        queryset=District.objects.all(),
        required=False,
        label=_("District"),
        widget=ModelSelect2Widget(
            model=District,
            search_fields=['title__icontains'],
        )
    )

    municipality = forms.ModelChoiceField(
        queryset=Municipality.objects.all(),
        required=False,
        label=_("Municipality"),
        widget=ModelSelect2Widget(
            model=Municipality,
            search_fields=['title__icontains'],
            dependent_fields={'district': 'district'},
        )
    )


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'
    form = ProfileForm

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.current_user = request.user
        return form


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.current_user.is_superuser:
            self.fields['groups'].queryset = Group.objects.filter(user=self.current_user)
            self.fields['user_permissions'].queryset = Permission.objects.filter(
                user=self.current_user
            )

    class Meta:
        model = User
        fields = '__all__'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_active')
    list_select_related = ('profile', )
    form = CustomUserChangeForm

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return get_queryset_for_user(queryset, request.user)

    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            self.readonly_fields = ('is_superuser',)
        form = super().get_form(request, obj, **kwargs)
        form.current_user = request.user
        return form


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
