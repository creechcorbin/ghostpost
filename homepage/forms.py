from django import forms


class AddPostForm(forms.Form):
    body = forms.CharField(max_length=280)
    post_type = forms.ChoiceField(choices=((False, 'Boast'), (True, 'Roast')))
