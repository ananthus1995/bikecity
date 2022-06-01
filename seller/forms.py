from django import forms
from seller.models import Bikes
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class BikeForm(forms.ModelForm):
    class Meta:
        model=Bikes
        fields='__all__'

        widgets={'bikename':forms.TextInput(attrs={'class':' form-control form-control-user','placeholder':'BikeName',"autofocus": True}),
                 'manufacturer':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Manufacturer'}),
                'bike_model':forms.NumberInput(attrs={'class':'form-control form-control-user','placeholder':'ModelYear'}),
                 'colour':forms.TextInput(attrs={'class':'form-control form-control-user','placeholder':'Colour'}),
                 'milage':forms.NumberInput(attrs={'class':'form-control form-control-user','placeholder':'Milage'}),
                 'price':forms.NumberInput(attrs={'class':'form-control form-control-user','placeholder':'Price'}),

        }

    def clean(self):
        super(BikeForm, self).clean()

        bikename=self.cleaned_data.get('bikename')
        if len(bikename)<5:
            self._errors['bikename'] = self.error_class(['Bikename minimum of 5 characters is required'])
            return self.cleaned_data

class SignUpForm(UserCreationForm):

    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']

class SigninForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput())

