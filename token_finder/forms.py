import django.forms

from token_finder.models import SpotPlayer


class KeyForm(django.forms.ModelForm):
    class Meta:
        model = SpotPlayer
        fields = [
            'national_code',
            'registry_code',
        ]
