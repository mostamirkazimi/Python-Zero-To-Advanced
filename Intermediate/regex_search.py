import re

text = "Hello Samiullah"

result = re.search("Samiullah", text)

if result:
    print("پیدا شد")
else:
    print("پیدا نشد")