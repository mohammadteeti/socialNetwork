from django import forms
from .models import Dweet, User
from django.contrib.auth.forms import UserCreationForm


class DweetForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Dweet somthing ...",
                "class": "textarea is-sucess is-medium",
                "name": "body",
            }
        ),
        label="",
    )

    class Meta:
        model = Dweet
        # fields='__all__' add all Dweet fields
        exclude = ("user",)


class RegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]
