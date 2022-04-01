from django import template

register = template.Library()

@register.filter(name='file_url')
def file_url(obj):
    """Removes all values of arg from the given string"""
    url = obj.external_file_url if obj.external_file_url else obj.file_url
    return url
