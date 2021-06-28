'''
1.2 Import line of python script

You have to do it for following formats:
import somelibrary
import somelibrary as sl
from somelibrary import somemodule
'''

import re

import_pattern = r'(from)?\s?\D*?\s?(import)\s\D*\s?(as)?\s?\D*'

import_regex = re.compile(import_pattern)

import_user = input("Give me import statement to check it capability: ")

if re.fullmatch(import_regex,import_user):
    print("Valid import")
else:
    print("Invalid import")
