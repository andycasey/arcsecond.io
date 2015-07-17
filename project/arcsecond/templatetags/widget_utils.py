__author__ = 'onekiloparsec'

# From http://vanderwijk.info/blog/adding-css-classes-formfields-in-django-templates/#comment-1193609278

from django import template
register = template.Library()

@register.filter
def add_css_attribute(field, css):
    if isinstance(field, str):
        return field

    attrs = {}
    definition = css.split(',')

    for d in definition:
        if ':' not in d:
            attrs['class'] = d
        else:
            t, v = d.split(':')
            attrs[t] = v

    return field.as_widget(attrs=attrs)
