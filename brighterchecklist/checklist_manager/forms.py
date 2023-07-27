from django import forms

class ChecklistTemplateForm(forms.Form):
    checklist_name = forms.CharField(label='Checklist Name', widget=forms.TextInput(attrs={'class': "form-control"}))
    checklist_details = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", "rows": "5"}), required=False)
