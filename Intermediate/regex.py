import re

text = "My phone number is 0781234567"

# پیدا کردن تمام اعداد
result = re.findall(r"\d+", text)

print(result)