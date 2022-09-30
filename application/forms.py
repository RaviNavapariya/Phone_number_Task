from django import forms
from .models import User
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class PhoneNumberForm(forms.ModelForm):
    phone_number = PhoneNumberField(region='IN',
    widget=PhoneNumberPrefixWidget(
            country_choices=[
                 ("CA", "Canada"),
                 ("FR", "France"),
                 ("IN", "India"),
            ],),)
    class Meta:
        model = User
        fields = ['username', 'password', 'phone_number']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",user.phone_number)
        if commit:
            user.save()
        return user
