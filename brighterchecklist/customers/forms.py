from django import forms

CUSTOMER_TYPE = [
    ("CM", "Checklist Manager"),
    ("CC", "Checklist Completer"),
]

class CustomerSignupForm(forms.Form):
    company_name = forms.CharField(label='Company Name', widget=forms.TextInput(attrs={'class': "form-control"}), required=False)
    firstname = forms.CharField(label='First Name [Required]', widget=forms.TextInput(attrs={'class': "form-control"}))
    lastname = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': "form-control"}), required=False)
    email = forms.CharField(label='Email Address', widget=forms.TextInput(attrs={'class': "form-control", "readonly":"readonly"}))
    customer_uuid = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': "form-control", "readonly": "readonly", 'hidden': 'true'}))

class ProfileUpdateForm(forms.Form):
    first_name = forms.CharField(label='First Name [Required]', widget=forms.TextInput(attrs={'class': "form-control w-75"}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': "form-control w-75"}), required=False)

class CustomerForm(forms.Form):
    company_name = forms.CharField(label='Company Name', widget=forms.TextInput(attrs={'class': "form-control"}), required=False)
    firstname = forms.CharField(label='First Name [Required]', widget=forms.TextInput(attrs={'class': "form-control"}))
    lastname = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': "form-control"}), required=False)
    email = forms.CharField(label='Email Address', widget=forms.TextInput(attrs={'class': "form-control"}))
    customer_type = forms.CharField(label='Customer Type', widget=forms.Select(attrs={'class': "form-control form-select"}, choices=CUSTOMER_TYPE) )
    customer_uuid = forms.CharField(label=False, widget=forms.TextInput(attrs={'class': "form-control", "readonly": "readonly", 'hidden': 'true'}))
