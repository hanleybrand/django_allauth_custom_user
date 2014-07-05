
from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model


class SignupForm(forms.ModelForm):
    # date_of_birth = forms.DateField()
    # gender = forms.TypedChoiceField(
    #     choices=settings.GENDER_CHOICES,
    #     widget=forms.Select(attrs={'class': 'input-lg'}),
    #     required=False,
    # )

    class Meta:
        model = get_user_model() # use this function for swapping user model
        fields = ('email', 'username', 'first_name', 'last_name',
                  'date_of_birth', 'gender')

    def signup(self, request, user):
        user.username = request.cleaned_data['username']
        user.first_name = request.cleaned_data['first_name']
        user.last_name = request.cleaned_data['last_name']
        user.date_of_birth = request.cleaned_data['date_of_birth']
        user.gender = request.cleaned_data['gender']
        user.save()
