from django import template

register = template.Library()

@register.filter
def split(value, delimiter=','):
    """Split a string into a list using the given delimiter."""
    return value.split(delimiter)

@register.filter
def get_item(dictionary, key):
    """Get an item from a dictionary using the given key."""
    return dictionary.get(key) 