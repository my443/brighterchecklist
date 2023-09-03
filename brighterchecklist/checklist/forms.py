from django import forms

class ChecklistForm(forms.Form):
    checklist_item_users_notes = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", "rows": "5"}),
                                        required=False, label=False)

class AssignedChecklistForm(forms.Form):
    assigned_checklist_custom_title = forms.CharField(label="Assigned Checklist Custom Name", widget=forms.TextInput(attrs={'class': "form-control", 'autofocus':True, 'onfocus':'this.select()', 'required':'True'}), required=False)
    assigned_checklist_notes = forms.CharField(label="Assigned Checklist Notes",
                                    widget=forms.Textarea(attrs={'class': "form-control", "rows": "5"}),
                                        required=False)


