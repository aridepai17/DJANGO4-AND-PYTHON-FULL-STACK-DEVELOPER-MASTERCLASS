from django import forms
from .models import Review
from django.forms import ModelForm

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__" #pass in all model fields as from fields
        
        labels = {
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'stars': 'Rating'
        }
        
        errormessages = {
            'stars':{
                'min_value': 'Rating must be between 1 and 5',
                'max_value': 'Rating must be between 1 and 5'
            }
        }

#class ReviewForm(forms.Form):
#   firstname = forms.CharField(label='First Name', max_length=100)
#   lastname = forms.CharField(label='Last Name', max_length=100)
#    email = forms.EmailField(label='Email')
#   review = forms.CharField(label='Please leave your review here',
#                             widget=forms.Textarea(attrs={'class':'myform',
#                          'rows':'2', 'cols':'2'}))