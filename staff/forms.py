from django import forms
from pages.models import StaticInfo
from profiles.models import UserProfile


class StaticInfoForm(forms.ModelForm):
    class Meta:
        model = StaticInfo
        fields = ('about_us', 'terms', 'privacy')


class EditUserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user_type',)
