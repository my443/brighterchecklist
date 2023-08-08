from django import forms

class ChecklistForm(forms.Form):
    checklist_item_users_notes = forms.CharField(widget=forms.Textarea(attrs={'class': "form-control", "rows": "5"}),
                                        required=False, label=False)
