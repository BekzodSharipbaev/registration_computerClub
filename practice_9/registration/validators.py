from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_username(value):
    value = value.lower()
    if value.startswith('admin') or value.endswith('admin'):
        raise ValidationError(_("This username already exists."))

def validate_password(value):
    min_length = 8
    if len(value) < min_length:
        raise ValidationError(_(f"Password must be at least {min_length} characters long."))
    
def validate_phone_number(value):
    value = str(value)
    if not value.isdigit() or len(value) != 9:
        raise ValidationError(_("Invalid phone number. Enter 9 digits without spaces or signs."))
    
def validate_age(value):
    if value < 16 or value > 60:
        raise ValidationError(_("Age must be between 16 and 60."))
               
def validate_positive_number(value):
    if value <= 0:
        raise ValidationError(_("Enter a positive number."))    
    