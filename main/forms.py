from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

class JoinForm(forms.Form):
    SPECTATOR = 'S'
    DEBATOR = 'D'
    MODERATOR = 'M'

    role = forms.ChoiceField(
        choices = (
            (SPECTATOR, 'Spectator'),
            (DEBATOR, 'Debator'),
            (MODERATOR, 'Moderator')
        ),
        widget = forms.RadioSelect,
        label = 'Select a Role',
        initial = 'S',
    )

    side = forms.ChoiceField(
        choices = 
        (
            ('A', 'A'),
            ('B', 'B'),
        ),
        widget = forms.RadioSelect,
        label = 'Select a Side',
        required = False,
    )

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('join', 'Join', css_class="btn-primary"))
    helper.add_input(Submit('cancel', 'Cancel', css_class="btn-secondary"))
	
    def __init__(self, data=None, *args, **kwargs):
        super(JoinForm, self).__init__(data, *args, **kwargs)

        if data and data.get('role') == self.DEBATOR:
            self.fields['side'].required = True

class TopicForm(forms.Form):
    topic = forms.CharField(label = 'Debate topic:', required = True)
	
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('set_topic', 'Set topic', css_class="btn-primary"))
    helper.add_input(Submit('cancel', 'Cancel', css_class="btn-secondary"))