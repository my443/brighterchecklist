from django import forms

class ChecklistForm(forms.Form):
    source = forms.CharField(label='Source', max_length=255)
    startdate = forms.DateTimeField(label='Start Date', required=False)
    iscomplete = forms.BooleanField(label='Is Complete', required=False)
