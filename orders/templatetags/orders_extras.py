from django import template

register = template.Library()

@register.simple_tag
def dictKeyLookup(the_dict, key):
   # Try to fetch from the dict, and if it's not found return an empty string.
   try:
       return the_dict.get(key, '')
   except:
       return ''

@register.simple_tag
def dictGetFirst(the_dict, key):
   # Try to fetch from the dict, and if it's not found return an empty string.
   try:
       return the_dict.get(key, '')[0].price
   except:
       return ''

@register.simple_tag
def dictGetSecond(the_dict, key):
   # Try to fetch from the dict, and if it's not found return an empty string.
   try:
       return the_dict.get(key, '')[1].price
   except:
       return ''

@register.simple_tag
def idGetFirst(the_dict, key):
   # Try to fetch from the dict, and if it's not found return an empty string.
   try:
       return the_dict.get(key, '')[0].id
   except:
       return ''

@register.simple_tag
def idGetSecond(the_dict, key):
   # Try to fetch from the dict, and if it's not found return an empty string.
   try:
       return the_dict.get(key, '')[1].id
   except:
       return ''
