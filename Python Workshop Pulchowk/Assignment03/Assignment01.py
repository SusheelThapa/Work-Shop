'''
Assignment 1:
Similar to password manager program taught in the session(take our you tube video as reference), create a secure password manager program using environment variables. Note: your program shouldn't contain passwords.
'''

import pyperclip
import os

'''Below must be include in environmetal variable'''
email = os.environ['EMAIL_PYTHON']
password = os.environ['PASSWORD_PYTHON']

'''Copy both email and password'''
pyperclip.copy(f"{email},{password}")