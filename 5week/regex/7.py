import re

def snake_to_camel(txt):
         components = txt.split('_')
         return components[0] + ''.join(x.capitalize() for x in components[1:])

print(snake_to_camel(input()))
