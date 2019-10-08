from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

def email_validator(value):
    if not '@indexial.com' in value:
        raise ValidationError('not a valid email')
    else:
        return value


def name_validators(value):
    if not value.isalpha():
        raise ValidationError('not a valid name')
    else:
        return value
mobile_regex = RegexValidator(regex='(0|91|\+91)[6-9]\d{9}|([6-9]\d{9})', message="Phone number not valid")

# def date_validator(value):
