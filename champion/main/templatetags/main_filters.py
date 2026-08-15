# уже не нужно
from django import template

register = template.Library()

@register.filter
def format_phone(value):
    if not value:
        return ''
    
    cleaned_value = str(value).replace(' ', '')
    return cleaned_value