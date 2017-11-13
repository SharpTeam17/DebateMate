from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

class JoinForm(forms.Form):
    radio_buttons = forms.ChoiceField(
        choices = (
            ('side_spectator', 'Spectator'),
            ('side_debator', 'Debator'),
            ('side_moderator', 'Moderator')
        ),
        widget = forms.RadioSelect,
        label ='Side',
        initial ='side_spectator'
    )

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('join', 'Join', css_class="btn-primary"))
    helper.add_input(Submit('cancel', 'Cancel', css_class="btn-secondary"))