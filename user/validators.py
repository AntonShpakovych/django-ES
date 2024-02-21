import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def password_validator(value):
    pattern = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    if not re.match(pattern, value):
        raise ValidationError(
            _(
                "Password must contain at least 8 characters, "
                "including at least one uppercase letter, "
                "one digit and one special character."
            ),
            code="invalid_password",
        )


class AdminPasswordValidation:
    def validate(self, password, user=None):
        password_validator(password)

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 digit, "
            "upper case letter, symbol and at least 8 length"
        )
