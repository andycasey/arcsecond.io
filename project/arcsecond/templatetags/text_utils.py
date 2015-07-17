__author__ = 'onekiloparsec'

from django import template

register = template.Library()

@register.filter
def substring_up_to_index(text, arg=-1):
    if arg < 0:
        return text
    if len(text) < arg:
        return text
    return text[:arg]

@register.filter
def substring_from_index(text, arg=-1):
    if arg == 0 or abs(arg) >= len(text):
        return text
    return text[arg:]

@register.filter
def text_length(text):
    return len(text)

@register.filter
def summary_with_endpoints_length(text, arg=0):
    if arg <= 0:
        return text
    separator = '...'
    if len(text) <= 2*arg+len(separator):
        return text
    return text[:arg]+separator+text[-arg:]

