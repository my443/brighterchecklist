from django import forms


class CustomerSignupForm(forms.Form):
    company_name = forms.CharField(label='Company Name', widget=forms.TextInput(attrs={'class': "form-control"}), required=False)
    firstname = forms.CharField(label='First Name [Required]', widget=forms.TextInput(attrs={'class': "form-control"}))
    lastname = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': "form-control"}), required=False)
    email = forms.CharField(label='Email Address', widget=forms.TextInput(attrs={'class': "form-control", "readonly":"readonly"}))
    customer_uuid = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': "form-control", "readonly": "readonly", 'hidden': 'true'}))