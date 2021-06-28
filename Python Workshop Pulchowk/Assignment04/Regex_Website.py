'''
1.3 Website address

The required formats are:
example.com
http://example.com
http://www.example.com
'''
import re

website_pattern = r'(http)s?(://)(www)?\.?\w*\.\D{3}'

website_regex = re.compile(website_pattern)

website_user = input("Give me website to check it capability: ")

if re.fullmatch(website_regex,website_user):
    print("Valid Website")
else:
    print("Invalid Website")
