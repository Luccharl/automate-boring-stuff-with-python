import re

credit = '1234 5678 1235 5143'

# credit_pattern = re.compile('(\d)\d{3}\s?')
# print(credit_pattern.sub(r'\1****', credit))

encrypt = credit[0]
encrypt += '*' * len(credit[1:])
print(encrypt)
