import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class CustomValidator(object):
    def __init__(self, password):
        self.password = password

    def validate(self, password, user=None):
        PASSWORD_VALIDATION = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'
        if not re.match(PASSWORD_VALIDATION, password):
            raise ValidationError(
                    "The password must contain at least 8 include digit and special symbol."
                )

    def get_help_text(self):
        return (
            "The password must contain at least 8 include digit and special symbol."
        )