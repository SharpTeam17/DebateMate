from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field

class JoinForm(forms.Form):
    role = forms.ChoiceField(
        choices = (
            ('S', 'Spectator'),
            ('D', 'Debater'),
            ('M', 'Moderator')
        ),
        widget = forms.RadioSelect,
        label ='Select a Role',
        initial = 'S',
    )
    side = forms.ChoiceField(
        choices = (
            ('A', 'A'),
            ('B', 'B'),
            ('Spectator', 'S')
        ),
        widget = forms.RadioSelect,
        label ='Select a side',
        initial = 'S',
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
    
class MakePostForm(forms.Form):
    content = forms.CharField(label = 'Post an argument: ', required = True)
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('submit', 'Submit!', css_class="btn-primary"))