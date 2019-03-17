from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        exclude = ('email',)
        fields = ('username', 'email', 'password')
        widgets={
                   "username":forms.TextInput(attrs={'placeholder':'username'}),
                   "email":forms.TextInput(attrs={'placeholder':'email','name':'Email','id':'common_id_for_imputfields','class':'input-class_name'}),
                   "password": forms.TextInput(attrs={'placeholder': 'password', 'name': 'Password', 'id': 'common_id_for_imputfields', 'class': 'input-class_name'}),
                }


class UserProfileInfoForm(forms.ModelForm):
    # portfolio = forms.URLField(required=False)
    # picture = forms.ImageField(required=False)
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
        widgets={
                   "portfolio_site":forms.TextInput(attrs={'placeholder':'portfolio_site','id':'common_id_for_imputfields','class':'input-class_name'}),
                }




