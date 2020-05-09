# isPhoneNumber.py validates and searches strings for phone numbers given the regex pattern.

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 404-543-1574.')
print('Phone number found: ' + mo.group())  # mo.group displays the whole match
