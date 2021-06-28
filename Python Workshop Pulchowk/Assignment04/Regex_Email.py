'''

1.1 Email address

The required format is
alphanumeric.alphanumeric@alphanumeric.alphanumeric.alphanumeric
The first period is optional The last period and the contents after that
is optional
'''

import re

email_pattern = r'\w*\.?\w*[@]\w*\.\w*\.?\w*?'

regex_email = re.compile(email_pattern)

email_input = input("Give to email address to verify it is email or not: ")

if re.fullmatch(regex_email, email_input):
    print(f"{email_input} is a valid email address.")
else:
    print(f"{email_input} isn't a valid email address.")
