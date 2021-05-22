from django import forms


class CardNameForm(forms.Form):
    card_name = forms.CharField(label='', max_length=20)
