from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import AuthenticationForm


class CrispyAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Login'))
        super(CrispyAuthenticationForm, self).__init__(*args, **kwargs)
