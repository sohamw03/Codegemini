from django import template

register = template.Library()

@register.filter(name="get_rep_filter")
def get_rep_filter(dict, key):
    return dict.get(key, "")