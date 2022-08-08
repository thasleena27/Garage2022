from django import template
register = template.Library()

def Expand(value): # Only one argument.
    """Converts a string into all lowercase"""
    if value==True:
     return 'Yes'
    else:
     return 'No'
register.filter('expand', Expand)