from django import template

register = template.Library()

def my_filter(value):
    return value + "This is Custom Filter"


register.filter('custom',my_filter)