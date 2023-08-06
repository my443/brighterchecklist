from django import forms

class ChecklistTemplateForm(forms.Form):
    checklist_name = forms.CharField(label='Checklist Name', widget=forms.TextInput(attrs={'class': "form-control"}))
    checklist_details = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", "rows": "5"}), required=False)

class ChecklistItemForm(forms.Form):
    item_short_text = forms.CharField(label='Template Item Short Text', widget=forms.TextInput(attrs={'class': "form-control", 'autofocus':True, 'onfocus':'this.select()'}), initial='<New Checklist Item>')
    item_description = forms.CharField(label='Template Item Description', widget=forms.Textarea(attrs={'class': "form-control", "rows": "5"}), required=False)

