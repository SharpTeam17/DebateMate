from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

class JoinForm(forms.Form):
    role = forms.ChoiceField(
        choices = (
            ('S', 'Spectator'),
            ('D', 'Debator'),
            ('M', 'Moderator')
        ),
        widget = forms.RadioSelect,
        label ='Select a Role',
        initial = 'S',
    )

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('join', 'Join', css_class="btn-primary"))
    helper.add_input(Submit('cancel', 'Cancel', css_class="btn-secondary"))