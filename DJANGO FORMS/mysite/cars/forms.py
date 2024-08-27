from django import forms

class ReviewForm(forms.Form):
    firstname = forms.CharField(label='First Name', max_length=100)
    lastname = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    review = forms.CharField(label='Please leave your review here',
                             widget=forms.Textarea(attrs={'class':'myform',
                            'rows':'2', 'cols':'2'}))