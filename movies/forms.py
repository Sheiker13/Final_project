from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Review, Rating


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text']


class RatingForm(forms.ModelForm):
    SCORE_CHOICES = [(i, str(i)) for i in range(1, 11)]

    score = forms.ChoiceField(
        choices=SCORE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select form-select-sm'})
    )

    class Meta:
        model = Rating
        fields = ['score']


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")
