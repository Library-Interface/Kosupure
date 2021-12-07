from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # is_creator = forms.BooleanField(label = "is_creator")
    # is_adult = forms.BooleanField(label = 'is_adult')
    date_of_birth = forms.DateField(required=False, label = "date of birth", widget=forms.TextInput(attrs=
                                {
                                    'type':'date',
                                }))
    class Meta:
        model = CustomUser
        fields = ('username', 'date_of_birth')

class CustomUserChangeForm(UserChangeForm):
    is_creator = forms.BooleanField(required=False, label = "This user is a creator (Cosplayer, Photographer, Cinematographer)")
    is_adult = forms.BooleanField(required=False, label = 'is_adult')
    website = forms.URLField(max_length=200, required=False)
    biography = forms.CharField(max_length=800, required=False)
    date_of_birth = forms.DateField(required=False, label = "date of birth", widget=forms.TextInput(attrs=
                                {
                                    'type':'date',
                                }))
    class Meta:
        model = CustomUser
        fields = ('username', 'biography', 'website', 'email', 'is_creator', 'is_adult', 'date_of_birth', 'first_name', 'last_name')