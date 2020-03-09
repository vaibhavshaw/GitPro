from django import forms


class RepoForm(forms.Form):
    organisation = forms.CharField(
        max_length=50, label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Organisation Name",
                "class": "form-control",
            }
        ))
    N = forms.IntegerField()
    M = forms.IntegerField()
