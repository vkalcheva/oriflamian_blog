from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

from oriflamian_blog.account.models import Profile
from oriflamian_blog.common.helpers import BootstrapFormMixin

UserModel = get_user_model()


class CreateProfileForm(BootstrapFormMixin, UserCreationForm):
    first_name = forms.CharField(max_length=Profile.FIRST_NAME_MAX_LEN,)
    last_name = forms.CharField(max_length=Profile.LAST_NAME_MAX_LEN,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)
        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            user=user,
        )
        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
        widgets = {
            'first_name': forms.TextInput(
                attrs={

                    'placeholder': 'Enter first name'
                }
            ),
            'last_name': forms.TextInput(
                attrs={

                    'placeholder': 'Enter last name',
                }
            ),

        }


class EditProfileForm(BootstrapFormMixin, UserChangeForm):
    first_name = forms.CharField(max_length=Profile.FIRST_NAME_MAX_LEN, )
    last_name = forms.CharField(max_length=Profile.LAST_NAME_MAX_LEN, )
    picture = forms.ImageField()
    age = forms.ChoiceField(choices=Profile.AGES)
    skin_type = forms.ChoiceField(choices=Profile.SKIN_TYPE)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'picture', 'age', 'skin_type')


class ChangePasswordForm(BootstrapFormMixin, PasswordChangeForm):
    old_password = forms.CharField(max_length=100)
    new_password1 = forms.CharField(max_length=100)
    new_password2 = forms.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = get_user_model()
        fields = ('old_password', 'new_password1', 'new_password2')