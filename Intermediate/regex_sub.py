import re

text = "Python is easy"

new_text = re.sub(
    "easy",
    "powerful",
    text
)

print(new_text)