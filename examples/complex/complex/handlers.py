
# This file needs to be imported from __init__.py

from django_mojeid.attribute_handlers import register_handler


@register_handler('full_name_handler')
def print_fullname_to_console(user, full_name):
    print('Full name >>>' +  str(full_name) + '<<< for user ' + str(user))


@register_handler('adult_handler')
def print_adult_to_console(user, adult):
    print('Adult >>>' +  str(adult) + '<<< for user ' + str(user))


@register_handler('valid_handler')
def print_valid_to_console(user, valid):
    print('Valid >>>' +  str(valid) + '<<< for user ' + str(user))
