from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

class JoinForm(forms.Form):
    text_input = forms.CharField(label = 'Username', required = True)

    radio_buttons = forms.ChoiceField(
        choices = (
            ('side_debator', 'Debators'),
            ('side_moderator', 'Moderators')
        ),
        widget = forms.RadioSelect,
        label ='Side',
        initial ='Debator'
    )

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('join', 'Join', css_class="btn-primary"))
    helper.add_input(Submit('cancel', 'Cancel', css_class="btn-secondary"))
	
class TopicForm(forms.Form):
    topic = forms.CharField(label = 'Debate topic:', required = True)
	
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('set_topic', 'Set topic', css_class="btn-primary"))
    helper.add_input(Submit('cancel', 'Cancel', css_class="btn-secondary"))