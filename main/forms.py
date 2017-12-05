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
            (DEBATOR, 'Debater'),
            (MODERATOR, 'Moderator')
        ),
        widget = forms.RadioSelect,
        label = 'Select a Role',
        initial = 'S',
    )
    side = forms.ChoiceField(
        choices = (
            ('A', 'A'),
            ('B', 'B'),
        ),
        widget = forms.RadioSelect,
        label ='Select a side',
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

class ReportForm(forms.Form):
    reason = forms.CharField(label = 'Reasoning:', required = True)
    post_id = forms.IntegerField(widget=forms.HiddenInput()) 
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('report_debater_submit', 'Report', css_class="btn-primary"))
    helper.add_input(Submit('cancel', 'Cancel', css_class="btn-secondary"))


class MakePostForm(forms.Form):
    content = forms.CharField(label = 'Post an argument: ', required = True, widget=forms.widgets.Textarea(attrs={'rows': 4, 'style':'resize:none;'}))
    source = forms.URLField(label = 'Post source: ', required = True)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('post_submit', 'Submit', css_class = "btn-primary"))
    helper.add_input(Submit('cancel', 'Cancel', css_class="btn-secondary"))

class MakeCommentForm(forms.Form):
    content = forms.CharField(label = 'Post a comment: ', required = True, widget=forms.widgets.Textarea(attrs={'rows': 4, 'style':'resize:none;'}))
    source = forms.URLField(label = 'Post a source: ', required = False)
    post_id = forms.IntegerField(widget=forms.HiddenInput())
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('comment_submit', 'Submit', css_class = "btn-primary"))
    helper.add_input(Submit('cancel', 'Cancel', css_class="btn-secondary"))

class ScoreArgumentForm(forms.Form):
    post_id = forms.IntegerField(widget=forms.HiddenInput())
    
    understands_topic = forms.ChoiceField(
        choices=(
            (1, '1: Strongly disagree'),
            (2, '2: Disagree'),
            (3, '3: Neutral'),
            (4, '4: Agree'),
            (5, '5: Strongly agree'),
        ),
    initial=3, widget=forms.RadioSelect, label='The debater clearly understands the debate topic and argued their viewpoint effectively. ',
    )
    
    respectful = forms.ChoiceField(
        choices=(
            (1, '1: Strongly disagree'),
            (2, '2: Disagree'),
            (3, '3: Neutral'),
            (4, '4: Agree'),
            (5, '5: Strongly agree'),
        ),
    initial=3, widget=forms.RadioSelect, label='The debater was respectful and did not engage in any inappropriate language or behavior. ',
    )
    
    logical = forms.ChoiceField(
        choices=(
            (1, '1: Strongly disagree'),
            (2, '2: Disagree'),
            (3, '3: Neutral'),
            (4, '4: Agree'),
            (5, '5: Strongly agree'),
        ),
    initial=3, widget=forms.RadioSelect, label='The debater tied their argument to a central idea and organized their argument in a logical fashion. ',
    )
    
    accurate_info = forms.ChoiceField(
        choices=(
            (1, '1: Strongly disagree'),
            (2, '2: Disagree'),
            (3, '3: Neutral'),
            (4, '4: Agree'),
            (5, '5: Strongly agree'),
        ),
    initial=3, widget=forms.RadioSelect, label='The debater used accurate information to argue their viewpoint. ',
    )
    
    convincing = forms.ChoiceField(
        choices=(
            (1, '1: Strongly disagree'),
            (2, '2: Disagree'),
            (3, '3: Neutral'),
            (4, '4: Agree'),
            (5, '5: Strongly agree'),
        ),
    initial=3, widget=forms.RadioSelect, label='This debater convinced me of their viewpoint. ',
    )
    
    helper = FormHelper()
    helper.form_method = 'POST'
    helper.add_input(Submit('rubric_submit', 'Submit', css_class = "btn-primary"))
    helper.add_input(Submit('cancel', 'Cancel', css_class="btn-secondary"))